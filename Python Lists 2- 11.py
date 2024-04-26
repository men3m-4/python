men3m=["mohamed","abdelmoniem","mosaad","radwan","elsayed"]
Cristiano=["Cristiano","Ronaldo","dos Santos","Aveiro."]
print(men3m,Cristiano)              #print the two lists like that ['mohamed', 'abdelmoniem', 'mosaad', 'radwan', 'elsayed'] ['Cristiano', 'Ronaldo', 'dos Santos', 'Aveiro.']
men3m.extend(Cristiano)             #add cristiano extended to men3m
print(men3m)                        #will print the two lists in the same square bracket
men3m=men3m + Cristiano
print(men3m)                        #will print the same output of the  men3m.extend(Cristiano)
men3m += Cristiano
print(men3m)                        #will print the same output of the  men3m.extend(Cristiano) and men3m=men3m + Cristiano
men3m.append("elbanna")             #will add new value(term) to the list (at the end of the list)
men3m.insert(1,"d")  #men3m.insert(  the location ,"the value")
men3m.remove("elsayed")             #to remove the value
print(men3m)
men3m.clear()                       #remove all values in the list
men3m.pop()                         #remove the last value in the list
what_was_popped =men3m.pop()        #pop remove the value and stor it in variable]
print(what_was_popped)
print(men3m.index("mosaad"))        #check if the value is exist in the list  or not

print(Cristiano.count("Ronaldo"))   #detemine how many Ronaldo in the list
men3m.sort()                        # Rearrangement with alpha  or from small to the big for numbers
list_new= men3m.copy()              # shallow copy يعني الجديده مش هتتغير بتغير القديمه
