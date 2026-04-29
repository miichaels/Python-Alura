import os

#Dicionário
restaurantes = [ {'nome': 'Praça', 'categoria':'Japonesa', 'ativo': False},
                 {'nome': 'Botecao', 'categoria':'Prato feito', 'ativo': True},
                 {'nome': 'Vinho seco', 'categoria':'Italiano', 'ativo': False},
                 {'nome': 'Mangariun', 'categoria':'Fitness', 'ativo': True}
                 ]

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ██2█████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
        """)


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')


def voltar_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    # linha = '*' * len(texto)
    # print(linha)
    # print(texto)
    # print(linha)


''' Docstring
Essa função é responsável por cadastrar um novo restaurante 

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
def cadastrar_novo_restaurante():

    exibir_subtitulo("Cadastrando Novo Restaurante")
    nome_restaurante = input('Nome do restaurante: ')

    categoria = input(f'Digite o nome da categoria do restaurante: {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'\nRestaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()


def finalizar_app():
    exibir_subtitulo('Programa finalizado com sucesso!')

def opcao_invalida():
    print("Opção invalida!\n")
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes:')
    print(f'{'Restaurante'.ljust(13)} | {'Categoria'.ljust(13)} | Status')
    for lista in restaurantes:
        nome_restaurante = lista['nome']
        categoria = lista['categoria']
        ativo = 'ativado' if lista['ativo'] else 'desativado'
        print(f" {nome_restaurante.ljust(13)} | {categoria.ljust(13)} | {ativo}")

    voltar_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado de Restaurante:')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')


    voltar_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input(f'Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
             print('Finalizando app\n')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


#Esse arquivo é o principal e nao pode ser importado
if __name__ == "__main__":
    main()











