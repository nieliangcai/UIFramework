import random
from faker import Factory

faker = Factory().create('zh_CN')
"""随机的虽好，但是也不一定就实用"""

def random_phone_number():
    '''生成随机电话号码'''
    return faker.phone_number()

def random_phone_num(pre):          #传入参数为手机号码前缀 like:133  135 153
    prefix = pre
    postfix = ""
    for i in range(8):                  #前缀三位，后缀8位
        suff = str(random.randint(1,8))
        postfix += suff
    return prefix+postfix
# print(random_phone_num('133'))

def random_name():
    """随机姓名"""
    return faker.name()

# print(random_name())
def random_email():
    """生成随机邮箱"""
    return faker.email()
# print(random_email())

def random_address():
    """随机地址"""
    return faker.address()

def random_ipv4():
    return faker.ipv4()

def random_str(min_chars =0,max_chars=8):
    """长度在min_chars-max_chars之间的字符串"""
    return faker.pystr(min_chars=min_chars,max_chars=max_chars)

def factory_generate_ids(starting_id=1,increment=1):
    """返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment"""
    def generate_started_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment
    return generate_started_ids()

def factory_choice_generator(values):
    """返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项"""
    def choice_generator():
        my_list = list(values)
        while True:
            yield random.choice(my_list)
    return choice_generator()