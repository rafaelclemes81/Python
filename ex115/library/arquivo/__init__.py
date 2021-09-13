from ex115.library.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[33mHouve um ERRO na criação do arquivo ...')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[33mErro ao ler o arquivo\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('\033[33mHouve um ERRO ao abrir o arquivo\033[m')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('\033[33mHouve um ERRO ao tentar escrever no arquivo.\033[m')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso.')
            a.close()
