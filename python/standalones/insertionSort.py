
array = [5,0,3,2,1,1,int('0xD',0),8] #define array length n
# array = [2,int('0xC',0),0,8,int('0xA',0),4,int('0xE',0),6]
# array = [8,7,6,5,4,3,2,1]

print(str(array))

#orignal
# i = 0
# while i<len(array)-1:
#     i += 1
#     x = array[i]
#     j = i
#     while j-1 >= 0 and array[j-1] > x:
#         array[j] = array[j-1]
#         array[j-1] = x
#         print(str(array))
#         j -= 1



#modified for hardware
for i in range(1,len(array)):
    temp_reg = array[i]
    j = i
    while not((j <= 0) or (array[j-1] <= temp_reg)):
        array[j] = array[j-1]
        array[j-1] = temp_reg
        print(str(array)+"     "+str(i)+"     "+str(j))
        j -= 1