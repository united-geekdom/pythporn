import time

num=int(input("Number of Faps: "))
speed = int(input("How fast is the fap (1-10): "))
length = int(input("Length of cawk (1-10): "))
volume = int(input("Volume of cum: "))
cum_chars = ["ﷺ","ﷻ","﷽"]
for k in range(num):
    for i in range(length): 
        cock = "8"
        for j in range (length-i-1):
            cock += "="
        cock += "C"
        for j in range(i):
            cock += "="
        cock += "D"
        print('\033[H\033[J', end='')
        time.sleep(1/(speed*length))
        print(cock)
    for i in range(length): 
        cock = "8"
        for j in range (i):
            cock += "="
        cock += "C"
        for j in range(length-i-1):
            cock += "="
        cock += "D"
        print('\033[H\033[J', end='')
        time.sleep(1/(speed*length))
        print(cock)
for i in range(volume):
    cock += cum_chars[i%3]
    print('\033[H\033[J', end='')
    time.sleep(0.5/volume)
    print(cock)
    