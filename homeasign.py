import random
import sys
#setup
ballsleft = 90
p1 = 15
p2 = 15
balls = random.sample(range(90), 90)
game_set = random.sample(range(90), 30)
p1_set = random.sample(game_set, 15)
p2_set = [i for i in game_set if not i in p1_set]
p1_field = [p1_set[:5], p1_set[5:10], p1_set[10:]]
p2_field = [p2_set[:5], p2_set[5:10], p2_set[10:]]
for p1_line in p1_field:
    p1_line.sort()
    p1_line.insert(random.randint(0, 4), ' ')
    p1_line.insert(random.randint(0, 5), ' ')
    p1_line.insert(random.randint(0, 6), ' ')
    p1_line.insert(random.randint(0, 7), ' ')
for p2_line in p2_field:
    p2_line.sort()
    p2_line.insert(random.randint(0, 4), ' ')
    p2_line.insert(random.randint(0, 5), ' ')
    p2_line.insert(random.randint(0, 6), ' ')
    p2_line.insert(random.randint(0, 7), ' ')
#functions
def field(p):
    if p == 0:
        print('{:-^26}'.format('Ваша карточка'))
        for line in p1_field:
            for i in line:
                print('{0:>2}'.format(i), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    elif p == 1:
        print('{:-^26}'.format('Карточка компьютера'))
        for line in p2_field:
            for i in line:
                print('{0:>2}'.format(i), end=' ')
            print()
        print('{:-^26}\n'.format('-'))

def your_move():
    answer = input('Зачеркнуть цифру? (y/n): ')
    if answer == 'y':
        if ball in p1_set:
            for i in p1_field:
                try:
                    i.insert(i.index(ball), '><')
                    i.pop(i.index(ball))
                except ValueError:
                    continue
            print('\OK')
            return 1
        else:
            print('\ngame over')
            sys.exit()

    if answer == 'n':
        if ball in p1_set:
            print('\ngame over')
            sys.exit()
        else:
            print('\OK')


def computers_move():
        if ball in p2_set:
            for j in p2_field:
                try:
                    j.insert(j.index(ball), '><')
                    j.pop(j.index(ball))
                except ValueError:
                    continue
            return 1
#game
for ball in balls:
    ballsleft -= 1
    print('\nНовый бочонок: {} (оталось {})\n'.format(ball, ballsleft))
    field(0)
    field(1)
    if your_move() == 1:
        p1 -=1
    if computers_move() == 1:
        p2 -= 1
    if p1 == 0:
        print('\nyou won')
        sys.exit()
    if p2 == 0:
        print('\ngame over')
    if ballsleft == 0:
        print('\ngame over')
        sys.exit()
