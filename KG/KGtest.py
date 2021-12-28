# -*- coding: GBK -*-
import os
import chardet
#�ַ�����ָ��λ��ƴ��
def Str_Insert(s, pos, str_add):
    str_list = list(s)    # �ַ���תlist
    str_list.insert(pos, str_add)  # ��ָ��λ�ò����ַ���
    str_out = ''.join(str_list)    # ���ַ�����
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
    if bool:        #R���������Ŀ¼
        start_index = r.index(start)
        end_index = start_index + 27
        R = Str_Insert(r, end_index, layer)
    else:
        r_addyear = Creat_Year(year,r)
        array.append(year)
        R = Str_Insert(r_addyear, 30, layer)
    return R,array

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
        if i == "":
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
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def is_title(stra):
    if len(stra) >= 3:
        return is_number(stra[0]) and stra[1] == "." or is_number(stra[1]) and is_number(stra[2]) or stra[2] == "."
    else:
        return False


f = open("Result1.txt","r",encoding='UTF-8-sig')#���д��encoding='UTF-8')�ڶ�ȡ�ļ��Ŀ�ͷ�����һ��\ufeff��ԭ������ԭtxt�ļ�û��ָ��utf-8���룬�����ļ�ʱ����������׺���뵼�µ�
lista=[]
line = f.readline()
lista.append(line.split())
#�ȶ��ļ�������list��
while line:
    line = f.readline()  #��ȡһ���ļ����������з�
    lista.append(line.split())
f.close() #�ر��ļ�
lista = lista [:-1]
#list�а���������ʽ������
#���кͼ���ʵʩ�ı�׼����ݵ�λ�������
#������ͷ�ֹ�ı�׼û����ݵ�λ�������
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
        Dlist.append(draft)     #Dlist����ݵ�λ�ķָ���

        drafter=drafter[:-1]
        # drafter = drafter.split(",")
        # dlist.append(drafter)   #dlist������˵ķָ���

    elif len(i)<=10:
        status, GBT, number, release_date, implementation_date, China_num, international_num, belong_unit, executive_unit, administration = i

    n,year = number.split("-")  #��׼��-��� �ָ�
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
    # for j in drafter:       #����˵�ƴ��Ŀǰ���ò�������һ�׶ν�������������µ���info����
    #     d = "\"U@" + j + "\" : {" + rels + "}"
    #     print(d)


# listb=File_Name('D:\���߰���\Learn space\����֪ʶͼ��\�ı��ļ�')#���ص��ǰ�������txt�ļ���list
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
#         if "����" in i :
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

