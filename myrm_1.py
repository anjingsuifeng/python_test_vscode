#!/usr/bin/python2
#coding:utf-8
import os, shutil
def myrm(path):
    if os.path.isfile(path):
        os.remove(path)
    else:    
        file_list = os.listdir(path)
        print file_list
        digui_deldir(path)
        # if s == True:
        #     return
        # else:
        #     digui_deldir(s)
ALL_DEL = "DEL"
def digui_deldir(path):
    for file_name in os.listdir(path):
        file_path = path + '/' + file_name
        if os.path.isfile(file_path):
            print("ll--file")
            os.remove(file_path)
        else:
            print("ll--dir")
            confirm = raw_input("File: %s Input DEL" % file_path)
            if not (confirm == ALL_DEL):
                continue
            else:
                shutil.rmtree(file_path)
            
if __name__ == "__main__":
    path = raw_input("please input a path\n(the current dir use './')")
    digui_deldir(path)