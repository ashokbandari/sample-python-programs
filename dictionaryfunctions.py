dic={'name':'ashok','age':22,'phn':[00000000,22222222]}
print(dic['name'])

#dictionary functions

d={'name':'ashok','age':22,'phn':[00000000,22222222]}
x=d.copy()
print(x)

y=d.get('age')
print(y)

d.pop('age')
print(d)


d.update({'address':'hyderabad'})

print(d.keys())

print(d.values())

#clear function 

m={'name':'ashok','age':22,'phn':[00000000,22222222]}
m.clear()
print(m)