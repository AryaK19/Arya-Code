#format method was beening used before f string methode
nname="Partha"
name ="Arya"

# a = f"my name is {name}"
# a = f"my name is {name} and his name is not {nname}"


a = "my name is {}".format(name)
a = "my name is {} ans his name is not {}".format(name,nname)
#you can put no. in braket in order to get the respective string..
a = "my name is {1} ans his name is not {0}".format(name,nname)
#so it is changed now ......

print(a)