# Purpose of Pass statement:
# In java suppose we dont want to do anything in if block, so what dont write anything in curley braces for if block like: if(x>2){}
# But we cant lave blank if block if we dont want to anything. So we write "Pass". This acts like a curley braces with no statement in it.

for i in range(1,11):
    if(i%2==0):
        pass
    else:
        print(i)

