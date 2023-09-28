import os
print(os.getcwd())
# prints the current directory

os.chdir(r'\Users\Tejas Shastri\OneDrive\Desktop\Codes')
print(os.getcwd())

print(os.listdir())
#Gives a list of all componets of the directory

# Creating a new folder in the directory -
os.mkdir("DemoDirectory1")
os.makedirs("DemoDirectory2/SubDirectory1") #used to make a directory with multiple levels
os.rmdir("DemoDirectory1") # Remove directories
os.removedirs("DemoDirectory2/SubDirectory1")

os.rename("x.txt", "y.txt")

print(os.stat("y.txt")) # Gives infor of the file
print(os.stat("y.txt").st_size) # Shows size
print(os.stat("y.txt").st_mtime) # (needs DateTime)Shows Modification Time

for dirpath, dirnames, filenames in os.walk(os.getcwd()): # Or just specify the path
     print("Current path = ", dirpath)
     print("Directories = ", dirnames)
     print("Files = ", filenames)
     print()

print(os.environ.get("DemoDirectory1")) # Prints Environment Variable "Home"'s Path

filepath = os.environ.get("DemoDirectory") + 'test.txt'
print(filepath)
# OR WE COULD DO...
filepathx = os.path.join(os.environ.get("DemoDirectory"), 'test.txt')
print(filepathx)

print(os.path.basename("/wtf/test.txt")) # Path is not real, yet it works
print(os.path.split("/wtf/test.txt")) # Full path will be shown
print(os.path.exists("/wtf/test.txt")) # Boolean Value

