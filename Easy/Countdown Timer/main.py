import time


# def countdown(t):
t = int(input("تایمت رو به ثانیه بنویس:"))

while t:

    mins, secs = divmod(t, 60)

    timer = '{:02d}:{:02d}'.format(mins, secs)

    print(timer, end="\n")

    time.sleep(1)

    t -= 1

print("تمام شد!")


