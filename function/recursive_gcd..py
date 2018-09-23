#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/23 19:36
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()
# 下面写上代码块
"""
使用欧几里德算法，这个已经有2000+年的历史了，这个比起上一个来的要高效，假设我们的最大公约数表示为f(a,b),并且有a>=b>0,
欧几里德就给了我们一个很好的定理，f(a,b)=f(b,a%b),有了这个等式我们就很容易得出这个算法的递归式，现在我们来看下这个等式是怎么来的
设有 r=a/b ,q=a%b
所以就有 
a=a/b*b+q ----(这里的a/b*b!=a ，原因就是我们用的是整数来计算的)
也就是 
a=r*b+q 
变换一下有：
q=a-r*b 设d=f(a,b)，a/d=m,b/d=n;
则 有q=dm-r*dn=d(m-rn)
所以q%d也为0；
设d|q表示d是q的约数；以下相同；
又有d|b;
所以有d|(b,q),
设D是(b,q)的最大公约数，则会有d<=D
a=r*b+q,由于D|(b,q),所以D|a,\
所以有D|(a,b)
所以有D<=d=f(a,b),\
结合上部分就有d<=D <+d,及D=d;
"""


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)
print(gcd(3012121212, 1212121212))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
