from Effects import print_text

class Score:
    def __init__(self, table):
        self.score_table = table

    def update(self, name, scores):
        self.score_table[name] = scores

    def print(self, x, y):
        step_x = 250
        step_y = 30

        for name, scores in self.score_table.items():
            print_text(name, x, y)
            x+= step_x
            print_text(str(scores), x, y)
            x -= step_x
            y += step_y