def choose_game_mode():
    print('TERMO\n')
    print('ESCOLHA O TIPO DE JOGO:')
    print('1 - Solo')
    print('2 - Dueto')
    print('3 - Quarteto')
    
    while True:
        try:
            user_choise = int(input('Choose the gamemode:'))
            return user_choise
        except ValueError:
            print('Please, type an valid option!')

