# # # # # # # # # # # # # # # # # # # # #
# Name: Function Handler                #
# Version : 1.0                         #
# Author : Dinar Hamid                  #
# # # # # # # # # # # # # # # # # # # # #
import random
import string

def randomString(length: int = 10) -> str:
    return ''.join([random.choices(string.ascii_letters + string.digits) for z in range(0, length)])


