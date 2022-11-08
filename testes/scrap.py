import sys
sys.path.insert(1, 'scrp_drogasil/')
from scrp_drogasil.scrap import pesquisa


def main():
    instancia=pesquisa.query("anador",pagina=2)
    print(len(instancia))
    instancia=pesquisa.query("dorflex")
    print(len(instancia))
    instancia=pesquisa.query("neosoro")
    print(len(instancia))
    instancia=pesquisa.query_quantidade("hidratante facial",quantidade=100)
    print(len(instancia))
    instancia=pesquisa.query_quantidade("protetor solar",quantidade=100)
    print(len(instancia))
    