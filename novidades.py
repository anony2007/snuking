#Snuking/Somos uma legião. 2021 ©

import os
import platform
import time
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

def main():
  clear()
  print("\n" + code_info + "Novidades.")

  print("\n" + code_info + f"O banco para consultar nomes está atualmente com mais de {Y}3 mil e 800 CPFs.{C}")
  print("\n" + code_info + "Alguns bugs foram consertados:")
  print(code_result + "Agora limpa o terminal independente da plataforma")
  print("\n" + code_info + "Temos, no menu, a função para atualizar automaticamente e uma função para te ajudar em caso de dúvidas")
  print("\n" + code_info + "Menu inicial da ferramenta e da consulta por nome refeitos")
  print("\n" + code_info + "Tudo com a melhor praticidade e interface")
  print("\n" + code_error + 'Qualquer dúvida consulte a função "Ajuda" no menu inicial!')
  opt = input(f'\n{C}[{G}+{C}] Deseja ir para o menu inicial?[{G}s{C}/{R}n{C}]: ')
  if opt == 's':
        clear()
        import consulta
        consulta.main()
  else:
        clear()
        print(f"\n{G}Somos uma legião.{C}\n")
        exit()

main()