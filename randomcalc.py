#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findsimplelp(a,b,c,x):
    y=(a*x+b)%c
    while x!=y:
        x=(a*x+b)%c
        y=(a*y+b)%c
        y=(a*y+b)%c
    n=1
    xx=(a*x+b)%c
    while x!=xx:
        xx=(a*xx+b)%c
        n=n+1
    return n
def findsimpleln(a,b,c,x,lp):
    n=0
    y=x
    for i in range(lp):
        y=(a*y+b)%c
    while y!=x:
        n=n+1
        x=(a*x+b)%c
        y=(a*y+b)%c
    return n

def calculatesimple(n, a, b, c, x0):
    numb=[x0]
    for i in range(n-1):
        numb.append((a*numb[i]+b)%c)
    return numb

def simplequality(a,b,c,x):
    q=[0]*20
    for i in range(400):
        q[int((x/c)*20)]+=1
        x=(a*x+b)%c
    s=0
    for i in q:
        s+=(20-i)**2
    s=s/400
    return s,q

def hardquality(a,b,c,d,x0,x1):
    q=[0]*20
    q[int((x0/d)*20)]+=1
    q[int((x1/d)*20)]+=1
    xold,x0,x1=x0,x1,(a*x1+b*x0+c)%d
    q[int((x1/d)*20)]+=1
    for i in range(400-3):
        xold,x0,x1=hardnext(xold,x0,x1,a,b,c,d)
        q[(x1*20)//d]+=1
    s=0
    for i in q:
        s+=(20-i)**2
    s=s/400
    return s,q

def hardnext(xold,x0,x1,a,b,c,d):
    return x0, (a*x0+b*xold+c)%d, (a*x1+b*x0+c)%d


def findhardlp(a,b,c,d,x0,x1):
    y0=(a*x1+b*x0+c)%d
    y1=(a*y0+b*x1+c)%d
    n=0
    xold,x0,x1=x0,x1,(a*x1+b*x0+c)%d
    yold,y0,y1=y0,y1,(a*y1+b*y0+c)%d
    while (x0!=y0) or (x1!=y1):
        xold,x0,x1=hardnext(xold, x0, x1, a, b, c, d)
        yold,y0,y1=hardnext(yold, y0, y1, a, b, c, d)
        yold,y0,y1=hardnext(yold, y0, y1, a, b, c, d)
        n=n+1
    n=1
    sxold,sx0,sx1=hardnext(xold, x0, x1, a, b, c, d)
    while (sx0!=x0) or (sx1!=x1):
        sxold,sx0,sx1=hardnext(sxold, sx0, sx1, a, b, c, d)
        n=n+1
    return n

def findhardln(a,b,c,d,x0,x1,lp):
    n=0
    yold,y0,y1=x0,x1,(a*x1+b*x0+c)%d
    for i in range(lp-1):
        yold,y0,y1=y0,y1,(a*y1+b*y0+c)%d
    while (x0!=y0) or (x1!=y1):
        n=n+1
        xold,x0,x1=x0,x1,(a*x1+b*x0+c)%d
        yold,y0,y1=y0,y1,(a*y1+b*y0+c)%d
    return n



def calculatehard(n, a, b, c, d, x0, x1):
    numb=[x0,x1]
    for i in range(n-2):
        numb.append((a*numb[i+1]+b*numb[i]+c)%d)
    return numb


if __name__ == '__main__':
    print(calculatesimple(20,1234,123,12,1))
