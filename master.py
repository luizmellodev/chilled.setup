from login import Login
from getSetups import getSetups
from src.browser import *

br = GLOBAL_BR
try:
    login = Login()
except:
    print('fodase')

try:
    getSetups()
except:
    print_exc()


