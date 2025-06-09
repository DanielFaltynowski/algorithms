def reduce(array, accumulator, predicate):
    for element in array:
        accumulator = predicate(accumulator, element)
    return accumulator

def filter(array, predicate):
    response = []
    for element in array:
        if predicate(element):
            response.append(element)
    return response


def mapper(array, predicate):
    response = []
    for element in array:
        response.append(predicate(element))
    return response


if __name__ == '__main__':
    l = [1, 2, 3]

    lr = reduce(l, 0, lambda acc, elem: acc + elem)
    lf = filter(l, lambda elem: elem >= 2)
    lm = mapper(l, lambda elem: elem * 4)

    print(f"Original list: {l}")
    print(f"Reduced list: {lr}")
    print(f"Filtered list: {lf}")
    print(f"Mapped list: {lm}")