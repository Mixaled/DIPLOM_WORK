import sys
from time import sleep
import time
import random
class Zadachki:
    def __init__(self):
        pass
    def convert(self, n):
        while not isinstance(n, int):
            try:
                n = int(n)
                return n
            except:
                print("It isn't what I need")
                break
    def correct_or(self, answer, inp):
        return 1 if inp == answer else 0

    def zadacha1(self):
        global answer
        answer = random.randint(1, 100)
        x = answer - random.randint(1, answer - 1)
        y = answer - x
        print(f"{x} + {y} = ")
        inp = input()
        inp = self.convert(inp)
        result = self.correct_or(answer, inp)
        return result
    def zadacha1_l(self):
        print(f"You lose the answer is {answer}")


def dead_game():
    print("Secret")
    timer = 0
    count = 0
    start_time = time.time()
    for i in range(1, 11):
        z = Zadachki()
        print(f'{i}:')
        res = z.zadacha1()
        timer = round(time.time() - start_time, 3)
        if res == 1:
            count += 1
            print("Time:", timer)
        else:
            z.zadacha1_l()
            game_over()
            break
    if count == 10 and timer < 50:
        print(f"Congratulation time {timer}")
    else:
        print('You are too slow need time less 50 sec')
        game_over()


def game_over():
    print("\t\t*_*")
    sys.exit()
dead_game()




