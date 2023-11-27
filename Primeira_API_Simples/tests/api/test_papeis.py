from fastapi.testclient import TestClient
from models.papel import Papel
from tests.utils.papeis import create_papel_invalido, create_papel_valido
import asyncio
import pytest
import ormar

#TestCLiente faz a conexão com a API, indo no arquivo de rotas

def test_lista_todos_os_papeis(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())
    
    response = client.get("/papeis/")
    content = response.json()

    assert response.status_code == 200
    assert len(content) == 1

#Teste adiciona papel

def test_cria_papel(client: TestClient) -> None:
    body = create_papel_valido()
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 200
    assert content["cnpj"] == body["cnpj"]

#Teste chamando a raiz para ver se está funcional

def test_cria_papel_com_sigla_invalida(client: TestClient) -> None:
    body = create_papel_invalido(['sigla'])
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 422

#assert serve para veirficar se funciona ou não, utilizado para fazer teste.

#Erro 404 

def test_obtem_um_papel_por_id(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())
    
#content é o carregamento do payload

    response = client.get(f"/papeis/{papel.id}")
    content = response.json()

    assert response.status_code == 200
    assert content["sigla"] == papel.sigla

def test_obtem_papel_inexistente_por_id(client: TestClient) -> None:
    response = client.get(f"/papeis/1")
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"

def test_update_papel_existente(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())

    novo_nome = "Novo nome"
    atributos_para_atualizar = {"nome": novo_nome}

    response = client.patch(f"/papeis/{papel.id}", json=atributos_para_atualizar)
    content = response.json()

    #Json = payload da requisição, sendo apenas a iformação. 
    #DTO = Data transfer object/ objeto de trans arquivo: são informações que nao vao para base de dados

    papel_atualizado = loop.run_until_complete(Papel.objects.get(id=papel.id))

    assert response.status_code == 200
    assert content["nome"] == novo_nome
    assert papel_atualizado.nome == novo_nome

def test_update_papel_inexistente(client: TestClient) -> None:
    novo_nome = "Novo nome"
    atributos_para_atualizar = {"nome": novo_nome}

    response = client.patch(f"/papeis/1", json=atributos_para_atualizar)
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"

def test_delete_papel_existente(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())

    response = client.delete(f"/papeis/{papel.id}")

    with pytest.raises(ormar.exceptions.NoMatch): 
        loop.run_until_complete(Papel.objects.get(id=papel.id))

    assert response.status_code == 200

def test_delete_papel_inexistente(client: TestClient) -> None:
    response = client.delete(f"/papeis/1")
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"