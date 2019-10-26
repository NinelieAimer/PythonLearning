import pandas as pd
import numpy as np
data = np.random.rand(2,19)
new_df = pd.DataFrame(data=data)
column=['Available','Deposit','Equity','Fee','Id','InitFund','MD','MDMAX','NAVPS','NAVPSMAX','Profit','Ranks','SettleDate','TotalFee','TotalMarketValue','UUID','company','rank','school']
lendf=len(new_df.columns)
lenco=len(column)
pass