from desafio_vue_django.scrp_drogasil.scrap import pesquisa


def main():
    instancia=pesquisa.query("anador",pagina=2)#0
    print(len(instancia))
    instancia=pesquisa.query("dorflex")#24
    print(len(instancia))
    instancia=pesquisa.query("neosoro")#5
    print(len(instancia))
    instancia=pesquisa.query_quantidade("hidratante facial",quantidade=100)#100
    print(len(instancia))
    instancia=pesquisa.query_quantidade("protetor solar",quantidade=100)#100
    print(len(instancia))
    