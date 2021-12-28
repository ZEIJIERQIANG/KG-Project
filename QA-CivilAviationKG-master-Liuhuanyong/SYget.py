# -*- coding: GBK -*-
import os
import chardet
import json

#批量获取标准文档txt
def File_Name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                L.append(os.path.join(root , file))
        return L

#根据标准文档txt获取每一个txt的内容
def Read_Txt(strj):
    listtxt=[]
    try:
        f = open(strj, 'rb')
        r = f.read()
        # 获取文本的编码方式
        f_charInfo = chardet.detect(r)
        # print(f_charInfo)  # 输出文本格式信息
        c=r.decode(f_charInfo['encoding'])
        listtxt = (c.replace("\r", "").split("\n\n"))
        f.close()
    except Exception as err:
        print(err)
        if f:
            f.close()
    return listtxt

#返回第一页的最后一行在list中的下标
def Last_Line_Index(list):
    for i in list:
        if i == "\n\n":
            break
    return list.index(i)

#返回航天标准中的标准号
def Find_GBT_Num(stra):
    lista = stra.split()
    resultstr = lista[0] + " " + lista[1]
    return resultstr

#判断一个unicode是否是数字"
def is_number(uchar):
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False
def is_float(num):
    """
    判断用户输入的是否为小数或整数
    :param num: str
    :return: bool
    """
    if (num.startswith("-") and num[1:].isdigit()) or num.isdigit():
        return True
    elif num.count(".") == 1 and not num.startswith(".") and not num.endswith("."):
        li = num.split(".")
        if li[0].startswith("-"):
            if li[0][1:].isdigit() and li[1].isdigit():
                return True
            else:
                return False
        else:
            if li[0].isdigit() and li[1].isdigit():
                return True
            else:
                return False
    else:
        return False
def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u3400' and uchar <= u'\u9fa5':
        return True
    else:
        return False
def is_title(stra):
    if len(stra) >= 3:
        return is_number(stra[0]) and is_number(stra[-1]) and ("." in stra)
    else:
        return False

#获取json文件中对应标准的数据
def Find_Jsondata(json_data, strGBT):
    try:
        return json_data[strGBT]
    except KeyError as err:
        return err

def dict_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

#把术语标题拆开成中英文和缩写
def Term_Analysis(strt):
    for i in range(len(strt)):
        if is_chinese(strt[i]) and not is_chinese(strt[i+1]):
            Cname = strt[:i+1]
            Ename = strt[i+1:]
            if  Ename[0] == ' ':
                Ename = Ename[1:]
            if '；' in Ename:
                tempindex = Ename.index('；')
                abb =Ename[tempindex+1:]
                Ename = Ename[:tempindex]
            else:
                abb = False
            break
    return Cname,Ename,abb

#编辑解释进字典，最终返回的是可直接添加到json的字典
def Write_To_Json(strvalue,Cname,abb):
    tempdict = {'attrs': None}
    if abb:
        explaindict = {'Chinesename': Cname, 'abbreviation': abb, 'explain': strvalue}
    else:
        explaindict = {'Chinesename': Cname, 'abbreviation': None, 'explain': strvalue}
    tempdict['attrs'] = explaindict
    dicta[strkey] = tempdict
    return dicta

with open('.\data\htdata.json','r',encoding='gbk')as fp:#从htdata中提取数据用gbk，其他时候utf-8
    json_data = json.load(fp)
    # print('这是文件中的json数据：',json_data)

listb=File_Name('D:\乱七八糟\Learn space\航天知识图谱\术语部分')#返回的是包含所有txt文件的list
for j in listb:
    GBT_num = "N@GB/T " + Find_GBT_Num(j.split("\\")[-1])[4:]
    temp = Read_Txt(j)
    k = len(temp)
    dicta = {}
    for i in temp[1:]:
        count = 0
        if "术语" in i :
            titlelist = i.split("\n")
            while count < len(titlelist):
                try:
                    if is_title(titlelist[count]):
                        count += 1
                        Chinesename,Englishname,abbreviation = Term_Analysis(titlelist[count])
                        strkey = "T@" + Englishname
                        strvalue = ""
                        while not is_title(titlelist[count+1]) and "缩略语" not in titlelist[count+1]:
                            count += 1
                            strvalue = strvalue + titlelist[count]
                        dicta = Write_To_Json(strvalue, Chinesename, abbreviation)
                    else:
                        count+=1
                except IndexError:
                    dicta = Write_To_Json(strvalue, Chinesename, abbreviation)
                    break
    try :
        Find_Jsondata(json_data, GBT_num)["next"].update(dicta)
    except:
        print(GBT_num)#输出的是没有在htdata中找到的标准号
# print(json_data)
json_str = json.dumps(json_data,default = dict_default, indent=4, ensure_ascii=False)
with open('.\data\htdata_shuyu_1.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)