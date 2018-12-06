import time
import subprocess as sp

abc = [15, 18, 23, 24]

for x in range(0, 3):
    print(abc[x], "IS HIGH")
    time.sleep(0.5)
    tmp = sp.call('clear',shell=True)
    print(abc[x], "IS LOW")
    time.sleep(0.5)
    tmp = sp.call('clear',shell=True)

for y in range(0, 5):
    x = 3
    print(abc[x], "Blink HIGH")
    time.sleep(0.5)
    tmp = sp.call('clear',shell=True)
    print(abc[x], "Blink LOW")
    time.sleep(0.5)
    tmp = sp.call('clear',shell=True)
