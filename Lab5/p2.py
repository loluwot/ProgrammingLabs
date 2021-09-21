def match_pattern(list1, list2):
    if len(list1) >= len(list2):
        for i in range(len(list1) - len(list2)):
            if list1[i:i+len(list2)] == list2:
                return True
        return False
    return False

print(match_pattern([4, 10, 2, 3, 50, 100], [2, 3, 50])) #True
print(match_pattern([4, 10, 2, 3, 51, 100], [2, 3, 50])) #False

