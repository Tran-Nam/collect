from multiprocessing import Pool 
import time
out = []
def func(a):
    global out
    x, y = a
    print(hex(id(x)))
    print(x)
    count=0
    for i in range(10**8):
        count+=i
    out.append(2)

# args = range(10)
args = [(1, 2), (2, 3), (3, 4)]
args1 = [(2, 4), (4, 6), (6, 8)]
args2 = [(1, 5)]
args3 = [(3, 5), (5, 4), (6, 19)]
arg = [args, args1, args2, args3]
res = []
t1 = time.time()
for ar in arg:
    for k in ar:
        # print(k)
        res.append(func(k))
print(time.time() - t1)
print(res)

p = Pool(3)
t2 = time.time()
# out = []
for ar in arg:
    p.map(func, ar)
print(time.time() - t2)
print(out)
