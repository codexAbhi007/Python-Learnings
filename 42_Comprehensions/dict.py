names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']



#@ 1.1
myDict1 = {}
for name,hero in zip(names,heroes):
    myDict1[name] = hero

print(myDict1)

#@1.2
myDict2 = {name:hero for name,hero in zip(names,heroes)}
print(myDict2)


#@2.1
myDict3 = {}
for name,hero in zip(names,heroes):
    if name != 'Peter':
        myDict3[name] = hero
print(myDict3)

#@2.1 
myDict4 = {name:hero for name,hero in zip(names,heroes) if name != 'Peter'}
print(myDict4)