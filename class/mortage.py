#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/25 22:02
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'


def findPayment(loan, r, m):
    # 请在下面编写代码
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))
    # 请不要修改下面的代码


class Mortgage(object):
    def __init__(self, loan, annRate, months):
        # 请在下面编写代码
        self.loan = loan
        self.rate = annRate / 1200.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, self.months)
        # 请不要修改下面的代码
        self.legend = None

    def makePayment(self):
        # 请在下面编写代码
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1] * self.rate
        self.owed.append(self.owed[-1] - reduction)
        # 请不要修改下面的代码

    def getTotalPaid(self):
        # 请在下面编写代码
        return sum(self.paid)
        # 请不要修改下面的代码

    def __str__(self):
        return 'The Mortgage is {self.legend}, Loan is {self.loan}, Months is {self.months}, Rate is {self.rate:.2f}, Monthly payment is {self.payment:.2f}'.format(
            self=self)


if __name__ == "__main__":
    print(Mortgage(100000, 6.5, 36))
    print(Mortgage(100000, 6.5, 120))
