class Musica:
    def __init__(self, titulo, cantor, estilo):
        self.titulo = titulo
        self.cantor = cantor
        self.estilo = estilo

    def exibir(self):
        return {
            'titulo': self.titulo,
            'cantor': self.cantor,
            'estilo': self.estilo
        }


def novo():
    titulo = input("Nome da música >> ")
    if buscar(titulo) == -1:
        cantor = input("Nome do cantor >> ")
        estilo = input("Estilo >> ")
        musica = Musica(titulo, cantor, estilo)
        lista.append(musica)
    else:
        print("Música já cadastrada!")


def consultar():
    nome = input("Informe o nome da música >> ")
    posicao = buscar(nome)
    if posicao != -1:
        print(lista[posicao].exibir())
    else:
        print("Música não cadastrada!")


def buscar(nome):
    for posicao, item in enumerate(lista):
        if item.titulo == nome:
            return posicao
    return -1


def buscar_cantor(nome):
    for posicao, item in enumerate(lista):
        if item.cantor == nome:
            return posicao
    return -1


def listar():
    print("\n")
    print([item.exibir() for item in lista])
    print("\n")


def gerar_playlist_por_musica():
    nome = input("Digite o nome da música >> ")
    posicao = buscar(nome)
    if posicao != -1:
        lista_por_musica.append(lista[posicao])
        print([item.exibir() for item in lista_por_musica])
    else:
        print("Música não cadastrada!")


def gerar_playlist_por_cantor():
    cantor = input("Digite o nome do cantor >> ")
    posicao = buscar_cantor(cantor)
    if posicao != -1:
        lista_por_cantor.append(lista[posicao])
        print([item.exibir() for item in lista_por_cantor])
    else:
        print("Cantor não cadastrado!")


lista = []
lista_por_musica = []
lista_por_cantor = []

if __name__ == '__main__':

    pare = True
    while pare:
        print("*" * 10, "Menu de Músicas", "*" * 10)
        print("1. Nova música")
        print("2. Consultar")
        print("3. Listar")
        print("4. Gerar playlist por música")
        print("5. Gerar playlist por cantor")
        print("6. Encerrar")
        opcao = int(input("Informe a opção desejada >> "))
        if opcao == 1:
            novo()

        if opcao == 2:
            consultar()

        if opcao == 3:
            listar()

        if opcao == 4:
            gerar_playlist_por_musica()

        if opcao == 5:
            gerar_playlist_por_cantor()

        if opcao == 6:
            pare = False
