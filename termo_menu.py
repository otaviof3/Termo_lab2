

def choose_game_mode():
  

    print('TERMO\n')
    print('ESCOLHA O TIPO DE JOGO:')
    print('1 - Solo')
    print('2 - Dueto')
    print('3 - Quarteto')
    
    while True:
        try:
            user_choise = int(input('Choose the gamemode: '))
            print('//type any other number to exit//')
            return user_choise
        except ValueError:
            print('Please, type a valid option!')

def menu(user_choise):
    while True:
        if user_choise == 1:
            print('a')
        elif user_choise == 2:
            pass
        elif user_choise == 3:
            pass
        else:
            break
