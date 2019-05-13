'''文本词频统计
    -需求：一篇文章，出现哪些词？哪些词出现的最多？
    -英文文本 还是 中文文本
    -噪音处理
'''
def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in "符号"：
        txt = txt.replace(ch," ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) +1
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))