import razm2
import time

for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            for d in range(1, 100):
                start_time = time.time()
                ans = razm2.Solution(f"{a} {b} {c} {d}")
                end_time = time.time()
               # print(end_time - start_time, ans,"   -   ", a,b,c,d)
    print(a)