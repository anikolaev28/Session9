import random
s = 0
while True:
    try:
        for i in range(0,10):
            s = s + random.randint(1,101)
            if s>900:
            print(s)
            break

