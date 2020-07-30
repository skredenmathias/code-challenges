def convert(list):
    # convert int list to string list
    s = [str(i) for i in list]
    
    # convert back to int & join list items using join()
    res = int("".join(s))

    return(res)

result_ll = ListNode()
arr1 = []
arr2 = []
# traverse through LL
current = l1
# print(current)
while current is not None:
    # append to front
    arr1.insert(0, current.val)
    current = current.next

current = l2
while current is not None:
    arr2.insert(0, current.val)
    current = current.next

# convert arrays to ints
# sum ints
result = convert(arr1) + convert(arr2)
print(result)
# return as LL
current = result_ll
# print(current)
if len(arr1) >= len(arr2):

    for i in range(len(arr1)):
        current = current.next
        max_range = len(arr1)
        
        current = ListNode(int(str(result)[max_range-1:max_range]))
        print('current.val ', current.val)
        print('arr1 ', arr1)
        arr1.pop()
        print('i, ', i)
        # print('arr1 ', arr1)
        # current = current.next
        print(current.val)
else:
    for i in range(len(arr2)):
        max_range = len(arr2)
        current = ListNode(int(str(result)[max_range-1:max_range]))
        # print(current)
        arr1.pop()
        current = current.next
        
print(current)
        