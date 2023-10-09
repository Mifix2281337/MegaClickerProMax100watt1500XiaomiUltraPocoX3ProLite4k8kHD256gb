import time
timing = time.time()

i = 5
while True:
    if time.time() - timing > 1.0:
        timing = time.time()
        i -= 1
        if i > 0:
            print(f"Осталось {str(i)} секунд")
        else:
            break