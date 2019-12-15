import numpy as np
import pandas as pd

class option:
    """
    N = number of binomial iterations
    S0 = initial stock price
    u = factor change of upstate
    r = risk free interest rate per annum
    K = strike price
    sigma = the volatility of a stock price
    T = Time
    """
    def __init__(self,S0,K,sigma,r):

        #Arguments
        self.r=r
        self.S0=S0
        self.K=K
        self.sigma=sigma
    
    def Euro_option(self,iter_times,T):
        u=np.exp(self.sigma*np.sqrt(T/iter_times))
        d=1/u
        F_times=iter_times+1
        temp_df=np.arange(F_times)
        new_temp=pd.Series(temp_df)
        p=(np.exp(self.r*T/iter_times)-d)/(u-d)
        pass

        def eve(x):
            fa=np.math.factorial(iter_times)/(np.math.factorial(iter_times-x)*np.math.factorial(x))
            value=np.maximum(self.S0*u**x*d**(iter_times-x)-self.K,0)
            pro=p**x*(1-p)**(iter_times-x)
            return fa*pro*value
        
        last=new_temp.map(eve)
        return last.sum()*np.exp(-self.r*T)

objs=option(S0=40,K=40,sigma=0.3,r=0.05)
a=objs.Euro_option(iter_times=4,T=8)
print(a)