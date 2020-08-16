# 21.枚举对象
s = ['a','b','c']
for i,v in enumerate(s,1):
    print(i,v)

# 22.计算表达式 》把str当成有效的表达式来求值
in [1]:s ='1+2+3'
      eval(s)
out[1]：9

# 23.查看变量所占用的字节数
in [1]:import sys
in [2]:a = {'a':1,"b":2.0}
in [3]:sys.getsizeof(a)
out[3]:240 #占用240个字节

# 24.过滤器 在函数中设定过滤条件，迭代元素，保留返回值为True的元素：
in [1]:fil = filter(lambda x: x>10,[1,11,2,45,7,6,13])

in [2]:list(fil)
out[2]:[11,45,13]

# 25.转为浮点类型
# 将一个整数或数值型字符串转换为浮点数
in [1]:float(3)
out[1]:3.0

#如果不能转化为浮点数，则会报ValueError:
in [2]:float('a')
# ValueError: could not convert string to float: 'a'

# 26.字符串格式化
# 格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法。
In [104]: print("i am {0},age{1}".format("tom",18))
i am tom,age18

# 27.冻结集合 创建一个不可修改的集合
in [1]:frozenset([1,1,3,2,3])
out[1]:frozenset([1,2,3])
#应为不可修改，所以没有像set一样的add和pop方法

# 28.动态获取对象属性
in [1]:class Student():
    def __init__(self,id,name):
        self.id = id
        self.name =name
    def __repr__(self):
        return 'id ='+self.id+', name ='+self.name

in [2]:xiaoming = Student(id='001',name='xiaoming')
in [3]:getattr(xiaoming,'name') # 获取小明这个实列的name属性值
out[3]:'xiaoming'

# 29.对象是否有这个属性
in [1]:class Student():
    def __init__(self,id,name):
        self.id = id
        self.name =name
    def __repr__(self):
        return 'id ='+self.id + ',name = '+self.name

in [2]:xiaoming = Student(id = '001',name = 'xiaoming')
in [3]:hasattr(xiaoming,'name')
out[3]:True

in [4]:hasattr(xiaoming, 'address')
out[4]:False

# 30.返回对象的哈希值
# 返回对象的哈希值，值得注意的是自定义的实例都是可哈希的，list, dict, set等可变对象都是不可哈希的(unhashable)
in [1]:hash(xiaoming)
out[1]:6139638

in [2]:hash([1,2,3])
# TypeError: unhashable type: 'list'

# 31.一键帮助
in [1]:help(xiaoming)
help on Student in module __main__ object:

class Student(builtins.object)
    Methods defined here:

    __init__(self, id, name)

    __repr__(self)

    Data descriptors defined here:

    __dict__
        dictionary for instance variables (if defined)

    __weakerf__
        list of weak references to the object (if defined)


# 32.对象门牌号 返回对象的内存地址
in [1]:id(xiaoming)
out[1]:98234208

# 33.获取用户输入
input()

# 34.转为整型 (不懂）
# int(x, base =10) , x可能为字符串或数值，将x 转换为一个普通整数。如果参数是字符串，那么它可能包含符号和小数点。如果超出了普通整数的表示范围，一个长整数被返回。
print(int('12',16))
out :18

# 35.isinstance
# 判断object是否为类classinfo的实例，是返回true
In [1]: class Student():
   ...:     def __init__(self,id,name):
   ...:         self.id = id
   ...:         self.name = name
   ...:     def __repr__(self):
   ...:         return 'id = '+self.id +', name = '+self.name

In [2]: xiaoming = Student(id='001',name='xiaoming')

in [3]:isinstance(xiaoming,Student)
out[3]:True

# 36.父子关系鉴定
in [1]:class undergraduate(Student):
    def studyCalss(self):
        pass
    def attendActivity(self):
        pass

in [2]:issubclass(undergraduate,Student)
out[2]:True

in [3]:issubclass(object,Student)
out[3]:False

in [4]:issubclass(Student,object)
out[4]:True

# 37.创建迭代器类型
# 使用iter(obj, sentinel), 返回一个可迭代对象, sentinel可省略(一旦迭代到此元素，立即终止)
in [1]:lst = [1,3,5]

in [2]:for i in iter(lst):
    print(i)

# 或者 (不是很清楚）
in [1]:class TestIter(object):
    def __init__(self):
        self.I=[1,2,3,4,5,6]
        self.i=iter(self.I)
    def __call__(self): #定义了__call__方法的类的实例是可调用的
        item = next(self.i)
        print('__call__ is called,fowhich would return',item)
        return item
    def __iter__(self):  #支持迭代协议(即定义有__iter__()函数)
        print('__iter__ is called!')
        return iter(self.I)
in [2]:t = TestIter()
in [3]:t() # 因为实现了__call__，所以t实例能被调用#
__call__ is called,which would return 1
out[3]:1

in [4]:for e in TestIter(): #因为实现了__iter__方法，所以t能被迭代
    print(e)
__iter__ is called!!
1
3
2
3
4
5

# 38.所有对象之根 》 object是所有类的基类
in [1]:o = object()

in [2]:type(o)
out[2]:object

# 39.打开文件 返回文件对象
in [1]:fo = open('D:/a.txt',mode='r',encoding='utf-8')
in [2]:fo.read()
out[2]:'\ufefflife is not so long,\nI use Python to play.'

# 40.次幂 base为底的exp次幂，如果mod给出，取余
in [1]:pow(3,2,4)
out[1]:1  # 3*3/4

# 41.打印
In [5]: lst = [1,3,5]

In [6]: print(lst)
[1, 3, 5]

In [7]: print(f'lst: {lst}')
lst: [1, 3, 5]

In [8]: print('lst:{}'.format(lst))
lst:[1, 3, 5]

In [9]: print('lst:',lst)
lst: [1, 3, 5]

# 42.创建属性的两种方式，
# 返回 property 属性，典型的用法：
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
    # 使用property类创建property属性 (不懂）
    x = property(getx,setx,delx,"i'am the 'x' property")

# 使用python装饰器，实现与上完全一样的效果代码：
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

# 43.创建range序列 1.range（stop） 2.range（start，stop[,step])
# 生成一个不可变序列：
in [1]:range(11)
out[1]:range(0,11)

in [2]:range(0,11,1)
out[2]:range(0,11)

# 44.反向迭代器
in [1]:rev reversed([1,4,2,3,1])

in [2]:for i in rev:
    print(i)

1
3
2
4
1


# 45.四舍五入 ndigits代表小数点后保留几位
in [1]:round(10.022233556, 3)
out[1]:10.022

in [2]:round(10.05, 1)
out[2]:10.1

