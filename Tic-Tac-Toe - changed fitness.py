# https://www.comp.nus.edu.sg/~fstephan/automatalecture04slides.pdf

import random
import numpy

def singleStrategy(strMat,board):
    s=strMat
    for i in range(len(s)):
        if board[s[i][0]][s[i][1]]==s[i][2] and (board[s[i][3]][s[i][4]]==0):
            board[s[i][3]][s[i][4]]=1
            return board
    return randomMove(board)
    

def mutation(t):
    for i in range(len(t)):
        r=random.randint(0,100)
        if (r<=4):
            if (r%3==0):
                r=random.randint(0,10)
                t[i][0]=(t[i][0]+r)%3
                r=random.randint(0,10)
                t[i][1]=(t[i][1]+r)%3
            if (r%3==1):
                r=random.randint(0,10)
                t[i][2]=r%3
            if (r%3==2):
                r=random.randint(0,10)
                t[i][3]=(t[i][3]+r)%3
                r=random.randint(0,10)
                t[i][4]=(t[i][4]+r)%3
    return t
                    
def splt(a,b):
    for i in range(len(b)):
        a.append(b[i])
    return a
        
def bestN(st,p,n):
    t=[]
    s=set()
    for i in range(n):
        a=-1
        b=0
        for i in range(len(p)):
            
            if (i in s):
                continue
            
            if (p[i]>a):
                a=p[i]
                b=i
        s.add(b)
        t.append(st[b])
    return t
                


def singleFitness(st,seed):
    p=0
    for i in range(len(seed)):
        for j in range(10):
            p+=points(singleGame(st,seed[i]))
    return p

def massive(a1):
    e=[]
    for i in range(len(a1)):
        re=[]
        for y in range(len(a1[i])):
            re.append(a1[i][y])
        e.append(re)
    return e

def cross(st, p, seed):
    s1=st
    q=p
    specS=[]
    specP=[]
    for l in range(int(len(st)/2)):
    #for l in range(7):
        s=s1
        q=p
        while (len(s)!=2):
            t=[]
            qe=[]
            for i in range(0,len(s),2):
                a=i
                b=i+1
                if (q[i]<q[i+1]):
                    a,b=b,a
                r=random.randint(0,100)
                if (r>10):
                    t.append(s[a])
                    qe.append(q[a])
                else:
                    t.append(s[b])
                    qe.append(q[b])
            s=t
            q=qe
        r=random.randint(1,len(s[0]))
        w=crossing(s[0],s[1],r)
        
        e=mutation(massive(w[0]))
        o=mutation(massive(w[1]))
        
        specS.append(e)
        specS.append(o)
        
        specP.append(singleFitness(e,seed))
        specP.append(singleFitness(o,seed))
    
    #r=bestN(st,p,2)
    
    #l=bestN(specS,specP,len(st)-2)    
    ans=[]
    #ans.append(r+l)
    ans.append(specS)
    ans.append(specP)
    return ans
    
                
        
def crossing(a,b,n):
    a1=[]
    b1=[]
    for i in range(n):
        a1.append(a[i])
        b1.append(b[i])
    for i in range(n,len(b)):
        a1.append(b[i])
        b1.append(a[i])
    t=[]
    t.append(a1)
    t.append(b1)
    return t      

def check(b):
    c=0
    for i in range(3):
        for j in range(3):
            if b[i][j]==0:
                c=c+1
    up=0
    for i in range(3):
        if ((b[0][up]==b[1][up])
            and (b[1][up]==b[2][up])
            and (b[0][up]!=0)):
            return b[0][up]
        up=up+1
    line=0
    for i in range(3):
        if  ((b[line][0]==b[line][1])
             and (b[line][1]==b[line][2])
             and (b[line][0]!=0)):
            return b[line][0]
        line=line+1
    if (b[0][0]==b[1][1]
        and b[1][1]==b[2][2]
        and (b[0][0]!=0)):
        return b[0][0]
    if (b[2][0]==b[1][1]
        and b[1][1]==b[0][2]
        and b[1][1]!=0):
        return b[1][1]
    if (c==0):
        return 3
    return 0


    
def randomMove(b):
    while True:
        x=random.randint(0,2)
        y=random.randint(0,2)
        #print(b)
        #print(x,y)
        if (b[x][y]==0):
            b[x][y]=1
            return b

def randomPlayerMove(b,s):
    r=random.Random(s)
    while True:
        x=r.randint(0,2)
        y=r.randint(0,2)
        if (b[x][y]==0):
            b[x][y]=2
            return b
    


def singleGame(star,seed):
    board=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #board=[[1, 2, 1], [2, 1, 1], [2, 2, 0]]
    c=0
    while (True):
        #print(board)
        if check(board)!=0:
            break
        if (c%2==0):
            board=singleStrategy(star,board)
        else:
            #randomMove(board)
            randomPlayerMove(board,seed)
        c=c+1
    return check(board)


def sing(s):
    if (s==0):
        return "Nu"
    if (s==1):
        return "X"
    return "O"

def stratOut(strat):
    print("x y symb x_pl y_pl")
    for i in range(len(strat)):
        print(str(strat[i][0])+" "+str(strat[i][1])+"  "+sing(strat[i][2])+"    "+str(strat[i][3])+"    "+str(strat[i][4]))

        
def points(n):
    if (n==2):
        return 0
    if (n==3):
        return 1
    if (n==1):
        return 3



def best(a,y,b):
    if (max(a[1])>=y):
        for i in range(len(a[1])):
            if a[1][i]==max(a[1]):
                return a[0][i]
    return b

def fitness(strat,seed):
    p=[0]*(len(strat))
    for i in range(len(strat)):
        for k in range(len(seed)):
            for j in range(10):
                p[i]+=points(singleGame(strat[i],seed[k]))
    return p




def starter():
    iteration=1000
    straSize=16
    seedSize=20
    strat=[]
    
    for i in range(straSize):
        singStrat=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],
                   [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],
                   [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        strat.append(singStrat)
    seed=[]
    for i in range(seedSize):
        seed.append(random.randint(1,1000))
    
    bst=singStrat
    p=fitness(strat,seed)
    for j in range(iteration):
        yt=strat
        ans=cross(strat,p,seed)
        print(ans[1])
        strat=ans[0]
        p=ans[1]
        if ((30*(seedSize)) in p):
            break
    print(ans[1])
    for i in range(len(strat)):
        stratOut(strat[i])
        
    print()
    print()
    #print(len(strat))
    #print(strat)
    return ans

def point(n):
    if (n==2):
        return 0
    if (n==3):
        return 2
    if (n==1):
        return 5
    
def final(ans):
    strat=ans[0]
    seed=[]
    for i in range(20):
        seed.append(random.randint(1000,2000))
        
    p=[0]*(len(strat))
    for j in range(len(seed)):
        for i in range(len(strat)):
            for t in range(10):
                p[i]+=point(singleGame(strat[i],seed[j]))
    for i in range(len(strat)):
        p[i]=p[i]/10
    print(p)
    
    
final(starter())



