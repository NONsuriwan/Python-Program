import os
import shutil

path=r'C:\Users\HP\Downloads\New folder\New folder\Path'                     #ต้นทาง
destination=r'C:\Users\HP\Downloads\New folder\New folder\Destination' #ปลายทาง                 
allfile=os.listdir(path)

for f in allfile:
    if f[-3:] == 'txt': #เปลี่ยนเลข - ตามสกุลไฟล์ เช่น .py ใช้  f[-2:] == 'py'
        source=os.path.join(path,f)
        dest=os.path.join(destination,f)
        #print(source)
        #print(dest)
        shutil.copy2(source,dest)
        #print('---------')
        
