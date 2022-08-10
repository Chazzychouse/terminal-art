import time
import random
from constant import colors
CEND      = '\33[0m'


color1 = colors[0]
color2 = colors[5]
n = 0
k = 19
counter = 0

while True:
    
    if counter == 20:
        color1 = colors[random.randint(0, 15)]
        color2 = colors[random.randint(0, 15)]
        counter = 0
    for j in range(20):
        
        if j != n and j != k:
            print((color1 +  "#" + CEND), end = "")
        else:
            print((color2 + "O" + CEND), end = "")
           
        
    print()
    time.sleep(0.04)
    if n == 19:
        n = 0
        k = 19
    else:
        n = n + 1
        k = k - 1
    counter += 1