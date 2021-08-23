import params, requests, defs, datetime
from bs4 import BeautifulSoup

__name__ = "dircognito"



# Váriaveis "globais"
argumentos = ""
nome_pagina = ""
wordlist = params.args.wordlist
link = defs.banner()
link = defs.protocolizacao(link)
cont = 0
print(link)
for l in link:
    if l == "/":
        cont += 1
    if cont == 2 and l != "/":
        nome_pagina += l
    if cont == 3:
        break

print(f'\nProcurando página: {nome_pagina}')
status = defs.verificando_levantado(link)
data = datetime.datetime.today()
if status == "ok":
    requisição = requests.get(link)
    soup = BeautifulSoup(requisição.content, 'html.parser')
    print(f"Site acessível {soup.head.contents[1].contents}")
    conteudo = defs.extracao_word(link, nome_pagina, wordlist, data)
    if params.args.output:
        if params.args.output == "default":
            defs.saida(conteudo)
        else:
            defs.saida(conteudo, params.args.output)
else:
    print("Falha na conexão com o link")
