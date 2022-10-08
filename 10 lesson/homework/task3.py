"""
Дан многомерный список в котором находится результат игры в крестики нолики,
выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
Необходимо учитывать то, что есть разные выигрышные варианты и программа должна их распознавать.

    ['o', 'o', 'o'],
    ['x', 'x', 'o'],
    ['x', 'o', 'x']
"""

X = 3
Y = 3
game_result = [
    ['x', 'o', 'x'],
    ['o', 'o', 'x'],
    ['x', 'x', 'o']
]
winner = 'Ничья'

print('\nРезультат игры:')
for a in range(X):
    for b in range(Y):
        print(game_result[a][b], end=' ')
    print()

for row in game_result:
    if row.count('x') == 3:
        winner = 'X'
    elif row.count('o') == 3:
        winner = 'O'

for col in range(Y):
    if game_result[0][col] == 'x' and game_result[1][col] == 'x' and game_result[2][col] == 'x':
        winner = 'X'
    elif game_result[0][col] == 'o' and game_result[1][col] == 'o' and game_result[2][col] == 'o':
        winner = 'O'

if game_result[0][0] == 'x' and game_result[1][1] == 'x' and game_result[2][2] == 'x' or \
        game_result[2][0] == 'x' and game_result[1][1] == 'x' and game_result[0][2] == 'x':
    winner = 'X'
elif game_result[0][0] == 'o' and game_result[1][1] == 'o' and game_result[2][2] == 'o' or \
        game_result[2][0] == 'o' and game_result[1][1] == 'o' and game_result[0][2] == 'o':
    winner = 'O'

print(f'\nРезультат: ({winner})')
