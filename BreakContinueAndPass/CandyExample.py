totalCandies=10
needCandies=int(input("How many candies you want:"))
for i in range(1,needCandies):
    if i>10:
        print('we only have 10 candies right now.')
        break
    print('Candy: ',i)


