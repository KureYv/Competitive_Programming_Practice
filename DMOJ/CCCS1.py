from sys import stdin, stdout

def main():
    x,y = stdin.readline().split()
    x = int(x)
    y = int(y)
    volume = str(int((x*y)/2))
    if (x%2 != 0 and y%2 != 0):
        volume = volume+".5"
    else:
        volume = volume+".0"
    return volume


if __name__ == "__main__":
    print(main())

