import resource


# 限制内存使用，设置可使用的总内存值即可
def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


if __name__ == "__main__":

    limit_memory(1024 * 1024 * 128)

    a = []
    b = []
    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            a.append(list(map(int, line.strip().split())))
    a.pop(0)
    # print(a)
    for begin, end in sorted(a):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])
    print(b)
