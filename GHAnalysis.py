import sys 
import getopt
import json
import os


def read_json(path):
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


def caculate_one(data,repo,event):
    ans=0
    for da in data:
        if  repo!='0':
            if  repo!=da['repo']['name']:
                continue
        if  da['type'] == event:
                ans=ans+1
    return ans
def caculate_two(data,username,event):
    ans=0
    for da in data:
        if  username!='0':
            if  username!=da['actor']['login']:
                continue
        if  da['type'] == event:
                ans=ans+1
    return ans
def caculate_ans(data,username,repo,event):
    ans=0
    for da in data:
        if  username!='0':
            if  username!=da['actor']['login']:
                continue
        if  repo!='0':
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
   
    opt,arg= getopt.getopt(sys.argv[1:],'i:u:r:e:',['init=','user=','repo=','event='])
    try:
        f=open("2020-01-01-15.json", encoding='utf-8')
        for line in f:
                data.append(json.loads(line))	
    finally:
        if f:
            f.close()
    if opt in ("-i" , "--init"):
        read_json(opt[0][1])
        exit()
    for opt,arg in opt:
        if opt in ("-u","--user"):
            username = arg
        elif opt in("-r","--repo"):
            repo = arg
        elif opt in ("-e","--event"):
            event = arg
    if  username=='0':
        print(caculate_one(data,repo,event))
    elif  repo=='0':
        print(caculate_two(data,username,event))
    else:
        print(caculate_ans(data , username , repo , event))
