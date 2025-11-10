# ----- Simple function accepting 2 parameters
def addition(x,y):
    c=x+y
    print(c)

addition(2,3) # Calling a fucntion

# ----- Function returning something -----
def multiplication(x,y):
    mul=x*y
    return mul

resultMul=multiplication(3,4)
print(resultMul)

# ---- V.Imp : ------ One function can return MULTIPLE times -----
def add_mul(x,y):
    add=x+y
    multi=x*y
    return add,multi

addStore,mulStore=add_mul(6,7)
print(addStore)
print(mulStore)


def add_mul_divide(x,y):
    add=x+y
    multi=x*y
    div=x/y
    return add,multi,div

addStore,mulStore,divStore=add_mul_divide(8,8)
print(addStore)
print(mulStore)
print(divStore)












