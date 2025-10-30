import random
linha_escolhida=[0]#vai guardar a linha que o usuario escolheu
coluna_escolhida=[0] #vai guardar a coluuna que o usuario escolheu
sair=0#variavel para sair dos loops

def colocar_bombas():#funçao que vai posicionar as bombas
    posicoes=random.sample([(i,j) for i in range(altura) for j in range (largura)], 1)[0]#pegando posiçoes aleatorias para as bombas
    quantidade=0
    while quantidade < bombas: #loop para colocar todas as bomba
        if mapa_real[posicoes[0]][posicoes[1]] == ' ': #se o local tiver vazio ele vai colocar uma bomba
            mapa_real[posicoes[0]][posicoes[1]] = '*'
            quantidade+=1
            posicoes=random.sample([(i,j) for i in range(altura) for j in range (largura)], 1)[0]#sortear novamente para o proximo loop
        else:#se tiver ocupado ele vai pegar outra posiçao
            posicoes = random.sample([(i,j) for i in range(altura) for j in range (largura)], 1)[0]


def contar_bombas(): #função que vai contar as bombas em volta da posição escolhida pelo usuãrio
    contagem = 0 #contar a quantidade de bombas ao redor
    linha_ini = linha_escolhida[0] - 1 #posiçao acima
    linha_fim = linha_escolhida[0] + 2 #posiçao abaixo
    coluna_ini = coluna_escolhida[0] - 1 #posiçao a esquerda
    coluna_fim = coluna_escolhida[0] + 2 #posiçao a direira
    for i in range(linha_ini, linha_fim):#loop para procurar nas 8 posiçoes em volta
        for j in range(coluna_ini, coluna_fim):
            if (i >= 0 and i < altura) and (j >= 0 and j < largura):
                if mapa_real[i][j] == '*':
                    contagem += 1
    return contagem #retorna o valor de bombas em volta


def mostrar_quantidade_bombas(quantidade_bombas):#funçao que vai colocar o numero de bombas em volta no campo escolhido
    if quantidade_bombas > 0:
        mapa_usuario[linha_escolhida[0]][coluna_escolhida[0]] = (str(quantidade_bombas))
    else:
        mapa_usuario[linha_escolhida[0]][coluna_escolhida[0]] = ' '
    

def printar_mapa():#funçao para printar o mapa do usuario
        for linha in mapa_usuario:
            print(' '.join(linha))

def printar_mapa_real():#funçao para printar o mapa real
    for linha in mapa_real:
            print(' '.join(linha))

while sair == 0: #loop para verificar o tamanho do mapa e a quantidade de bombas
    print('Bem-vindo ao Campo Minado'.center(30, '-'))
    print()
    try:
        altura = int(input('Informe a altura (MIN 3, MAX 10): '))
        largura = int(input('Informe a largura (MIN 3, MAX 10): '))
        if altura < 3 or largura < 3 or altura > 10 or largura > 10:
            print('\nErro: A altura e a largura devem estar entre 3 e 10.\n')
            continue 
        quantidade_bombas_max = (altura * largura) - 1
        
        print(f'Tamanho do mapa: {altura}x{largura}.')
        bombas = int(input(f'Informe a quantidade de bombas (MAX {quantidade_bombas_max}): '))
        if bombas < 1 or bombas > quantidade_bombas_max:
            print(f'\nErro: O número de bombas deve ser pelo menos 1 e no máximo {quantidade_bombas_max}.\n')
            continue
        print('\nValores aceitos! Iniciando o jogo...')
        sair = 1 
    except ValueError:
        print('\nEntrada inválida. Por favor, digite *apenas* números inteiros.\n')

sair=0 #retornando o valor original 
    
mapa_real=[[' ' for _ in range(altura)] for _ in range(largura)]#Criando o mapa real
mapa_usuario=[['#' for _ in range(altura)] for _ in range(largura)]#criando o mapa que sera mostrado para o usuario
colocar_bombas()#chamando a funçao que ira colocar as bombas
livre=(altura*largura)-bombas #a quantidade de casas que não tem bombas
while sair == 0:#interface do usuário
    print()
    if mapa_usuario==[['M' for _ in range(altura)] for _ in range(largura)] or livre==0 :#se o usuario marcar todas as casas ou o numero de casas livres chegar a 0 o usuario ganha
        print('AEEEE VOCÊ VENCEU!!!!!!!'.center(50,'-'))
        printar_mapa()
        break
    printar_mapa()
        
    print('Use (A) para abrir, (M) para marcar e (S) para sair')
    try:
        acao_escolhida = input('Qual ação você ira escolher? ').lower()
    
        print('-'*20)
        
        match(acao_escolhida):

            case 'a':
                    linha_escolhida[0]= int(input('Insira a linnha escolhida: '))-1#pegando a linha escolhida e tirando 1 pois a lista começa em 0
                    coluna_escolhida[0]= int(input('Insira a coluna escolhida: '))-1#pegando a coluna escolhida
                    if coluna_escolhida[0]>=largura and linha_escolhida[0]>=altura:#verificaçao de valores
                        print('Informe valores válidos! ')
                    elif (mapa_real[linha_escolhida[0]][coluna_escolhida[0]]) == '*': #verificando se caiu em uma bomba
                        printar_mapa_real()
                        print('KABUUUUUMMM você perdeu!')
                        break
                    else:
                        contagem = contar_bombas()#se der tudo certo vai chamar a funçao de contar as bombas em volta
                        mostrar_quantidade_bombas(contagem)#vai colocar o numero de bombas em volta no mapa
                        livre-=1  #vai tirar um campo livre
            case 'm':
                linha_escolhida[0]= int(input('Insira a linnha escolhida: '))-1#mesma coisa do case a
                coluna_escolhida[0]= int(input('Insira a coluna escolhida: '))-1
                if (mapa_usuario[linha_escolhida[0]][coluna_escolhida[0]]) == '#':#se a casa nao tiver sido aberta, ele vai marcar
                    (mapa_usuario[linha_escolhida[0]][coluna_escolhida[0]])='M'
                else:
                    print('não é possível marcar esta posição!'.upper())#se a casa ja estiver sido aberta ele nao vai deixar marcar
            case 's':#fechar o programa
                print('\n Obrigado por jogar !')
                sair = 999
            case _:# se o usuario digitar algo que nao foi pedido
                print('\nInforme um dos caracteres informados!\n')
    except (ValueError):
        print('\nInforme um dos caracteres informados!\n')