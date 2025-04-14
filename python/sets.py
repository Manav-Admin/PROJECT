#normal sets 
my_sets1={10,20,33,42,55,60}
print(my_sets1)

#mixed data types
my_sets2={101,'manav',20000,(1,2,3)}
print(my_sets2)

#duplicated values not allowed 
my_sets3={10,20,10,33,33,42,50}
print(my_sets3)

#adding values to the set
my_sets3.add(55)
print(my_sets3)

#updating the set   
my_sets3.update([60,70,80])
print(my_sets3)

#add list and set
my_sets3.update([100,200,300],{400,500,600})
print(my_sets3)

print('removing the value from the set  with error') 
my_sets4 = {10,20,30,40,50}
print(my_sets4)
#my_sets4.remove(4) # this will give error
#print(my_sets4)
print("remove the value from the set without error")
my_sets4.discard(1) # this will not give error
print(my_sets4)

#discard  elements with proper value 
my_sets4.discard(50)
print(my_sets4)

#remove 
my_sets4.remove(40)
print(my_sets4)

print("pop")
my_sets5={60,70,80,90,100}
print(my_sets5)

print(my_sets5.pop())
print(my_sets5)

my_sets5.clear()
print(my_sets5)

#union 
mysets6={10,20,30,40}
mysets7={50,60,70,80}
print(mysets6.union(mysets7)) # this will give the union of both sets
print(mysets6 | mysets7) # this will give the union of both sets

#intersection
mysets8={10,20,30,40}
mysets9={30,40,50,60}
print(mysets8.intersection(mysets9)) # this will give the intersection of both sets
print(mysets8 & mysets9) # this will give the intersection of both sets

#difference
mysets10={10,20,30,40} 
mysets11={30,40,50,60}
print(mysets10 - mysets11)  # this will give the difference of both sets
print(mysets10.difference(mysets11)) # this will give the difference of both sets
