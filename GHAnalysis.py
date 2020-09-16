import sys 
import getopt
import json
import os


def init(path):
    os.getcwd() 
    filelist = os.listdir(path)
    f2=open('2020-01-01-15.json','w',encoding='utf-8')
    for file in filelist:
        pathname=path+'\\'+file
        try:
            f=open(pathname,encoding='utf-8')
            for line in f:
                f2.write(line)
        finally:
            if f:
                f.clone()
    return 0


def one(data,repo,event):
    ans=0
    for da in data:
        if  repo!=da['repo']['name']:
            continue
        if  da['type'] == event:
            ans=ans+1
    return ans
def two(data,username,event):
    ans=0
    for da in data:
        if  username!=da['actor']['login']:
            continue
        if  da['type'] == event:
            ans=ans+1
    return ans
def three(data,username,repo,event):
    ans=0
    for da in data:
        if  username!=da['actor']['login']:
            continue
        if  repo!=da['repo']['name']:
            continue
        if  da['type'] == event:
            ans=ans+1
    return ans

if __name__ == '__main__':
  
    data=[]
    username='0'
    repo='0'
    event='0'

    try:
        f=open("2020-01-01-15.json", encoding='utf-8')
        for line in f:
                data.append(json.loads(line))	
    finally:
        if f:
            f.close()
    opt,arg= getopt.getopt(sys.argv[1:],'i:u:r:e:',['init=','user=','repo=','event='])
    if opt in ("-i" , "--init"):
        init(opt[0][1])
        exit()
    for opt,arg in opt:
        if opt in ("-u","--user"):
            username = arg
        elif opt in("-r","--repo"):
            repo = arg
        elif opt in ("-e","--event"):
            event = arg
    if  username=='0':
        print(one(data,repo,event))
    elif  repo=='0':
        print(two(data,username,event))
    else:
        print(three(data , username , repo , event))
