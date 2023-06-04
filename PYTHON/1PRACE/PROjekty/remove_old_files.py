import os 
import datetime

rootdir = os.getcwd()
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        file_status = os.stat(file)
        print(file)
        print ("last accces date"),
        print (datetime.datetime.fromtimestamp(file_status.st_atime))
        print ("last modified date") ,
        print (datetime.datetime.fromtimestamp(file_status.st_mtime))
        if (datetime.datetime.fromtimestamp(file_status.st_mtime)) > (datetime.datetime(2022,1,1)):
            #os.remove(file)
        #else:
          print("no")