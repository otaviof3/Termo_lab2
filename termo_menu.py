import os

def clear_screen():
    # Try to clear the screen for various operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_game_mode():
    # Clear the terminal screen
    clear_screen()

    print('TERMO\n')
    print('ESCOLHA O TIPO DE JOGO:')
    print('1 - Solo')
    print('2 - Dueto')
    print('3 - Quarteto')
    
    while True:
        try:
            user_choice = int(input('Choose the gamemode: '))
            return user_choice
        except ValueError:
            print('Please, type a valid option!')

