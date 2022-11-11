from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json

class pesquisa:
    @staticmethod
    def get_request(url, render = False):
        session = HTMLSession()
        res = session.get(url)
        try:
            res.raise_for_status()
        except ValueError as e:
            raise('Dead link')
        if render:
            res.html.render(sleep = 3, timeout = 60)
        return res.html.raw_html


    
    @staticmethod
    def query(palavrasChave:str,pagina:int=0):
        retorno=""
        keywords=palavrasChave.split(" ")
        url="https://www.drogasil.com.br/search?w="
        for keyword in keywords:
            url+=keyword
            if keyword != keywords[-1]:
                url+="+"
        if pagina !=0:
            url+="&p="+str(pagina)
        html_doc=pesquisa.get_request(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        json_=json.loads(soup.select('script',id="__NEXT_DATA__",type="application/json")[-1].contents[0])
        produtos=json_['props']["pageProps"]["initialData"]["products"]
        produtos_processados=[]
        for produto in produtos:
            produto_processado={}
            produto_processado['nome']=produto["name"]
            produto_processado['imagem']=produto['image']
            produto_processado['categoria']=produto['subcategory']
            produto_processado['dosagem']=produto['dosage']
            produto_processado['quantidade']=produto['qty']
            produto_processado['link']="https://"+str(produto['urlKey'][2:])
            produto_processado['marca']=produto['brand']
            produto_processado['preco']=produto['valueTo']
            produto_processado['desconto']=round(produto['valueFrom']-produto['valueTo'],2)
            produto_processado['descontoPctg']=round(100-((produto['valueFrom']/produto['valueTo'])*100),2)*-1
        
            produtos_processados.append(produto_processado)
        retorno=produtos_processados
        return retorno
    
    @staticmethod
    def query_quantidade(palavrasChave:str,quantidade:int=24):
        retorno=[]
        for i in range(0,quantidade,24):
            query_=pesquisa.query(palavrasChave=palavrasChave,pagina=round(i/24,0))
            if query_==[]:
                return retorno
            else:
                retorno=[*retorno,*query_]
            if len(retorno)>=quantidade:
                return retorno[:quantidade]
        return retorno
            