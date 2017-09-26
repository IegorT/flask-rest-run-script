from random import randint


ARRAY_LENGTH = 10
MIN = 0
MAX = 100

def script_1():

    data = [randint(MIN, MAX) for _ in range(ARRAY_LENGTH)]
    return data


if __name__ == "__main__":
    print(script_1())