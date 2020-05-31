import numpy as np

# n = np.arange(0, 50, 5)  # list of all numbers <=49 divisible by 5
# print(n)

#
# array = np.array([1,2,3,4,5,6])
# print(array)
#
# a =np.ones((2,3),dtype=np.int16)
# print(a)
#
# b= np.empty((2,3))
# print(b)
# k = range(20)
# print(k)
# for i in k:
#     i[...] *= 2
# print(k)

"""
n= np.random.choice([0,2,4],16).reshape(4,4)
print(n)

print(">>",type(np.mean(n,axis=1)),np.mean(n,axis=1))
a=np.array([1,1,1,1])
a=a.reshape([-1,1])
print(a)
print(n-a)
"""

my_arr= np.random.choice([0, 2], 16).reshape(4, 4)
print(my_arr)
mean_arr=np.mean(my_arr, axis=1) #  nX1 array with mean of each row
mean_arr_T=mean_arr.reshape([-1,1]) #mean_arr converted to 1Xn dimension (vertical) array
my_arr= my_arr - mean_arr_T # subtracting mean of each row from elements of each row


print(my_arr)


