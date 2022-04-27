str1=input('请输入字符串：')
str2=str1[-1::-1]
if str2==str1:
    print('%s是回文数'%str1)
else:
    print('%s不是回文数'%str1)
