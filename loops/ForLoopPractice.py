# --- For loop with List
list=[1,2,3,4,5,6,7,8]
for i in list:
    print(i)

# --- For loop with String
str='Nikhil'
for i in str:
    print(i)

# --- Mention List in for loop. Here we directly mention List in for loop ---
for i in [2,3,4,"nikhil"]:
    print(i)

# IMP: ****** Range concept *******
# --- Its like if you want to print something in range. For example from 0 to 8
for k in range(9): # 9 will be excluded
    print(k)

# --- if you  dont want to start from 0 BUT you want to print from 2 to 7
for l in range(2,8):
    print(l)

# --- If you want to print from 1 till 9 but with the DIFFERENCE of 2
# you have to define 3 things namely, start, end(excluded), range Difference
for m in range(1,10,2):
    print(m)

# IMP: If you want to print in BACKWARD direction --------
for n in range(10,1,-1):
    print(n)

# -- start from 1 until 20 and only print EVEN Numbers ----
for p in range(1,20):
    if p%2==0:
        print(p)


