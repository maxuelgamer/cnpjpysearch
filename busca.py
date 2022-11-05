# CNPJ TESTE 32.301.253/0001-91
import requests
import time
import sys
    
def replace(cnpj):
    chars = "/.- "
    for char in chars:
        cnpj = cnpj.replace(char, "")
    request(cnpj)    
    
def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    total = len(iterable)
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    printProgressBar(0)
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    print()
     
def request(cnpj_tratado):
    resp = requests.get(f"https://receitaws.com.br/v1/cnpj/{cnpj_tratado}")
    items = list(range(0, 100))
    for item in progressBar(items, prefix = 'Progress:', suffix = 'Complete', length = 50):
        time.sleep(0.05)
    if resp.status_code == 200:
        time.sleep(2)
        resp_json = resp.json()
        if resp_json["status"] == "ERROR":
            print(resp_json["message"])
        else:    
            print(f'''
                        
                ==========================================================================      
                ╔══╗      ╔╗     ╔═══╗                ╔╗  ╔╗          ╔═══╗╔═╗ ╔╗╔═══╗  ╔╗
                ║╔╗║     ╔╝╚╗    ║╔═╗║                ║║ ╔╝╚╗         ║╔═╗║║║╚╗║║║╔═╗║  ║║
                ║╚╝╚╗╔══╗╚╗╔╝    ║║ ╚╝╔══╗╔═╗ ╔══╗╔╗╔╗║║ ╚╗╔╝╔══╗     ║║ ╚╝║╔╗╚╝║║╚═╝║  ║║
                ║╔═╗║║╔╗║ ║║     ║║ ╔╗║╔╗║║╔╗╗║══╣║║║║║║  ║║ ╚ ╗║     ║║ ╔╗║║╚╗║║║╔══╝╔╗║║
                ║╚═╝║║╚╝║ ║╚╗    ║╚═╝║║╚╝║║║║║╠══║║╚╝║║╚╗ ║╚╗║╚╝╚╗    ║╚═╝║║║ ║║║║║   ║╚╝║
                ╚═══╝╚══╝ ╚═╝    ╚═══╝╚══╝╚╝╚╝╚══╝╚══╝╚═╝ ╚═╝╚═══╝    ╚═══╝╚╝ ╚═╝╚╝   ╚══╝
                ==========================================================================
                
                ==========================  
                    RESULTADO CNPJ
                    {resp_json["cnpj"]}
                ==========================  
                Nome: {resp_json["nome"]}
                Telefone: {resp_json["telefone"]}
                Email: {resp_json["email"]}
                Data Abertura: {resp_json["abertura"]}
                Capital Social: {resp_json["capital_social"]}
                ==========================
                Endereço: Rua: {resp_json["logradouro"]} 
                Numero: {resp_json["numero"]}
                Cep: {resp_json["cep"]}
                Cidade {resp_json["municipio"]}
                ==========================
            ''')
    else:
        print("Aguarde alguns segundos e tente novamente!")    
        
if __name__ == "__main__":
    if sys.argv[1] == "-cnpj":
        replace(sys.argv[2])
