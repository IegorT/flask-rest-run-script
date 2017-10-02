from random import randint

def script_2(tpl):
    MIN, MAX, array_length = tuple(int(x) for x in tpl)
    data = dict((x, randint(MIN, MAX)) for x in range(array_length))
    return data


if __name__ == "__main__":
    print(script_2((0, 100, 5)))
