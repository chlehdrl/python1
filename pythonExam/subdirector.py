import os

path="C:/"
def get_subdir(path):
    try:
            dirfiles=os.listdir(path)
    except PermissionError:
            return

    subdir_list=[]
    for each in dirfiles:
            full_name = path + each
            if os.path.isdir(full_name):
                    subdir_list.append(full_name+"/")
    return  subdir_list
print(get_subdir(path))
