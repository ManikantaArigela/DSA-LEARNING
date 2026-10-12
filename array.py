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