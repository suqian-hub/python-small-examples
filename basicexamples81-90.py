# 82.chain高效串联多个容器对象
# chain函数串联a和b，兼顾内存效率同时写法更加优雅。
from itertools import chain
a = [1,2,3,0]
b = (2,4,56)

for i in chain(a,b):
    print(i)
###结果：1，2，3，0，2，4，56

# 83.product案例
def product(*args,repeat = 1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y]for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
# 调用函数：
rtn = product('xyz','12',repeat=3)
print(list(rtn))
# [('x','1','x','1','x','1'),('x','1','x','1','x','2'),.....

# 84.