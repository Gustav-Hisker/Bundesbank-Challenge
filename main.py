
class Bank:
    def __init__(self, r, p, ID):
        self.M = set()
        self.r = r
        self.p = p
        self.ID = ID


def readFileData(path):
    with open(path) as f:
        m, b, d = map(int, f.readline().strip().split(" "))
        W = {}
        for i, w in enumerate(map(int, f.readline().strip().split(" "))):
            W[i] = w

        B = set()
        mode = False
        cur = None
        i = 0
        for line in f:
            line = line.strip()
            if mode:  #
                m, r, p = map(int, line.split(" "))
                cur = Bank(r, p, i)
            else:  # Münzen
                cur.M = set(map(int, line.split(" ")))
                B.add(cur)

            mode = not mode
            i += 1

        return m, b, d, W, B


def greedy(path):
    m, b, d, W, B = readFileData(path)

    aScores = {}

    for
