#CalHamletV1.py
def getText():
    txt = open("jieba.txt", "r").read()   #字符串类型
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
 
hamletTxt = getText()   #字符串类型
words  = hamletTxt.split()   #列表类型
counts = {}   #定义空字典
for word in words:           
    counts[word] = counts.get(word,0) + 1   #向空字典添加 键值对 
items = list(counts.items()) #返回字典中 键值对 信息并转换为列表类型
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
