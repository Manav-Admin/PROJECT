#creatng tuple empty 
tuple1=()
print(tuple1) #output: ()
tuple2=(1,2,3)
print(tuple2) #output: (1, 2, 3)
print("no | name | salary | designation")
tuple3=(101,'Manav',20000,"MANAGER")
print(tuple3)
empno,empname,empsalary,empdesignation=tuple3
print(empno) #output: 101
print(empname) #output: Manav
print(empsalary) #output: 20000
print(empdesignation) #output: MANAGER

#nested tuple
tuple4=(102,"Mango",20000,"manager",[69])
print(tuple4) #output: (102, 'Mango', 20000, 'manager', [69])

print(tuple4[0]) #output: 102
print(tuple4[1][0])
print(tuple4[3][1])
print(tuple4[4])


#tupple counting and index
tuple5=('m','a','n','a','v')
print(tuple5.count('a'))
print(tuple5.index('n')) #output: 2

#tuple operation

tuple6=('m','a','n','a','v')
print('m' in tuple6) #output: True

#iteration in tuple 
tuple6=('m','a','n','a','v')
for letter in tuple6:
    print(letter) #output: m a n a v

#in-built function 
tuple6=('m','a','n','a','v','10','200','30','5')
print(len(tuple6)) #output: 9
print(min(tuple6))  #output: 10
print(sorted(tuple6))
print(max(tuple6)) #output: 