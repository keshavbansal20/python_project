def remove_common_letters(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if (list1[i] == list2[j]):
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                return [list1 + ['*'] + list2, True]
    return [list1 + ['*'] + list2, False]


p1 = input('enter the name')  # inputname
p1.lower()
p1.replace(' ', '')
p1_list = list(p1)
p2 = input('enter the second name')
p2.lower()
p2.replace(' ', '')
p2_list = (list(p2))
proceed = True
while proceed:
    ret_list = remove_common_letters(p1_list, p2_list)
    con_list = ret_list[0]
    proceed = ret_list[1]
    split_list_index = con_list.index('*')
    p1_list = con_list[:split_list_index]
    p2_list = con_list[split_list_index + 1:]

count = len(p1_list) + len(p2_list)
result = ['friends', 'love', 'affection', 'money', 'enemy', 'sibli']

while len(result)>1:
    split_index = (count % len(result)) - 1
    if split_index >= 0:
        left = result[:split_index]
        right = result[split_index + 1:]
        result = left + right
    else:
        result = result[:len(result) - 1]
print('Relationship Status', result[0])




