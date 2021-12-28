# -*- coding: GBK -*-
import os
import chardet
#字符串在指定位置拼接
def Str_Insert(s, pos, str_add):
    str_list = list(s)    # 字符串转list
    str_list.insert(pos, str_add)  # 在指定位置插入字符串
    str_out = ''.join(str_list)    # 空字符连接
    return  str_out

def Creat_Year (year,r):

    new_year = "\"Y@" + year + "\" : {\n\t" + "\"attrs\" : {},\n},"
    R = Str_Insert(r, 0, new_year)
    return R
def Find_Year(year,array):
    result = year in array
    return result
def Processing_Layers(year,bool,array,layer,r):
    start = "Y@" + year
    if bool:        #R中已有年份目录
        start_index = r.index(start)
        end_index = start_index + 27
        R = Str_Insert(r, end_index, layer)
    else:
        r_addyear = Creat_Year(year,r)
        array.append(year)
        R = Str_Insert(r_addyear, 30, layer)
    return R,array

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
        if i == "":
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
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def is_title(stra):
    if len(stra) >= 3:
        return is_number(stra[0]) and stra[1] == "." or is_number(stra[1]) and is_number(stra[2]) or stra[2] == "."
    else:
        return False


f = open("Result1.txt","r",encoding='UTF-8-sig')#如果写成encoding='UTF-8')在读取文件的开头会出现一个\ufeff，原因在于原txt文件没有指定utf-8编码，而读文件时改了其他后缀编码导致的
lista=[]
line = f.readline()
lista.append(line.split())
#先读文件，读到list里
while line:
    line = f.readline()  #读取一行文件，包括换行符
    lista.append(line.split())
f.close() #关闭文件
lista = lista [:-1]
#list中包含两种形式的数据
#现行和即将实施的标准有起草单位和起草人
#被代替和废止的标准没有起草单位和起草人
Dlist = []
dlist = []
rels = "\"rels\" : {}"
attrs = "\"attrs\" : {}"
next = "\"next\" : {}"
info = "\"info\" : {}"
for i in lista:
    draft = []
    drafter = ""
    if len(i)>=11:
        status, GBT, number, start_time, end_time, China_num, international_num, belong_unit, executive_unit, administration, draft, drafter = i
        draft=draft[:-1]
        draft=draft.split(",")
        Dlist.append(draft)     #Dlist是起草单位的分割结果

        drafter=drafter[:-1]
        # drafter = drafter.split(",")
        # dlist.append(drafter)   #dlist是起草人的分割结果

    elif len(i)<=10:
        status, GBT, number, release_date, implementation_date, China_num, international_num, belong_unit, executive_unit, administration = i

    n,year = number.split("-")  #标准号-年份 分割
    technical_term=""
    inherit=""
    # Y = "\"Y@" + year + "\": {" + attrs + "}"
    N = "\"N@" + GBT + " " + n + "-" + year + "\": {\n\t\t\"attrs\": {\n\t\t\t\"release_date\": \"" + start_time + "\",\n\t\t\t\"implementation_date\": \"" + end_time + "\",\n\t\t\t\"status\": \"" + status + "\",\n\t\t\t\"inherit\": \"" + inherit + "\",\n\t\t\t\"technical_term\": \"" + technical_term + "\",\n\t\t\t\"drafter\": \"" + drafter + "\"\n\t\t}"
    C = "\"C@" + China_num + "\": {" + rels + "}"
    I = "\"I@" + international_num + "\": {" + rels + "}"
    U = "\"U@" + belong_unit + "\": {" + rels + "}"
    E = "\"E@" + executive_unit + "\": {" + rels + "}"
    A = "\"A@" + administration + "\": {" + rels + "}"

    D=""
    R=""
    for index, j in enumerate(draft):
        if index ==len(draft) - 1:
            D = D + "\t\"D@" + j + "\": {" + rels + "}"
        else :
            D = D + "\t\"D@" + j + "\": {" + rels + "},\n" + "\t\t"
    # print(D)
    if D:
        first_layer = "\t\"next\": {\n\t\t\t" + C + ",\n\t\t\t" + I + ",\n\t\t\t" + U + ",\n\t\t\t" + E + ",\n\t\t\t" + A + ",\n\t\t" + D + "\n\t\t}"
    else:
        first_layer = "\t\"next\": {\n\t\t\t" + C + ",\n\t\t\t" + I + ",\n\t\t\t" + U + ",\n\t\t\t" + E + ",\n\t\t\t" + A + "\n\t\t}"
    seconde_layer = "\t" + N + ",\n\t" + first_layer + "\n\t},"
    print(seconde_layer)
    # for j in drafter:       #起草人的拼接目前还用不到，第一阶段将起草人整个留下当做info保存
    #     d = "\"U@" + j + "\" : {" + rels + "}"
    #     print(d)


# listb=File_Name('D:\乱七八糟\Learn space\航天知识图谱\文本文件')#返回的是包含所有txt文件的list
# sylist = []
# cache = []
# for j in listb:
#     print("-----------------------------------------------------------------------------------------------------------")
#     GBT_num = Find_GBT_Num(j.split("\\")[-1])
#     # print(GBT_num)
#     temp = Read_Txt(j)
#     k=Last_Line_Index(temp)+1
#     count = 0
#     GBTnum_definitions = []
#     for i in temp[1:]:
#         if "术语" in i :
#             # print(i)
#             titlelist = i.split("\n")
#             while count < len(titlelist):
#                 try:
#                     if is_title(titlelist[count]):
#                         cache = []
#                         count += 1
#                         cache.append(GBT_num)
#                         cache.append(titlelist[count])
#                         while not is_title(titlelist[count+1]):
#                             count += 1
#                             cache.append(titlelist[count])
#                         sylist.append(cache)
#                     else:
#                         sylist.append(cache)
#                         count+=1
#                 except IndexError:
#                     break

