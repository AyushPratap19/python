import shutil 
import os


#Here are some examples of how you can use the shutil module in your Python code:
#comment out each line one by one see see its functionality

# shutil.copy( "walrus.py", "main.py") #(uncomment this)
#this copies the content of main2.py to main.py(automatically created if not present)
#if something is already there in main.py it will be overwritten

# shutil.copy2( "walrus.py", "main.py") #(uncomment this)
#this copies the content including mata data of main2.py to main.py(automatically created if not present)


# shutil. copytree("tutorial_main2", "mytutorial" ) #(uncomment this)
#This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.
#I created tutorial_main2 folder inside it I created file.file ,using copytree a same folder with same file created

# shutil.move("tutorial_main2/file.file","file.file") #(uncomment this)
#this moves file from one place to another 
#file.file which was previously present in tutorial_main2 moves out of it
#if we create one new folder(xyz) and writes shutil.move("mytutorial/file.file","xyz/file.file")
# shutil.move("mytutorial/file.file","xyz/file.file") #(uncomment this)

# shutil.rmtree( "mytutorial") #(uncomment this)
#it deletes a directory or folder but cannot delete a file

#os. remove( "main.py")#file can only be removed by os module