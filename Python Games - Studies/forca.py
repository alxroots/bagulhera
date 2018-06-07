import random, os

hangmanpics = ['''
 +---+
 |   |
     |
     |
     |
     |
=======
''', '''
 +---+
 |   |
 O   |
     |
     |
     |
=======
''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
=======
''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=======
''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=======
''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=======
''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=======
''']


palavras = 'claro estrutura atual organização apresenta tendências sentido aprovar manutenção todos recursos funcionais envolvidos empenho analisar consolidação estruturas impacto indireto reavaliação formas ação'.split()

def obter_palavra_aleatoria(var_palavra_as_lista):
    posicao_palavra = random.randint(0, len(var_palavra_as_lista) - 1)
    return var_palavra_as_lista[posicao_palavra]

def mostrar_quadro(img_hangman, missed_letters, correct_letters, secret_word):
    os.system('clear')
    print("============ Bem vindo! Este é o jogo da forca. ==============")
    print()
    print(img_hangman[len(missed_letters)])
    print()

    print('!!! CUIDADO !!!! Observe as letras que você já errou => ', end=' ')
    for letra in missed_letters:
        print(letra, end=' ')
    print()

    blanks = '_' * len(secret_word)# Multiplicar o underscore pelo tamanho da palavra secreta.

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters: #could be == instead of in ??
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]



    for letra in blanks:
        print(letra, end=' ')
    print()

def palpitar(l_jogado):
    '''
    Funcao que testa se o jogador usou uma letra e não qualquer outra coisa
    e contabiliza letra jogada retornando o valor da letra que foi jogada
    '''
    while True:
        print()
        print('Digite seu palpite: ')
        palpite = input()
        palpite = palpite.lower()
        if len(palpite) != 1:
            print("Você deve digitar apenas uma letra.")
        elif palpite in l_jogado:
            print("Esta letra já foi escolhida")
        elif palpite not in 'abcdefghijklmnopqrstuvxwyz':
            print("Você não digitou uma letra. !!Atenção!! Tente novamente.")
        else:
            return palpite


def jogar_novamente():
    '''
    Caso o jogador queira jogar novamente a função retorna True
    '''
    print("Deseja jogar novamente? Digite Sim ou Não")
    return input().lower().startswith('s')


#THE GAME

#default variaveis
erros = ''
acertos = ''
palavra_secreta = (obter_palavra_aleatoria(palavras))
game_finished = False


while True:

    mostrar_quadro(hangmanpics, erros, acertos, palavra_secreta)
    palpite_definido = palpitar(erros + acertos) #Definir palpite

    if palpite_definido in palavra_secreta:

        acertos = acertos + palpite_definido

        #Verificando se o jogador ganhou
        todasLetras_Encontradas = True
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] not in acertos:
                todasLetras_Encontradas = False
                break
        if todasLetras_Encontradas:
            print(f'Show!!! Você encontrou a palavra secreta que é == {palavra_secreta} ==')
            game_finished = True
    else:
        erros = erros + palpite_definido

        if len(erros) == len(hangmanpics) - 1:
            mostrar_quadro(hangmanpics, erros, acertos, palavra_secreta)
            print(f'Você estourou sua cota de palpites e não acertou a palavra == {palavra_secreta} ==')

            game_finished = True

    #Jogar novamente?
    if game_finished:
        if jogar_novamente():
            #default variaveis
            erros = ''
            acertos = ''
            palavra_secreta = (obter_palavra_aleatoria(palavras))
            game_finished = False
        else:
            break
