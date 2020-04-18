import sys


def start(filename):
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
        for index in range(len(lines), step=2):
            print(lines[index])
            answer = input('(\\a for answer) >>> ')
            while answer != lines[index]:
                if answer == "\\a":
                    print(lines[index + 1])
                else:
                    answer = input('(wrong; \\a for answer) >>> ')


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        start(filename)
