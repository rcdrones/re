import re


def my_fun():
    global  p1,key
    pattern1 = re.compile(p1)
    print(pattern1.findall(key))
    

##a = 'nihao\nnihao'
##print(a)
##
##
##
##k = r"nihao\tnihao"  # r = raw
##print(k)

##
##key = r"<h1>n<h1>"
##p1 = r"<h1>.<h1>"   # . 表示任意一个字符，必须要有才符合
##pattern1 = re.compile (p1)
##print(pattern1.findall (key))
####
####
##key = r"<h1><h1>"
##p1 = r"<h1>.<h1>"  # . 表示任意一个字符，必须要有才符合
##pattern1 = re.compile(p1)
##print(pattern1.findall(key)) #return null
####
#key = r"<h1>nihao<h1>"
##p1 = r"<h1>.<h1>"
##pattern1 = re.compile(p1)
##print(pattern1.findall(key)) # return null
##
##
##key = r"<h1>nihao<h1>"
##p1 = r"<h1>.+>"                 # + 表示重复出现1次到多次
##pattern1 = re.compile(p1)
##print(pattern1.findall(key))


##key = r"<h1>2333<h1>"
##p1 = r"<h1>2333.+<h1>"                 # + 表示重复出现1次到多次
##pattern1 = re.compile(p1)
##print(pattern1.findall(key))        #return null
##
##
##
##key = r"<h1><h1>"
##p1 = r"<h1>.*<h1>"                 # *表示重复0次到多次
##pattern1 = re.compile(p1)
##print(pattern1.findall(key)) 


##key = r"11dfds111rcdrones@gmail.com888fgfd"
##p1 = r"rcdrones@gmail\.c.+m"
##pattern1 = re.compile(p1)
##print(pattern1.findall (key))
##
##
##key = r"11dfds111rcdrones@gmail.cm888fgfd"
##p1 = r"rcdrones@gmail\.c.+m"  # cm 和com 没有匹配到
##pattern1 = re.compile(p1)
##print(pattern1.findall (key))


##
##key = r"http://163.com      https://sina.com"
##p1 = r"https*"    # s是匹配条件，  *号表示重复0次到无数次
##pattern1 = re.compile(p1)
##print(pattern1.findall (key))
##
##
##key = r"http://163.com      httpsss://sina.com"
##p1 = r"https*"    # s是匹配条件，  *号表示重复0次到无数次
##pattern1 = re.compile(p1)
##print(pattern1.findall (key))

###----------------------------------------------------
##key = r"http://163.com111mmmm"
##p1 = r"https*.*m"    # m是匹配条件， 默认是贪婪匹配整个字符串到末尾
##pattern1 = re.compile(p1)
##print(pattern1.findall (key))
##
##
##key = r"http://163.com111mmmm"
##p1 = r"https*.*?m"    # ? 是管理后面的匹配条件，一旦匹配就结束
##pattern1 = re.compile(p1)
##print(pattern1.findall (key))
###-------------------------------------------


##key = r"http://163.com111       https://sina.com"
##p1 = r"https*.*?m"    # m是匹配条件， 默认是贪婪匹配整个字符串到末尾
##pattern1 = re.compile(p1)
##print(pattern1.findall (key))
##a = pattern1.findall (key)
##print(type(a))
##print(len(a))
##
##for i in a:
##    print(i)


##key = "<wTml>nihao<HtmL>"
##p1 = "<[hH][Tt][Mm][Ll]>.*<[hH][Tt][Mm][Ll]>"
##pattern1 = re.compile(p1)
##print(pattern1.findall(key))

##
##key = "@cat11hat11qat11"
##p1 = "@.+?at"
##pattern1 = re.compile(p1)
##print(pattern1.findall(key))





##key = "@cat11hat11qat11"
##p1 = "@.+?at"
##my_fun()


##key = "cat hat qat"
##p1 = "[^q]at"   # 表示非q字符都做匹配！
##my_fun()

##
##key = "sa and  saas ans saaaaaaas"
##p1 = "sa{1,2}"
##my_fun()



key = r"Smart UPS Ver2.0,V512,B2222,O333,C45"
##p1 = r"Ver\d.\d"
p1 = r"(?<=V)\d+"
##p1 = r"B\d+"
##p1 = r"O\d+"
##p1 = r"C\d+"
pattern1 = re.compile(p1)
match1 = re.search(pattern1 , key)
print(1+int(match1.group(0)))




##              总结：
##                             前序条件               .           表示任意字符匹配1次
##                                                         a、b、c        表示特定字符重复匹配1次       
##                                                    附加条件                   +      表示  前序条件符合1次到多次
##                                                                                         *       表示  前序条件符合0次到多次
##                                                                                        {a,b} 表示前序条件符合a次到b次
##             
##                           后续条件      xxx    a、b、c   表示贪婪的匹配最后一个特定字符
##                                                  附加条件                     ?a    表示 后续a第一次出现，就结束匹配
##
##                          通用条件        [abc]               表示abc里面自动匹配1个字符
##                                                   [^a]                表示非a 都做匹配
##                                                      \d                   表示数字
##                                                  ()                      表示一个子表达式
##                                                      \1 \2 \3       表示子表达式在后面的动态引用
##
##    
##
##           快捷键：    alt+3   框选增加 #            alt+4 是取消#
##
##


##key = r"192.168.1.56"
###p1 = "\d+.*\d+"
##
##p1 = r"\d{1,3}\..+\d"
##my_fun()




##
##key = r"<html><body><h1>nihao abc</h1></body></html>"
##p1 = r"(?<=<h1>).+?(?=</h1>)"
##pattern1 = re.compile(p1)
##match1 = re.search(pattern1 , key)
##print(match1.group(0))




##
##key = r"<html><body><h1>nihao abc</h1></body></html>"
##p1 = r"<h1>.+?</h1>"
##pattern1 = re.compile(p1)
##match1 = re.search(pattern1 , key)
##print(match1.group(0))


##
##key = r"<html><body><h1>nihao abc</h3></body></html>"
##p1 = r"<h[1-6]>.+?</h[1-6]>"
##pattern1 = re.compile(p1)
##match1 = re.search(pattern1 , key)
##print(match1.group(0))
##
##
##key = r"<html><body><h1>nihao abc</h1></body></html>"
##p1 = r"<(h)([1-6])>.+?</\1\2>"             
##pattern1 = re.compile(p1)
##match1 = re.search(pattern1 , key)
##print(match1.group(0))




