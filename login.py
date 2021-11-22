import os  # importa o sistema
from src.verify import *  # Baixa os arquivos para o selenium
from src.browser import *
import time
from getpass import getpass


profile = input('Informe o nome de usuário do instagram (i.e @ladygaga)\n\n')
limit = input('Informe o número de usuários para seguir (i.e 5)\n\n')
filename = input(
    'Informe o nome do arquivo para salvar os dados (i.e Follower1\n\n')

login = input('Informe o seu login do Instagram')
password = getpass('Informe a sua senha do Instagram')

results = []

try:
        login = ID('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input')
        login.send_keys(Keys.CONTROL, "a")
        login.send_keys(login)

        password = ID('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input')
        password.send_keys(Keys.CONTROL, "a")
        password.send_keys(password)
        time.sleep(8)
        CLICK('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button')
except:
    print('Erro ao tentar fazer o login automático')

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
