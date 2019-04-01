# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 20:10
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_tuple.py
#整数 浮点数 字符串 布尔值 True False

#元组 关键字 tuple  符号 ()   所有的符号都是英文状态下的符号
#1:特征
#>1.1.圆括号括起来的数据，都是元组，看类型 type
#>1.2.空元组t_1=()
#>1.3.如果一个元组里面只有一个元素，要在元素后面加一个逗号 t_1=('1',)
#>1.4.元组里面可以包含各种类型的数据 整数 浮点数 字符串 布尔值 True False 元组
#>1.5.元素有元素之间是用逗号给开的,看元素的长度 len
#>1.6.取值方式：与字符串一样  根据索引取值  可以切片取值
#取单个值的方式 元组名[索引值]  索引值从0开始数
#嵌套取值 怎么取   剥洋葱 一片一片的往里面剥开
# t=(2,0.0089,'1',True,(1,2,3,'hello'))
# s=t[-1]#取出值 存到s变量里面
# print(s[-1])
# print(s[3])
# print(t[-1][3][1])
# print(t[4][3][1])
#切片：同字符串 元组名[索引开始值:索引结束值:步长]
#取左不取右
t=(2,0.0089,'1',True,(1,2,3,'hello'))
# #把索引值为偶数的打印出来
# print(t[0:5:2])#0 2 4
print(t[::2])
# print(t[:5:2])

#>1.7.元组他是有序数据 但是不支持增删改
t=(2,0.0089,'1',True,(1,2,3,'hello'),2,3,4,5)
print(t.index(2,1))
print(t[t.index(2,1)])

#2：用法 和 场景
#
