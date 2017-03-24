#!/usr/bin/python2
#coding:utf-8

#给定源文件路径，目标文件路径，把文件从源路径移动（剪切）到目标路径。参考linux中的move命令。
import os,shutil
def mymove(origin_path,target_path):
    if origin_path == '':
        origin_path = os.getcwd()
    if os.path.isfile(target_path):
        os.rename(origin_path,target_path)
    else:
        shutil.move(origin_path, target_path)




if __name__ == "__main__":
    myorigin_path = raw_input("origin path is:")
    mytarget_path = raw_input("target path is:")
    mymove(myorigin_path, mytarget_path)