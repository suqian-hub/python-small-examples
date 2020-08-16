# 1.求绝对值
print(abs(-6))

# 2.元素都为真
print(all([1, 0, 3, 6]))   # 有0为false

print(all([1,2,3]))

# 3.至少一个元素为真
print(any([0,0,0,[]]))   #全0为false

print(any([1,0,0]))   #为true

print(any([1,[]]))   #为true

# 4.ascii展示对象（调用__repr__)
class student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'id = '+self.id +', name = '+self.name

xiaoming = student(id='1',name='xiaoming')

print(ascii(xiaoming))

# 5.十进制转二进制
print(bin(10))

# 6.十转八
print(oct(9))

# 7.十转十六
print(hex(15))

# 8.判断是真是假
print(bool([0,0,0]))     #true
print(bool([]))          #false
print(bool([1,0,1]))     #true

# 9.字符串转字节
s = "apple"
s_tran = bytes(s,encoding= 'utf-8')
print(s_tran)

# 10.转为字符串
i = 100
i_tran = str(i)
print(i_tran)