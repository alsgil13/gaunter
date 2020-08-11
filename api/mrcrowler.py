import requests
from bs4 import BeautifulSoup
import json

lapsi = 'http://dgp.cnpq.br/dgp/espelhogrupo/9931131070811617'
fisica_rd = 'http://dgp.cnpq.br/dgp/espelhogrupo/7548264580175587'
paleo = 'http://dgp.cnpq.br/dgp/espelhogrupo/2300081346727364'

def getPesquisadores(url):
    membros = '{"Pesquisadores" : ['
    conteudo = requests.get(url)
    sopa = BeautifulSoup(conteudo.text, 'html.parser')
    rhdiv = sopa.find(id='idFormVisualizarGrupoPesquisa:j_idt261')
    rhdivtd = rhdiv.find_all('td')
    i = 0
    for td in rhdivtd:
        if(i%4==0):
            membros = membros + '"' + td.contents[0] + '",'
            #membros.append(td.contents[0])
        i+=1
    #retira última virgula
    membros = membros[:-1]
    #fecha json literal
    membros = membros + "]}"

    return json.dumps(membros, ensure_ascii=False)

def getEstudantes(url):
    estudantes = '{"Estudantes" : ['
    conteudo = requests.get(url)
    sopa = BeautifulSoup(conteudo.text, 'html.parser')
    rhdiv = sopa.find(id='idFormVisualizarGrupoPesquisa:j_idt278_data')
    rhdivtd = rhdiv.find_all('td')
    i = 0
    for td in rhdivtd:
        if(i%4==0):
            estudantes = estudantes + '"' + td.contents[0] + '",'
            #estudantes.append(td.contents[0])
        i+=1
    #retira última virgula
    estudantes = estudantes[:-1]
    #fecha json literal
    estudantes = estudantes + "]}"

    return json.dumps(estudantes, ensure_ascii=False)    

def getTecnicos(url):
    tecnicos = '{"Técnicos" : ['
    conteudo = requests.get(url)
    sopa = BeautifulSoup(conteudo.text, 'html.parser')
    rhdiv = sopa.find(id='idFormVisualizarGrupoPesquisa:j_idt295_data')
    rhdivtd = rhdiv.find_all('td')
    i = 0
    for td in rhdivtd:
        if(i%4==0):
            tecnicos = tecnicos + '"' + td.contents[0] + '",'
            #tecnicos.append(td.contents[0])
        i+=1
    #retira última virgula
    tecnicos = tecnicos[:-1]
    #fecha json literal
    tecnicos = tecnicos + "]}"

    return json.dumps(tecnicos, ensure_ascii=False)    

def getIdentificacao(url):
    conteudo = requests.get(url)
    sopa = BeautifulSoup(conteudo.text, 'html.parser')
    #Procura pelo nome do Grupo
    nomediv = sopa.find(id='tituloImpressao')
    nome = nomediv.find_all('h1')
    nome = nome[0].contents[0].strip()
    #começa a montagem do objeto literal    
    info = '{"Identificação" : { "Nome" : "' + nome + '" , '
    #filtrando estruturas
    container = sopa.find(id='identificacao')
    l = container.find_all('label',class_='control-label')      #labels
    c = container.find_all('div',class_='controls')             #valores
    #iterando resultado e montando o objeto literal com as informações
    for x in range(len(l)):
        if(len(l[x].contents[0]) > 1):
            #verifica se tem mais de um líder, de acordo com a regras do CNPq pode ter no máximo 2
            if(("Líder(es) do grupo" in l[x].contents[0]) and (len(c[x].contents) >= 8)):
                info = info + '"' + (str(l[x].contents[0]).strip())[:-1] + '" : ["'  + str(c[x].contents[0]).strip() + '", "' + str(c[x].contents[8]).strip() + '"], '
            else:
                info = info + '"' + (str(l[x].contents[0]).strip())[:-1] + '" : "'  + str(c[x].contents[0]).strip() + '", '
    #remove a última virugla
    info = info[:-2]
    #fecha json literal
    info = info + '} }'
    return json.dumps(info, ensure_ascii=False)

def getEndereco(url):
    endereco = '{"Endereço" : {'
    conteudo = requests.get(url)
    sopa = BeautifulSoup(conteudo.text, 'html.parser')
    container = sopa.find(id='endereco')
    l = container.find_all('label',class_='control-label')      #labels
    c = container.find_all('div',class_='controls')             #valores
    for x in range(len(l)):
        if(len(l[x].contents[0]) > 1):
            if('Contato do grupo' in str(l[x].contents[0]).strip()):
                contato = c[x].contents[0].text
                endereco = endereco + '"' + (str(l[x].contents[0]).strip())[:-1] + '" : "'  + contato + '", '
            elif('Website' in str(l[x].contents[0]).strip()):
                sitio = c[x].contents[0].text
                endereco = endereco + '"' + (str(l[x].contents[0]).strip())[:-1] + '" : "'  + sitio + '", '
            else:
                endereco = endereco + '"' + (str(l[x].contents[0]).strip())[:-1] + '" : "'  + str(c[x].contents[0]).strip() + '", '
    #remove a última virugla
    endereco = endereco[:-2]
    #fecha json literal
    endereco = endereco + "} }"
    return json.dumps(endereco, ensure_ascii=False)



def getLinhas(url):
    linhas = '{"Linhas de Pesquisa" : ['
    conteudo = requests.get(url)
    sopa = BeautifulSoup(conteudo.text, 'html.parser')
    tabledata = sopa.find(id='idFormVisualizarGrupoPesquisa:j_idt241_data')
    tdlist = tabledata.find_all('td')
    i = 0
    for td in tdlist:
        if(i%4==0): #seleciona apenas o noem da linha de pesquisa
            linhas = linhas + '"' + td.contents[0] + '",'
        i+=1
    #retira última virgula
    linhas = linhas[:-1]
    #fecha json literal
    linhas = linhas + "]}"

    return json.dumps(linhas, ensure_ascii=False)


def getInstParceiras(url):
    parsas = '{"Instituições parceiras relatadas pelo grupo" : ['
    conteudo = requests.get(url)
    sopa = BeautifulSoup(conteudo.text, 'html.parser')
    tabledata = sopa.find(id='idFormVisualizarGrupoPesquisa:j_idt378_data')
    tdlist = tabledata.find_all('td')
    i = 0
    for td in tdlist:
        if(i%4==0): #seleciona apenas o noem da linha de pesquisa
            parsas = parsas + '"' + td.contents[0] + '",'
        i+=1
    #retira última virgula
    parsas = parsas[:-1]
    #fecha json literal
    parsas = parsas + "]}"

    return json.dumps(parsas, ensure_ascii=False)

#print(getPesquisadores(fisica_rd))
#print(getPesquisadores(lapsi))
#print(getIdentificacao(lapsi))
print(getInstParceiras(paleo))
