import jieba
import wordcloud
import imageio
#设置分词目录
content = [line.strip() for line in open('D:\\456.txt', 'r', encoding='utf-8-sig').readlines()]
wordcloud.STOPWORDS.update(content)
#读取需要分词的文件，并且将分好的词存为txt
with open('D:\\789.txt',encoding='utf-8') as f:
    t=f.read()
ls=jieba.lcut(t)
txt=" ".join(ls)
#设置词云图
w=wordcloud.WordCloud(width=2000,height=1400,font_path="msyh.ttc")
w.generate(txt)
#生成
w.to_file(r'D:\pic5.png')