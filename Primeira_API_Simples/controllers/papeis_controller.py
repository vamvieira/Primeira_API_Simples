from fastapi import APIRouter
import ormar
from controllers.utils.delete_controller import delete_controller
from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada
from controllers.utils.get_all_controller import get_all_controller
from controllers.utils.get_controller import get_controller
from controllers.utils.patch_controller import patch_controller
from controllers.utils.post_controller import post_controller

from models.papel import Papel
from models.requests.papel_update import PapelUpdate

router = APIRouter()

#Responsavél por gravar os itens setados(Adicionados) no BD.

@router.post("/")
@post_controller
async def add_item(entidade: Papel):
    pass

# @router.post("/")
# async def add_item(papel: Papel):
#     await papel.save()
#     return papel

@router.get("/")
@get_all_controller(Papel)
async def list_item():
    pass

#REALIZAR UMA NOVA ROTA DE SOLICITAÇÃO POR NOME, CNPJ.

@router.get("/{id}")
@get_controller(Papel)
async def get_papel(id: int):    
    pass

# -->>> ANTIGO CÓDIGO DO GET 1 <<<-- #

# @router.get("/{papel_id}")
# @entidade_nao_encontrada
# async def get_papel(papel_id: int, response: Response):
#     papel = await Papel.objects.get(id=papel_id)
#     return papel

#Pegar o papel que existe no get, pegar as propriedades que deseja atualizar, 
#transformar em dicionario e excluir  o que não estiver selecionadas

@router.patch("/{id}")
@patch_controller(Papel)
async def patch_papel(propriedades_atualizadas: PapelUpdate, id: int):
    pass
# -->>> ANTIGO CÓDIGO DO PATH 1 <<<-- #

# @router.patch("/{papel_id}")
# @entidade_nao_encontrada
# async def patch_papel(propriedades_atualizacao: PapelUpdate, papel_id: int):
# papel_salvo = await Papel.objects.get(id=papel_id)
# propriedades_atualizadas = propriedades_atualizacao.dict(exclude_unset=True)
# await papel_salvo.update(**propriedades_atualizadas)
# return papel_salvo

@router.delete("/{papel_id}")
@delete_controller(Papel)
async def delete_papel(id: int):
    pass

# -->>> ANTIGO CÓDIGO  DELETE 2 <<<-- #
#@router.delete("/{papel_id}")
#@entidade_nao_encontrada
#async def delete_papel(papel_id: int):
#    papel = await Papel.objects.get(id=papel_id)
#    return await papel.delete()

# -->>> ANTIGO CÓDIGO  DELETE 1 <<<-- #
#@router.delete("/{papel_id}")
#async def delete_papel(papel_id: int, response: Response):
#    try:
#        papel = await Papel.objects.get(id=papel_id)
#        return await papel.delete()
#    except ormar.exceptions.NoMatch:
#        response.status_code = 404
#        return {"mensagem": "Entidade não encontrada"}