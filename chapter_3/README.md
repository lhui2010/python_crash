####Summary
本章学习了列表

#####列表的定义
列表由一系列**按特定顺序**排列的元素组成。元素可以是**各种类型**，相互之间毫无关系。

#####列表的建立与方法
```
#建立空列表，用方括号表示
my_first_list=[]
my_first_list=["a", "b", 1, 2.0]

#追加元素
my_first_list.append("last")

#末尾删除元素并返回值
last_elem=my_first_list.pop()

#删除元素
my_first_list.del(0)

#按值删除元素
my_first_list.remove("a")

#插入元素
my_first_list.insert(3,"c")

#索引元素
my_first_list[0]
my_first_list[1]
..
my_first_list[-1]

#永久排序
my_first_list.sort()

#永久逆向排序
my_first_list.sort(reverse=True)
my_first_list.sort(reverse)

#返回排序结果
result=sorted(my_first_list)

#返回列表长度
my_list_length=len(my_first_list)

```

学到了列表的六个方法（.append() .sort() .pop() .del() .remove() .insert())，两个函数(sorted() len())

其中.del()与.pop()类似，参数都是索引的位置，但有以下两处不同：

1. pop()可以返回被删除的值，.del()不可以。
2. pop()可以不加任何参数，.del()不可以。

#####课外学习
其他书本上没介绍的方法，还有

* .count() 输入参数为值，比如my\_first\_list.count('a')，返回a出现次数；
* .index() 输入参数为值，比如my\_first\_list.index('a')，返回a所在索引；
* .clear()  清空整个列表
* .extend() 连接两个列表，等同于s += t
* .copy() 复制整个列表，或者用s2=s[:]，但测试s2=s也可以

#####心得
感觉像练了一个新英雄，到手后先熟悉他有什么技能

