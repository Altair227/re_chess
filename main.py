import re
from src.board import Board


def print_board(board: Board):
    print('  +' + '----+' * 8)
    for row in range(8, 0, -1):
        print(str(row) + ' |', end='')
        # print(str(row - 1) + ' |', end='')
        for col in range(8):
            print(' ', end='')
            player = board.get_item(row - 1, col)
            if player:
                print(player.char, end='')
            else:
                print('  ', end='')
            print(' |', end='')
        print()
        print('  +' + '----+' * 8)
    print('   ', end='')
    ix = ord('A')
    for col in range(8):
        print(f' {chr(ix + col)}   ', end='')
        # print(f' {col}   ', end='')
    print()


def print_menu():
    print('exit                       - Выход')
    print('<col><row> <col><row> - движение фигуры')


_board = Board()
pattern = r'^([A-H]{1}[1-8]{1}) ([A-H]{1}[1-8]{1})$'
while True:
    print_board(_board)
    print()
    print('Ходят', end=' ')
    if _board.color.is_white():
        print('белые')
    else:
        print('черные')
    print()
    print_menu()
    print()
    cmd = input('Введите команду: ').strip()
    try:
        if cmd == 'exit':
            break
        match = re.match(pattern, cmd)
        if match is None:
            raise Exception('Неверная команда')
        char_start = match.group(1)
        char_end = match.group(2)
        start = _board.convert(char_start)
        end = _board.convert(char_end)
        if not start or not end:
            raise Exception('Неверные координаты')
        player = _board.get_item(*start)
        if not player:
            raise Exception(f'В {char_start} отсутствует фигура')
        if player.color != _board.color:
            raise Exception('Вы не можете двигать чужие фигуры')
        end_item = _board.get_item(*end)
        if not end_item:
            if not player.can_move(_board, *start, *end):
                raise Exception('Вы не можете так двигаться')
        elif player.color == end_item.color:
            raise Exception('Вы не можете атаковать свои фигуры')
        elif not player.can_attack(_board, *start, *end):
            raise Exception('Вы не можете атаковать данную фигуру')
        _board.move(*start, *end)

    except Exception as e:
        print(e)
        input('Нажмите любую клавишу для продолжения...')
