from sys import stdin, stdout



def main():
    numlist = []
    num = int(stdin.readline())
    for i in range(num):
        X,Y = map(int, stdin.readline().split())
        numlist.append(X+Y)
    return numlist


if __name__ == "__main__":
    for i in main():
        print(i)