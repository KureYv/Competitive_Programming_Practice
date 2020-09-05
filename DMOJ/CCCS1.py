from sys import stdin, stdout

def main():
    x,y = stdin.readline().split()
    x = int(x)
    y = int(y)
    volume = (x*y)/2
    return volume


if __name__ == "__main__":
    print(main())

