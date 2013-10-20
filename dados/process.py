import numpy as np
import pandas as pd
from unidecode import unidecode

def trimmZeros(keyvector):
    result = []
    for key in keyvector:
        if str(key) == 'nan': key = ''
        result.append(str(key).strip('0'))
    return result



def read(path,columns={"CD_METADADOS": str, "CD_PAI": str}):
    """
    Le dados, retira zeros das bordas, coloca CD_METADADOS como chave.
    (O panda suporta chaves repetidas)
    """
    data = pd.read_csv(path,dtype=columns)
    ## Por algum motivo o CD_METADADOS nao é lido como string..
    keynames = trimmZeros(data['CD_METADADOS'])
    del data['CD_METADADOS']
    data.index = keynames
    ## data.rename(keynames)
    return(data)



def parse(data, meta,
          col_data = ['NR_VALOR','NR_VALOR2','NR_VALOR3'],
          col_time = ['AAEXERCICIO','CD_MENSAL'],
          col_meta = ['CD_PAI','NR_NIVEL'],
          col_name = ['DS_NOME_ESTRUTURA'],
          maxlevel = 2 ):
    """
    Retorna uma tabela desejavel:
    Seleciona as colunas a serem retiradas;
    Limpa os campos acima do nivel maximo;
    Substitui a chave pelo nome da variavel.
    """
    meta = meta[meta['NR_NIVEL'] <= maxlevel]
    for i in xrange(len(meta)):
        meta.ix[i,col_name[0]] = meta.ix[i,col_name[0]].strip()

    result = data[col_data + col_time].join(meta[col_meta + col_name],how='inner')
    for i in xrange(len(result)):
        x = result.ix[i,"CD_PAI"]
        if x != '':
            result.ix[i,"CD_PAI"] = meta.ix[x,col_name[0]]
            
    result.set_index(col_name[0], inplace=True)
    return(result)



def getParent(index,df,levels=10000):
    parents = df['CD_PAI']
    current = index
    ids = []
    while(levels > 0 and current != '' and levels > 0):
        ids.append(current)
        print ids
        current = parents[current]
        levels -= 1
    ids.reverse()
    return(ids)



def getChildren(key,df):
    names = df.index
    ids = []
    for n in names:
        if key in n:
            ids.append(n)
    return(sorted(ids))


def urlFriendly(string,fmt="latin1"):
    s = unicode(string,fmt)
    dec = unidecode(s)
    return (str(dec).lower().replace(" ","-"))

def printToFile(path,data):
    f = open(path,'w')
    f.write("{"+",".join(
        ['"'+ urlFriendly(key) + '":' +
         data.loc[key].to_json(orient='records',double_precision=2)
         for key in data.index.unique()])+
        "}")
    f.close()
    
def read_and_convert(in_paths,out_path):
    if type(in_paths) == type([]):
        dfs=[]
        for f in in_paths:
            dfs.append(pd.read_csv(f))
            d = pd.concat(dfs)
    else:
        d = pd.read_csv(in_paths)
    d = d[(d['AAEXERCICIO'] < 2013) |
          (d['CD_MENSAL'] < 11)]
    printToFile(out_path,d)
    
read_and_convert(["bruto/despesas_nivel_1.csv","bruto/despesas_nivel_2.csv"],
                 "despesa.json")

read_and_convert(["bruto/arrecadacao_nivel_1.csv","bruto/arrecadacao_nivel_2.csv"],
                 "arrecadacao.json")

read_and_convert("bruto/divida_nivel_1.csv","divida.json")

# desp_anuais = pd.concat(
#     [pd.read_csv("bruto/despesas_nivel_1.csv"),
#      pd.read_csv("bruto/despesas_nivel_2.csv")])
# desp_anuais = desp_anuais[(desp_anuais['AAEXERCICIO'] < 2013) |
#                           (desp_anuais['CD_MENSAL'] < 11)]
# printToFile("despesa.json",desp_anuais)


# arrec_anuais = pd.concat([
#     pd.read_csv("bruto/arrecadacao_nivel_1.csv"),
#     pd.read_csv("bruto/arrecadacao_nivel_2.csv")])
# printToFile("arrecadacao.json",arrec_anuais)

# divida_anuais = pd.read_csv("bruto/divida_nivel_1.csv")
# printToFile("divida.json",divida_anuais)



###### PARSING DOS DADOS .CSV
### Essas operacoes processam a base de dados disponibilizada pelo movimentominas.
### Atualmente nos não estamos utilizando ela devido as suas limitacoes.
# desp_data = read('bruto/despesa_dados.csv')
# arrec_data = read('bruto/arrecadacao_dados.csv')
# arrec_meta  = read('bruto/arrecadacao_metadados.csv')
# arrec_meta['CD_PAI'] = trimmZeros(arrec_meta['CD_PAI'])
# arrec=parse(arrec_data,arrec_meta)
# printToFile("arrecadacao2012.json",arrec)

# desp_meta = read('bruto/despesa_metadados.csv')
# desp_meta['CD_PAI'] = trimmZeros(desp_meta['CD_PAI'])
# desp=parse(desp_data,desp_meta)
# printToFile("despesa.json",desp)

# divida_data = read('bruto/divida_dados.csv')
# divida_meta = read('bruto/divida_metadados.csv')

# divida_meta['CD_PAI'] = trimmZeros(divida_meta['CD_PAI'])
# divida = parse(divida_data,divida_meta)
# printToFile("divida2012.json",divida)



#### Informacao dos dados
## CD_METADADOS: Indice
## CD_PAI: nó pai
## FL_ARVORE: (bool) tem nivel inferior ou nao
## DS_NOME_ESTRUTURA: nome da entidade
## NR_NIVEL: nivel hierarquico da entidade
## CD_DIMENSAO: ????

## CD_METADADOS: Indice (nao é unico)
## CD_MENSAL: Mes de referencia
## NR_VALOR: Valor previsto inicial / despesa realizada
## NR_VALOR2: Valor previsto atualizado / Valor emepenho
## NR_VALOR3: valor efetivado acumulado / NaN
