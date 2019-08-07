# -*- coding : utf-8 -*-
# @time   : 2019-08-06 12:46
# @Author : Zhicong Hu
# @Studid : 29489636

import re



#grab the unique patent id
inFile=open("sample_input.txt","r")
grant_id=re.findall("(?:<us-patent-grant.*?file=\")(.*?)(?:-.*?)",inFile.read(),re.M)
inFile.close()

patentTitle=[]


#grab the content of each paragraph by patent id
inFile=open("sample_input.txt","r")

for i in grant_id:
    inFile = open("sample_input.txt", "r")
    print(i)
    para=re.findall("(?:<us-patent-grant.*?)(?:file=\"{0})(.*?)(?:</us-patent-grant)".format(i),inFile.read(),re.S)

    #retrieve patent_title
    tmpPatentTitle=re.findall('(?:<invention-title id=.*?>)(.*?)(?:</invention-title>)',para[0])
    print((tmpPatentTitle))
    patentTitle.append(tmpPatentTitle)


    #retrieve kind

    inFile.close()


#只是个测试文件，看outPutCsv2.py


#confirm by writer2
