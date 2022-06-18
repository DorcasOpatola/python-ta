import sys
import os


def prime(s):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

for i in range(2,12):
    if prime(i):
        print(i)


def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
