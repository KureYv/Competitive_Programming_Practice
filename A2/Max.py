from sys import stdin, stdout

def input():
    return stdin.readline().split()

def main(lists):
    max = lists[0]
    for i in lists:
        if int(i) > int(max):
            max = i
    return max


if __name__ == "__main__":
    stdout.write(main(input()))