import copy
import random

class Hat:
    
    def __init__(self, **kwargs):
        if len(kwargs) == 0:
            raise TypeError(f"The hat must be created with at least one argument")
        number_of_balls = 0
        for key, value in kwargs.items():
            number_of_balls += value
        if number_of_balls == 0:
            raise ValueError(f"The hat must be created with at least one ball")
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)
    
    def draw(self, number_of_balls):
        draw_balls = []
        number_of_balls_to_draw = min(number_of_balls, len(self.contents))
        for _ in range(number_of_balls_to_draw):
            element = random.choice(self.contents)
            self.contents.remove(element)
            draw_balls.append(element)
        return draw_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    kwargs = {i: vars(hat)['contents'].count(i) for i in set(vars(hat)['contents'])}
    N = num_experiments
    M = 0
    expected_balls_list = []
    for key, value in expected_balls.items():
            for _ in range(value):
                expected_balls_list.append(key)
    for _ in range(N):
        hat_copy = Hat(**kwargs)
        draw = hat_copy.draw(num_balls_drawn)
        experiment_true = True
        for key, value in expected_balls.items():
            if draw.count(key) < value:
                experiment_true = False
        if experiment_true:
            M += 1
    probability = M/N
    return probability

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)