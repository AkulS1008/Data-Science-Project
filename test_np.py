from math import gcd, trunc
import numpy as np
from numpy import random, ufunc
"""
#Create numpy array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print(arr)

#Sclicing array
slice_array = arr[:3, ::3] 
print(slice_array)
 
#Adding 3D array
arr1 = np.array([[[1,2], [3,4]], [[5,6], [7,8]], [[9,0], [1,2]]])
print(arr1)
print(arr1.ndim) #Prints dimension of array

#Numpy arrays can be indexed
print(arr[1] + arr[2]) #Adds both rows
print(arr[1] * arr[2])
print(arr[1] - arr[2])

#Iterates through 3D array with numpy        
for x in np.nditer(arr1): #Takes care of all dimensions
    print(x)
for x in np.nditer(slice_array):
    print(x)
for x in np.nditer(arr):
    print(x)

#Iterates through 3D array without numpy
for x in arr1:
    for y in x:
        for z in y:
            print(z)

#Deep copying array
a = arr.copy()
a[0] = [1, 4, 7]

#Prints (numrow, numcol) for 1D
arr2 = np.array([[[1,2], [3,4]], [[5,6], [7,8]], [[9,0], [1,2]]])
print(arr2.shape)

#Changing shape of array
l = np.array([[[1,2], [3,4]], [[5,6], [7,8]], [[9,0], [1,2]]])
new_arr = l.reshape(4, 3)
print(new_arr)
l = np.array([[[1,2], [3,4]], [[5,6], [7,8]], [[9,0], [1,2]]])
new_arr = l.reshape(-1) #Makes a 1D array
print(new_arr)

#Concats 2 arrays
l1 = np.array([1, 2, 3, 4])
l2 = np.array([4, 5, 6, 7])
e = np.concatenate((l1, l2))
print(e)
l1 = l1.reshape(2, 2)
l2 = l2.reshape(2, 2)
e = np.concatenate((l1, l2), axis = 1) #concats first and second rows of both arrays, which are 1D
print(e)

#Splits the array into 'parameter' parts
e = np.array([1, 2, 3, 4, 5, 6])
x = np.array_split(e, 4)
print(x)

#Gives indexes of target element in array
arr = np.array([1, 2, 3, 4, 5, 4, 4, 5, 6, 7, 8])
arr1 = np.where(arr % 2 == 1) #Gives odd value indexes
print(arr1)

#Sorts 1D array
arr = np.array([1, 2, 3, 4, 5, 4, 4, 5, 6, 7, 8])
print(np.sort(arr))
#Sort 2D array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print(np.sort(arr)) #Sorts each row
#Sorts string array
l = np.array(["Apple", "Orange", "Zebra", "Bananna"])
print(np.sort(l)) #Sorts by ASCII values

#Filter arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4, 5, 6, 7, 8])
filter_array = arr > 6 #Any value > 6, put in new array
print(arr[filter_array]) #Gives [7, 8]
print(arr[arr % 2 == 0])

#Returns random integer between 0 and 20
a = random.randint(20)
print(a)

#Returns random no. b/w 0 and 1
print(random.rand())

#Gives array of random integers (depending on no. of parameters) b/w 1 and 20
a = random.randint(20, size = (2, 3, 3))
print(a)
a = random.rand(2, 3, 3)
print(a)

#Returns random element, repeated randomly depending on size
a = random.choice([2, 4, 6, 8, 10], size = (3, 3))
print(a)
a = random.choice(["red", "blue", "green"], size = (2, 3))
print(a)

#Give probability parameter to control number of occurences
marbles = random.choice(["red", "blue", "green"], p = [0.5, 0.2, 0.3], size = (3, 3))
print(marbles)

#Shuffles array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
random.shuffle(arr)
print(arr)
arr_diff = random.permutation(arr) #creates different array
print(arr_diff)

#Using function to do functions
def myadd(x, y):
    return x + y
a = np.frompyfunc(myadd, 2, 1)
print(a([1, 2, 3], [4, 5, 6]), type(a))
print(np.add([1, 2, 3], [4, 5, 6]))
print(np.multiply([1, 2, 3], [4, 5, 6]))
print(np.divide([1, 2, 3], [4, 5, 6]))
print(np.mod([4, 5, 6], [1, 2, 3]))
print(np.power([1, 2, 3], [4, 5, 6]))
print(np.subtract(np.add([1, 2, 3], [4, 5, 6]), np.multiply([1, 2, 3], [4, 5, 6])))

#Gives absolute values of all elements
a = np.absolute([-1, -2, -3])
print(a)

#Gives occurence of 4
a = random.choice([2, 4, 6, 8, 10], size = (4, 3))
target = 4
filter_array = a == 4
print(a)
print(a[filter_array])
print(len(a[filter_array]))

#Create checker board
brd = random.choice([0], size = (8, 8))
brd[::2, 1::2] = 1
brd[1::2, ::2] = 1
print(brd)
#OR
c = 2
for i in range(len(brd)):
    for j in range(len(brd[i])):
        if c % 2 == 1:
            brd[i][j] = 1
        c += 1
    c += 1
print(brd)

#Problem 3
brd = random.choice([0], size = (9, 9))
brd[::, ::3] = 1
brd[::, 1::3] = 2
brd[::, 2::3] = 3
print(brd)

#Functions
arr = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size = (3, 3))
print(arr)
print(arr.max())
print(arr.min())
print(arr.mean())
arr.sort()
print(arr)
print()

#Reverses elements in rows
arr = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size = (3, 3))
print(arr)
print(arr[::, ::-1])

#Reverses everything, row order and columns 
arr = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size = (3, 3))
print(arr)
print(np.flip(arr)) 
arr = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size = (3, 3))
print(np.ones([2, 2]))
print(np.zeros([2, 2]))

#Checks if 2 arrs are equal
arr1 = np.array([1, 2, 3, 4, 5, 8])
arr2 = np.array([1, 2, 3, 4, 5, 6])
arr3 = arr1 == arr2
print(arr3.all())
arr = np.array([4, 5, 6, 7, 4])
print(4 in arr)

#Find GCF and LCM of elements
arr1 = np.array([1, 2, 3, 4, 5, 8])
GCF = np.gcd.reduce(arr1)
LCM = np.lcm.reduce(arr1)
print(GCF, LCM)

#Rounds each element
arr1 = np.array([1, 2, 3, 4, 5])
r = np.trunc(arr1)
print(r)
r = np.ceil(arr1)
print(r)
r = np.floor(arr1)
print(r)
print(np.cumsum(arr1)) #Cumulative sum
print(np.cumprod(arr1))

#Making set and doing functions
arr = [1, 2, 3, 4, 5]
arr1 = [4, 5, 6, 7, 8]
sarr1 = np.unique(arr)
sarr2 = np.unique(arr1)
print(np.union1d(sarr1, sarr2))
print(np.intersect1d(sarr1, sarr2))
print(np.setdiff1d(sarr1, sarr2))
print(np.setdiff1d(sarr2, sarr1))

#Find mean
arr = [1, 2, 3, 4, 5]
np.mean(arr)
np.median(arr)

#Transverse
arr = random.choice([1, 2, 3, 4, 5], size = (3, 2))
print(arr)
print(arr.reshape(2, 3))

#Function
l = [random.choice([1, 2, 3, 4, 5], size = (3)), random.choice([1, 2, 3, 4, 5], size = (3)), random.choice([1, 2, 3, 4, 5], size = (3))]
print(l)
new_l = []
for i in range(len(l)):
    new_l.append(np.sum(l[i]))
print(new_l)

#Set functions for strings
sarr1 = np.array(["my", "day", "is", "great"])
sarr2 = np.array(["is", "your", "day", "great"])
print(np.union1d(sarr1, sarr2))
print(np.intersect1d(sarr1, sarr2))
print(np.setdiff1d(sarr1, sarr2))
print(np.setdiff1d(sarr2, sarr1))

#It will concat each character with " "
arr1 = np.array(["my", "day", "is", "great"])
print(np.char.join("_", arr1))
print(np.str_.join("_", arr1)) #Combines all elements to one word with "_" b/w them

#String functions
sarr1 = np.array(["My", "Day", "iS", "gReaT"])
sarr2 = np.array(["is", "your", "day", "great"])
print(np.char.not_equal(sarr1, sarr2)) #True if not qual
print(np.char.equal(sarr1, sarr2)) #True if equal
print(np.char.swapcase(sarr1))
print(np.char.endswith(sarr1, "Day"))
"""
