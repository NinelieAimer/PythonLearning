---
title: "回归之melt"
author: "陈玲倩"
date: "2018年10月16日"
---
library(openxlsx)
library(dplyr)
#批量读入文件夹中的xlsx文件
path <- "C:/Users/13750/Desktop/各种表"
mfiles <- list.files(path, pattern = "*.xlsx", full.names = TRUE)
datalist <- lapply(mfiles, function(x) read.xlsx(x)) 
#批量melt数据，并批量生成表
library(reshape2)
for ( i in 1:length(datalist)) {
  b<-melt(datalist[[i]],
          measure.vars = c('上饶','九江','南昌','吉安',	'宜春',	'抚州',	'新余',	'景德镇',	'萍乡',	'赣州',	'鹰潭'),
          varible.name = 'cs',
          value.name = "price")
  write.xlsx(b,file = paste("C:/Users/13750/Desktop/各种表2/",i,".xlsx",sep=""))
  } 

