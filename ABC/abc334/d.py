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

n,q = map(int, input().split())
r = list(map(int, input().split()))
query = [int(input()) for _ in range(q)]

r.sort()

s = [0] * (n+1)
for i in range(n):
  s[i+1] = s[i] + r[i]

for i in range(q):
    print(bisect_right(s,query[i])-1)