import random
def take_word():
    number = random.randint(0,95)
    file = open("palavras_termo.txt", "r")
    aleatory_word = file.readlines()
    word = aleatory_word[number]
    return word
    

def user_input():
    while True:
        try:
            inputa = input("type >> ")
            return inputa.upper()
        except ValueError:
            print("oi - wot are you typ'ing")
    

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
