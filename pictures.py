# -*- coding: utf-8 -*-
import re
import sys



def format_url():
    with open(sys.argv[1]) as f: 
        data = str(f.readlines())
        reg = re.compile('src="(https.*?)"',re.S)
        res = reg.findall(string=data)
    if len(res)!=0:
        y,m,d,_ = sys.argv[1].split('/')[1].split('-')
        div = """<div class="day">\n\t<div class="date">"""+y+'年'+m+'月'+d+"""日 | 北京市 </div>\n\t<div class="show">\n"""
        pic_list=""
        for item in res:
            pic_list+='\t\t<div class="list"><img id="img" src="'+item+'"></div>\n'
        div=div+pic_list+"\t</div>\n</div>\n"
        print(div)

format_url()
 