#!/usr/bin/python2
#coding:utf-8

def collatz(number):
    if number % 2 == 0:
        
        print number//2
        return number//2
    else:
        print 3*number + 1
        return 3*number + 1

def digui_col(number):
    s = collatz(number)
    if s == 1:
        return 
    else:
        digui_col(s)

if __name__ == "__main__":
    number = int(raw_input("please input a int_number:"))
    digui_col(number)
        
