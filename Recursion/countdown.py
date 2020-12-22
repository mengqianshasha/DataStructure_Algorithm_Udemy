import time

def countdown(n):
    if n == 0:
        return 0
    else:
        print(n)
        time.sleep(1)
        return countdown(n-1)


print(countdown(5))