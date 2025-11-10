# Print from 1 to 10. Skip the statement print if i is even number
# Loop ke andar jab Python ko continue milta hai, to current iteration ko chhod deta hai aur next iteration pe jump kar jaata hai.

for i in range(1,11):
    if i%2==0:
        continue
    print(i)
