info = {"Carla", 19, False, 5.9, 19}
print(info)
# Sets are unordered,no duplicate elements,unchangeable
ayush={}
print(type(ayush)) #since set and  dictionary have the same syntax, so to declare empty set:-
ayush=set()
print(type(ayush))

# methods in sets
# i) union,add and update
s1={1,2,5,6}
s2={3,6,8}
print(s1.union(s2)) #here s1 and s2 are unchanged
s1.add(7)
s1.update(s2) #here s1 is changed or s1=s1+s2 or to add more than 1 item to a set we use update
print(s1,s2)

#ii)intersection and intersection_update
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1,s2)

#iii) symmetric_difference(jo values common nhi h)
print(s1.symmetric_difference(s2))
print(s1,s2)
s1.symmetric_difference_update(s2)
print(s1,s2)

#iv)difference(A-B:as per set theory) set A se saari B ki values nikaal do
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))
cities.difference_update(cities2)
print(cities2,cities)

#v)disjoint set(returns True if both the sets are different else false)
print(s1.isdisjoint(s2))

#vi) superset(A is said to be superset of B only if all values of B are present in A) and subset
cities = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Seoul","Kabul"}
print(cities.issuperset (cities2))
cities3 = {"Tokyo","Madrid", "Delhi"}
print(cities. issuperset (cities3))
print(cities3. issubset (cities))

#vii) remove,discard,pop,del,clear
cities.remove("Tokyo")
cities.discard("tokyo")#discard do not throws an error if the value is not present in the set but remove does
print(cities)
#pop randomly pops an element from the set
random=cities.pop()
print(random) #to get to know which element is poped
print(cities) #every time we run this we will get different answers as set are unordered and elements are poped randomly
# del(cities2)
# print(cities2) #this will give error as variable is itself deleted(uncomment to check)
cities.clear()
print(cities) #this gives an empty set
if "Delhi" in cities3:
    print("yes")
else:
    print("no")