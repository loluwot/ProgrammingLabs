def list1_starts_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for l1, l2 in zip(list1, list2):
            if l1 != l2:
                return False
        return True
    return False

print(list1_starts_with_list2([1,2,3,4], [1,2,3]))  #true
print(list1_starts_with_list2([1,2,3,4], [1,2,4]))  #false