# # #append()
l = ['a', 'b', 'c']
l.append(34)    #['a','b','c','34']
l.append(34.3)  #['a','b','c','34','34.3']
l.append(4+3j)  #['a','b','c','34','34.3','4+3j']
l.append(True)   #['a','b','c','34','34.3','4+3j','True']
l.append(None)   #['a','b','c','34','34.3','4+3j','True','none']
l.append([0,1,2]) #['a','b','c','34','34.3','4+3j','True','none',[0,1,2]]
l.append((3,4,5)) #['a','b','c','34','34.3','4+3j','True','none',[0,1,2],(3,4,5)]
l.append({6,7,8})  #['a','b','c','34','34.3','4+3j','True','none',[0,1,2],(3,4,5),{6,7,8}]
l.append({9:'a', 10:'b', 11:'c'})   #['a','b','c','34','34.3','4+3j','True','none',[0,1,2],(3,4,5),{6,7,8},{9:'a', 10:'b', 11:'c'}]
l.append('rakesh') #['a','b','c','34','34.3','4+3j','True','none',[0,1,2],(3,4,5),{6,7,8},{9:'a', 10:'b', 11:'c'},'rakesh']
l.append(range(12,15))  #['a','b','c','34','34.3','4+3j','True','none',[0,1,2],(3,4,5),{6,7,8},{9:'a', 10:'b', 11:'c'},'rakesh',range(12,15)]
print(l) #['a','b','c','34','34.3','4+3j','True','none',[0,1,2],(3,4,5),{6,7,8},{9:'a', 10:'b', 11:'c'},'rakesh',range(12,15)]

# extend() 
l = ['a', 'b', 'c']
#l.extend(34)    #int is not iterable
#l.extend(34.3)  #float
#l.extend(4+3j)        
#l.extend(True)   #bool not iterable
#l.extend(None)
l.extend([0,1,2]) #['a','b','c',0,1,2]
l.extend((3,4,5)) #['a','b','c',0,1,2,3,4,5]
l.extend({6,7,8})                   #['a','b','c',0,1,2,3,4,5,6,7,8]
l.extend({9:'a', 10:'b', 11:'c'})   #['a','b','c',0,1,2,3,4,5,6,7,8,9,10,11]
l.extend('rakesh')                  #['a','b','c',0,1,2,3,4,5,6,7,8,9,10,11,'r','a','k','e','s','h']
l.extend(range(12,15))              #['a','b','c',0,1,2,3,4,5,6,7,8,9,10,11,'r','a','k','e','s','h',12,13,14]
print(l)

# insert() 
#positive index
l = ['a', 'b', 'c', 'd'] 
l.insert(2, 'hi')           # ['a','b','hi','c','d']        
print(l)
l.insert(10, 'hi')        # # ['a','b','hi','c','d','hi']  
print(l)
#negative index
l = ['a', 'b', 'c', 'd', 'e']
l.insert(-2, 'hi')           # ['a','b','c','hi','d','e'] 
print(l)
l.insert(-100, 'hi')
print(l)                     # ['hi','a','b','c','hi','d','e'] 

#pop()
l = [1, 2, 3, 4, 5]
a = l.pop()           #5[1,2,3,4]
print(a, l)
b = l.pop(2)          #3[1,2,4]
print(b, l)
#c = l.pop(7) 
del l[0]        #1[2,4]
print(l)         #[2,4]

# remove()
l = [1, 2, 3, 4]
a  = l.remove(3)   # none[1,2,4]
print(a, l)
#print(l.remove(5)) #error

# # clear()  
l = [1, 2, 3, 4, 5]
l.clear()
print(l)   #[]

# # reverse() 
l = [1, 2, 3, 4, 5]
print(id(l))      
a = l.reverse()
print(a, l)         # none[5,4,3,2,1]
print(id(l))

# sort()  
l = [1,4,2,6,5,3]
print(id(l)) 
a = l.sort()  #[1,2,3,4,5,6]
print(a, l)
print(id(l))
l = [50,10,40,20,30]
print(l.sort(reverse=True)) #[50,40,30,20,10]
print(l)


# index() 
l = [1, 2, 1, 4, 6, 1, 7]
print(l.index(1))            #0
print(l.index(1, 3))         #5
#print(l.index(1, 3, 5))
#print(l.index(9))

# count() 
l = [1, 2, 1, 4, 1, 6, 7, 1]
print(l.count(1))      #4
print(l.count(9))   #0


# # index() 
l = (1, 2, 1, 4, 6, 1, 7)
print(l.index(1))            #0
print(l.index(1, 3))         #5
# print(l.index(1, 3, 5))
# print(l.index(9))

# # count() 
l = (1, 2, 1, 4, 1, 6, 7, 1)
print(l.count(1))   #4
print(l.count(9))  #0