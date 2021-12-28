# 存放相关映射
from operator import mul, add

# 前缀-标签映射字典
PREFIX_LABEL_MAP = {
    'Y': "Year",     # 年份
    # 'C': "Catalog",  # 目录
    # 'I': "Index",    # 指标
    # 'A': "Area"      # 地区/机场/公司集团
    'N': "StandardNumber",       #标准号
    'C': "CCS",                  #中国标准分类号
    'I': "ICS",                  #国际标准分类号
    'U': "Unit",                 #归口单位
    'E': "Executive",            #执行单位
    'A': "Administration",       #主管部门
    'D': "Draft",                #起草单位
    'd': "drafter",              #起草人
    'T': "Term"                  #术语和定义
}
# 前缀-结构关系映射字典
# PREFIX_S_REL_MAP = {'Y-C': "include", 'C-I': "include", 'I-I': "contain",
#                     'I-A': "locate", 'A-A': "contain"}
PREFIX_S_REL_MAP = {'Y@N': "包含",'N@C': "拥有", 'N@I': "拥有", 'N@U': "归属",
                    'E@N': "执行",'N@E': "被执行",
                    'A@N': "管理", 'N@A': "被管理",
                    'N@D': "被起草",'D@N': "起草",
                    'd@N': "起草",
                    'N@T': "具有"}
# 前缀-值关系映射字典
# PREFIX_V_REL_MAP = {'Y-C': "info", 'Y-I': "value", 'Y-A': None}
PREFIX_V_REL_MAP = {'Y@N': "info", 'Y@C': None, 'N@C': None, 'N@I': None, 'N@U': None, 'E@N': None, 'N@A': None, 'D@N': None, 'd@N': None, 'N@A': None, 'N@T': None}

# 数字字符映射
Char2CharDigit = {'零': '0', '一': '1', '二': '2', '三': '3', '四': '4', '五': '5',
                  '六': '6', '七': '7', '八': '8', '九': '9', '两': '2', '千': '', '十': ''}
Char2Digit = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
              '六': 6, '七': 7, '八': 8, '九': 9, '两': 2, '千': 0, '十': 10,
              '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 10}
# 指代字符映射
Ref2Digit = {'去': -1, '上': -1, '前': -2, '大': -1}


def map_digits(year: str) -> str:
    new_year = year
    # 替换
    for k, v in Char2CharDigit.items():
        new_year = new_year.replace(k, v)
    # 填充
    if len(new_year) == 2:
        new_year = '20' + new_year
    return new_year


def map_refs(year: str, num: int, base_year: int) -> str:
    n = 0
    map_dict = Ref2Digit
    operator = add
    if num in (2, 3):
        n = -1 if num == 2 else 1
        map_dict = Char2Digit
        operator = mul

    for ch in year:
        d = map_dict.get(ch)
        if d:
            n = operator(n, d)
    if num == 3:
        return ','.join([str(base_year - i) for i in range(1, n + 1)])
    else:
        return str(base_year + n)
