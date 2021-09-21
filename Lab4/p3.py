def lists_are_the_same(list1, list2):
    for elem1, elem2 in zip(list1, list2):
        if elem1 != elem2:
            return False  
    return True

