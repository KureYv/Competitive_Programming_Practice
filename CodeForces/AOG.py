from sys import stdin, stdout

def objectnum():
    return int(input())

def inputs():
    return input().split()



def min(inputs):
    min = inputs[0]
    for i in inputs:
        if int(i) < int(min):
            min = i
    return min

def max(inputs):
    max = inputs[0]
    for i in inputs:
        if int(i) > int(max):
            max = i
    return max
    

def main(objectnum, inputs, max, min):
    counter = 0
    locate = inputs.index(max)
    for i in range(locate):
        position = locate - i
        temp = inputs[position]
        inputs[position] = inputs[position - 1]
        inputs[position - 1] = temp
        counter+=1
    locates = len(inputs) - inputs[::-1].index(min) - 1
    for i in range(objectnum - locates-1):
        position = locates + i
        temp = inputs[position]
        inputs[position] = inputs[position + 1]
        inputs[position + 1] = temp
        counter+=1
    return counter

if __name__ == "__main__":
    a =objectnum()
    b = inputs()
    stdout.write(str(main(a, b, max(b), min(b))))