import copy
import random


class Hat:
    def __init__(self, **args):
        self.my_dict = args
        self.contents = []
        self.copy_of_contents = []
        for k, v in self.my_dict.items():
            for i in range(0, v):
                self.contents.append(k)
                self.copy_of_contents.append(k)

    def draw(self, number_of_draws):
        if self.contents.__len__() <= number_of_draws:
            return self.copy_of_contents

        else:
            drawn = random.sample(self.contents, number_of_draws)
            for i in range(0, number_of_draws):
                self.contents.remove(drawn[i])
            return drawn

    def set_copy(self):
        self.contents = self.copy_of_contents.copy()


def experiment(**args):
    hat = copy.copy(list(args.values())[0])
    expected_balls = list(args.values())[1]
    num_balls_drawn = list(args.values())[2]
    num_experiments = list(args.values())[3]

    m = 0
    n = num_experiments

    for i in range(0, num_experiments):
        favorable_case = False
        current_dict = {}
        hat.set_copy()
        current_list = hat.draw(num_balls_drawn)
        for j in range(0, len(current_list)):
            if current_list[j] not in list(current_dict.keys()):
                current_dict[current_list[j]] = 1
            else:
                current_dict[current_list[j]] += 1
            for k, v in expected_balls.items():
                if k in current_dict.keys():
                    if v <= current_dict[k]:
                        favorable_case = True
                    else:
                        favorable_case = False
                        break
                else:
                    favorable_case = False
                    break
        if favorable_case:
            m += 1

    return m / n
