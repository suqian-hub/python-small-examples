# 46.转为集合类型 返回一个set对象，集合内不允许有重复元素
in [1]:a = [1,4,2,3,1]
in [2]:set(a)
out[2]:{1,2,3,4}

# 47.转为切片对象
# class slice(start, stop[, step])
# 返回一个表示由 range(start, stop, step) 所指定索引集的 slice对象，它让代码可读性、可维护性变好。
in [1]:a = [1,4,2,3,1]
in [2]:my_slice_meaning = slice(0,5,2)

in [3]:a[my_slice_meaning]
out[3]:[1,2,1]

# 48.拿来就用的排序函数
in [1]:a = [1,4,2,3,1]

in [2]:sorted(a, reverse=True)
out[2]:[4,3,2,1,1]

in [3]:a = [{'name':'xiaoming','age':18,'gender':'male'},{'name':'xiaohong','age':20,'gender':'female'}]
in [4]:sorted(a,key=lambda x:x['age'],reverse=False)
out[4]:
[{'name': 'xiaoming', 'age': 18, 'gender': 'male'},
 {'name': 'xiaohong', 'age': 20, 'gender': 'female'}]

# 49.求和函数
in [1]:a = [1,4,2,3,1]
in [2]:sum(a)
out[2]:11

in [3]:sum(a,10) # a 和 10 一起求和
out[3]:21

# 50.转元组 tuple() 将对象转为一个不可变的序列类型
in [1]:i_am_list = [1,3,5]
in [2]:i_am_tuple = tuple(i_am_list)
in [3]:i_am_tuple
out[3]:(1,3,5)

# 51.查看对象类型
# class type(name, bases, dict)
# 传入一个参数时，返回 object 的类型：
In [1]: class Student():
   ...:     def __init__(self,id,name):
   ...:         self.id = id
   ...:         self.name = name
   ...:     def __repr__(self):
   ...:         return 'id = '+self.id +', name = '+self.name

in [2]:xiaoming = Student(id= '001',name='xiaoming')
in [3]:type(xiaoming)
out[3]:__main__.Student

in [4]:type(tuple())
out[4]:tuple

# 52.聚合迭代器 创建一个聚合了来自每个可迭代对象中的元素的迭代器：
in [1]:x =[3,2,1]
in [2]:y =[4,5,6]
in [3]:list(zip(y,x))
out[3]:[(4,3),(5,2),(6,1)]

in [4]:a = range(5)
in [5]:b = list('abcde')
in [6]:b
out[6]:['a','b','c','d','e']

in [7]:[str(y) + str(x) for x,y in zip(a,b)]
out[7]:['a0','b1','c2','d3','e4']

# 53.nonlocal 用于内嵌函数中
# 关键词nonlocal常用于函数嵌套中，声明变量i为非局部变量；
# 如果不声明，i+=1表明i为函数wrapper内的局部变量，
# 因为在i+=1引用(reference)时,i未被声明，所以会报unreferenced variable的错误。
def excepter(f):
   i = 0
   t1 = time.time()
   def wrapper():
      try:
         f()
      except Exception as e:
         nonlocal i
         i += 1
         print(f'spending time:{round(t2 - t1,2)}')
   return wrapper


# 54.global 声明全局变量 先回答为什么要有global，一个变量被多个函数引用，想让全局变量被所有函数共享。
# 抛出异常：UnboundLocalError，原来编译器在解释i+=1时会把i解析为函数h()内的局部变量，
# 很显然在此函数内，编译器找不到对变量i的定义，所以会报错。
#
# global就是为解决此问题而被提出，在函数h内，显式地告诉编译器i为全局变量，
# 然后编译器会在函数外面寻找i的定义，执行完i+=1后，i还为全局变量，值加1：
i = 0
def h():
   global i
   i += 1
h()
print(i)

# 55.链式比较
i = 3
print(1 < i < 3) # False
print(1 < i <= 3) # True

# 56.不用else和if实现计算器
from operator import *
def calculator(a,b,k):
   return {
      '+':add,
      '-':sub,
      '*':mul,
      '/':truediv,
      '**':pow
   }[k](a,b)

calculator(1,2,'+') # 3
callable(3,4,'**') #81

# 57.链式操作
from operator import (add, sub)

def add_or_sub(a,b,oper)
   return (add if oper == '+' else sub)(a,b)

add_or_sub(1,2,'-') # -1

# 58.交换两元素
def swap(a,b):
   return b,a
print(swap(1,0)) # (0,1)

# 59.去最求平均
def score_mean(lst):
   lst.sort()
   lst2 = lst[1:(len(lst)-1)]
   return round((sum(lst2)/len(lst2)),1)

lst=[9.1,9.0,8.1,9.7,19,8.2,8.6,9.8]
score_mean(lst) # 9.1

# 60.打印99乘法表
# 一共有10 行，第i行的第j列等于：j*i，
# 其中,
# i取值范围：1<=i<=9
# j取值范围：1<=j<=i
# 根据例子分析的语言描述，转化为如下代码：

for i in range(1,10):
   for j in range(1 ,i+1):
      print('%d * %d = %d' % (j, i, j * i),end="\t")
   print()

# 61.全展开
# 有如下数组
[[[1,2,3],[4,5]]]
#要将其完全展开成一维的。这个小例子实现的flatten是递归版，两个参数分别表示带展开的数组，输出数组。
from collections.abc import *
def flatten(lst,out_lst = None):
   if out_lst is None:
      out_lst = []
   for i in lst:
      if isinstance(i,Iterable): # 判断i是否可迭代
         flatten(i, out_lst)     # 尾数递归
      else:
         out_lst.append(i)       # 产生结果
   return out_lst
# 调用flatten:
print(flatten([[[1,2,3],[4,5]]]))
print(flatten([[[1,2,3],[4,5]]，[6,7]]))
print(flatten([[[1,2,3],[4,5,6]]]))
# 结果
[1,2,3,4,5]
[6,7,1,2,3,4,5]
[1,2,3,4,5,6]

# numpy 里的 flatten 与上面的函数实现有些微妙的不同：
import numpy
b = numpy.array([[1,2,3],[4,5]])
b.flatten()
array([list([1,2,3]),list([4,5])],dtype=object)

# 62.列表等分
import math import ceil

def divide(lst,size):
   if size <= 0:
      return [lst]
   return [lst[i * size:(i + 1)*size] for i in range (0,ceil(len(lst)/size))]

r = divide([1,3,5,7,9],2)
print(r) # [[1,3],[5,7],[9]]

r = divide([1,3,5,7,9],0)
print(r) # [[1,3,5,7,9]]

r = divide([1,3,5,7,9],-3)
print(r) # [[1,3,5,7,9]]

# 63.列表压缩
def filter_false(lst):
   return list(filter(bool,lst))

r = filter_false([None,0,False, '', [],'ok',[1,2]])
print(r) # ['ok',[1,2]]

# 64.更长列表
def max_length(*lst):
   return max(*lst,key=lambda v:len(v))

r = max_length([1,2,3],[4,5,6,7],[8])
print(f'更长的列表{r}') #[4,5,6,7]

r = max_length([1,2,3],[4,5,6,7],[8,9])
print(f'更长的列表是{r}') #[4,5,6,7]

# 65.求众数
def top1(lst):
   return max(lst,default='列表为空'，key=lambda v:lst.count(v))

lst = [1,3,3,2,1,1,2]
r = top1(lst)
print(f'{lst}中出现次数最多的元素为：{r}')  #[1, 3, 3, 2, 1, 1, 2]中出现次数最多的元素为:1

# 66.多表之最
def max_lists(*lst):
   return max(max(*lst, key=lambda v:max(v)))

r = max_lists([1,2,3],[6,7,8],[4,5])
print(r) # 8

# 67.列表查重
def has_duplicates(lst):
   return len(lst) == len(set(lst))

x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
has_duplicates(x) # false
has_duplicates(y) # true

# 68.列表反转
def reverse(lst):
   return lst[::-1]

r = reversed([1,-2,3,4,1,2])
print(r) # [2,1,4,3,-2,1]

# 69.浮点数等差数列
def rang(start, stop, n):
   start,stop,n = float('%.2f' % start),float('%.2f' % stop),int('%.d' % n)
   step = (stop - start)/n
   lst = [start]
   while n>0:
      start,n = start+step,n-1
      lst.append(round((start),2))
   return lst
rang(1,8,10)
   # 1.0,1.7,2.4,3.1,3.8,4.5,5.2,5.9,6.6,7.3,8.0

# 70.按条件分组
def bit_by(lst, f):
   return[ [x for x in lst if f(x)],[x for x in lst if not f(x)]]

records = [25,89,31,34]
bit_by(records, lambda x: x<80) # [[25,31,34],[89]]

