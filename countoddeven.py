data=int(input("Enter a number of elements in the series: "))
list=[]
for i in range(data):
 value=int(input("Enter an element: "))
 list.append(value)
odd = sum(1 for i in list if i%2==1)
even= sum(1 for i in list if i%2==0)
print ("The number of odd elements: " +str(odd))
print ("The number of even elements: "+str(even))
