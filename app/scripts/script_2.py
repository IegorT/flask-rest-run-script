from random import randint

ARRAY_LENGTH = 10
MIN = 0
MAX = 100

def script_2():
    data = dict((x, randint(MIN, MAX)) for x in range(ARRAY_LENGTH))
    return data


if __name__ == "__main__":
    print(script_2())