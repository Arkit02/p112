import os
import shutil

from_dir="C:/Users/Arkit/Downloads"
to_dir="C:/Users/Arkit/Downloads/di"
listOfFiles=os.listdir(from_dir)
#print(listOfFiles)
for i in listOfFiles:
    name,extension=os.path.splitext(i)
    #print(name)
   # print(extension)
    if extension=='':
        continue
    if extension in ['.pdf',".txt",".docx",".doc"]:
        path1=from_dir+"/"+i
        path2=to_dir+"/"+"DocumentFile"
        path3=to_dir+"/"+"DocumentFile"+"/"+i
        if os.path.exists(path2):
          print("moving "+i+"....")
          shutil.move(path1,path3)
        else:
          os.makedirs(path2)
          print("moving"+i+'...')
          shutil.move(path1,path3)
