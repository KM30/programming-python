#GovRptWordCloud.py

import jieba
import wordcloud
import os

#提取文件，及获取数据
f=open('jieba.txt','r',encoding='utf-8')
t=f.read()
f.close()
#数据格式化
ls=jieba.lcut(t)
txt="".join(ls)
#词云分词
w=wordcloud.WordCloud(\
    width=1000,height=700,\
    background_color='white',
    font_path='msyh.ttc')
w.generate(txt)
w.to_file('grwordcloudm.png')
