import math
from bisect import bisect_left, bisect_right
from tabnanny import check
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional
from sortedcontainers import SortedList
from collections import Counter, deque
from queue import Queue
from collections import defaultdict
import heapq
import sys

sys.setrecursionlimit(120000)

n = int(input())
a = list(map(int, input().split()))
q = int(input())

a.sort()

for i in range(q):
    b = int(input())
    num = bisect_right(a,b)
    if num < len(a):
        print(min(abs(b-a[num-1]), abs(b-a[num])))
    else:
        print(abs(b-a[num-1]))
