# Termo, Dueto ou Quarteto / Escolha do Jogo #
# Defina palavra(s) escolhida(s) / Não podem ser as mesmas no Dueto ou Quarteto #
# Escreva palavra #
# Verifique se é válida / Está no .txt, são letras do alfabeto #
# Compara com a(s) palavras(s) e define se é amarelo, verde ou preto #
# 6, 7 ou 9 tentativas respectivamente #
# Apenas conte tentativas caso a palavra seja válida #
# Caso acerte (todas) a(s) palavra(s) pare o jogo e mande uma mensagem de sucesso #
# Reiniciar o jogo? #
import random
def take_word():
    number = random.randint(0,95)
    file = open("palavras_termo.txt", "r")
    aleatory_word = file.readlines()
    word = aleatory_word[number]
    return word
def user_input():
    for i in range(5):
        inputa = input("type >> ")
        if len(inputa) != 5:
            print('Error - digite uma palavra de 5 letras')
        else:
            try:
                int(inputa)
                raise InvalidInput ("type a word, not number")
            except ValueError:
                return inputa.upper()
        return inputa
class Compair:
    def position(word, inputa):
        #print("  ----  ", inputa, word)
        resultado = "| "
        for index in range(5):
            if word[index] == inputa[index]:
                resultado = resultado + f"\033[92m{inputa[index]}\033[0m | "
            else:
                resultado = resultado + f"{inputa[index]} | "
        return resultado
    def letter(word, inputa):
        list_letter = []
        resultado = "| "
        for leatter in word:
            for i in inputa:
                if leatter in i:
                    list_letter.append(leatter)
        for letra in inputa:
            if letra in list_letter:
                resultado = resultado + f"\033[93m{letra}\033[0m | "
            else:
                resultado = resultado + f"{letra} | "
        return resultado
def main():
    word = take_word()
    inputa = user_input()
    certo = Compair.position(word, inputa)
    meio = Compair.letter(word, inputa)
    print(certo)
    print(meio)
    #compair(word, inputa)
main()
