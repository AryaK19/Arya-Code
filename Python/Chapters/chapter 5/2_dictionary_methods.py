#dictionary methods
d = {
  "fast": "In a Quick Manner",
  "arya": "Name of a boy",
  "marks": [1,2,3,4],
  "another d": {"arya": "good boy"},
  1:"2-1"
}
# can convert to list
print(list(d.keys())) # prints the keys of the dictionary

print(d.values()) # prints the values of the dictionary

print(d.items()) # prints the keys,values of the dictionary

#can add things to dictionary
d1 = { "slow" : " well slow... ",
 "dance": "to dance",
 "make": "to create"
} 
d.update(d1)
print(d.items())

# get method
print(d.get("arya")) # prints value of arya
print(d["arya"])# prints value of arya

# but if the thing is not present 
print(d.get("arya1")) # it will not give an error
# print(d["arya1"]) # it will give error

# etc ..... (methods)