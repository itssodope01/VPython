def common_elements(lst1, lst2):
    c_elements = []
    for i in lst1:
        for j in lst2:
            if i == j:
                c_elements.append(i)

    return c_elements

list1 = [1, 2, 3, 4, 5]
list2 = [1, 7, 3, 9, 5]

result = common_elements(list1, list2)

print(result)
