#!/usr/bin/env python3

import sys

try:
    incomes = (sys.argv[1])
except:
    print('sys.argv error')
income = int(incomes)
ti = income - 3500

if ti < 0:
    tp = 0
elif 0 <= ti <= 1500:
    tp = ti * 0.03
elif 1500 < ti <= 4500:
    tp = ti * 0.1 - 105
elif 4500 < ti <= 9000:
    tp = ti * 0.2 - 555
elif 9000 < ti <= 35000:
    tp = ti * 0.25 - 1005
elif 35000 < ti <= 55000:
    tp = ti * 0.3 - 2755
elif 55000 < ti <= 80000:
    tp = ti * 0.35 - 5505
else:
    tp = ti * 0.45 -13505

print('{:.2f}'.format(tp))



