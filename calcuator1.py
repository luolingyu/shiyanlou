#!/usr/bin/env python3
#tax_income 应纳所得额，tax_payable:应纳税额 简写（tp），income:收入 ，social_security：社保
#各项保险费占工资比列：养老8％，医疗2％，失业：0.5％，工伤、生育0，公积金6％
#计算应纳所得额＝工资－各项保险费－起征点（3500）
#计算税额 ＝ 应纳税所得额＊税率 －速算扣除数

import sys

def calculator(income, id):
    s= income*(0.08+0.02+0.005+0.06)
   
    ti = income - s -3500 
    
    if ti < 0:
        tp = 0
        print("no payable")
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
        tp = ti * 0.45 - 13505
    at = income - s - tp
        
    print("{}:{:.2f}".format(id,at))
    
if __name__=='__main__':
    try:
        for arg in sys.argv[1:]:
            id,incomes=arg.split(':')
            income =(int(incomes))
            calculator(income, id)
    except:
        print('Paeameter error')
