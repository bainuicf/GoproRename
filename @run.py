'''
@文件    :goprorename.py
@说明    :
@时间    :2022/06/11 14:06:34
@作者    :ShellC
@版本    :1.0
'''
from importlib.resources import path
import os
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 定义前缀
PRE= "gopro_"
# 定义gopro系统生成的所有文件格式
FILE_TYPE=[".lrv", ".mp4"]

# 重命名函数：输入参数为当前目录，执行成功返回true。
def reName(path):
    # 获取当前目录所有文件名，存入列表
    fileNames= os.listdir(path)
    for fileName in fileNames:
        # 获取文件扩展名
        type= os.path.splitext(fileName)[-1].lower()
        # 判断是否为gopro文件格式，如果是则进行处理
        if type in FILE_TYPE:
            # 通过前缀判断是否已做过更名处理，如已处理则跳过，否则重命名
            sign= fileName[0:6]            
            if sign != PRE:
                # 重命名规则
                newName= PRE+ fileName[0:2]+ fileName[4:8]+ fileName[2:4]+ fileName[8:]
                os.rename(fileName, newName)
    return True

if __name__ == '__main__':
    # 获取当前目录
    path= os.getcwd()       
    # 执行重命名
    reName(path)    



    
