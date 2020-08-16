# 71.map实现向量运算
# 多序列运算函数—map(function,iterabel,iterable2)
lst1 = [1,2,3,4,5,6]
lat2 = [3,4,5,6,3,2]
list(map(lambda x,y:x*y+1,lst1,lst2))
# [4,9,16,25,16,13]

# 72.值最大的字典 (不清晰）
def max_pairs(dic):
    if len(dic) == 0:
        return dic
    max_val = max(map(lambda v:v[1],dic.item()))
    return [item for item in dic.item() if item [1] == max_val]

r = max_pairs({'a':-10,'b':5,'c':3,'d':5})
print(r) # [('b',5),('d',5)]

# 73.合并两个字典
def merge_dict(dic1,dic2):
    return {**dic1,**dic2} # python3.5后支持一行代码合并
merge_dict({'a':1,'b':2},{'c':3})
# {‘a':1,'b':2,'c':3}

# 74.topn字典
from heapq import nlargest
# 返回字典d前n个最大值对应的键

def topn_dict(d,n):
    return nlargest(n,d,key=lambda k:d[k])

topn_dict({'a':10,'b':8,'c':9,'d':10},3)
# ['a','b','c']

# 75.异位词
from collections import Counter

# 检查两个字符串是否是 相同字母异序词，简称：互为变位词
def anagram(str1,str2):
    return Counter(str1) == Counter(str2)

anagram('eleven+two', 'twelve+one') # True 这是一对神奇的变位词
anagram('eleven','twelve') #False

# 76.逻辑上合并字典
# （1）两种合并字典方法 这是一般的字典合并写法
dic1 = {'x':1,'y':2}
dic2 = {'y':3,'z':4}
merged1 = {**dic1,**dic2}
# {'x':1,'y':3,'z':4}

# 修改merged['x']=10，dic1中的x值不变，merged是重新生成的一个新字典。
# 但是，ChainMap却不同，它在内部创建了一个容纳这些字典的列表。因此使用ChainMap合并字典，修改merged['x']=10后，dic1中的x值改变，如下所示：
from collections import ChainMap
merged2 = ChainMap(dic1,dic2)
print(merged2)  #ChainMap({'x':1,'y':2},{'y':3,'z':4})

# 77.命名元组提高可读性
from collections import ChainMap
merged2 = ChainMap(dic1,dic2)
print(merged2)
# ChainMap({'x':1,'y':2},{'y':3,'z':4})

# 77.命名元组提高可读性 (不懂）
from collections import namedtuple
Point = namedtuple('Point',['x','y','z']) # 定义名字为Point的元组，字段属性有x，y，z
lst = [Point(1.5,2,3.0),Point(-0.3,-1.0,2.1),Point(1.3,2.8,-2.5)]
print(lst[0].y-lst[1].y)  # 3.0


# 78.样本抽样
# 使用sample抽样，如下列子从100个样本中随机抽样10个。
from random import randint,sample
lst = [randint(0,50) for _ in range(100)]
print(lst[:5]) # [38,19,11,3,6]
lst_sample = sample(lst,10)
print(lst_sample)
# [33,40,35,49,24,15,48,29,37,24]

# 79.重洗数据集
# 使用 shuffle用来重洗数据集，值得注意shuffle是对lst就地(in place)洗牌，节省存储空间
from random import shuffle
lst = [randint(0,50) for _ in range(100)]
shuffle(lst)
print(lst[:5]) # [50,3,48,1,26]

# 80.10个均匀分布的座标点
# random模块中的uniform(a,b)生成[a,b)内的一个随机数，如下生成10个均匀分布的二维坐标点

from random import uniform

in [1]: [(uniform(0,10),uniform(0,10))for _ in range(10)]
out[1]:
[(9.244361194237328, 7.684326645514235),
 (8.129267671737324, 9.988395854203773),
 (9.505278771040661, 2.8650440524834107),
 (3.84320100484284, 1.7687190176304601),
 (6.095385729409376, 2.377133802224657),
 (8.522913365698605, 3.2395995841267844),
 (8.827829601859406, 3.9298809217233766),
 (1.4749644859469302, 8.038753079253127),
 (9.005430657826324, 7.58011186920019),
 (8.700789540392917, 1.2217577293254112)]

# 81.10个高斯分布的坐标点
#random模块中的gauss(u,sigma)生成均值为u, 标准差为sigma的满足高斯分布的值，
#如下生成10个二维坐标点，样本误差(y-2*x-1)满足均值为0，标准差为1的高斯分布：
from random import gauss
x = range(10)
x = [2*xi+1+gauss(0,1) for xi in x]
points = list(zip(x,y))
### 10个二维点
[(0, -0.86789025305992),
 (1, 4.738439437453464),
 (2, 5.190278040856102),
 (3, 8.05270893133576),
 (4, 9.979481700775292),
 (5, 11.960781766216384),
 (6, 13.025427054303737),
 (7, 14.02384035204836),
 (8, 15.33755823101161),
 (9, 17.565074449028497)]



