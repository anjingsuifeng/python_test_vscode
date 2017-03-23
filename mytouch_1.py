#!/usr/bin/python2
#coding:utf-8
'''创建文件：在指定目录下创建文件，参考linux的touch命令'''
import os

def my_touch(target_name, file_name):
    if target_name == '':
        target_name = os.getcwd()
        
    if not os.path.exists(target_name):
        os.mkdir(target_name)
        print target_name

    file_path = target_name +'/'
    file_path = file_path + file_name
    print file_path
    f = open(file_path, 'w')
    if not f:
        return False
    return True

if __name__ == "__main__":
    dir_name = raw_input("please input the dir_name\n(the current directory use enter)")
    file_name = raw_input("please input the file_name:")
    if not my_touch(dir_name, file_name):
        print file_name, "failed"
    else:
        print file_name, "success"