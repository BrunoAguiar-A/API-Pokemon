import requests
from dataclasses import dataclass

"""
Instruções para TODOS os exercícios/funções abaixo:
1. Veja as instruções de como instalar o treinador e os testes no documento entregue junto com este arquivo.
2. Se um determinado parâmetro de uma função deve ser inteiro, então esta função deve rejeitar valores não-numéricos ou numerais não-inteiros nesse parâmetro.
3. Da mesma forma, se um parâmetro de uma função deve ser uma string, então esta função deve rejeitar valores que não sejam do tipo string nesse parâmetro.
4. Strings em branco são sempre consideradas inválidas.
5. Se algum dos parâmetros ser inválido, uma ValueError deve ser lançada. Recomenda-se usar as funções check_int e check_str acima para ajudar na validação.
6. Em todos os casos onde procura-se algum tipo de pokémon pelo nome ou pelo número e o mesmo não existir, uma exceção PokemonNaoExisteException deve ser lançada.
7. Em todos os casos onde procura-se algum treinador cadastrado e o mesmo não existir, uma exceção TreinadorNaoCadastradoException deve ser lançada.
8. Em todos os casos onde procura-se algum pokémon cadastrado e o mesmo não existir, uma exceção PokemonNaoCadastradoException deve ser lançada.
9. Em todos os casos onde tenta-se cadastrar um pokémon e o mesmo já exista, uma exceção PokemonJaCadastradoException deve ser lançada.
10. Todos os nomes de pokémons que aparecerem como parâmetros devem ser aceitos em minúsculas, MAIÚSCULAS ou até mesmo MiStUrAdO. Lembre-se dos métodos lower() e upper() da classe string.
11. Todos os nomes de pokémons, cores, jogos, movimentos, etc. recebidos e devolvidos pela PokeAPI estão em letras minúsculas e assim devem ser mantidas.

Alguns exemplos de URLs que podem servir de inspiração:
http://pokeapi.co/api/v2/

http://pokeapi.co/api/v2/pokemon/39/
http://pokeapi.co/api/v2/pokemon/jigglypuff/

http://pokeapi.co/api/v2/pokemon-species/39/
http://pokeapi.co/api/v2/pokemon-species/jigglypuff/

http://pokeapi.co/api/v2/evolution-chain/11/
http://pokeapi.co/api/v2/growth-rate/1/
http://pokeapi.co/api/v2/pokemon-color/2/

"""

"""
Não altere estas URLs. Elas são utilizadas para conectar no treinador e no PokeAPI, respectivamente.
"""
site_treinador = "http://127.0.0.1:9000"
site_pokeapi = "https://pokeapi.co"

"""
Vamos precisar destas quatro exceções personalizadas.

Abaixo, criamos excessões com nomes personalizados.

"""
class PokemonNaoExisteException(Exception):
    pass 

class PokemonNaoCadastradoException(Exception):
    pass

class TreinadorNaoCadastradoException(Exception):
    pass

class PokemonJaCadastradoException(Exception):
    pass

"""
Esta função certifica-se de que seu parâmetro é um número inteiro e lança uma ValueError se não for.
"""
def check_int(a):
    if type(a) is not int or a < 0:
        raise ValueError()

"""
Esta função certifica-se de que seu parâmetro é uma string e que não está vazia e lança uma ValueError se não for.
"""
def check_str(a):
    if type(a) is not str or a == "":
        raise ValueError()

"""
Esta classe será utilizada no exercício 12 abaixo.
"""
@dataclass()
class Pokemon:
    nome_treinador: str
    apelido: str
    tipo: str
    experiencia: int
    nivel: int
    cor: str
    evoluiu_de: str



"""
1. Dado o número de um pokémon, qual é o nome dele?
"""
def nome_do_pokemon(numero):
    if numero is not check_int(numero):
        url = f'http://pokeapi.co/api/v2/pokemon/{numero}/'
        r = requests.get(url)
        if r.status_code == 404:
            raise PokemonNaoExisteException
        dici = r.json()
        return dici['name']




"""
2. Dado o nome de um pokémon, qual é o número dele?
"""
def numero_do_pokemon(nome):
    if nome is not check_str(nome):
        url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}/"
        r = requests.get(url)
        if r.status_code == 404:
            raise PokemonNaoExisteException
        dici = r.json()
        return dici['id']
"""
3. Dado o nome ou número de um pokémon, qual é o nome da cor (em inglês) predominante dele?
"""
def color_of_pokemon(nome):
    if nome is not check_str(nome):
        url = f'https://pokeapi.co/api/v2/pokemon-species/{nome.lower()}/'
        r = requests.get(url)
        if r.status_code == 404:
            raise PokemonNaoExisteException
        dici = r.json()
        return dici['color']['name']

"""
4. Dado o nome ou número de um pokémon, qual é o nome da cor (em português) predominante dele?
Os nomes de cores possíveis em português são "marrom", "amarelo", "azul", "rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto".
No entanto, a pokeapi ainda não foi traduzida para o português! Como você pode dar um jeito nisso?
"""
def cor_do_pokemon(nome):
    if nome is not check_str(nome):
        url = f'https://pokeapi.co/api/v2/pokemon-species/{nome.lower()}/'
        r = requests.get(url)
        if r.status_code == 404:
            raise PokemonNaoExisteException
        dici = r.json()
        color = {"yellow":"amarelo", 'blue':'azul','pink':'rosa','gray':'cinza','brown':'marrom',
        'purple':'roxo','red':'vermelho','white':'branco','green':'verde','black':'preto'}
        if dici['color']['name'] in color:
            return color[dici['color']['name']]

"""
5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
Os nomes dos tipos de pokémons em português são "normal", "lutador", "voador", "veneno", "terra", "pedra", "inseto", "fantasma", "aço", "fogo", "água", "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
Todo pokémon pode pertencer a um ou a dois tipos diferentes. Retorne uma lista contendo os tipos, mesmo que haja somente um.
Se houver dois tipos, a ordem não é importante.
"""
def tipos_do_pokemon(nome):
    if nome is not check_str(nome):
        url = f'https://pokeapi.co/api/v2/pokemon/{nome.lower()}/'
        r = requests.get(url)
        if r.status_code == 404:
            raise PokemonNaoExisteException
        lista = []
        dici = r.json()
        elemento = {'normal':'normal','fighting':'lutador','flying':'voador','poison':'veneno',
        'ground':'terra','rock':'pedra','bug':'inseto','ghost':'fantasma','steel':'aço',
        'fire':'fogo','water':'água','grass':'grama','electric':'elétrico','psychic':'psíquico',
        'ice':'gelo','dragon':'dragão','dark':'noturno','fairy':'fada'}
        for x in dici['types']:
            if x['slot'] > 0:
                lista.append(elemento[x['type']['name']])
        return lista

"""
6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
Retorne None se o pokémon não tem evolução anterior. Por exemplo, evolucao_anterior('bulbasaur') == None
"""
def evolucao_anterior(nome):
    if nome is not check_str(nome):
        url = f'https://pokeapi.co/api/v2/pokemon-species/{nome.lower()}/'
        r = requests.get(url)
        if r.status_code == 404:
            raise PokemonNaoExisteException
        dici = r.json()
        if dici['evolves_from_species'] != None:
            return dici['evolves_from_species']['name']
        if dici['evolves_from_species'] == '':
            return None

"""
7. Dado o nome de um pokémon, liste para quais pokémons ele pode evoluiur.
Por exemplo, evolucoes_proximas('ivysaur') == ['venusaur'].
A maioria dos pokémons que podem evoluir, só podem evoluir para um único tipo de pokémon próximo. No entanto, há alguns que podem evoluir para dois ou mais tipos diferentes de pokémons.
Se houver múltiplas possibilidades de evoluções, a ordem delas não importa. Por exemplo:
evolucoes_proximas('poliwhirl') == ['poliwrath', 'politoed']
Note que esta função dá como resultado somente o próximo passo evolutivo. Assim sendo, evolucoes_proximas('poliwag') == ['poliwhirl']
Se o pokémon não evolui, retorne uma lista vazia. Por exemplo, evolucoes_proximas('celebi') == []

O exercicio 7 é opcional e bastante dificil. Se quiser, desligue os testes e vá para o 8!
"""
def evolucoes_proximas(nome):
    if nome is not check_str(nome):
        url = f'https://pokeapi.co/api/v2/pokemon-species/{nome.lower()}/'
        r = requests.get(url)
        
        if r.status_code == 404:
            raise PokemonNaoExisteException()
        lista = []
        dados = r.json()
        url_evolucao = dados['evolution_chain']['url']
        resposta_evolucao = requests.get(url_evolucao)
        dados_evolucao = resposta_evolucao.json()
        chain = dados_evolucao['chain']
        while chain:
            if chain['species']['name'] == nome.lower():
                for evolucao in chain.get('evolves_to', []):
                    lista.append(evolucao['species']['name'])
                break
            chain = chain.get('evolves_to', [])[0] if chain.get('evolves_to') else None
        
        return lista

"""
8. A medida que ganham pontos de experiência, os pokémons sobem de nível.
É possível determinar o nível (1 a 100) em que um pokémon se encontra com base na quantidade de pontos de experiência que ele tem.
Entretanto, cada tipo de pokémon adota uma curva de level-up diferente (na verdade, existem apenas 6 curvas de level-up diferentes).
Assim sendo, dado um nome de pokémon e uma quantidade de pontos de experiência, retorne o nível em que este pokémon está.
Valores negativos de experiência devem ser considerados inválidos.
"""
def nivel_do_pokemon(nome, experiencia):
    if nome is check_str(nome) or experiencia is check_int(experiencia) :
        raise ValueError()
    else:
        url = f'https://pokeapi.co/api/v2/pokemon-species/{nome.lower()}/'
        r = requests.get(url)
        if r.status_code == 404:
            raise PokemonNaoExisteException
        dici = r.json()
        rate =  dici['growth_rate']['url']
        rs = requests.get(rate)
        dic = rs.json()
        nivel = 0
        for dicxp in dic['levels']: #dicxp é um dicionario com 2 chaves, for em uma lista recebe os elementos direto.
            if dicxp['experience'] <= experiencia:
                nivel = dicxp['level']
        return nivel


"""
A partir daqui, você precisará rodar o servidor treinador.py na sua máquina para poder
fazer a atividade. Não precisa mexer no arquivo, basta rodar ele.

Os testes relativos ao treinador.py estao no arquivo pokemon_treinador_unittest.py

9. Dado um nome de treinador, cadastre-o na API de treinador.
Retorne True se um treinador com esse nome foi criado e False em caso contrário (já existia).

Dicas teste 9: Use o verbo PUT, URL {site_treinador}/treinador/{nome}
para criar um treinador. Se ele já existe, será retornado um cod de status
303. Se não existe, cod status 202.
"""
def cadastrar_treinador(nome):
    if nome is not check_str(nome):
        r = requests.put(f'{site_treinador}/treinador/{nome}')
        if r.status_code == 202:
            return True
        else:
            return False


"""
10. Imagine que você capturou dois pokémons do mesmo tipo. Para diferenciá-los, você dá nomes diferentes (apelidos) para eles.
Logo, um treinador pode ter mais do que um pokémon de um determinado tipo, mas não pode ter dois pokémons diferentes com o mesmo apelido.

Dados: um nome de treinador, um apelido de pokémon, um tipo de pokémon e uma quantidade de experiência, 

cadastre o pokémon com o tipo correspondente, na lista do treinador que foi passado, usando a API (o servidor) do treinador.
Certifique-se de que todos os dados são válidos.

Inicio teste 10 -- para passar o 10a
* Para cadastrar um pokemon, usar a url {site_treinador}/treinador/{nome_treinador}/{apelido_pokemon},
 enviando um arquivo json com a chave tipo (por exemplo tipo=pikachu) e a chave experiência
* Para enviar um dicionario pra uma URL, usando o verbo put
requests.put(url,json = {"tipo":"pikachu","experiencia"...})


Mais dicas teste 10: 
* Pode ser necessário usar a pokeapi para verificar se um pokemon existe --
 se eu falar que o geremias é dono de um pokemon do tipo homer, deve ocorrer uma excessao, porque homer não é uma espécie válida de pokemon
* Se voce receber um status 404, isso indica um treinador nao encontrado
* Se voce receber um status 409, isso indica que o pokemon já existia e você
está fazendo um cadastro dobrado
* Se voce receber um status 202, isso indica criação bem sucedida
"""

def cadastrar_pokemon(nome_treinador, apelido_pokemon, tipo_pokemon, experiencia):
    if nome_treinador is not check_str(nome_treinador) and apelido_pokemon is not  check_str(apelido_pokemon) and tipo_pokemon is not check_str(tipo_pokemon) and experiencia is not check_int(experiencia):
        url = f'{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}'
        r = requests.put(url,json = {'apelido':apelido_pokemon,"tipo":tipo_pokemon,'experiencia':experiencia})
        if r.status_code == 404:
            raise TreinadorNaoCadastradoException
        mi = tipo_pokemon.lower()
        urls = f'https://pokeapi.co/api/v2/pokemon/{mi}/'
        rs = requests.get(urls)
        if rs.status_code == 404:
            requests.delete(url,json = {'apelido':apelido_pokemon,"tipo":tipo_pokemon,'experiencia':experiencia})
            raise PokemonNaoExisteException
        if r.status_code == 409:
            raise PokemonJaCadastradoException
    else:
        raise ValueError()
        




"""
11. Dado um nome de treinador, um apelido de pokémon e uma quantidade de experiência, localize esse pokémon e acrescente-lhe a experiência ganha.

Dicas ex 11:
utilize a URL {site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}/exp
Por exemplo, se for o pokemon com apelido terra
do treinador lucas, a URL ficaria: {site_treinador}/treinador/lucas/terra/exp


Utilize o verbo POST, enviando um arquivo json com a chave experiencia (o valor dessa chave é o tanto de exp que eu quero acrescentar)


Um cod de status 404 pode significar 2 coisas distintas: ou o treinador não existe,
ou o treinador existe mas o pokemon não. Isso pode verificado acessando a resposta.text
(em vez do usual, que seria resposta.json())

O cod de status de sucesso é o 204
"""
def ganhar_experiencia(nome_treinador, apelido_pokemon, experiencia):
    if nome_treinador is not check_str(nome_treinador) and apelido_pokemon is not  check_str(apelido_pokemon)  and experiencia is not check_int(experiencia):
        url = f'{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}/exp'
        r = requests.post(url,json = {'experiencia': experiencia })
        if r.status_code == 404:
            if 'Treinador não existe' in r.text:
                raise TreinadorNaoCadastradoException
            else:
                raise PokemonNaoCadastradoException
    else:
        raise ValueError()
        
       
"""
12. Dado um nome de treinador e um apelido de pokémon, localize esse pokémon na API do treinador e retorne um objeto da classe Pokemon, prenchida com os atributos definidos na classe


Dicas 12:
pegar os dados na url "{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}"
acessada com o verbo GET
para preencher o objeto Pokemon, voce vai fornecer
* nome treinador (veio como argumento da funcao)
* apelido pokemon (veio como argumento da funcao)
* tipo (veio do get que você fez -- chave tipo do dicionário)
* experiencia (veio do request que você fez -- chave experiencia do dicionário)
* nivel do pokemon (calcular usando a pokeapi -- voce ja fez essa funcao, use ela)
* cor do pokemon (em portugues, pegar da pokeapi -- voce ja fez essa funcao, use ela)
* evolucao anterior (pegar da pokeapi -- voce ja fez essa funcao, use ela)
Retornar o objeto pokemon
Erros 404 podem ser treinador nao existe ou pokemon nao existe -- verifique resposta.text para ver qual dos dois -- já fizemos isso antes
"""
def localizar_pokemon(nome_treinador, apelido_pokemon):
    if nome_treinador is not check_str(nome_treinador) and apelido_pokemon is not  check_str(apelido_pokemon):
        url = f'{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}'
        r = requests.get(url)
        if r.status_code == 404:
            if  'Treinador não existe' in r.text:
                raise TreinadorNaoCadastradoException
            else:
                raise PokemonNaoCadastradoException
        dici = r.json()
        poke = dici['tipo']
        lvl = nivel_do_pokemon(poke, dici['experiencia'])
        pokemon = Pokemon(nome_treinador, apelido_pokemon,dici['tipo'], dici['experiencia'], lvl, str(cor_do_pokemon(poke)), str(evolucao_anterior(poke)))
        return pokemon
    else:
        raise ValueError()
    
"""
13. Dado o nome de um treinador, localize-o na API do treinador e retorne um dicionário dos seus pokemons. 
As chaves do dicionário serão os apelidos dos pokémons dele, e os valores serão os tipos (pikachu, bulbasaur ...) deles.

Essas informações estão na URL "{site_treinador}/treinador/{nome_treinador}",
acessiveis com o verbo GET
Consulte ela com seu navegador e veja o que tem lá! (talvez você queira usar
as funções anteriores para criar um treinador e seus pokemons...)
"""
def detalhar_treinador(nome_treinador):
    if not check_str(nome_treinador):
        url = f'{site_treinador}/treinador/{nome_treinador}'
        r = requests.get(url)
        
        if r.status_code == 404:
            raise TreinadorNaoCadastradoException()

        dados_treinador = r.json()
        
        if 'pokemons' not in dados_treinador:
            raise PokemonNaoCadastradoException()
        
        lista = []
        for x in dados_treinador['pokemons']:
            apelido = dados_treinador["pokemons"][x]['apelido']
            tipo = dados_treinador["pokemons"][x]['tipo']
            lista.append((apelido,tipo))

            
        return dict(lista)

"""
14. Dado o nome de um treinador, localize-o na API do treinador e exclua-o, juntamente com todos os seus pokémons.

Usar o verbo delete na url do treinador. A mesma que a gente já usou várias vezes.
O status code vai de informar se o treinador não existia (com qual status code?)
"""
def excluir_treinador(nome_treinador):
    if not check_str(nome_treinador):
        url = f'{site_treinador}/treinador/{nome_treinador}'
        r = requests.delete(url)
        if r.status_code == 404:
            raise TreinadorNaoCadastradoException()


"""
15. Dado o nome de um treinador e o apelido de um de seus pokémons, localize o pokémon na API do treinador e exclua-o.

Usar o verbo delete na url do pokemon: {site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}
O status code vai de informar se o treinador não existe, ou se o pokemon nao existe 
(status code 404, não deixe de verificar se foi o pokemon ou treinador que não existia)
"""
def excluir_pokemon(nome_treinador, apelido_pokemon):
     if not all(check_str(param) for param in (nome_treinador, apelido_pokemon)):
        url = f'{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}'
        r = requests.delete(url)
        if r.status_code == 404:
            if  'Treinador não existe' in r.text:
                raise TreinadorNaoCadastradoException
            else:
                raise PokemonNaoCadastradoException

