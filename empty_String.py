t=[(),(1,),[],'abc',(),(),(1,),('a',),('a','b'),((),),'']
data = []
for i in t:
    if i != '' and i != [] and i != ():
        data.append(i)
print(data)