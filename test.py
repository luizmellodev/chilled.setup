from selenium.webdriver import Chrome
from instascrape import Profile, scrape_posts
from src.browser import *
from dotenv import load_dotenv
from src.verify import *  # Baixa os arquivos para o selenium



br = GLOBAL_BR
count = 0

#45667260989%3AwiG70kxZAuVlTz%3A27


headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": "45667260989%3A6a6TbL72mGDkQB%3A26"
}
br.get(f'https://www.instagram.com/')
time.sleep(2)
load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
try:
    GET(f'/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(f'{login}')
    GET(f'/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(f'{password}')
    time.sleep(2)
    CLICK('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
except:
    br.close()
    print_exc()

if(WAIT_GET('/html/body/div[1]/section/main/div/div/div/div/button')):
    CLICK('/html/body/div[1]/section/main/div/div/div/section/div/button')

if(WAIT_GET('/html/body/div[5]/div/div/div/div[3]/button[2]')):
    CLICK('/html/body/div[5]/div/div/div/div[3]/button[2]')
    time.sleep(3)


profile = Profile("isetups")
profile.scrape(headers=headers)

posts = profile.get_posts(webdriver=br, login_first=False, max_failed_scroll=300)
scraped, unscraped = scrape_posts(posts, silent=False, headers=headers, pause=15)

for post in scraped:
    if count >= 3:
        break
    fname = post.upload_date.strftime("%Y-%m-%d %Hh%Mm")
    post.download(fp=f"~\\Desktop\\teste-codce\\{fname}.png")
    count +=1
