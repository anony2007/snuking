#Snuking/Somos uma legião. 2021 ©

import os, requests, time
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
code_details = C + '[' + Y + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

def main():
  clear()
  api = requests.get("https://ipapi.co/json")
  resultado = api.json()
  ip = resultado['ip']
  print("\n" + code_info + "IP.")
  print(code_details + f"Seu IP: {ip}")
  print(f'''
{C}[{G}i{C}] Formas de operação: 

[{G}1{C}] Consultar meu IP.
[{G}2{C}] Consultar IP.
[{G}3{C}] Localizar.
[{G}4{C}] Voltar.
[{G}5{C}] {R}Sair.{C}
''')
  tool = input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool == "1":
     consultar(ip)
  elif tool == "2":
     ip=input(f'{C}[{G}*{C}] Informe o IP a ser consultado (COM pontos): {B}')
     consultar(ip)
  elif tool == "3":
     ip=input(f'{C}[{G}*{C}] Informe o IP a ser consultado (COM pontos): {B}')
     clear()
     localizar(ip)
  elif tool == "4":
     import consulta
     consulta.main()
  elif tool == "5":
      clear()
      print(f"\n{G}Somos uma legião.{C}\n")
      exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     main()


def again():
  opt = input("\n" + f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ')
  if opt == "s":
      clear()
      main()
  elif opt == "n":
      print(f"\n{G}Somos uma legião.{C}\n")
      exit()
  else:
      clear()
      print(f'{C}[{R}-{C}] Seleção inválida.')
      time.sleep(0.2)
      exit()

#Snuking/Somos uma legião. 2021 ©

def maps(ip):
  opt = input("\n" + f'{C}[{G}+{C}] Deseja localizar no {Y}Google Maps{C}?[{G}s{C}/{R}n{C}]: ')
  if opt == "s":
      localizar(ip)
  elif opt == "n":
      again()
  else:
      print(f'{C}[{R}-{C}] Seleção inválida.')
      time.sleep(0.2)
      exit()

#Snuking/Somos uma legião. 2021 ©

def consultar(ip):
  clear()
  api = requests.get(f"https://ipapi.co/{ip}/json")
  resultado = api.json()
  ip = resultado['ip']
  print("\n" + f"{C}Endereço de IP: {B}{resultado['ip']}{C}")
  print(f"Cidade: {B}{resultado['city']}{C}")
  print(f"Região: {B}{resultado['region']}{C}")
  print(f"País: {B}{resultado['country_name']}{C}")
  print(f"Abreviação do país: {B}{resultado['country']}{C}")
  print(f"Capital do país: {B}{resultado['country_capital']}{C}")
  print(f"População do país: {B}{resultado['country_population']}{C}")
  print(f"Moeda: {B}{resultado['currency']}{C}")
  print(f"Nome da moeda: {B}{resultado['currency_name']}{C}")
  print(f"Código da região: {B}{resultado['region_code']}{C}")
  print(f"Código postal: {B}{resultado['postal']}{C}")
  print(f"Código do país: {B}{resultado['country_code']}{C}")
  print(f"Código do país ISO3: {B}{resultado['country_code_iso3']}{C}")
  print(f"Área do país: {B}{resultado['country_area']}{C}")
  print(f"País TLD: {B}{resultado['country_tld']}{C}")
  print(f"Código área: {B}{resultado['country_area']}{C}")
  print(f"Código do continente: {B}{resultado['continent_code']}{C}")
  print(f"União Européia: {B}{resultado['in_eu']}{C}")
  print(f"Latitude: {B}{resultado['latitude']}{C}")
  print(f"Longitude: {B}{resultado['longitude']}{C}")
  print(f"Fuso horário: {B}{resultado['timezone']}{C}")
  print(f"Código de Chamada: {B}{resultado['country_calling_code']}{C}")
  print(f"línguas: {B}{resultado['languages']}{C}")
  print(f"ASN: {B}{resultado['asn']}{C}")
  print(f"ORG: {B}{resultado['org']}{C}")
  print(f"Deslocamento UTF: {B}{resultado['utc_offset']}{C}")
  print(f"Versão: {B}{resultado['version']}{C}")
  maps(ip)


def localizar(ip):
  api = requests.get("https://ipapi.co/json")
  resultado = api.json()
  print(code_info + "Google Maps")
  print(code_info + "Gerando URL...")
  time.sleep(0.5)
  print ('\n' + code_result + f'Google Maps: {Y}' + 'https://www.google.com/maps/place/' + f"{resultado['latitude']}" + '+' + f"{resultado['longitude']}")
  again()


main()

#Snuking/Somos uma legião. 2021 ©
