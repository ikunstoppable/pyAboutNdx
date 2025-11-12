# 1.有四个数字1，2，3，4， 能组成多少个互不相同且无重复数字的三位数
def number_in3():
    result = []
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != k and j != k and i != j:
                    result.append(int(str(i)+str(j)+str(k)))
    print(result)

# number_in3()
# 2.企业发放的奖金根据利润提成。利润（i）低于或者等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元按10%提成，高于10万元的部分，可提成7.5%；20万元到30万元之间时，高于20万元的部分，可提成5%；40万到60万之间时，
# 高于40万元的部分，可提成3%；60万元到100万元之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润i，计算应发奖金总数
def lt100k(profit):
    return profit*0.1
def gt100k_lt200k(profit):
    return lt100k(100000)+(profit - 100000)*0.075
def gt200k_lt300k(profit):
    return gt100k_lt200k(200000)+(profit-200000)*0.05
def gt400k_lt600k(profit):
    return gt200k_lt300k(400000)+(profit-400000)*0.03
def gt600k_lt1000k(profit):
    return gt400k_lt600k(600000)+(profit-600000)*0.015
def gt1000k(profit):
    return gt600k_lt1000k(1000000)+(profit-1000000)*0.01

def month_bounce(i):
    result = 0
    if i <= 100000:
        result = lt100k(i)
    elif i > 100000 & i <= 200000:
        result = gt100k_lt200k(i)
    elif i > 200000 & i <= 400000:
        result = gt200k_lt300k(i)
    elif i > 400000 & i <= 600000:
        result = gt400k_lt600k(i)
    elif i > 600000 & i <= 1000000:
        result = gt600k_lt1000k(i)
    elif i > 1000000:
        result = gt1000k(i)
    print(result)


# month_bounce(1000000)

# 输入3个数，并进行排序
def maxnumber():
    num_list = []
    for i in range(3):
        current_num = int(input('输入数字:'))
        num_list.append(current_num)
    print(num_list)
    result = num_list.sort()
    print(num_list)
#数组方法sort只会改变原属组午饭回
# maxnumber()

#将1个列表的数字复制到另一个列表
def copy_number_only(rawlist):
    copy_reuslt = []
    for item in rawlist:
        print(type(item))
        if isinstance(item,int):
            copy_reuslt.append(item)

    print(copy_reuslt)

# copy_number_only([1,2,3,4,5,'233'])

# 5.暂停1m输出并格式化时间
import time
def time_loop(times):
    for item in range(times):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(1)

# time_loop(10)

# 6.水仙花数：一个三位数，其各位数字立方和等于该数本身
def narcissus_num():
    for item in range(100,1000):
        num1 = int(item / 100)
        num2 = int(int(item / 10) - num1 * 10)
        num3 = int(item % 10)
        if num1**3+num2**3+num3**3==item:
            print(item)

# narcissus_num()

# 7.输入一行字符串，分别统计英文字母，空格，数字和其他字符的个数
def counts_chars():
    inputstr = input('input u string:')
    letters = 0
    space = 0
    digit = 0
    others = 0
    for item in inputstr:
        if item.isalpha():
            letters += 1
        elif item.isspace():
            space+=1
        elif item.isdigit():
            digit += 1
        else:
            others +=1
    print('char = %d, space=%d, digit=%d,others=%d' % (letters, space, digit, others))

# counts_chars()

# 8.一个球从100米高度自由下落，每次落地后反弹至原高度的一半，再落下，球在第十次落地时，共经过多少米，第十次反弹多高
def ball_method():
    init_height = 100
    back_height_rate = 0.5
    current_height = init_height
    all_height = init_height
    for item in range(1,11):
        current_height = current_height * back_height_rate
        print(current_height)
        all_height += (current_height * 2)
    print('10次后当前的反弹高度为：%f，球的总路径：%d' % (current_height, all_height))

# ball_method()

# 9. 两个3*3的矩阵，实现其对应位置的数据相加，并返回一个新举证
def matrix_add():
    x = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    y = [
        [10,10,10],
        [20,20,20],
        [30,40,50],
    ]
    z = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ]
    for i in range(3):
        for j in range(3):
            z[i][j] = x[i][j] + y[i][j]

    print(z)

# matrix_add()


# 10.匿名函数求和
sum_value = lambda x,y:x+y
# print(sum_value(1,20))


# 11.查找字符串的位置
def str_index(str1, str2):
    return str1.find(str2)
# print('hello world'.find('rld'))

# 12.在字典中找到年龄最大的人并输出
people = {
    'red': 23,
    'blue': 99,
    'purple': 50
}
maxage = 0
for key in people.keys():
    print(key)
    maxage = max(maxage, people[key])

# print(maxage)


# 13.列表转为字典
k=['red', 'blue']
v = [233, 100]

# print(dict([k,v]))


    