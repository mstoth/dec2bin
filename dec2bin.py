# example decimal to binary conversion function

def dec2bin(num):
    result = []
    while num > 0:
        if num % 2 == 1:
            result.append(1)
        else:
            result.append(0)
        num=num/2
    result.reverse()
    return result

def dec2bins(num):
    result = ""
    while num > 0:
        if num % 2 == 1:
            result = "1" + result
        else:
            result = "0" + result
        num = num/2
    return result

