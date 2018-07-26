####Summary

本章学习了列表的用法，以及缩进的重要性。Python一般使用四个空格作为缩进的标志。

#####列表的遍历

```python

#要点有三个：for in的语句；冒号（Colon）结尾；循环内的缩进

magicians = ['Wicked', 'Blast', 'Mavel']
for magician in magicians:
    print (magician)

#使用range输出，需要记住的是range是左闭右开的区间(off-by-one behavior)
In [7]: for num in range(1,6):
   ...:     print (num)
   ...:
1
2
3
4
5

#range是一个单独的对象，如果需要作为列表处理，需要转换
In [11]: a=range(1,6)

In [12]: type(a)
Out[12]: range

In [13]: a=list(range(1,6))

In [14]: type(a)
Out[14]: list


#Python one-liner
#正规叫法为list comprehension
squares = [value**2 for value in range(1,11)]
print (squares)

#数组的切片
>>>players = ['charles', 'martina', 'michael', 'florence', 'eli']
>>>print(players[:3]) #等同于print 0:3，依然是左闭右开，只打印0,1,2三个元素
['charles', 'martina', 'michael']

#拷贝数组
backup_players = players [:]
#如果使用cp_players = players，那么意味着Python建立一个新的变量cp_players，然后将其链接到players的数据上


```

#####元组的定义与引用

```python

dimensions = (200, 50)

#引用
dimensions[0]

#遍历，与数组相同
for dimension in dimensions:
    print (dimension)

#元组可以和元组间进行操作，比如重新赋值
dimensions = (400, 100)


#代码的Style

原则参考：
1. PEP8 https://python.org/ dev/peps/pep-0008/
2. 单行不超过80字符
```
