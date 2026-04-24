import os
p = 'C:/Users/Leo/Documents/pk111'
res = os.scandir(p)
for item in res:
    print(item.name)