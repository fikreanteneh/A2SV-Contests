

from collections import Counter
import math


n = int(input())


_2div = n//2

_3div = n//3
_23div = n//6
_3div -= _23div

_5div = n//5
_25div = n//10
_5div -= _25div
_35div = n//15
_5div -= _35div
_235div = n//30
_5div += _235div

_7div = n//7
_27div = n//14

_7div -= n//_27div



