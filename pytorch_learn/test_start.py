#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/21 21:02
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch
import torch.optim as optim


class Net(nn.Module):  # 需要继承这个类
    def __init__(self):
        super(Net, self).__init__()  # 建立了两个卷积层，self.conv1, self.conv2，注意，这些层都是不包含激活函数的
        self.conv1 = nn.Conv2d(1, 6, 5)  # 1 input image channel, 6 output channels, 5x5 square convolution kernel
        self.conv2 = nn.Conv2d(6, 16, 5)  # 三个全连接层
        self.fc1 = nn.Linear(16 * 5 * 5, 120)  # an affine operation: y = Wx + b
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):  # 注意，2D卷积层的输入data维数是 batchsize*channel*height*width
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))  # Max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)  # If the size is a square you can only specify a single number
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


# net = Net()
# print(net)
# print(len(list(net.parameters())))
#
# input = Variable(torch.randn(1, 1, 32, 32))
# out = net(input)

net = Net()  # create your optimizer
optimizer = optim.SGD(net.parameters(), lr=0.01)

learning_rate = 0.001
input_data = torch.randn(2, 1, 32, 32)
# input_data=Variable(input_data)
target = torch.FloatTensor(2, 10).random_(8)
print(target)
criterion = torch.nn.MSELoss(reduction='mean')
# in your training loop:
for i in range(1000):
    optimizer.zero_grad()  # zero the gradient buffers，如果不归0的话，gradients会累加
    output = net(input_data)  # 这里就体现出来动态建图了，你还可以传入其他的参数来改变网络的结构

    loss = criterion(output, target)
    loss.backward()  # 得到grad，i.e.给Variable.grad赋值
    optimizer.step()  # Does the update，i.e.

print(output)
