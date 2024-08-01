ali_scores = {
    "dini": (12, 1),
    "riazi": (17, 3),
    "arabi": (8, 2),
    "fizik": (15, 3),
    "zaban": (20, 2),
}


def status(scores):
    for name, score in scores.items():
        if score[0] >= 10:
            print(name, ": passed")
        else:
            print(name, ": failed")


def average(scores):
    vahedha = []
    nomarat = []
    for name, score in scores.items():
        # print(name,score[0]*score[1])
        vahedha.append(score[1])
        nomarat.append(score[0] * score[1])

    print(sum(nomarat) / sum(vahedha))


average(ali_scores)
