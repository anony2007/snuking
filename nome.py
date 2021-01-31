#Snuking/Somos uma legião. 2021 ©

import re
import pprint
import time
import os

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

arquivo = r'banco.txt'
ler = open(arquivo, encoding="UTF-8")
conteudo_arquivo = ler.read()

def main():
   os.system("clear")
   print("\n" + code_info + "Nome.")
   print(f'''
{C}[{G}i{C}] Formas de operação: 

[{G}1{C}] Banco de dados.
[{G}2{C}] Todos os nomes.
[{G}3{C}] Consultar nome.
[{G}4{C}] Buscar nome.
[{G}5{C}] Voltar.
[{G}6{C}] {R}Sair.{C}
''')
   tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
   if tool == "1":
        banco()
   elif tool == "2":
        nomes()
   elif tool == "3":
        consultar()
   elif tool == "4":
        buscar()
   elif tool == "5":
        import consulta
        consulta.main()
   elif tool == "6":
        os.system("clear")
        print(f'\n{G}Somos uma legião.{C}\n')
        exit()
   else:
        os.system("clear")
        print(f'{C}[{R}-{C}] Seleção inválida.')
        time.sleep(0.2)
        main()

def nova():
    nova=input('\n' + f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
    if nova=='s' or nova=='sim':
       os.system("clear")
       main()
    else:
        os.system("clear")
        print(f'\n{G}Somos uma legião.{C}\n')
        exit()

def nova2():
    nova=input('\n' + f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
    if nova=='s' or nova=='sim':
       os.system("clear")
       main()
    else:
        print(f'\n{G}Somos uma legião.{C}\n')
        exit()

def banco():
    filtro = r'[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ \S]+'
    banco = re.findall(filtro, conteudo_arquivo)
    converted_list = [x.upper() for x in banco]
    os.system("clear")
    print("\n" + code_info + f"Banco de dados (Nome completo; CPF; Data de nascimento).{B}\n")
    pprint.pprint(converted_list)
    print("\n" + code_info + "Banco de dados (nome completo; CPF; Data de nascimento).")
    print(f'{code_result}Resultado:{G}', len(converted_list), f"{C}")
    nova()

def nomes():
    i = 1;
    filtro = r'[A-Za-zâáàâãêéèêíïóôõöúçñÂÁÀÂÃÊÉÈÍÏÓÔÕÖÚÇÑ ]+'
    nomes = re.findall(filtro, conteudo_arquivo)
    while i < len(nomes):
       del nomes[i]
       i=i+1
    converted_list = [x.upper() for x in nomes]
    os.system("clear")
    print("\n" + code_info + f"Banco de dados (todos os nomes).{B}\n")
    pprint.pprint(converted_list)
    print("\n" + code_info + "Banco de dados (todos os nomes).")
    nova()

def buscar():
    name = input(f'{C}[{G}*{C}] Informe o nome ({R}recomendação:{C} nome completo): {B}').upper()
    filtro = f'{name}[A-Za-zâáàâãêéèêíïóôõöúçñÂÁÀÂÃÊÉÈÍÏÓÔÕÖÚÇÑ ]+'
    names = re.findall(filtro, conteudo_arquivo)
    converted_list = [x.upper() for x in names]
    os.system("clear")
    print("\n" + code_info + "Encontrados:\n")
    pprint.pprint(converted_list)
    print("\n" + code_info + "Banco de dados (Nome completo).")
    print(f'{code_result}Resultado:{G}', len(converted_list), f"{C}")
    nova()

def consultar():
    name = input(f'{C}[{G}*{C}] Informe o nome ({R}recomendação:{C} nome completo): {B}').upper()
    filtro = f'{name}[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ \S]+'
    banco = re.findall(filtro, conteudo_arquivo)
    converted_list = [x.upper() for x in banco]
    os.system("clear")
    print("\n" + code_info + "Encontrados:\n")
    pprint.pprint(converted_list)
    print("\n" + code_info + "Banco de dados (Nome completo; CPF; Data de nascimento).")
    print(f'{code_result}Resultado:{G}', len(converted_list), f"{C}")
    nova2()

main()