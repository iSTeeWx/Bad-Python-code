def main():
    board: list = create_board()

    playing: bool = True
    player: chr = '0'

    while playing:
        player = ['0', 'X'][player == '0']

        valid_start: bool = False
        valid_destination: bool = False

        from_x: int = -1
        from_y: int = -1
        to_x: int = -1
        to_y: int = -1

        print_list(board)
        print('Turn of', player)

        while not valid_start:
            while from_x == -1:
                temp: str = input('From X: ')

                if test_input(temp):
                    from_x = int(temp) - 1
                else:
                    error('Not a valid number!\nShould be between but not including 0-9')

            while from_y == -1:
                temp: str = input('From Y: ')

                if test_input(temp):
                    from_y = int(temp) - 1
                else:
                    error('Not a valid number!\nShould be between but not including 0-9')

            if board[from_y][from_x] != player:
                error('You don\'t have a piece in this space')
                from_x = -1
                from_y = -1
                valid_start = False
            else:
                valid_start = True

        while not valid_destination:
            while to_x == -1:
                temp: str = input('To X: ')

                if test_input(temp):
                    to_x = int(temp) - 1
                else:
                    error('Not a valid number!\nShould be between but not including 0-9')

            while to_y == -1:
                temp: str = input('To Y: ')

                if test_input(temp):
                    to_y = int(temp) - 1
                else:
                    error('Not a valid number!\nShould be between but not including 0-9')

            if from_x == to_x and from_y == to_y:
                error('Not a valid number!\nShould be different from starting position')
                to_x = -1
                to_y = -1
                continue

            if abs(to_x - from_x) > 1 or abs(to_y - from_y) > 1:
                error('Not a valid number!\nDestionation is to far')
                to_x = -1
                to_y = -1
                continue

            if board[to_y][to_x] == player:
                error('Space already occupied by self')
                to_x = -1
                to_y = -1
                valid_destination = False
            else:
                valid_destination = True

        board[from_y][from_x] = '???'
        board[to_y][to_x] = player


def test_input(str_in: str) -> bool:
    if str_in == '':
        return False
    return str_in in '12345678'

def error(cause: str) -> None:
    print('|', '#' * len(cause), '|')
    print('|', cause, '|')
    print('|', '#' * len(cause), '|')

def create_board() -> list:
    width: int = 8
    height: int = 8

    out = [['???' for _ in range(width)] for __ in range(height)]

    for i in range(width):
        # Player that sits at the top of the grid
        out[0][i] = 'X'
        # Player that sits at the bottom of the grid
        out[height - 1][i] = '0'

    return out

def print_list(list_in: list) -> None:
    # https://stackoverflow.com/a/45027722
    print('\n'.join(map(''.join, list_in)))


if __name__ == '__main__':
    main()
