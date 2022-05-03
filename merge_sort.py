

def merge_two_sort(list1,list2):
    sorted_list=[]
    while list1 and list2:
        if list1[0]>list2[0]:
            sorted_list.append(list2[0])
            list2.pop(0)
        else:
            sorted_list.append(list1[0])
            list1.pop(0)
    if list1:
        sorted_list=sorted_list+list1
    if list2:
        sorted_list=sorted_list+list2
    return sorted_list



def divide_and_sort(list):
    if len(list)<2:
        return list
    mid=len(list)//2
    left= list[mid:]
    right=list[:mid]
    return  merge_two_sort(divide_and_sort(left),divide_and_sort(right))



check=divide_and_sort(list=[5,8,12,56,7,9,45,51])
print(check)