# 7.26
# 一、输出类型信息 type（）
# 方式一：使用print直接输出
print(type("无畏契约"))
print(type(9))
print(type(9.9))
# 方式二：使用变量存储type()
string_type = type("无畏契约")
print(string_type)

# 二、数据类型转换
# int(x),float(x),str(x)
num = str(11)
print(type(num), num)

num1 = int("11")
print(type(num1), num1)

num2 = float(11)
print(type(num2), num2)
num3 = int(9.9)
print(type(num3), num3)

# 三、标识符命名规则：只允许出现英文，中文，数字，下划线（_） 数字不可以开头，不可使用关键字

# 四、运算符  + - * / //(取整除) %(取余) **(指数)
#    复合运算符 += -= *= /= //= %= **=   (x+=1 ==  x=x+1)

# 练习
money = 50
bql = 10
kl = 5
print("当前钱包余额： ", money)
print("购买了冰淇淋，花费", bql)
print("购买了可乐，花费： ", kl)
print("最终，钱包剩余：", money-bql-kl)
