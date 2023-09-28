d = {
  "Fast": "In a Quick Manner",
  "Arya": "Name of a boy",
  "Marks": [1,2,3,4],
  "Another d": {"arya": "good boy"}
}
print(d['Fast'])
print(d['Arya'])
print(d['Marks'])
print(d['Another d']['arya'])
# unorder
# mutable
d['Marks'] = [45,55]
print(d['Marks'])
# it is a index ( it over wrights)