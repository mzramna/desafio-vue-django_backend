url de pesquisa segue padrão:
https://www.drogasil.com.br/search?w={keyword1}+{keyword2}

produtos são listados no json:
-> script id="__NEXT_DATA__" type="application/json"
    -> produtos na hierarquia 'props' -> "pageProps" -> "initialData" -> "products"
    -> valores uteis ["name"] ['image'] ['subcategory'] ['dosage'] ['qty'] ['urlKey'] ['brand'] ['valueTo'] 
      -> (['valueFrom']-['valueTo'])=[valor de desconto]
      -> calcular pctg de desconto
  