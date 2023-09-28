def r_s(string, word, change): 
    n=string.replace(word, change) 
    return n.strip()
a='Arya is a good boy'

f = r_s(a, 'Arya', 'Partha')
print(f)