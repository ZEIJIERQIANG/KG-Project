import requests
import urllib.request

def Replace_Space(str):
    str_result = str.replace("\t", "")
    str_result = str_result.replace("\r", "")
    str_result = str_result.replace("\n","")
    return str_result

def Str_Cut(str1,begin,end):
    try:
        if begin == 0:
            str_cut_result = str1[:str1.index(end)]
        elif end == 0:
            str_cut_result = str1[str1.index(begin):]
        elif type(begin) is int:
            str_cut_result = str1[begin:str1.index(end)]
        elif type(end) is int:
            str_cut_result = str1[str1.index(begin):end]
        else:
            str_cut_result=str1[str1.index(begin):str1.index(end)]
    except ValueError:
        str_cut_result='No string exists'
    return str_cut_result

Basic_Information1='<div class="basic-info cmn-clearfix">'
BI1_str0='标准号'
BI1_str1='中国标准分类号'
BI1_str2='国际标准分类号'
BI1_str3='发布日期'
BI1_str4='实施日期'
BI1_str5='归口单位'
BI1_str6='执行单位'
BI1_str7='起草单位'
BI1_str8='主管部门'
BI1_str9='起草人'
BI1_str10='相近标准'

url_list = [
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CE9C983E05397BE0A0AED11",#1
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CEBC983E05397BE0A0AED11",#2
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CECC983E05397BE0A0AED11",#3
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CEDC983E05397BE0A0AED11",#4
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CEEC983E05397BE0A0AED11",#5
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CEFC983E05397BE0A0AED11",#6
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CF0C983E05397BE0A0AED11",#7
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CF1C983E05397BE0A0AED11",#8
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CF2C983E05397BE0A0AED11",#9
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CF3C983E05397BE0A0AED11",#10
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CF4C983E05397BE0A0AED11",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542C3CC983E05397BE0A0AED11",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542C3DC983E05397BE0A0AED11",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542C40C983E05397BE0A0AED11",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CE2C983E05397BE0A0AED11",#15
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=C3386C490C828B79E05397BE0A0AC288",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=C3386C490BC68B79E05397BE0A0AC288",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B691BB7786C0D126E05397BE0A0AF3B3",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B691BB778686D126E05397BE0A0AF3B3",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C2F21CB3E05397BE0A0A92D0",#20
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C2F41CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C2F51CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C2F61CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C3DB1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C3081CB3E05397BE0A0A92D0",#25
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C3EA1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C30E1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C3ED1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C3EF1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C3F01CB3E05397BE0A0A92D0",#30
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C3F21CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C4181CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C41B1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C41C1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C4351CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C4361CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C4371CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C4381CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C4391CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C43A1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C43B1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C43C1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C43D1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C43E1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C2E11CB3E05397BE0A0A92D0",#45
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C2E41CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C2E81CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C2EA1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B4C25880C2EB1CB3E05397BE0A0A92D0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B13990C15C3E5DDAE05397BE0A0A0D35",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=B13990C15C3F5DDAE05397BE0A0A0D35",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0FC3F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0FD3F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0FE3F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0D13F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0D23F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0D33F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0F93F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0FA3F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0FB3F2EE05397BE0A0A6C0B",#60
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0973F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0983F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0CE3F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0CF3F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0D03F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E08E3F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E08F3F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0903F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=AB005698E0913F2EE05397BE0A0A6C0B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=A73D6262FE0072E3E05397BE0A0A6CEB",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=A73D6262FEBD72E3E05397BE0A0A6CEB",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=A73D6262FEBE72E3E05397BE0A0A6CEB",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=A73D6262FEBF72E3E05397BE0A0A6CEB",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=A73D6262FEC072E3E05397BE0A0A6CEB",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=A47A713B763B14ABE05397BE0A0ABB25",#75
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=A24AF19F40E85C2EE05397BE0A0A5E0D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=A24AF19F40CF5C2EE05397BE0A0A5E0D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=9BFCCC5CED700F87E05397BE0A0A747C",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=9BFCCC5CED710F87E05397BE0A0A747C",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=9BFCCC5CED720F87E05397BE0A0A747C",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=996A838ABFAC8372E05397BE0A0AD949",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=996A838ABFFE8372E05397BE0A0AD949",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=996A838AC0008372E05397BE0A0AD949",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=996A838AC0088372E05397BE0A0AD949",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C5DD4F2CE05397BE0A0AB3E0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C5F64F2CE05397BE0A0AB3E0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C59C4F2CE05397BE0A0AB3E0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C5864F2CE05397BE0A0AB3E0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C4C04F2CE05397BE0A0AB3E0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C4C14F2CE05397BE0A0AB3E0",#90
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C5554F2CE05397BE0A0AB3E0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C5564F2CE05397BE0A0AB3E0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C4D94F2CE05397BE0A0AB3E0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C4EE4F2CE05397BE0A0AB3E0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=95A47695C4F24F2CE05397BE0A0AB3E0",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=91890A0DA60E80C6E05397BE0A0A065D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=91890A0DA60E80C6E05397BE0A0A065D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=91890A0DA50480C6E05397BE0A0A065D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=91890A0DA50680C6E05397BE0A0A065D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=91890A0DA67480C6E05397BE0A0A065D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=91890A0DA67680C6E05397BE0A0A065D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=91890A0DA67780C6E05397BE0A0A065D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=91890A0DA67880C6E05397BE0A0A065D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=91890A0DA67A80C6E05397BE0A0A065D",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=8AA1F5D36F2AA8DBE05397BE0A0AB19B",#105
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=8AA1F5D36E70A8DBE05397BE0A0AB19B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=8AA1F5D36F31A8DBE05397BE0A0AB19B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=8AA1F5D36E44A8DBE05397BE0A0AB19B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=8AA1F5D36E21A8DBE05397BE0A0AB19B",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=8531C702DB916551E05397BE0A0ACD16",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=7E2903B0D51F5A63E05397BE0A0AF660",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82B77D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82B77D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82B80D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82EBDD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82EBED3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82ECBD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82DDBD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82E38D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82E39D3A7E05397BE0A0AB82A",#120
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82E39D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82ED2D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82ED3D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82ED4D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82ED5D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82ED6D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82ED7D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82ED8D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D826EDD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82771D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82772D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82773D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82775D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82776D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82B04D3A7E05397BE0A0AB82A",#135
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82B06D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82B07D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82B67D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82D17D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82D6AD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82D6BD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82D85D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82BF5D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82BF6D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82BF7D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82D64D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82DC0D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82DC1D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82C16D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82C17D3A7E05397BE0A0AB82A",#150
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82C2DD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82C2FD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82C5CD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82C89D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82D9CD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D826C5D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D827BFD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D828A2D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D828CAD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82956D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82442D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82660D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82661D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82669D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8266AD3A7E05397BE0A0AB82A",#165
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8266BD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8267AD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8267BD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8267CD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8267DD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8267DD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8267FD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82680D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82681D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82683D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82684D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8269BD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82140D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82145D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D821B3D3A7E05397BE0A0AB82A",#180
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D821D2D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82296D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D824B1D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D824E2D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82515D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8260AD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D81931D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8140DD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D81165D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8117BD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8117CD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8117DD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D813BAD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D813BBD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D81065D3A7E05397BE0A0AB82A",#195
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80DCBD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80EE7D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80F36D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80F38D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80F3AD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80C94D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80C95D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80C96D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80C98D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80CB0D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80CB1D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80CB2D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80CB3D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80CB4D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80DF4D3A7E05397BE0A0AB82A",#210
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80DF5D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80DF6D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80DF7D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80EAFD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80A0CD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80A73D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8054DD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80C58D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80C5AD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80C7AD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80A7DD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80A7ED3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80A7FD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80A9BD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8088DD3A7E05397BE0A0AB82A",#225
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80235D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F2C5D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F2C6D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F2C7D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F3B4D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F101D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EDE9D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8012ED3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F783D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D803C4D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F2B0D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E907D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E908D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E909D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E90AD3A7E05397BE0A0AB82A",#240
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EE61D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EE62D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EFA3D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EFA4D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EFFAD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F01FD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F020D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EB2DD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F9BDD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D803C6D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EAE0D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EAFAD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EB3DD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EBB1D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7EBB2D3A7E05397BE0A0AB82A",#255
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E8CBD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E981D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E982D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E983D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D803C6D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D800B6D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E3B9D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E3BAD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E3E1D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D800F0D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D25ED3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7FBEED3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F60AD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D2B7D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D48DD3A7E05397BE0A0AB82A",#270
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D242D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D243D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F698D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7F6F5D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D003D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D04FD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D050D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D051D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D052D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D77AF4D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D77B11D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D77577D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D775EDD3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7FDB9D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8206FD3A7E05397BE0A0AB82A",#285
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D82191D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7FBB8D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7FBE2D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7FCE2D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D77927D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D76DF2D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D76FA8D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7FBB1D3A7E05397BE0A0AB82A",
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D79100D3A7E05397BE0A0AB82A",#294
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D79475D3A7E05397BE0A0AB82A",#304
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D786DCD3A7E05397BE0A0AB82A",#306
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78708D3A7E05397BE0A0AB82A",#307------------------下面是废止或者被替代-----------------
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7A68BD3A7E05397BE0A0AB82A",#295
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7AD7FD3A7E05397BE0A0AB82A",#296
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7ADA1D3A7E05397BE0A0AB82A",#297
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7A5DAD3A7E05397BE0A0AB82A",#298
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7A774D3A7E05397BE0A0AB82A",#299
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D76759D3A7E05397BE0A0AB82A",#300
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78D82D3A7E05397BE0A0AB82A",#301
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78D83D3A7E05397BE0A0AB82A",#302
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78D84D3A7E05397BE0A0AB82A",#303
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D764A9D3A7E05397BE0A0AB82A",#305
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78A5FD3A7E05397BE0A0AB82A",#308
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78D1ED3A7E05397BE0A0AB82A",#309
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78D1FD3A7E05397BE0A0AB82A",#310
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78D20D3A7E05397BE0A0AB82A",#311
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78D8DD3A7E05397BE0A0AB82A",#312
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78D8ED3A7E05397BE0A0AB82A",#313
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78D8FD3A7E05397BE0A0AB82A",#314
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80A4BD3A7E05397BE0A0AB82A",#315
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78FBED3A7E05397BE0A0AB82A",#316
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D78203D3A7E05397BE0A0AB82A",#317
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7B0D1D3A7E05397BE0A0AB82A"]#318
#response=requests.get(url,proxies=proxies)
f = open("html.txt", "w")
for url in url_list:
    result = []
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request, timeout=40)
    res = response.read().decode('utf-8')
    Information=Replace_Space(res)
    # Information=res[38000:-16000]
    print(url_list.index(url)+40)

    # -------------------------------------------------标准状态--------------------------------------------------
    try:
        body = Information[Information.index('<span class="s-status label label-primary">'):]
        state = body[43:body.index('</span')]
    except ValueError:
        body = Information[Information.index('<span class="s-status label label-danger">'):]
        state = body[42:body.index('</span')]
    result.append(state)
    result.append('   ')
    #---------------------------------------------------标准号---------------------------------------------------
    #截取标准号所在str片段
    body=Information[Information.index(BI1_str0):Information.index(BI1_str3)]
    #选择此str片段的所需起始字符和结束字符，起始字符是包含在截取内容内部的
    start='GB'
    end='</dd'
    standard_num=Str_Cut(body,start,end)
    #print('标准号:')
    #print(standard_num)
    result.append(standard_num)
    result.append('   ')
    #--------------------------------------------------发布日期--------------------------------------------------
    body=Str_Cut(Information,BI1_str3,BI1_str4)
    body=Replace_Space(body)
    cut_str='value">'
    body_cut=body[body.index(cut_str):]
    end='</dd'
    release_date=body_cut[7:body_cut.index(end)]
    #print('发布日期:')
    #print(release_date)
    result.append(release_date)
    result.append('   ')
    #--------------------------------------------------实施日期--------------------------------------------------
    body=Str_Cut(Information,BI1_str4,BI1_str1)
    body=Replace_Space(body)
    body_cut=Str_Cut(body,'value">',0)
    implementation_date=Str_Cut(body_cut,7,'</dd')
    #print('实施日期:')
    #print(implementation_date)
    result.append(implementation_date)
    result.append('   ')
    #-----------------------------------------------中国标准分类号-----------------------------------------------
    body=Str_Cut(Information,BI1_str1,BI1_str2)
    body=Replace_Space(body)
    start='value">'
    end='</dd'
    body_cut=Str_Cut(body,start,0)
    China_standard_classification_num=Str_Cut(body_cut,7,end)
    #print('中国标准分类号:')
    #print(China_standard_classification_num)
    result.append(China_standard_classification_num)
    result.append('   ')
    #-----------------------------------------------国际标准分类号-----------------------------------------------
    body=Str_Cut(Information,BI1_str2,BI1_str5)
    body=Replace_Space(body)
    start='</div> " >'
    end='</span>'
    body_cut=Str_Cut(body,start,0)
    international_standard_classification_num=Str_Cut(body_cut,10,end)
    result.append(international_standard_classification_num)
    result.append('   ')
    #--------------------------------------------------归口单位--------------------------------------------------
    body=Str_Cut(Information,BI1_str5,BI1_str6)
    start='blank">'
    end='</a></dd>'
    body_cut=Str_Cut(body,start,0)
    affiliated_unit=Str_Cut(body_cut,7,end)
    result.append(affiliated_unit)
    result.append('   ')
    #--------------------------------------------------执行单位--------------------------------------------------
    body = Str_Cut(Information, BI1_str5, '主管部门</dt><dd')#BI1_str5='归口单位',BI1_str8='主管部门'
    start = 'blank">'
    end = '</a></dd>'
    body_cut = Str_Cut(body, start, 0)
    executable_unit = Str_Cut(body_cut, 7, end)
    result.append(executable_unit)
    result.append('   ')
    #--------------------------------------------------主管部门--------------------------------------------------
    body=Str_Cut(Information,'主管部门</dt><dd','起草单位</h2>')
    body=Replace_Space(body)
    start='blank">'
    end='</a></dd>'
    body_cut=Str_Cut(body,start,0)
    competent_department=Str_Cut(body_cut,7,end)
    #print('主管部门:')
    #print(competent_department)
    result.append(competent_department)
    result.append('   ')
    #--------------------------------------------------起草单位--------------------------------------------------
    body=Str_Cut(Information,BI1_str7,BI1_str9)
    body=Replace_Space(body)
    start='<span'
    end='</span>'
    body_cut = Str_Cut(body, start, '。')
    drafting_unit = Str_Cut(body_cut, 21, end)
    # print('起草单位:')
    while drafting_unit!='No string exists':
        #print(drafting_unit)
        result.append(drafting_unit)
        result.append(',')
        body=Str_Cut(body_cut,drafting_unit,0)
        body_cut = Str_Cut(body, start, 0)
        drafting_unit = Str_Cut(body_cut, 21, end)
    result.append('   ')
    #--------------------------------------------------起草人--------------------------------------------------
    body=Str_Cut(Information,BI1_str9,BI1_str10)
    body=Replace_Space(body)
    start='<span'
    end='</span>'
    body_cut=Str_Cut(body,start,'。')
    drafter=Str_Cut(body_cut,21,end)
    # print('起草人:')
    while drafter!='No string exists':
        result.append(drafter)
        result.append(',')
        body=Str_Cut(body_cut,drafter,0)
        body_cut = Str_Cut(body, start, 0)
        drafter = Str_Cut(body_cut, 21, end)
    result.append('\n')
    print(result)

    #-------------------------------------------------写入txt--------------------------------------------------

    f.writelines(result)
f.close()