# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:55:10 2020

@author: Geo
"""

import os, shutil, pathlib
from collections import defaultdict

def make_directory(dir_):
    for dir_name in dir_:
        try:
            pathlib.Path(dir_name).mkdir(parents=True, exist_ok=False)
        except:
            print("Need check for make directory ==>", dir_name)


def make_path(dir_name, file_name: str):
    source_path = os.path.join(work_space, file_name)

    if dir_name == None:
        return source_path
    move_path = os.path.join(work_space, dir_name)

    return move_path + "\\", source_path


def list_file_move(dir_name, file_list : list):
    local_move_path = ""
    for idx, file_name in enumerate(file_list):
        if idx == 0:
            move_path, source_path = make_path(dir_name, file_name)
            local_move_path = move_path
        else:
            source_path = make_path(None, file_name)
        print(source_path)
        shutil.move(source_path, local_move_path)
        

def directory_arrangement(work_space, sep):
    work_space = work_space
        
    li = os.listdir(work_space)
    dir_file_dic = defaultdict(list)
    
    for i in li:
        dir_file_dic[str(i.split(sep)[0])].append(i)
    
    print(dir_file_dic)
    
    ## 디렉토리 생성 
    make_directory(list(dir_file_dic.keys()))

    for dir_name, file_list in dir_file_dic.items():
        list_file_move(dir_name,file_list)


if __name__=="__main__":
    work_space = "C:\\Users\\Geo\\Desktop\\종다리"    
    if os.getcwd() != work_space:
        os.chdir(work_space)

    directory_arrangement(work_space, ".")
