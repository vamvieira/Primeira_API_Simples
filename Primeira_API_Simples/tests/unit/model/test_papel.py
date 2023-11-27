from tests.utils.papeis import create_papel_valido, create_papel_invalido
from models.papel import Papel
import pytest

def test_cria_papel_valido() -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)

#criando teste de sigla invalida
def test_cria_papel_com_sigla_invalida() -> None:
    with pytest.raises(ValueError, match='A sigla do papel é inválida!'):
        atributos = create_papel_invalido(['sigla'])
        papel = Papel(**atributos) 

#** - dicionário, tem a possibilidade de passar parâmetro para uma função
# desencapsular, quando muda o objeto de origem para o objeto de destino python
# Vaso -> Objeto
#Objeto -> Classe

#with - compilador de erros, 