# -*- coding: utf-8 -*-
"""
Description: 比较两个txt文件的不同之处
Environment: 默认的python3即可
Example:     终端输入 python diftest.py xxx.txt xxx.txt > diftest.html
			 然后浏览器打开html文件，可以找到不同之处
Author:      syf
Date:        2020.4.1
"""


import difflib		# 文本之间的差异库
import sys			# 系统强烈交互库

''' 设置在终端输入参数 '''
try:
    file1=sys.argv[1]           #第一个参数文件
    file2=sys.argv[2]           #第二个参数文件
except Exception as e:
    print ("Error: " + str(e))
    sys.exit()
	
	
def readfile(filename):             
    """ 读取个文件的函数
    parameter:
        filename:要读取的文件
    return:
        text:读取出来的字符串
    example:
		file1_lines=readfile(file1)
    """
    try:                        #检测异常
        df=open(filename,encoding='utf-8')              #打开文件
        text=df.read().splitlines(keepends=True)         #读取文件内容，并根据行进行分割
        df.close()                          #关闭文件
        return text                         #返回文件内容字符串
    except IOError as e:                           #抛出异常
        print ("ERROR: " + str(e))
        sys.exit()
		
''' 判断文件内容是否为空 '''		
if file1=="" or file2=="":
    print ("please input filename and filename")
    sys.exit()
	
''' 分别读取两个文件 '''
file1_lines=readfile(file1)
file2_lines=readfile(file2)


''' 测试代码，直接用路径获取目标文件 '''
# filename1 = 'C:/Users/gzsyf/Desktop/ip.py'
# filename2 = 'C:/Users/gzsyf/Desktop/ip.py'
# with open(filename1) as f1 , open(filename2) as f2:
	# file1_lines = f1.read().splitlines(keepends=True)
	# file2_lines = f2.read().splitlines(keepends=True)
	
''' 创建HtmlDiff类对象 '''
diff=difflib.HtmlDiff()                

''' 测试代码 '''
# result = diff.make_file(file1_lines,file2_lines)
# with open('diff.html','w') as f:
	# f.write(result)
	
print (diff.make_file(file1_lines,file2_lines))

"""Reference
[1] https://www.cnblogs.com/biaopei/p/7730530.html
[2] https://blog.csdn.net/Aplox/article/details/103834638?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param
"""