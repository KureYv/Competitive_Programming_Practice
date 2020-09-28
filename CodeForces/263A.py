from sys import stdin,stdout
center = [3,3]
matrix = []


def input():
    for i in range(0,5):
        matrix.append(stdin.readline().split())
    return matrix

def search(matrix):
    counter = 0
    countera = 0
    x = 0
    for i in range(0,5):
        for a in range(0,5):
            if(matrix[i][a] == "1"):
                x = [i,a]
    return x


def main(x):
    a = x[0]+1-3
    b = x[1]+1-3
    return (abs(int(a))+abs(int(b)))

if __name__ == "__main__":
    print(main(search(input())))