# -*- coding : utf-8 -*-
# @time   : 2019-08-06 22:39
# @Author : Zhicong Hu
# @Studid : 29489636

import re
import pandas as pd

grant_id=[]
patent_title=[]
kind=[]
number_of_claims=[]
inventors=[]
citations_applicant_count=[]
citations_examnier_count=[]
claim_text=[]
abstract=[]

inFile=open("sample_input.txt","r")
outFile=open("CodeTestResult.txt","w+")
para=re.findall("(?:<us-patent-grant.*?)(?:file=\")(.*?)(?:</us-patent-grant)",inFile.read(),re.S)
for i in para:
    #retrive patentid
    tmpGrantId = re.findall("(.*?)(?:-\w+.XML.*?)", i, re.M)
    grant_id.append(tmpGrantId[0])


    #retrieve patent_title
    tmpPatentTitle=re.findall('(?:<invention-title id=.*?>)(.*?)(?:</invention-title>)',i,re.S)
    patent_title.append(tmpPatentTitle[0])


    #retrieve kind
    tmpKind=re.findall('(?:<doc-number>{0}.*?)(?:</doc-number>.*?)(?:<kind>)(.*?)(?:</kind>)'.format(tmpGrantId[0][2:]),i,re.S)
    kind.append(tmpKind[0])



    #retrieve number of claims

    tmpNumOfClaim=re.findall('(?:<number-of-claims>)(.*?)(?:</number-of-claims>)',i,re.S)
    number_of_claims.append(tmpNumOfClaim[0])



    #retrieve inventors
    tmpInventorsLname=re.findall("(?:<inventor)(?:.*?)(?:<last-name>)(.*?)(?:</last-name>)(?:.*?)(?:</inventor>)",i,re.S)
    tmpInventorsFname = re.findall("(?:<inventor)(?:.*?)(?:<first-name>)(.*?)(?:</first-name>)(?:.*?)(?:</inventor>)",i,re.S)
    tmpInventorList=''
    for j in range(len(tmpInventorsLname)):
        if j+1==len(tmpInventorsLname):
            nameStr=tmpInventorsFname[j]+' '+tmpInventorsLname[j]
        else:
            nameStr = tmpInventorsFname[j] + ' ' + tmpInventorsLname[j]+","
        tmpInventorList=tmpInventorList+nameStr
    inventors.append(tmpInventorList)

    #retrive citations applicant count and examiner count
    tmpApplicantCitation=re.findall("(cited by applicant)",i)
    tmpExaminerCitation=re.findall("(cited by examiner)",i)
    citations_applicant_count.append(len(tmpApplicantCitation))
    citations_examnier_count.append(len(tmpExaminerCitation))


    #retrieve claim text
    tmpClaimText1=re.findall("(?:<claim-text>)(.*?)(?:</claim-text>)",i,re.S)
    for l in range(len(tmpClaimText1)):
        tmpClaimText1[l]=re.sub('<claim-text>',' ',tmpClaimText1[l])
        tmpClaimText1[l] = re.sub('<.*?claim-ref.*?>', ' ', tmpClaimText1[l])
        tmpClaimText1[l] = re.sub('<.*?>', ' ', tmpClaimText1[l])
        tmpClaimText1[l] = re.sub('\n', '', tmpClaimText1[l])
        tmpClaimText1[l] = re.sub('  ', ' ', tmpClaimText1[l])
        tmpClaimText1[l] = re.sub(' ; , (?:\w)', '. ', tmpClaimText1[l])


    ClaimStr=''
    for m in tmpClaimText1:
        ClaimStr+=m
    claim_text.append(ClaimStr)

    #finally retrieve abstract text
    tmpAbstract=re.findall("(?:<abstract.*?>\n<p .*?>)(.*?)(?:</abstract>)",i,re.S)
    for n in range(len(tmpAbstract)):
        tmpAbstract[n]=re.sub("</p>",'',tmpAbstract[n])
        tmpAbstract[n] = re.sub("<.*?claim-ref.*?>", ' ', tmpAbstract[n])
        tmpAbstract[n] = re.sub("<.*?>", ' ', tmpAbstract[n])
        tmpAbstract[n] = re.sub("\n", '', tmpAbstract[n])
        tmpAbstract[n] = re.sub("  ", ' ', tmpAbstract[n])
        tmpAbstract[n] = re.sub(" ; , (?:\w)", ' ', tmpAbstract[n])
    AbsStr=''
    for n in tmpAbstract:
        AbsStr+=n
    abstract.append(AbsStr)
'''
print(len(grant_id))
print(len(patent_title))
print(len(kind))
print(len(number_of_claims))
print(len(inventors))
print(len(citations_applicant_count))
print(len(citations_examnier_count))
print(len(claim_text))
print(len(abstract))
'''

inFile.close()

column=['grant_id','patent_title','kind','number_of_claims'
,'inventors','citations_applicant_count','citations_examiner_count','claims_text','abstract']

df=pd.DataFrame([grant_id,patent_title,kind,number_of_claims,inventors
                ,citations_applicant_count,citations_examnier_count,
                claim_text,abstract])
df=df.T
outFile.close()
df.columns=column
df.to_csv(path_or_buf="./CodeTestResult.txt",index=False,na_rep="NA")


