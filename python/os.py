import os
print(os.getcwd()) # this will give the current working directory
print(os.listdir()) # this will give the list of files and directories in the current working directory
os.chdir('C:\\Users\\Lenovo\\Desktop\\coding\\project\\python ') # this will change the current working directory to the specified path    
print(os.listdir())
os.remove('example.txt')
print(os.listdir()) # this will give the list of files and directories in the current working directory