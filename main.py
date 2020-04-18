import sys


def start(filename):
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
        for index in range(0, len(lines), 2):
            print(lines[index][:-1])
            answer = input('(\\a for answer) >>> ')
            while answer != lines[index + 1][:-1]:
                if answer == "\\a":
                    print(lines[index + 1][:-1])
                answer = input('(wrong; \\a for answer) >>> ')


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        start(filename)
