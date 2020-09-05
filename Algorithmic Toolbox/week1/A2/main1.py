import random


def main():
    input()
    lst = list(map(int, input().split()))
    max_num1 = lst.pop()
    max_num2 = lst.pop()
    for i in lst:
        if i > max_num1:
            max_num2 = max_num1
            max_num1 = i
        elif i > max_num2:
            max_num2 = i
    print(max_num1 * max_num2)


if __name__ == '__main__':
    main()
