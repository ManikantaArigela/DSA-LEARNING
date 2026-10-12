# fid the largest number in the array
def find_big(arr):
    max_elm = arr[0]
    for i in arr:
        if i > max_elm:
            max_elm = i
    return max_elm


ar =[10,20,304,506,905,4]
print("largest " , find_big(ar))


print("using the max function ",max(ar))



# second largest number in the array


#approaches
''' 
first sorting and picking the second  element in the array
traversing the array and usinf if conditions to find the second largest for this first find the smallest number and travesal of all the array and then fing the second element
'''
def find_second_largest(aa):
    unique_sorted = sorted(set(aa))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]
a=[45,76,23,98,45,76]
print(" the second largest number in the array",find_second_largest(a))

