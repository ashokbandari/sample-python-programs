#""DATA STRUCTURES USING FUNCTIONS""
 
#LIST 

def list(*a):
    print([a])
    length=(len(a))
    print(length)
list(1,2,3,4)


#TUPLE

def tuple(*b):
    print(b)
    minval=(min(b))
    print(minval)
    maxval=(max(b))
    print(maxval)
tuple(1,2,5.5,20,50)


#SET

def set(a,b):
  print(a.union(b))
set({1,2,3},{4,5,6})

#DICTIONARY


def dic(**d):
    print(d)
dic(name= 'ashok',age= 22,address= 'hyderabad')	