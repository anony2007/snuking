#Snuking/Somos uma legião. 2021 ©

import requests, time, re
import os
import platform

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

clear()

#Snuking/Somos uma legião. 2021 ©

def main():
  clear()
  print("\n" + code_info + "Vizinhos.")
  print(f'''
{C}[{G}i{C}] Formas de operação: 

[{G}1{C}] Consultar CPF.
[{G}2{C}] Voltar.
[{G}3{C}] {R}Sair.{C}
''')
  tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool=='1':
    cpf=input(f'{C}[{G}*{C}] Informe o CPF a ser consultado (sem pontos ou traços): {B}')
    vizinhos(cpf)
    consultar(cpf)
  elif tool=='2':
    clear()
    import consulta
    consulta.main()
  elif tool=='3':
    clear()
    print(f'\n{G}Somos uma legião.{C}\n')
    exit()
  else:
    clear()
    print(f'{C}[{R}-{C}] Seleção inválida.')
    time.sleep(0.2)
    main()

def vizinhos(num):
   cpf = num
   nomes = requests.get(
r"https://tudosobretodos.info/{}".format(num))
   viz = re.findall(r"[A-Z]+ [A-Z ]+", nomes)
   clear()
   print("\n" + code_info + f"Vizinhos encontrados:{B}\n")
   print(viz)
   continuar(cpf)

def continuar(num):
    cpf = num
    opt = input(f'\n{C}[{G}+{C}] Deseja ver outros vizinhos?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        clear()
        vizinhos(cpf)
    else:
        consultar()

def consultar():
    opt = input(f'\n{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        clear()
        main()
    else:
        print(f"\n{G}Somos uma legião.{C}\n")
        exit()

header = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
                              'upgrade-insecure-requests': '1', 'save-data': 'on',
                              'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                              'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
                              'sec-fetch-user': '?1',
                              'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                              'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
                              'cookie': '_ga=GA1.2.971515152.1596724424',
                              'cookie': '_gid=GA1.2.109978583.1596724424'}

main()

