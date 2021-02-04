import requests, urllib3
import os
import time
import platform

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

urllib3.disable_warnings()

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

clear()

def main():
 clear()
 print("\n" + code_info + "Placa.")
 print(f'''
{C}[{G}i{C}] Formas de operação: 

[{G}1{C}] Consultar placa.
[{G}2{C}] Voltar.
[{G}3{C}] {R}Sair.{C}
''')

 tool=input(code_result + f'Selecione a forma de operação: {B}')
 if tool=='1':
    placa = input(code_details + f"Informe a placa (sem traço):{B} ")
    if len(placa) != 7:
        clear()
        print(code_error + f"\n{R}Placa inválida/inexistente. {C}\n")
        main()
    else:
        banco = requests.get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False)
        resultado = banco.json()
        print(code_info + "Encontrando a placa...")
        clear()
        print(f"{C}Ano: {B}{resultado['ano']}{C}")
        print(f"Data: {B}{resultado['data']}{C}")
        print(f"Modelo: {B}{resultado['modelo']}{C}")
        print(f"Ano do modelo: {B}{resultado['anoModelo']}{C}")
        print(f"Cor: {B}{resultado['cor']}{C}")
        print(f"Marca: {B}{resultado['marca']}{C}")
        print(f"Roubo/furto: {B}{resultado['dataAtualizacaoRouboFurto']}{C}")
        print(f"Situação: {B}{resultado['situacao']}{C}")
        print(f"Placa: {B}{resultado['placa']}{C}")
        print(f"Chassi: {B}{resultado['chassi']}{C}")
        print(f"UF: {B}{resultado['uf']}{C}")
        print(f"Município: {B}{resultado['municipio']}{C}")
        print(f"Modificada em: {B}{resultado['dataAtualizacaoCaracteristicasVeiculo']}{C}")
        print(f"Alarme atualizado: {B}{resultado['dataAtualizacaoAlarme']}{C}")
        print(f"Mensagem de retorno: {B}{resultado['mensagemRetorno']}{C}")
        print(f"Código de retorno: {B}{resultado['codigoRetorno']}{C}")

        nova=input('\n' + f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
        if nova=='s' or nova=='sim':
           clear()
           print(code_info + "Espere 60 segundos ou haverá erros")
           main()
        else:
          print(f'\n{G}Somos uma legião.{C}\n')
          exit()

 elif tool == "2":
        clear()
        import consulta
        consulta.main()
 elif tool == "3":
        clear()
        print(f'\n{G}Somos uma legião.{C}\n')
        exit()
 else:
        clear()
        print(code_error + "Seleção inválida.")
        time.sleep(0.2)
        main()


main()