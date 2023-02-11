def details(name,age,address):
    print("student details",name,age,address)
details('ashok',22,'hyderabad')


#passing list using forloop 

def values(a):
    for i in a:
	     print(a)
values([1,2,3,4,5])   

#Orbitary arguments 

def num(*x):
    print(a)
num(10,20,30,40,50,70)

#keywords arguments

def data(**n):
	print(n)
data(name='ashok',age=22,degree='b.tech',address='hyderabad')	