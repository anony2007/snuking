#Snuking/Somos uma legião. 2021 ©

import os
import platform
def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

def youtube():
   if platform.system() == "Windows":
      import webbrowser
      webbrowser.open_new_tab("https://youtube.com/channel/UC3HJVMAGPQnL3EglFcaFsKg")
   else:
       os.system("termux-open-url https://youtube.com/channel/UC3HJVMAGPQnL3EglFcaFsKg")

clear()
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

os.system("python3 -m pip install --upgrade pip")
os.system("pip install -r requirements.txt")
clear()
print(code_result + "Instalado com sucesso.\n")
os.system("python consulta.py")
