# Gaunter
Webservice que captura Informações de Espelhos de Grupos de Pesquisa do CNPq.
><i>"Ele sempre concede exatamente aquilo que desejamos. Esse é o problema"</i>

O presente webservice é composto por 7 rotas GET responsáveis cada um por extrair uma parter das informações constantes nos espelhos dos Grupos de Pesquisa cadastrados no <a href="http://lattes.cnpq.br/web/dgp#">DGP</a>. 

Todas a rotas devem receber o código númerico que identifica o grupo. Este código é encontrado no final das URLs dos espelhos dos Grupos de Pesquisa.
<hr>
<h5>Exemplo:</h5>

> Grupo de pesquisa em Paleoherpetologia

> Endereço para acessar o espelho do Grupo: <a>dgp.cnpq.br/dgp/espelhogrupo/<b>2300081346727364</b></a>

> Neste caso o código que identifica o grupo é: 2300081346727364
<hr>

<h2>Rotas</h2>
<h3>Presquisadores</h3>

> [host]/getPesquisadores/\<id>
Retorna um Json com uma lista de todos os pesquisadores
<h5>Exemplo:</h5>

```json
{
    "Pesquisadores": [
        "Alessandro Martins da Costa",
        "Martin Eduardo Poletti",
        "Patrícia Nicolucci"
    ]
}
```

<h3></h3>
<h3></h3>
<h3></h3>
<h3></h3>
<h3></h3>
<h3></h3>
<h3></h3>
