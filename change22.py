import pandas as pd
import sys


def analysis(file,id):
    df =  pd.read_json(file) #打开json，
    d = df[df['user_id']== id]
    times = len(d)
    minutes = d['minutes'].sum()
    return times,minutes


if __name__=='__main__':
    args = sys.argv[1:]
    '''
    for arg in args:
        file,sid = arg.split(':')
        if not file or id:
            print(0)
    id = int(sid) 
    '''
    file, id = args
    print(analysis(file, int(id)))
#id = sys.argv[1]
#file = int(sys.argv[2])
#
