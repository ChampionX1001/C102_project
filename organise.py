import os
import shutil
sourcedir="./test"
#destinationdir="C:/Users/vraje/Downloads/Rohan Inampudi/Personal/Python/Byjus Classes/C102"
destinationdir="."
listofiles=os.listdir(sourcedir)
print(sourcedir)

for filename in listofiles:
    name, extension=os.path.splitext(filename)
    print(name)
    print(extension)
    if (extension==""):
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.ipt', '.stl', '.svg']:
        path1=sourcedir + '/' + filename
        print(path1)
        path2=destinationdir + '/' + "imagefiles"
        path3=destinationdir+"/"+"imagefiles"+"/"+filename

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)