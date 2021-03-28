#找列表中最大的数字

def max_xsj(list):#与标准答案基本相同
    if(len(list) == 1):
        return list[0]
    else:
        if (max_xsj(list[1:]) > list[0]):
            return max_xsj(list[1:])
        else:
            return list[0]


def max_result(list):
    if (len(list)==0):
        return None
    if (len(list)==1):
        return list[0]
    else:
        sub_max = max(list[1:])
        if list[0] > sub_max:
            return list[0]
        else:
            return sub_nax

a = [1,2, 33, 4, 5]
print(max_xsj(a))
