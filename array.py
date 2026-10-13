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



# second smallest number in the array


#approaches
''' 
first sorting and picking the second  element in the array
traversing the array and usinf if conditions to find the second largest for this first find the smallest number and travesal of all the array and then fing the second element
'''
def find_second_largest(aa):
    unique_sorted = sorted(set(aa))
    return unique_sorted[1]
a=[45,76,23,98,45,76]
print(" the second largest number in the array",find_second_largest(a))




# dupliactes in the array
def duplicates(array):
    hashset = set()
    for i in array:
        if i in hashset:
            return True
        hashset.add(i)
array = [1,2,32,1,2]
print("boolean result " ,duplicates(array) )


#anagram
def anagram(str1,str2):
    #return sorted(str1) == sorted(str2)
    if len(str1) != len(str2):
        return False
    countS,countT = {}, {}
    for i in range(len(str1)):
        countS[str1[i]] = 1 +countS.get(str1[i],0)
        countT[str2[i]] = 1+ countT.get(str2[i],0)
    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True
str1 = "one"
str2 = "noe"
print("is anagram", anagram(str1,str2))