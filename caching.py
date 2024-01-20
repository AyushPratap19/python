from functools import lru_cache#least recently used cache
import time
#this is used to improve performance of a program
#which uses repeated values again and again
#so those values are moved to lru cache and when that value is used again it doesnt get computed
@lru_cache(maxsize=None)
def fn(n):
    time.sleep(5)
    return n*5
print(fn(1))
print("Done for 1")
print(fn(2))
print("Done for 2")
print(fn(3))
print("Done for 3")
#if we again use the same values again it will not take any time 
print(fn(1))
print("Done for 1")
print(fn(2))
print("Done for 2")
print(fn(3))
print("Done for 3")