# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FuturePipeline(object):
    def __init__(self):
        data=np.random.rand(2,20)
        self.new_df=pd.DataFrame(data=data,columns=[
            'Available','Deposit','Equity','Fee','Id','InitFund','MD','MDMAX','NAVPS','NAVPSMAX','Profit','Ranks','SettleDate',
            'TotalFee','TotalMarketValue','UUID','company','rank','school','mobile'
        ])
    def process_item(self, item, spider):
        personal=item['personal']
        df=pd.DataFrame(data=personal)
        df['company']=item['company']
        df['rank']=item['rank']
        df['school']=item['school']
        df['mobile']=item['mobile']
        self.new_df=pd.concat([self.new_df,df])
        return item

    def close_spider(self,spider):
        self.new_df.drop('UUID',axis=1,inplace=True)
        self.new_df=self.new_df[2:]
        self.new_df.to_excel('data.xlsx')