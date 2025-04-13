arr = [10,20,30,40,50]
print(arr[-1])

brand= ["apple","microsoft","google","amazon"]
print(brand)
length_brand=len(brand)
print(length_brand)
brand.append('ibm')
print(brand)

#Removing of elements from list
brand.remove("apple")
print(brand)
brand.pop(2)
print(brand)
del brand[1]
print(brand)
del brand[0]
print(brand)
del brand[-1]
print(brand)
brand.clear()

#replasing or modifying the elements 
cars=["RR","BMW","GT","BT","PORSH"]
print(cars)
cars[0]="Rolls Rollys"
print(cars)
cars[-1]="MC"
print(cars)

#concanating the list
joining=[10,20,30]
print(joining)
join=joining+[40,50,60]
print(join)

#slicing an array
fruits=["apple","bannana","mango","grapes","orange"] 
print(fruits[1:4])
print(fruits) #output ['bannana', 'mango', 'grapes']
print(fruits[:3])
print(fruits) #output ['apple', 'bannana', 'mango']
print(fruits[-4:])
print(fruits) #output ['bannana', 'mango', 'grapes', 'orange']
print(fruits[-3:-1])
print(fruits) #output ['mango', 'grapes']

#repeat the arry
name =["manav"]
rep = name * 5
print(rep) #output ['manav', 'manav', 'manav', 'manav', 'manav']

#multidimensional array
multd=[[1,2],[3,4],[5,6]]
print(multd)
print(multd[0])
print(multd[2][0])

