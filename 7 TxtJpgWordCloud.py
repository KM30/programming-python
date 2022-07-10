#GovRptWordCloudv2.py
import jieba
import wordcloud
import imageio

jpg=input("Please input the path of the jpg you want to open:" )
mask =imageio.imread(jpg+".jpg")
excludes = { }
st=input("Please input the path of the txt you want to open:" )
f = open(st+".txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    )
w.generate(txt)
w.to_file("grwordcloudm.png")
