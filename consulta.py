#Snuking/Somos uma legião. 2021 ©

import requests, time
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

print(f'''{C}
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ▓▓▓▓██░░░░░░░░░░░░░░░░▓▓██▓▓
      ██░░░░                    ░░░░▓▓
    ▓▓░░                            ░░▓▓
  ██░░                                ░░██
  ██    ░░░░▓▓░░░░      ░░░░░░░░░░░░    ▓▓
  ▓▓  ▓▓░░▒▒▓▓▓▓▓▓░░    ░░▓▓▓▓▓▓▒▒░░▓▓  ▓▓
  ▓▓██          ▓▓██    ████          ██▓▓
  ▓▓            ░░░░    ░░░░          ░░▓▓
  ▓▓▒▒  ▒▒▒▒▓▓▒▒░░░░    ░░░░▒▒▒▒▓▓▒▒  ▒▒▓▓
  ▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓░░    ░░▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓
  ▓▓░░  ░░░░░░░░  ▓▓    ██  ░░░░░░░░  ░░▓▓
  ▓▓  ░░░░        ▓▓    ██        ░░░░  ▓▓
  ▓▓░░░░░░░░      ▓▓    ██      ░░░░░░░░▓▓
  ▓▓░░░░░░░░            ▓▓        ░░░░  ██
  ▓▓░░▓▓        ▓▓        ▓▓        ▓▓░░▓▓
  ▓▓░░▓▓▓▓        ▓▓░░░░▓▓        ▓▓▓▓░░▓▓
  ▓▓░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░▓▓
  ▓▓░░░░░░▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓
    ▒▒  ░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒░░░░▒▒
      ▓▓    ░░░░░░░░░░░░░░░░░░░░  ░░▓▓
      ▓▓░░    ░░░░░░██▓▓░░░░░░    ░░▓▓
        ▓▓░░        ▓▓▓▓        ░░▓▓
          ▓▓░░    ░░▓▓▓▓░░    ░░▓▓
            ▓▓░░  ░░▓▓▓▓░░  ░░▓▓
              ██░░  ▓▓▓▓  ░░▒▒
                ▓▓▓▓▓▓▓▓▓▓▓▓
             SNUKING / ANONYMOUS
'''); time.sleep(1.5)
clear()

#Snuking/Somos uma legião. 2021 ©


def main():
  clear()
  print(f'''{G}
\n
.----.______
|           |
|    ___________
|   /          /
|  /          /
| /          /
|/__________/ 1.0.2
{C}
 ''')

  print("\n" + code_info + "Menu.")

  print(f'''
{C}[{G}i{C}] Formas de operação: 
[{G}1{C}] IP.
[{G}2{C}] Nome.
[{G}3{C}] CPF.
[{G}4{C}] CEP.
[{G}5{C}] CNPJ.
[{G}6{C}] Placa.
[{G}7{C}] Telefone.
[{G}8{C}] YouTube.
[{G}9{C}] Atualizar.
[{G}10{C}] Novidades.
[{G}11{C}] Ajuda.
[{G}12{C}] {R}Sair.{C}
''')
  tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool == "1":
     clear()
     import ip
     ip.main()
  elif tool == "2":
     clear()
     import nome
     nome.main()
  elif tool == "3":
     clear()
     import cpf
     cpf.main()
  elif tool == "4":
     clear()
     import cep
     cep.main()
  elif tool == "5":
     clear()
     import cnpj
     cnpj.main()
  elif tool == "6":
     clear()
     import placa
     placa.main()
  elif tool == "7":
     clear()
     import telefone
     telefone.main()
  elif tool == "8":
     youtube()
     main()
  elif tool == "9":
     import update
  elif tool == "10":
     import novidades
     novidades.main()
  elif tool == "11":
     import ajuda
     ajuda.main()
  elif tool == "12":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     main()
main()

#Snuking/Somos uma legião. 2021 ©