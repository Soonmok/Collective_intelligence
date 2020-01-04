from math import sqrt


def uclidian_sim(data1, data2):
    sim_value = 0

    if len(data1) != len(data2):
        raise ValueError("length of two dataset should be equal")
    for score1, score2 in list(zip(data1, data2)):
        sim_value += pow(score1 - score2, 2)
    return 1 / (1 + sqrt(sim_value / len(data1)))


def pearson_sim(data1, data2):
    if len(data1) != len(data2):
        raise ValueError("length of two dataset should be equal")
    n = len(data1)

    avg1 = sum([x for x in data1]) / n
    avg2 = sum([x for x in data2]) / n
    covariance1 = sqrt(sum([pow(x - avg1, 2) for x in data1]))
    covariance2 = sqrt(sum([pow(x - avg2, 2) for x in data2]))

    psum = sum([(x - avg1) * (y - avg2) for x, y in list(zip(data1, data2))])

    pearson_sim = psum / (covariance1 * covariance2)
    assert (-1 <= pearson_sim) and (pearson_sim <= 1)
    return pearson_sim


def jaccard_sim(set_a, set_b):
    return len(set_a & set_b) / len(set_a.union(set_b))