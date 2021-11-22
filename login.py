from os import error
import sys # importa o sistema
from typing import KeysView  
from src.verify import *  # Baixa os arquivos para o selenium
from src.browser import *
import time
from getpass import getpass
from dotenv import load_dotenv


# profile = input('Informe o nome de usuário do instagram (i.e @ladygaga)\n\n')
# limit = input('Informe o número de usuários para seguir (i.e 5)\n\n')
# filename = input(
#     'Informe o nome do arquivo para salvar os dados (i.e Follower1\n\n')

class Login():
    def loginUser():
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

    def saveInfo():
        if(WAIT_GET('/html/body/div[1]/section/main/div/div/div/div/button')):
            CLICK('/html/body/div[1]/section/main/div/div/div/section/div/button')

    def quitChrome():
        br.close()
        br.quit()


    br = GLOBAL_BR
    # Realiza a busca
    br.get(f'https://www.instagram.com/')
    time.sleep(2)
    loginUser()
    try:
        saveInfo()
    except:
        pass
    quitChrome()


# login /html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input
# senha /html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input
# botao /html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button

# # Faz a criação da pasta resultados
# dir_path = os.path.join('./usuarios', filename)
# if not os.path.exists('./usuarios'):
#     os.makedirs('./usuarios')

# if not os.path.exists(dir_path):
#     os.makedirs(dir_path)

# with open('{}.txt'.format(os.path.join(dir_path, "Results")), 'w', encoding='utf-8') as text:
# 	for res in results:
# 		text.write(res['username'] + '\t' + res['errorClick'] + '\t' + res['errorTxt'] + '\n')
# 	with open('{}.txt'.format(os.path.join(dir_path, "Inputs")), 'w', encoding='utf-8') as text:
# 		text.write(f'Profile username: {profile}\n Limit: {limit}')
