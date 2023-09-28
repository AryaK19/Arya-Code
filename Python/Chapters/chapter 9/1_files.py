#There are vareous thing to do with files in python
#close files onces opened 
# use a open funtion to read the content of file

f = open('D:\python arya\chapter 9\sample.txt','r')# if (  , " ") nothing mentioned it will take 'r'
data = f.read()# if reaten 5 in () first five files will be printed
print(data)
f.close()