import random
def take_word():
    number = random.randint(0,95)
    file = open("palavras_termo.txt", "r")
    aleatory_word = file.readlines()
    word = aleatory_word[number]
    return word
    

def user_input():
    try:
        while True:
            inputa = str(input("type >> ")).upper()
            return inputa
    except ValueError:
        print("oi - wot are you typ'ing")
    

def compair(word, inputa):
    for leatter in word:
        for i in inputa:
            if leatter in i:
                print(word, leatter)
                
        

def main():
    word = take_word()
    inputa = user_input()
    compair(word, inputa)
main()
