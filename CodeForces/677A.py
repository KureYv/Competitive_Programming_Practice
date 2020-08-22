from sys import stdin, stdout

def main():
    num, height = stdin.readline().split()
    num = int(num)
    height = int(height)
    count = num
    fh = stdin.readline().split()
    for i in range(0,int(num)):
        if int(fh[i]) > height:
            count+=1
    return count
    
if __name__ == "__main__":
    stdout.write(str(main()))