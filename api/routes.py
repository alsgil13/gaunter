from flask import Flask, request, json
import mrcrowler

app =Flask("Gaunter")



@app.route('/getPesquisadores/<code>',methods=['GET'])
def pesq(code):
    url = 'http://dgp.cnpq.br/dgp/espelhogrupo/' + code
    data = mrcrowler.getPesquisadores(url)
    data = json.loads(data)
    return data
    
@app.route('/getEstudantes/<code>',methods=['GET'])
def estudantes(code):
    url = 'http://dgp.cnpq.br/dgp/espelhogrupo/' + code
    data = mrcrowler.getEstudantes(url)
    data = json.loads(data)
    return data
    
@app.route('/getTecnicos/<code>',methods=['GET'])
def tecnos(code):
    url = 'http://dgp.cnpq.br/dgp/espelhogrupo/' + code
    data = mrcrowler.getTecnicos(url)
    data = json.loads(data)
    return data

@app.route('/getId/<code>',methods=['GET'])
def ids(code):
    url = 'http://dgp.cnpq.br/dgp/espelhogrupo/' + code
    data = mrcrowler.getIdentificacao(url)
    data = json.loads(data)
    return data

@app.route('/getEndereco/<code>',methods=['GET'])
def endereco(code):
    url = 'http://dgp.cnpq.br/dgp/espelhogrupo/' + code
    data = mrcrowler.getEndereco(url)
    data = json.loads(data)
    return data

@app.route('/getLinhas/<code>',methods=['GET'])
def linhas(code):
    url = 'http://dgp.cnpq.br/dgp/espelhogrupo/' + code
    data = mrcrowler.getLinhas(url)
    data = json.loads(data)
    return data

@app.route('/getParceiros/<code>',methods=['GET'])
def parsas(code):
    url = 'http://dgp.cnpq.br/dgp/espelhogrupo/' + code
    data = mrcrowler.getInstParceiras(url)
    data = json.loads(data)
    return data

app.run()