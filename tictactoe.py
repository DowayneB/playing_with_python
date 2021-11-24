square = {
    'a': {
        '1': '■',
        '2': '■',
        '3': '■',
    },
    'b': {
        '1': '■',
        '2': '■',
        '3': '■',
    },
    'c': {
        '1': '■',
        '2': '■',
        '3': '■',
    }
}


def change(val, holder):
    letter, number = val
    if letter not in ['a', 'b', 'c']:
        change(input('Your input contain a letter between a and c first  (e.g. a1), please choose another cell '),
               holder)
        return
    if 1 > int(number) or int(number) > 3:
        change(input(
            'Your input contain a number between 1 and 2 after the letter (e.g. a1), please choose another cell '),
            holder)
        return
    if square[letter][number] != '■':
        change(input('you cant change an already set block, please choose another cell '), holder)
        return
    else:
        square[letter][number] = '{}'.format(holder)


def display():
    print('|   | 1  2  3')
    print('--------------')
    for letter in square:
        print('| {} |'.format(letter) + ' {}  {}  {} '.format(square[letter]['1'], square[letter]['2'],
                                                              square[letter]['3']))
    print('')
