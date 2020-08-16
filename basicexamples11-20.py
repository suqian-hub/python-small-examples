# 11.判断对象是否可以调用 (不懂）
In [1]:callable(str)
Out[1]:True

In [2]:callable(int)
Out[2]:True

In [3]:xiaoming
Out[3]:id = 001, name = xiaoming

In [4]:callable(xiaoming)
Out[4]:False

#另一种写法
In [1]:class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'id = '+self.id + ',name = '+self.name

    def __call__(self):
        print('I can be called')
        print(f'my name is {self.name}')

In [2]:t = Student('001','xiaoming')

In[3]:t()

# 12.十进制转ascii
In [1]:chr(65)
Out[1]:'A'

# 13.ascii转十进制 （查看某个ascii字符对应的十进制数）
In [1]:ord('A ')
out[1]:65

# 14.类方法 》》classmethod装饰器对应的函数不需要实列化，不需要self参数，
# 但第一个参数需要是表示自身类的cls参数，可以来调用类的属性，类的方法，实例化对象等
In [1]:class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'id = '+self.id +', name = '+self.name
    @classmethod
    def f(cls):
        print(cls)

# 15.执行字符串表示的代码
# 将字符串编译成python能识别或可执行的代码，也可以将文字读成字符串再编译。
in [1]:s = "print('helloworld')"

in [2]: r = compile(s,"<string>","exec")

in [3]: r
out[3]:<code object <module> at 0x0000000005DE75D0, file "<string>", line 1>

in [4]: exec(r)
helloworld

# 16.创建复数
in [1]:complex(1,2)
out[1]:(1+2j)   #复数：实部 + 虚部

# 17.动态删除对象的属性
in [1]:delattr(xiaoming,'id')

in [2]:hasattr(xiaoming,'id')
out[2]:False

# 18.转为字典 》创建数据字典
in [1]:dict()
out[1]:{}    #字典格式“{}”，key ：value

in [2]:dict(a ='a',b ='b')
out[2]:{'a':'a', 'b':'b'}

in [3]:dict(zip(['a','b'],[1,2]))
out[3]:{'a':1, 'b':2}

in [4]:dict([('a',1),('b',2)])
out[4]:{'a':1, 'b':2}

# 19.一键查看对象所有方法
# 不带参数时返回当前范围内的变量、方法和定义的类型列表；
# 带参数时返回参数的属性，方法列表。
in [96]:dir(xiaoming)
out[96]:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',

 'name']

# 20.取商和取余数
in [1]:divmod(10,3)
out[1]:(3,1)





