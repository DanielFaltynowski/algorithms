def reduce(arr, acc, reducer):
    for elem in arr:
        acc = reducer(acc, elem)
    return acc

def filter(arr, condiction):
    res = []
    for elem in arr:
        if condiction(elem):
            res.append(elem)
    return res


def mapper(arr, scale):
    res = []
    for elem in arr:
        res.append(scale(elem))
    return  res


if __name__ == '__main__':
    l = [1, 2, 3]

    lr = reduce(l, [], lambda acc, elem: acc + [elem * 3])
    lf = filter(l, lambda elem: elem >= 2)
    lm = mapper(l, lambda elem: elem * 4)

    print(f"Original list: {l}")
    print(f"Reduced list: {lr}")
    print(f"Filtered list: {lf}")
    print(f"Mapped list: {lm}")