from functools import wraps
import ormar

from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada

#Criamos um decorator em forma de função para realizar o delete,
#na controller, criando uma função interna

#recebe a função "delete_papel", que está no papeis_controller,
#retornando a função que também possui id, recebendo o modelo.
#Vai buscar a entidade "Ação" e deletar
#

def delete_controller(modelo: ormar.Model):
    def inner(func):
        @entidade_nao_encontrada
        @wraps(func)
        async def wrapper(id: int):
            entidade = await modelo.objects.get(id=id)
            return await entidade.delete()
        return wrapper
    return inner