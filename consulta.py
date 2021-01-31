#Snuking/Somos uma legião. 2021 ©

import requests, time
import os


os.system("clear")
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
os.system("clear")

#Snuking/Somos uma legião. 2021 ©

def main():
  os.system("clear")
  print(f'''{G}
\n
.----.______
|           |
|    ___________
|   /          /
|  /          /
| /          /
|/__________/
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
[{G}8{C}] {R}Sair.{C}
''')
  tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool == "1":
     os.system('clear')
     import ip
     ip.main()
  elif tool == "2":
     os.system('clear')
     import nome
     nome.main()
  elif tool == "3":
     os.system('clear')
     import cpf
     cpf.main()
  elif tool == "4":
     os.system('clear')
     import cep
     cep.main()
  elif tool == "5":
     os.system('clear')
     import cnpj
     cnpj.main()
  elif tool == "6":
     os.system('clear')
     import placa
     placa.main()
  elif tool == "7":
     os.system('clear')
     import telefone
     telefone.main()
  elif tool == "8":
     os.system("clear")
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     os.system("clear")
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     main()
main()

#Snuking/Somos uma legião. 2021 ©