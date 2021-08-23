"""
Irá verificar se houve os parâmetros passados corretamente e se houve algum pedido para o programa
Caso esteja procurando por vasculha de DNS, coloque DNS no final do código e no lugar de --url|-u, deixe:
    --dns | -d
"""
import argparse, sys,capa_dircognito

__name__ = "params"
# ======================================================================================================================#
parser = argparse.ArgumentParser(prog='DirCognito', formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=capa_dircognito.capa,
                                 epilog="""
===================================================================
https://github.com/Intern-Yago
maked by: Yago Victor

""")
# ======================================================================================================================#
if sys.argv[len(sys.argv) - 1] == "DNS":
    parser.add_argument('--dns', "-d", required=True, help="Definição do endereço DNS do servidor")
else:
    parser.add_argument("-u", '--url', required=True, help="Endereço url do site")
# ======================================================================================================================#
parser.add_argument("-w", '--wordlist', required=True,
                    help="Caminho para a wordlist do brute force na vasculha")
parser.add_argument("-e", "--extensao", help="Descoberta de arquivos com tais extensoes [Separe apenas por vírgula")
# ======================================================================================================================#
parser.add_argument('-o', '--output',help="Caso não queira perder a saída que o programa obteve, salve em um arquivo")
# ======================================================================================================================#
parser.add_argument('-v', '--version', action='version', version=f'%(prog)s 1.0')

args = parser.parse_args()
