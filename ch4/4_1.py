#编写sum函数的代码

def sum_result(list):
    if list ==[]:
        return 0
    return list[0]+sum(list[1:])


def sum_xsj(list):
    result =0
    if (len(list) >1):
        # a = list.pop(0)
        result = list[0]+sum_xsj(list[1:])
        return result           # 这里不能掉了result,否则如果进了这个分支，函数就没法返回。这里的要点是递归函数是解决问题的最小单元，能独立解决小规模的问题；
    else:
        return result +list[0]


A = [2,3,6]
print(sum_xsj(A))
print(sum_result(A))
