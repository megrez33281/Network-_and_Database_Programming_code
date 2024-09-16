def sum(list):
    sum=0
    for i in range(0, len(list)):
        sum=sum+list[i]
    return sum

print(sum([0,1,2,3]))

def sum_recursion(list):
    if len(list)==1:
        return(list[0])
    else:
        return(list[0]+sum_recursion(list[1:]))

print(sum_recursion([0,1,2,3]))

