import os
path='C:/Users/ahmad\iCloudDrive/Python/Python Operating Sys/python'
for i in range(20):
    file_name = f'text-{i}.txt'
    open(f"C:/Users/ahmad\iCloudDrive/Python/Python Operating Sys/python/{file_name}",'w')


for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        #print(file)
        fileName,fileExt=os.path.splitext(file)
        #print(fileName)
        #print(fileExt)
        filename,filenumber=fileName.split('-')
        newName=f'{filenumber}-{filename}{fileExt}'
        os.rename(os.path.join(path,file),os.path.join(path,newName))
        # print(filenumber,filename)
        # print(file)