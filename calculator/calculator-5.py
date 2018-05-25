#!/usr/bin/env python3

import getopt
import sys
import configparser
import csv
from multiprocessing import Process,Queue,Lock
from datetime import datetime 

class Args(object):
    def __init__(self):
        self.C = ''
        self.c = ''
        self.d = ''
        self.o = ''
        try:
            opts, args = getopt.getopt(sys.argv[1:],'-C:-c:-d:-o:')
        except:
            print('getopts error')
        for key,value in opts:
            if key == '-C':
                self.C = value
            elif key == '-c':
                self.c = value
            elif key == '-d':
                self.d = value
            elif key == '-o':
                self.o = value
            else:
                sys.exit()
args = Args()
class Config(object)
    def __init__(self):
	    self.config = self._read_config()
	def _read_config(self):	
		config = {'f':0}
		config = configpaeser.ConfigParser
		config.read('args.c')
		if args.C and args.C.upper() in config.sections():
		    return config[args.C.upper()]
		else:
		    return config['DEFAULT']
		    
		try:
		    with open(args.c) as c:
			    for k in c.readlines():
                k = k.strip().split('=')
                key,value = k[0].strip(),k[1].strip('=')
                try:
                    if key == 'JiShuL' or key=='JiShuH':
                        config[key] = float(value)
                    else:
                        config['f'] += float(value)
                except:
                    print('Config Error')
        return config

config = Config().config


			
class UserData(object):
    def __init__(self):
        self.userdata = self._read_users_data()
    def _read_users_data(self):
        userdata = []
        with open(args.d,'r') as d:
            for line in d:
                try:
                    line = list(line.strip().split(','))
                    with lock:
                        queue.put([line[0],int(line[1])])
                        
                except:
                    print('userdata error')		
		
		
class IncomeTaxCalculator(object):
    #社保
    def cacl_social_money(self,salary):
        config = Config().config
        smoney = salary * config['f']
        if salary < config['JiShuL']:
            smoney = config['JiShuL'] * config['f']
        if salary > config['JiShuH']:
            smoney = config['JiShuH'] * config['f']
        return smoney
   #应税所得额 ti
    def cacl_tax_payable(self,salary,smoney):
        ti = salary - smoney - 3500
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
            tp = ti * 0.45 - 13505
        return tp
	def cacl_for_user_datatime(self):
	    return datetime.now().strftime('%Y-%m-%d %H:%H%M')

    #税后工资
    def cacl_for_all_userdata(self):
        with lock:
            while not queue.empty():
                user = queue.get()
                smoney = self.cacl_social_money(user[1])
                tp = self.cacl_tax_payable(user[1],smoney)
                at = user[1] - smoney - tp
				datetime = cacl_for_user_datatime(user[1],)
                result = (user[0],'{:.2f}'.format(user[1]),'{:.2f}'.format(smoney),'{:.2f}'.format(tp),'{:.2f}'.format(at),'{:.2f}'.format(datatime))
                queue2.put(result)
   
    def export(self, default='csv'):
        while not queue2.empty():
            with lock:
                results = queue2.get()
            with open(args.o, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(results)
       

if __name__=='__main__':
   queue = Queue()
   queue2 = Queue()
   lock = Lock()
   process1 = Process(target=UserData()._read_users_data())
   process1.start()
   process1.join()
   process2 = Process(target= IncomeTaxCalculator().cacl_for_all_userdata())
   process2.start()
   process2.join()
   process3 = Process(target=IncomeTaxCalculator().export())
   process3.start()
   process3.join()
