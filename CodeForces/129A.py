from sys import stdin, stdout

num = int(stdin.readline())
array = stdin.readline().split()

def main(array):
    count = 0
    for i in range(0,num):
        sum = 0
        lists = 0
        for e in range(0,num):
            if(int(e != i)):
                sum+=int(array[e])
        if(sum%2==0):
            count+=1
    return count
                

if __name__ == "__main__":
    print(main(array))