import time

i = 0

while i < 4:
    print(i)
    time.sleep(1)
    i += 1
    if i == 4:
        i = 0