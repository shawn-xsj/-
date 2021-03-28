#计算元素数


def num_xsj(list): #与标准答案一致
    if (list == []):
        return 0
    return 1+num_xsj(list[1:])


A = [2,3,4,5,6]
print(num_xsj(A))
