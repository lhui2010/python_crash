#Summary
本章学习了变量的命名方法:
可以数字、字母加下划线组合，除了数字不能打头，其余两个都可以。

###字符串

```python
#字符串的赋值:可以双引，也可以单引。如果单引内部的字符有单引，用转义符\'表示。python -c 似乎也是这个规则。
name="this's good"
name='"good", he said'
name='"good to go, t\'", he said'

```

第一个函数print()
1. 支持\t作为制表符，\n作为换行符
2. 后面必须接括号。

```
#字符串之间的连接使用+表示。
print ("hello" + "world")

#并以字符串变量为例，了解了四种字符串变量的方法
name.upper()
name.lower()
name.title()
name.strip()
name.rstrip()
name.lstrip()

#未赋值的字符串常量也可以使用方法：
python -c 'print ("hello".title())'

#变量的方法返回值可以直接赋值给变量：
name=name.title()
```

###数字

Python中的数字有两种类型：整型和浮点

了解Python对数字表达式的定义
1. 表达式之间可以有空格，也可以没有
2. \*\*代表乘方
3. Python3中整型相除，返回值为浮点；Python 2中返回值为整型
4. 支持括号

学习了数字类型转字符串类型的方法
.str()
