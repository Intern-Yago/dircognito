import platform,os,urllib.request as url, params, capa_dircognito
# Variáveis
protocolos_rede = ["http", "https", "smtp", "ftp", "pop"]
cont = 0

def layout(name_site, wordlist, data):
    initial_layout = f"""
{SO()} {platform.version()}|{os.getlogin()}
{data}
======================
  Site    :{name_site}
  Wodlist :{wordlist}
======================"""
    return initial_layout
"""
Arquivo que irá armazenar todas as funções no intuito de organizar de uma melhor forma para não ficar 
bagunça no código principal
"""

# -------------Funções-------------#
# SO
def SO():
    sistema = platform.system()
    return sistema


SO()


# Visualização do banner
def banner():
    """
    --> Demonstração do banner da ferramenta

    :return:O retorno é o link oferecido pelo usuário
    """

    print(capa_dircognito.logo)
    link = params.args.url
    return link


# Acessibilidade do site
def verificando_levantado(link):
    """
    --> Análise para saber se o site indicado está ou não na rede ou é possível acessar pelo seu acesso

    :param link: Link do site que o usuário quer fazer a verificação
    :return: Retorna o estado atual do link oferecido, se está permitido o uso ou não
    """

    try:
        url.urlopen(link)
        status = "ok"
    except:
        status = "error"
        return status
    else:
        return status


# Protocolizar link
def protocolizacao(link):
    """
    --> Caso o usuário não forneça o protocolo do link oferecido, esta função irá colocar de acordo com a permissão

    :param link: Link do site
    :return: Link com o protocolo na frente
    """

    global protocolos_rede, cont
    for protols in protocolos_rede:
        if protols not in link[:5]:
            cont += 1
    if cont == 5:
        protocolo = input(
            "\n[Caso não saiba, basta pressionar enter e será usado o http]\nQual é o protocolo?\n>").lower()
        if protocolo == "":
            protocolo = "http"
            print("Selecionado -> http")
        else:
            while protocolo not in protocolos_rede:
                print("\nSelecione os protocolos disponíveis")
                print(protocolos_rede)
                protocolo = input("Diga o seu protocolo\n:")
            print(f"Selecionado -> {protocolo}")
        link = link[:0].join(f"{protocolo}://") + link
    return link


# Extração da wordlist

def extracao_word(link, name_site_layout, wordlist_layout, data_layout):
    word = params.args.wordlist
    try:
        files = open(word, "r")
        arquivo = open(word, "r")
    except FileNotFoundError or FileExistsError:
        print("Este arquivo não existe ou foi escrito errado")
        exit()
    else:
        url = link
        const = ""
        contador_final = len(arquivo.readlines())
        contagem = 1
        for linha in files.readlines():
            print(capa_dircognito.logo)
            print(layout(name_site_layout, wordlist_layout, data_layout))
            print(f"{contagem} {contador_final}")
            print(const)
            print(linha)
            contagem += 1
            link += f"/{linha}"
            status = verificando_levantado(link)
            if status == "ok":
                const += f"\n{linha}\n"
            link = url
            if contagem <= contador_final:
                os.system("cls")
        conteudo = "Dircognito"+layout(name_site_layout, wordlist_layout, data_layout) + const
        return conteudo


# Criação do arquivo de saída
conta = 0
def saida(conteudo, path="dircognito\\rel.txt"):
    global conta
    """
    Esta função serve para criar um arquivo com a saída que o programa obteve

    :param path: Para a criação é necessário o parâmetro do caminho onde será criado o arquivo |
    Por padrão ele já vem com um diretório dircognito e um rel em texto
    """
    if conta >= 2:
        print("ERROR[Arquivo padrão já criado]")
        print("Indique outro arquivo ou delete")
        exit()
    else:
        def directory(dir_):
            try:
                os.system(f"mkdir {dir_}")
            except:
                Exception()
            else:
                saida(conteudo, path)

        if path.count("\\") > 1 or path.count("/") > 1:
            print(
                "ERROR[Programa ainda em desenvolvimento]\nAinda não aceitamos caminho desta forma. Caminho default "
                "criado")
            saida(conteudo)
            exit()
        if "\\" in path or "/" in path:
            if "\\" in path:
                divisor = path.index("\\")
            else:
                divisor = path.index("/")
            dir = path[:divisor]
            if dir == ".":
                dir = os.getcwd()
            if not os.path.exists(dir):
                directory(dir)
            else:
                if not os.path.exists(path):
                    try:
                        file_ = open(path, "w+")
                    except:
                        print("Arquivo já existente!, Criando default")
                        conta += 1
                        saida(conteudo)
                    else:
                        file_.write(conteudo)
                else:
                    print("Arquivo já existente! Criando default")
                    conta+=1
                    saida(conteudo)
        else:
            if not os.path.exists(path):
                try:
                    file_ = open(path, "w+")
                except:
                    if conta == 1:
                        print("Arquivo padrão já existente")
                    else:
                        print("Arquivo já existente! Criando default")
                    conta += 1
                    saida(conteudo)
                else:
                    file_.write(conteudo)
            else:
                if conta == 1:
                    print("Arquivo padrão já existente")
                else:
                    print("Arquivo já existente! Criando default")
                conta += 1
                saida(conteudo)
# -----------Fim funções-----------#
