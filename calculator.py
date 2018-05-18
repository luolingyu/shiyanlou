#!/usr/bin/env python3
#tax_income 应纳所得额，tax_payable:应纳税额，income:收入
import sys
try:
    print(sys.argv[1])
except:
    print('error')

income = int(sys.argv[1])   #工资收入
tax_income = income - 3500   #计算应纳所得额＝工资－各项保险费－起征点（3500）
#计算税额 ＝ 应纳税所得额＊税率 －速算扣除数
if tax_income <= 0:
    print("{:.2f}".format(0.00))
elif 0 < tax_income <= 1500:
    tax_payable = tax_income * 0.03
    print("{:.2f}".format(tax_payable))
elif 1500 < tax_income <= 4500:
    tax_payable = tax_income * 0.1 - 105
    print("{:.2f}".format(tax_payable))
elif 4500 < tax_income <= 9000:
    tax_payable = tax_income * 0.2 - 555
    print("{:.2f}".format(tax_payable))
elif 9000 < tax_income <= 35000:
    tax_payable = tax_income * 0.25 - 1005
    print("{:.2f}".format(tax_payable))
elif 35000 < tax_income <= 55000:
    tax_payable = tax_income * 0.3 - 2755
    print("{:.2f}".format(tax_payable))
elif 55000 < tax_income <= 80000:
    tax_payable = tax_income * 0.35 - 5505
    print("{:.2f}".format(tax_payable))
else:
    tax_payable = tax_income * 0.45 - 13505
    print("{:.2f}".format(tax_payable))



