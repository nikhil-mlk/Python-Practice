# addition=lambda x,y:x+y
#
# result=addition(3,4)
# print(result)

#  listOfEvenNumber=[]
#  def evenNumbers(li):
#      for i in range(len(li)):
#          numb=list[i]
#          if numb%2==0:
#              listOfEvenNumber.append(numb)
#      return listOfEvenNumber
#
#  list=[1,2,3,4,5,6,7,8,9]
#
#  result=evenNumbers(list)
#  print(result)


li=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda value:value%2==0,li))
print(result)


li1=[1,2,3,4,5,6,7,8,9]

result=list(map(lambda numb:numb*2,li1))
print(result)






