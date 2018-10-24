# 测试数据
import random

N = 100000
MAX = 1000000000

with open('./input.txt', 'w', encoding='utf-8') as f:
    f.write('%s\n' % N)

    randomIndex = random.sample(range(1, MAX), N)
    for i in randomIndex:
        f.write('%s %s\n' % (random.randint(0, i - 1), i))
