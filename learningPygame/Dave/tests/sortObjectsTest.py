class ScoreEntry:
    def __init__(self, name, score, time_stamp):
        self.name = name
        self.score = score
        self.time_stamp = time_stamp

    def __repr__(self):
        return self.name + " " + str(self.score)


Frank = ScoreEntry('Frank', 300, 20)
Bob = ScoreEntry('Bob', 200, 8)
Alice9 = ScoreEntry('Alice9', 200, 9)
Alice12 = ScoreEntry('Alice12', 200, 12)
Alice10 = ScoreEntry('Alice10', 200, 10)
Alice11 = ScoreEntry('Alice11', 200, 11)
Leo = ScoreEntry('Leo', 100, 20)
my_list = [Bob, Alice9, Leo, Alice10, Alice11, Alice12, Frank]

print(my_list)

my_list = sorted(my_list,
                 key=lambda score_entry: (score_entry.score, -score_entry.time_stamp),
                 reverse=True)
print(my_list)
