from sys import stdin, stdout



def main():
    list = []
    num = int(input())
    for i in range(num):
        c = input()
        if("+" in c):
            b = c.split(" ")
            sum = int(b[0]) + int(b[2])
            correctnum = b[4]
            
        else:
            b = c.split(" ")
            sum = int(b[0]) - int(b[2])
            if(b[4] == "-"):
                correctnum = b[5]*-1
            else:
                correctnum = b[4]
        if(sum == int(correctnum)):
            list.append("YES")
        else:
            list.append("NO")
    return list



if __name__ == "__main__":
    counter = 1
    for i in main():
        print("Case "+ str(counter) +": " + str(i))
        counter+=1
