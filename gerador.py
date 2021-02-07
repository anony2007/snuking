#Snuking/Somos uma legião. 2021 ©

import requests, time
import os, base64, re, json
import platform
from random import randint
from random import choice

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

a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
a=a.encode('ascii')
a=base64.b64decode(a)
a=a.decode('ascii')

#Snuking/Somos uma legião. 2021 ©

def Lemail():
    opt = input(f'\n{C}[{G}+{C}] Deseja {Y}gerar novamente{C} um {Y}email{C}?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        clear()
        email()
    else:
        again()

def Ltelefone():
    opt = input(f'\n{C}[{G}+{C}] Deseja {Y}gerar novamente{C} um {Y}telefone{C}?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        clear()
        telefone()
    else:
        again()

def Lregião():
    opt = input(f'\n{C}[{G}+{C}] Deseja {Y}gerar novamente{C} uma {Y}região{C}?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        região()
    else:
        again()

def Lestado():
    opt = input(f'\n{C}[{G}+{C}] Deseja {Y}gerar novamente{C} um {Y}Estado{C}?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        estado()
    else:
        again()

def Lcidade():
    opt = input(f'\n{C}[{G}+{C}] Deseja {Y}gerar novamente{C} um {Y}email{C}?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        email()
    else:
        again()

def Lcidade():
    opt = input(f'\n{C}[{G}+{C}] Deseja {Y}gerar novamente{C} uma {Y}cidade{C}?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        cidade()
    else:
        again()

def again():
    opt = input(f'\n{C}[{G}+{C}] Deseja voltar?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        clear()
        main()
    else:
        print(f"\n{G}Somos uma legião.{C}\n")
        exit()

def consultar_cep(cep):
    if len(cep) != 8:
        print(f"\n{R}CEP inválido/inexistente {C}\n")
        exit()
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    address_data = request.json()
    if 'erro' not in address_data:
        print()
        print(f"{C}[{G}i{C}] CEP encontrado.")
        print()
        print(f"CEP: {B}{address_data['cep']}{C}")
        print(f"ENDEREÇO: {B}{address_data['logradouro']}{C}")
        print(f"COMPLEMENTO: {B}{address_data['complemento']}{C}")
        print(f"BAIRRO: {B}{address_data['bairro']}{C}")
        print(f"CIDADE: {B}{address_data['localidade']}{C}")
        print(f"ESTADO: {B}{address_data['uf']}{C}")
        print(f"IBGE: {B}{address_data['ibge']}{C}")
        print(f"GIA: {B}{address_data['gia']}{C}")
        print(f"DDD: {B}{address_data['ddd']}{C}")
        print(f"SIAFI: {B}{address_data['siafi']}{C}")
        print()
    else:
        print(f'\n{R}{cep} é CEP inválido/inexistente{C}\n')
    print(code_result + "Concluído.")
    again()

def consultar(cpf):
  print(code_info + "Consultando o CPF gerado...")
  time.sleep(1.5)
  try:
    h={
    'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
    'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID; FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
    'Host': "www.juventudeweb.mte.gov.br"
    }
    r=requests.post(a, headers=h, data=f'acao=consultar%20cpf&cpf={cpf}&nocache=0.7636039437638835').text
    c = re.search('NRCEP="(.*?)"', r).group(1)
    print(f'''
{C}CPF: {B}{re.search('NRCPF="(.*?)"', r).group(1)}
{C}Nome: {B}{re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()}
{C}Nascimento: {B}{re.search('DTNASCIMENTO="(.*?)"', r).group(1)}
{C}Nome da Mae: {B}{re.search('NOMAE="(.*?)"', r).group(1).title()}
{C}Endereco: {B}{re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()}, {re.search('NRLOGRADOURO="(.*?)"', r).group(1)}
{C}Complemento: {B}{re.search('DSCOMPLEMENTO="(.*?)"', r).group(1).title()}
{C}Bairro: {B}{re.search('NOBAIRRO="(.*?)"', r).group(1).title()}
{C}Cidade: {B}{re.search('NOMUNICIPIO="(.*?)"', r).group(1).title()}-{re.search('SGUF="(.*?)"', r).group(1)}
{C}CEP: {B}{re.search('NRCEP="(.*?)"', r).group(1)}
''')
    print(code_info + "Consultando CEP...")
    time.sleep(1.5)
    consultar_cep(c)
  except(AttributeError):
    again()

def cpf():
  url = requests.get(
"http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a")
  res = url.json()
  cpf = res['data']['number']
  print(f"{C}CPF: {B}" + cpf)
  print(
f"{C}FORMATO: {B}" + res['data']['number_formatted'])
  print(f"{C}TIPO: {B}" + res['data']['message'] + C)
  consultar(cpf)

def endereço():
  clear()
  print("\n" + code_info + "Geografia.")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Tudo.
[{G}2{C}] Região.
[{G}3{C}] Estado.
[{G}4{C}] Cidade.
[{G}5{C}] CEP.
[{G}6{C}] Voltar.
[{G}7{C}] {R}Sair.{C}
''')
  tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool == "1":
     clear()
     completo()
     again()
  elif tool == "2":
     região()
     again()
  elif tool == "3":
     clear()
     estado()
     again()
  elif tool == "4":
     clear()
     cidade()
     again()
  elif tool == "5":
     clear()
     print("sem")
     main()
  elif tool == "6":
     main()
  elif tool == "7":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     endereço()

def outro():
    opt = input(f'\n{C}[{G}+{C}] Deseja {Y}escolher outra região{C}?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        manual()
    else:
        again()

def Wregião(re):
  clear()
  url1 = requests.get(
f"http://geradorapp.com/api/v1/states/{re}?token=4f8d9149be4858c837b8b38f5c0d194a")
  res1 = url1.json()
  data = res1['data']
  print("\n" + code_info + f"Região:{Y} {res1['data'][0]['region']['name']} ({res1['data'][0]['region']['abbreviation']})\n")
  for i in range(len(data)):
    print(f"{C}ESTADO:{B}",
    res1['data'][i]['name'],f"({res1['data'][i]['abbreviation']})")
    print(f"{C}CAPITAL:{B}",
    res1['data'][i]['capital'])
    print(f"{C}CÓDIGO DO ESTADO:{B}",
    res1['data'][i]['code_uf'])
    print("\n")
  outro()

def manual():
  clear()
  print("\n" + code_info + "Endereço (tudo).")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{Y}+{C}] Selecione uma região:
[{G}1{C}] Norte (N).
[{G}2{C}] Nordeste (NE).
[{G}3{C}] Centro-Oeste (CO).
[{G}4{C}] Sudeste (SE).
[{G}5{C}] Sul (S).
[{G}6{C}] voltar.
[{G}7{C}] {R}Sair.{C}
''')
  tool=input(f'{C}[{G}+{C}] Região:{B} ')
  if tool == "1" or tool == "n" or tool == "N" or tool == "norte" or tool == "Norte":
     Wregião("n")
  elif tool == "2" or tool == "ne" or tool == "nordeste" or tool == "Nordeste":
     Wregião("ne")
  elif tool == "3" or tool == "co" or tool == "CO" or tool == "centro-oeste" or tool == "Centro-Oeste":
     Wregião("co")
  elif tool == "4" or tool == "se" or tool == "SE" or tool == "sudeste" or tool == "Sudeste":
     Wregião("se")
  elif tool == "5" or tool == "s" or tool == "S" or tool == "sul" or tool == "Sul":
     Wregião("s")
  elif tool == "6":
     completo()
  elif tool == "7":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     manual()

def automático():
  regiões = ['N', 'NE', 'CO', 'SE', 'S']
  r = choice(regiões)
  Wregião(r)

def completo():
  clear()
  print("\n" + code_info + "Geografia (tudo).")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{Y}+{C}] Selecione o modo:
[{G}1{C}] Automático.
[{G}2{C}] Manual.
[{G}3{C}] voltar.
[{G}4{C}] {R}Sair.{C}
''')
  tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool == "1":
     clear()
     automático()
  elif tool == "2":
     clear()
     manual()
  elif tool == "3":
     clear()
     endereço()
  elif tool == "4":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     completo()

def região():
  clear()
  print("\n" + code_info + "Região.\n")
  url1 = requests.get(
f"http://geradorapp.com/api/v1/regions?token=4f8d9149be4858c837b8b38f5c0d194a")
  res = url1.json()
  n = 4
  i = randint(0, n)
  print(f"{C}REGIÃO:{B}",
res['data'][i]['name'],f"({res['data'][i]['abbreviation']})")
  Lregião()

def estado():
  clear()
  print("\n" + code_info + "Estado.\n")
  url1 = requests.get(
"http://geradorapp.com/api/v1/states?token=4f8d9149be4858c837b8b38f5c0d194a")
  res1 = url1.json()
  n = 26
  i = int(randint(0,n))
  print(f"{C}ESTADO:{B}",
res1['data'][i]['name'],f"({res1['data'][i]['abbreviation']})")
  print(f"{C}CAPITAL:{B}",
res1['data'][i]['capital'])
  print(f"{C}REGIÃO:{B}", res1['data'][i]['region']['name'],f"({res1['data'][i]['region']['abbreviation']})")
  print(f"{C}CÓDIGO DO ESTADO:{B}", res1['data'][i]['code_uf'])
  Lestado()

def cidade():
  clear()
  print("\n" + code_info + "Cidade.\n")
  url2 = requests.get(
"http://geradorapp.com/api/v1/cities?token=4f8d9149be4858c837b8b38f5c0d194a")
  res2 = url2.json()
  n = 5563
  i = int(randint(0,n))
  print(f"{C}CIDADE:{B}",
  res2['data'][i]['name'])
  print(f"{C}CÓDIGO DO MUNICÍPIO:{B}",
  res2['data'][i]['code_mun'])
  print(f"{C}ESTADO:{B}",
  res2['data'][i]['state']['name'],f"({res2['data'][i]['state']['abbreviation']})")
  print(f"{C}CAPITAL:{B}",
  res2['data'][i]['state']['capital'])
  print(f"{C}CÓDIGO DO ESTADO:{B}",
  res2['data'][i]['state']['code_uf'])
  Lcidade()

def consultar_cnpj(cpnj1):
    print(f"{C}[{Y}i{C}] Receita Federal: ")
    url1='https://www.receitaws.com.br/v1/cnpj/{}'.format(cpnj1)
    res=requests.get(url1);req1=res.json()
                                         
    br=f"\n{C}[{G}i{C}] CNPJ encontrado.\nDATA_SITUAÇÃO: {B}{req1['data_situacao']}{C}\nMOTIVO_SITUAÇÃO: {B}{req1['motivo_situacao']}{C}\nCOMPLEMENTO: {B}{req1['complemento']}{C}\nTIPO: {B}{req1['tipo']}{C}\nNOME: {B}{req1['nome']}{C}\nTELEFONE: {B}{req1['telefone']}{C}\nSITUAÇÃO: {B}{req1['situacao']}{C}\nBAIRRO: {B}{req1['bairro']}{C}\nENDEREÇO: {B}{req1['logradouro']}{C}\nNÚMERO: {B}{req1['numero']}{C}\nCEP: {B}{req1['cep']}{C}\nMUNICÍPIO: {B}{req1['municipio']}{C}\nFANTASIA: {B}{req1['fantasia']}{C}\nPORTE: {B}{req1['porte']}{C}\nABERTURA: {B}{req1['abertura']}{C}\nNATUREZA_JUDICIAL: {B}{req1['natureza_juridica']}{C}\nUF: {B}{req1['uf']}{C}\nCNPJ: {B}{req1['cnpj']}{C}\nÚLTIMA_ATUALIZAÇÃO: {B}{req1['ultima_atualizacao']}{C}\nSTATUS: {B}{req1['status']}{C}\nEMAIL: {B}{req1['email']}{C}\nEFR: {B}{req1['efr']}{C}\nSITUAÇÃO_ESPECIAL: {B}{req1['situacao_especial']}{C}\nDATA_SITUAÇÃO_ESPECIAL:{B}{req1['data_situacao_especial']}{C}\nCAPITAL_SOCIAL: {B}{req1['capital_social']}{C}\nATIVIDADE_PRINCIPAL: {B}{req1['atividade_principal'][0]['text']}{C}\nATIVIDADES_SECUNDÁRIAS:{B}"
    print(br)
    n = int(len(req1['atividades_secundarias']))
    for i in range(0, n):
       print(code_result + B + req1['atividades_secundarias'][i]['text'] + C)
    again()

def cnpj():
  url = requests.get(
"http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a")
  res3 = url.json()
  print(f"{C}CNPJ: {B}" + res3['data']['number'])
  print(f"{C}FORMATO: {B}" + res3['data']['number_formatted'])
  print(f"{C}TIPO: {B}" + res3['data']['message'])
  cnpj = res3['data']['number']
  print(code_info + "Consultando CNPJ...")
  time.sleep(1.5)
  consultar_cnpj(cnpj)


def placa():
  url = requests.get(
"http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a")
  res = url.json()
  print(f"CPF: {B}" + res['number'])
  print(f"{C}FORMATO: {B}" + res['number'])
  print(f"{C}TIPO: {B}" + res['number'])

def telefone():
  url = requests.get(
"http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a")
  res = url.json()
  print(f"CPF: {B}" + res['data']['number'])
  print(f"{C}FORMATO: {B}" + res['number'])
  print(f"{C}TIPO: {B}" + res['number'])

def bin_c(num):
   url = requests.get(f"https://binlist.io/lookup/{num}/")
   res = url.content
   bin = json.loads(res)
   if bin["success"] == True:
      print("\n" + code_info + "Resultado:\n")
      print(f"{C}BIN: {B}" + bin["number"]["iin"])
      print(f"{C}NOME: {B}" + bin["bank"]["name"])
      print(f"{C}BANDEIRA: {B}" + bin["scheme"])
      print(f"{C}CATEGORIA: {B}" + bin["category"])
      print(f"{C}TIPO: {B}" + bin["type"])
      print(f"{C}PAÍS: {B}" + bin["country"]["name"] + f'({bin["country"]["alpha2"]})')
      print(f"{C}TELEFONE: {B}" + bin["bank"]["phone"])
      print(f"{C}URL: {B}" + bin["bank"]["url"] + f"{C}")
      Lbin()
   else:
       while bin["success"] != True:
                i = str(randint(0, 9))
                k = str(randint(0, 9))
                m = str(randint(0, 9))
                l = str(randint(0, 9))
                i2 = str(randint(0, 9))
                k2 = str(randint(0, 9))
                time.sleep(1)
                bin =i+k+m+l+i2+k2
                bin_c(bin)

def Lnome():
    opt = input(f'\n{C}[{G}+{C}] Deseja {Y}gerar novamente{C} um {Y}nome{C}?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        clear()
        nome()
    else:
        again()

def Lbin():
    opt = input(f'\n{C}[{G}+{C}] Deseja {Y}gerar novamente{C} uma {Y}BIN{C}?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        clear()
        bin()
    else:
        again()

def Lcns():
    opt = input(f'\n{C}[{G}+{C}] Deseja {Y}gerar novamente{C} um {Y}CNS{C}?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        clear()
        cns()
    else:
        again()

def bin():
  i = str(randint(0, 9))
  k = str(randint(0, 9))
  m = str(randint(0, 9))
  l = str(randint(0, 9))
  i2 = str(randint(0, 9))
  k2 = str(randint(0, 9))
  time.sleep(1)
  bin =i+k+m+l+i2+k2
  bin_c(bin)
  Lbin()

def ip():
  i = str(randint(0, 9))
  k = str(randint(0, 9))
  m = str(randint(0, 9))
  l = str(randint(0, 9))
  i2 = str(randint(0, 9))
  k2 = str(randint(0, 9))
  m2 = str(randint(0, 9))
  l2 = str(randint(0, 9))
  i3 = str(randint(0, 9))
  k3 = str(randint(0, 9))
  m3 = str(randint(0, 9))
  l3 = str(randint(0, 9))
  ip ="172."+l+i2+k2+"."+m2+l2+i3+"."+k3
  consultar_ip(ip)

def consultar_ip(ip):
 clear()
 api = requests.get(f"https://ipapi.co/{ip}/json")
 resultado = api.json()
 if ip in resultado:
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
  localizar(ip)
 else:
     while ip not in resultado:
            i = str(randint(0, 5))
            k = str(randint(0, 5))
            m = str(randint(0, 5))
            l = str(randint(0, 5))
            i2 = str(randint(0, 5))
            k2 = str(randint(0, 5))
            m2 = str(randint(0, 5))
            l2 = str(randint(0, 5))
            i3 = str(randint(0, 5))
            k3 = str(randint(0, 5))
            m3 = str(randint(0, 5))
            l3 = str(randint(0, 5))
            ip ="172."+"158"+"."+m2+l2+i3+"."+k3
            print(ip)
            consultar_ip(ip)


def localizar(ip):
  api = requests.get("https://ipapi.co/json")
  resultado = api.json()
  print(code_info + "Google Maps")
  print(code_info + "Gerando URL...")
  time.sleep(0.5)
  print ('\n' + code_result + f'Google Maps: {Y}' + 'https://www.google.com/maps/place/' + f"{resultado['latitude']}" + '+' + f"{resultado['longitude']}")
  again()

def pessoa():
  pais="BR"
  pessoa = requests.get("https://randomuser.me/API/?nat="+pais).json()
  sexo = pessoa['results'][0]['gender']
  if sexo == 'female':
      sexo2 = sexo.replace('female', 'Mulher')
      sexo3 = 'F'
  else:
      sexo2 = sexo.replace('male', 'Homem')
      sexo3 = 'M'
  print("\n" + code_info + "Encontrado:\n")
  print(f"{C}NOME:{B}", pessoa['results'][0]['name']['first'], pessoa['results'][0]['name']['last'])
  print(f"{C}GÊNERO:{B}", sexo2 + f" ({sexo3})")
  print(f"{C}TÍTULO:{B}", pessoa['results'][0]['name']['title'])
  print(f"{C}DATA DE NASCIMENTO:{B}", pessoa['results'][0]['dob']['date'][0:10])
  print(f"{C}IDADE:{B}", pessoa['results'][0]['dob']['age'])
  print(f"{C}TELEFONE:{B}", pessoa['results'][0]['name']['first'], pessoa['results'][0]['phone'])
  print(f"{C}CELULAR:{B}", pessoa['results'][0]['name']['first'], pessoa['results'][0]['cell'])
  print(f"{C}PAÍS:{B}", pessoa['results'][0]['location']['country'])
  print(f"{C}ESTADO:{B}", pessoa['results'][0]['location']['state'])
  print(f"{C}CIDADE:{B}", pessoa['results'][0]['location']['city'])
  print(f"{C}RUA:{B}", pessoa['results'][0]['location']['street']['name'])
  print(f"{C}NÚMERO:{B}", pessoa['results'][0]['location']['street']['number'])
  print(f"{C}CEP:{B}", pessoa['results'][0]['location']['postcode'])
  print(f"{C}LATITUDE:{B}", pessoa['results'][0]['location']['coordinates']['latitude'])
  print(f"{C}LONGITUDE:{B}", pessoa['results'][0]['location']['coordinates']['longitude'])
  print(f"{C}FUSO HORÁRIO:{B}", pessoa['results'][0]['location']['timezone']['description'], f" ({pessoa['results'][0]['location']['timezone']['offset']})")
  print("\n" + code_info + "Rede sociais da pessoa:")
  time.sleep(1)
  print(f"{C}USUÁRIO:{B}", pessoa['results'][0]['login']['username'])
  print(f"{C}EMAIL:{B}", pessoa['results'][0]['email'])
  print(f"{C}SENHA:{B}", pessoa['results'][0]['login']['password'])
  again()

def email():
  pais="BR"
  pessoa = requests.get("https://randomuser.me/API/?nat="+pais).json()
  print(f"{C}USUÁRIO:{B}", pessoa['results'][0]['login']['username'])
  print(f"{C}EMAIL:{B}", pessoa['results'][0]['email'])
  print(f"{C}SENHA:{B}", pessoa['results'][0]['login']['password'])
  Lemail()


def nome():
  pais="BR"
  pessoa = requests.get("https://randomuser.me/API/?nat="+pais).json()
  sexo = pessoa['results'][0]['gender']
  if sexo == 'female':
      sexo2 = sexo.replace('female', 'Mulher')
      sexo3 = 'F'
  else:
      sexo2 = sexo.replace('male', 'Homem')
      sexo3 = 'M'
  print(f"{C}NOME:{B}", pessoa['results'][0]['name']['first'], pessoa['results'][0]['name']['last'])
  print(f"{C}GÊNERO:{B}", sexo2 + f" ({sexo3})")
  Lnome()

def cns():
  cns = requests.get(
"http://geradorapp.com/api/v1/cns/generate?token=4f8d9149be4858c837b8b38f5c0d194a"
).json()
  mensagem = cns['data']['message']
  cns = cns['data']['number']
  print(f"{C}CNS: {B}" + cns)
  print(f"{C}TIPO: {B}" + mensagem + C)
  Lcns()


def telefone():
  pais="BR"
  pessoa = requests.get("https://randomuser.me/API/?nat="+pais).json()
  print(f"{C}TELEFONE:{B}", pessoa['results'][0]['name']['first'], pessoa['results'][0]['phone'])
  print(f"{C}CELULAR:{B}", pessoa['results'][0]['name']['first'], pessoa['results'][0]['cell'])
  Ltelefone()

def main():
  clear()

  print("\n" + code_info + "Gerador.")

  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Pessoa.
[{G}2{C}] Nome.
[{G}3{C}] CPF.
[{G}4{C}] Geografia.
[{G}5{C}] CNPJ.
[{G}6{C}] Telefone.
[{G}7{C}] Email.
[{G}8{C}] BIN.
[{G}9{C}] CNS.

[{G}99{C}] Voltar.
[{G}00{C}] {R}Sair.{C}
''')
  tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool == "1":
     clear()
     pessoa()
  elif tool == "2":
     clear()
     nome()
  elif tool == "3":
     clear()
     cpf()
  elif tool == "4":
     clear()
     endereço()
  elif tool == "5":
     clear()
     cnpj()
  elif tool == "6":
     clear()
     telefone()
  elif tool == "7":
     clear()
     email()
  elif tool == "8":
     clear()
     print(code_info + "Gerando BIN...")
     bin()
  elif tool == "9":
     clear()
     cns()
  elif tool == "99":
     import consulta
     consulta.main()
  elif tool == "00":
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