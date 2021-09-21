def list_to_str(lis):
    fstr = '{}, '*len(lis)
    fstr = fstr[:-2]
    return '[' + fstr.format(*lis) + ']'

print(list_to_str([1,2, 3,4,5]))