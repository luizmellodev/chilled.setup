from typing import KeysView  
from src.verify import *  # Baixa os arquivos para o selenium
from src.browser import *
import time
from login import Login


class getSetups():
    br = GLOBAL_BR
    def goToLink(br):
        br.get('https://www.instagram.com/isetups/')
        time.sleep(3)
        
        while(True):
            print('oi')
            br.sendKeys(Keys.PAGE_DOWN)
    goToLink(br)
    Login.quitChrome(br)
        

        