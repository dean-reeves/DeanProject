def 打印九九乘法表():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}", end='\t')
        print()

打印九九乘法表()
