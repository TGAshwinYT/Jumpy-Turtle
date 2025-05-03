import csv
import os
def Save():
    s=open("score.txt","r")
    sco=s.read()
    l=open(r"assets\text file\PlayerName_Login.txt","r")
    name=l.read()
    with open("Scoreboard.csv","r") as f:
        r=csv.reader(f)
        newlist=[]
        u=True
        for i in r:
            if i[0]==name:
                i[1]=sco
                u=False
            newlist.append(i)
    with open("Scoreboard.csv","w",newline='') as f:
        w=csv.writer(f)
        w.writerows(newlist)
    if u:
        z=open("Scoreboard.csv","a",newline='')
        w=csv.writer(z)
        newlist=[name,sco]
        w.writerow(newlist)
        z.close()
    s.close()

def Score_retive():
    if os.path.exists('Scoreboard.csv'):
        with open("Scoreboard.csv","r") as o:
            r=csv.reader(o)
            f=open("score.txt","w+")
            l=open(r"assets\text file\PlayerName_Login.txt","r")
            n=l.read()
            q=True
            for i in r:
                if i[0] == n:
                    f.write(i[1])
                    q=False
                    break
            if q:
                f.write("0")
            f.close()
    else:
        with open("Scoreboard.csv","w") as o:
            pass
