# -*- coding: GBK -*-
import os
import chardet
import json

#������ȡ��׼�ĵ�txt
def File_Name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                L.append(os.path.join(root , file))
        return L

#���ݱ�׼�ĵ�txt��ȡÿһ��txt������
def Read_Txt(strj):
    listtxt=[]
    try:
        f = open(strj, 'rb')
        r = f.read()
        # ��ȡ�ı��ı��뷽ʽ
        f_charInfo = chardet.detect(r)
        # print(f_charInfo)  # ����ı���ʽ��Ϣ
        c=r.decode(f_charInfo['encoding'])
        listtxt = (c.replace("\r", "").split("\n\n"))
        f.close()
    except Exception as err:
        print(err)
        if f:
            f.close()
    return listtxt

#���ص�һҳ�����һ����list�е��±�
def Last_Line_Index(list):
    for i in list:
        if i == "\n\n":
            break
    return list.index(i)

#���غ����׼�еı�׼��
def Find_GBT_Num(stra):
    lista = stra.split()
    resultstr = lista[0] + " " + lista[1]
    return resultstr

#�ж�һ��unicode�Ƿ�������"
def is_number(uchar):
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False
def is_float(num):
    """
    �ж��û�������Ƿ�ΪС��������
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
    """�ж�һ��unicode�Ƿ��Ǻ���"""
    if uchar >= u'\u3400' and uchar <= u'\u9fa5':
        return True
    else:
        return False
def is_title(stra):
    if len(stra) >= 3:
        return is_number(stra[0]) and is_number(stra[-1]) and ("." in stra)
    else:
        return False

#��ȡjson�ļ��ж�Ӧ��׼������
def Find_Jsondata(json_data, strGBT):
    try:
        return json_data[strGBT]
    except KeyError as err:
        return err

def dict_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

#���������𿪳���Ӣ�ĺ���д
def Term_Analysis(strt):
    for i in range(len(strt)):
        if is_chinese(strt[i]) and not is_chinese(strt[i+1]):
            Cname = strt[:i+1]
            Ename = strt[i+1:]
            if  Ename[0] == ' ':
                Ename = Ename[1:]
            if '��' in Ename:
                tempindex = Ename.index('��')
                abb =Ename[tempindex+1:]
                Ename = Ename[:tempindex]
            else:
                abb = False
            break
    return Cname,Ename,abb

#�༭���ͽ��ֵ䣬���շ��ص��ǿ�ֱ����ӵ�json���ֵ�
def Write_To_Json(strvalue,Cname,abb):
    tempdict = {'attrs': None}
    if abb:
        explaindict = {'Chinesename': Cname, 'abbreviation': abb, 'explain': strvalue}
    else:
        explaindict = {'Chinesename': Cname, 'abbreviation': None, 'explain': strvalue}
    tempdict['attrs'] = explaindict
    dicta[strkey] = tempdict
    return dicta

with open('.\data\htdata.json','r',encoding='gbk')as fp:#��htdata����ȡ������gbk������ʱ��utf-8
    json_data = json.load(fp)
    # print('�����ļ��е�json���ݣ�',json_data)

listb=File_Name('D:\���߰���\Learn space\����֪ʶͼ��\���ﲿ��')#���ص��ǰ�������txt�ļ���list
for j in listb:
    GBT_num = "N@GB/T " + Find_GBT_Num(j.split("\\")[-1])[4:]
    temp = Read_Txt(j)
    k = len(temp)
    dicta = {}
    for i in temp[1:]:
        count = 0
        if "����" in i :
            titlelist = i.split("\n")
            while count < len(titlelist):
                try:
                    if is_title(titlelist[count]):
                        count += 1
                        Chinesename,Englishname,abbreviation = Term_Analysis(titlelist[count])
                        strkey = "T@" + Englishname
                        strvalue = ""
                        while not is_title(titlelist[count+1]) and "������" not in titlelist[count+1]:
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
        print(GBT_num)#�������û����htdata���ҵ��ı�׼��
# print(json_data)
json_str = json.dumps(json_data,default = dict_default, indent=4, ensure_ascii=False)
with open('.\data\htdata_shuyu_1.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)