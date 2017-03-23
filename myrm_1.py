#!?usr/bin/python2
#coding:utf-8
import os
def myrm(path):
    if os.path.isfile(path):
        os.remove(path)
    else:
        file_list = os.listdir(path)
        print file_list
        if not file_list:
            os.rmdir(path)
        else:
            print "%s incloud dirs,you can not del it" %path
        # for i in range(len(file_list)):
        #     file_path = path + '/' + file_list[i]
        #     if os.path.isfile(file_path):
        #         os.remove(file_path)
        #     else:
        #         print "%s incloud dirs" %file_path


if __name__ == "__main__":
    input_path = raw_input("please input a path\n(the current dir use './')")
    myrm(input_path)