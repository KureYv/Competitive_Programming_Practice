from sys import stdin, stdout

array = []
def main():
    T = int(stdin.readline())

    for i in range(T):
        counter = 0
        maxX = 0
        maxY = 0
        lists = list(stdin.readline())
        for i in lists:
            if i == "R":
                maxX +=1
            if i == "L":
                maxX -=1
            if i == "U":
                maxY +=1
            if i == "D":
                maxY -=1
            if i == "?":
                counter+=1
        minX = maxX
        minY = maxY
        for i in range(counter):
            maxX +=1
            maxY +=1
            minX -=1
            minY -=1
        array.append([str(minX),str(minY),str(maxX),str(maxY)])
    return array
        

if __name__ == "__main__":
    for i in main():
        print(' '.join(i))


