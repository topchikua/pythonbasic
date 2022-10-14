"""
Дан многомерный список. Вывести на экран все четные столбцы, у которых первый элемент больше последнего.
[1 6 8 5 4 0 3],
[5 7 8 9 4 2 1],
[6 0 7 8 1 2 5],
[5 7 2 7 5 2 1]

8 3
8 1
7 5
2 1
"""

sets_num = [
    [1, 6, 8, 5, 4, 0, 3],
    [5, 7, 8, 9, 4, 2, 1],
    [6, 0, 7, 8, 1, 2, 5],
    [5, 7, 2, 7, 5, 2, 1]
]

for i in range(len(sets_num)):
    for j in range(len(sets_num[i])):
        if j % 2 == 0 and sets_num[0][j] > sets_num[-1][j]:
            print(sets_num[i][j], end=' ')
    print()