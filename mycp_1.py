#!/usr/bin/python2
#coding:utf-8
# 给定源文件路径，目标文件路径，把文件从源路径复制到目标路径。参考linux中的cp命令。
#cp命令用来将一个或多个源文件或者目录复制到指定的目的文件或目录。
#它可以将单个源文件复制成一个指定文件名的具体的文件或一个已经存在的目录下。
#cp命令还支持同时复制多个文件，当一次复制多个文件时，目标文件参数必须是一个已经存在的目录，否则将出现错误。

import os,shutil

def mycp(origin_path,target_path):
    if os.path.isfile(origin_path):
        if os.path.isfile(target_path) or os.path.exists(target_path):
            confirm = raw_input("File: %s Input COPY" % origin_path)
            if not (confirm == 'COPY'):
                print "do not copy"
            else:
                shutil.copy(origin_path, target_path)
        else:
            print "%s is a dir which is not fined" %target_path
    else:
        if os.path.exists(target_path):
            for file_name in os.listdir(origin_path):
                origin_path_name = origin_path + "/" + file_name
                shutil.copy(origin_path_name, target_path)
        else:
            print "%s is a dir,but %s can not fined" %(origin_path, target_path)
       
                
if __name__ == "__main__":
    myorigin_path = raw_input("origin path is:")
    mytarget_path = raw_input("target path is:")
    mycp(myorigin_path, mytarget_path)