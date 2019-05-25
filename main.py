null = "null"

import random




# IPv8 IP Generater. By Frankie Astori (c) 2019 sharkyReal MIT LICENSE
sections = 0
bits = 256
bits_section = 32
section1 = null
section2 = null
section3 = null
section4 = null
section5 = null
section6 = null
section7 = null
section8 = null
section9 = null
section10 = null
section11 = null
section12 = null
section13 = null
section14 = null
section15 = null
section16 = null
full_IPv8_IP = null


def loop():
    while (bits_section == 32):
        for x in range(32):
            section1 = x
        for y in range(32):
            section2 = y
        for w in range(32):
            section3 = w
        for r in range(32):
            section4 = r
        for t in range(32):
            section5 = t
        for b in range(32):
            section6 = b
        for d in range(32):
            section7 = d
        for k in range(32):
            section8 = k
        for o in range(32):
            section9 = o
        for p in range(32):
            section10 = p
        for l in range(32):
            section11 = l
        for n in range(32):
            section12 = n
        for c in range(32):
            section13 = c
        for z in range(32):
            section14 = z
        for g in range(32):
            section15 = g
        for v in range(32):
            section16 = v
        full_IPv8_IP = section1 + section2 + section3 + section4 + section5 + section6 + section7 + section8 + section9 + section10 + section11 + section12 + section13 + section14 + section15 + section16
        print(full_IPv8_IP)

    
loop()