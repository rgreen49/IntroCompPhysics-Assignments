'''
A python module to exhibit the use of the __main__ name.
'''
import os
import shutil

def Zip(assignment_num):
    list_path = '.'
    target_name = f'assignments{os.path.sep}assignment{assignment_num:02d}'
    if not os.path.exists(target_name):
        os.makedirs(target_name)
    
    for f in os.listdir(list_path):
        split_num = (f.split("_"))[0]
        if split_num[1:] == str(assignment_num):
            dest = target_name + os.path.sep + f
            src = list_path + os.path.sep + f
            shutil.copy(src,target_name) 
    
    shutil.make_archive('assignment_archive', 'tar', '.', 'assignments')


