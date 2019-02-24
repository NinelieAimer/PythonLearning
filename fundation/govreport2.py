#govreport2
import word
import wordcloud
from scipy import imread
mask=imread("fivestart.png")
f=open("C:\\Users\\57206\\Desktop\\新时代中国特色社会主义.txt","r",ecoding="utf-8")
t=f.read()
f.close()
ls=word.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",mask=mask,width=1000,height=700,background_color="white")
w.generate(w)
w.to_file("govreport2.png")
