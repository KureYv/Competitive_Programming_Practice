from sys import stdin,stdout

def input():
    return int(stdin.readline())

def main(num):
    if num < 1:
        stdout.write("Don't be lazy, it takes only few minutes, you can do it.")
    elif num == 1:
        stdout.write("Good Job")
    else:
        stdout.write("You Rocks Man")
        
if __name__ == "__main__":
    main(input())
