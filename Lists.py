num = [1,2,3,4,5,6,7,8,0]
target = 4

a = num[0]
b = num[0]

x = 0
y = 0

answer = 0

while answer != target:
    answer = a+b
    if answer != target & b < max(num):
        b+=1
        y = b
        answer = a+b 
    elif answer != target & a < max(num):
        a+=1
        answer = a+b 
        x = a
        break

nums=[x,y]
print(nums)
