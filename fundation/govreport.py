#govreport
import word
import wordcloud
f=open("C:\\Users\\57206\\Desktop\\","r",encoding="utf-8")
t=f.read()
f.close()
ls=word.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,background_color="white",max_words=10)
w.generate(txt)
w.to_file("wordscounts.png")
