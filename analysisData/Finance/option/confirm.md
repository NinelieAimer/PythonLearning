# Derivation of the black-scholes-merton option-pricing formula from a binomal tree

- We all know the payoff from a European call option is 

  - $$
    \max (S_0u^jd^{n-j}-K,0)
    $$

- So that the expected payoff from the call option is

  - $$
    \sum_{j=0}^{n}\frac{n!}{(n-j)!j!}p^j(1-p)^{n-j}\max (S_0u^jd^{n-j}-K,0)
    $$

- We discount this at the risk-free rate r to obtian the option price ,as we are in risk-neutral world

  - $$
    c=e^{-rT}\sum_{j=0}^{n}\frac{n!}{(n-j)!j!}p^j(1-p)^{n-j}\max (S_0u^jd^{n-j}-K,0)
    $$

- We should choose the value ,when the option value is not equal to zero. So we have:

  - $$
    S_0u^jd^{n-j}>K
    $$

- It follows that

  - $$
    \ln(S_0/K)>-j\ln(u)-(n-j)\ln(d)
    $$

- Beacuse the $u=e^{\sigma\sqrt{T/n}}$  and $d=e^{-\sigma\sqrt{T/n}}$  , we have:

  - $$
    \ln(S_0/K)>n\sigma\sqrt{T/n}-2j\sigma\sqrt{T/n}\\
    j>\frac{n}{2}-\frac{\ln(S_0/K)}{2\sigma\sqrt{T/n}}
    $$

- So we the option price can be:

  - $$
    c=e^{-rT}\sum_{j>\alpha}\frac{n!}{(n-j)!j!}p^j(1-p)^{n-j}(S_0u^jd^{n-j}-K)
    $$

  - and the $\alpha$ is 

    - $$
      \alpha=\frac{n}{2}-\frac{\ln(S_0/K)}{2\sigma\sqrt{T/n}}
      $$

- We define 

  - $$
    U_1=\sum_{j>\alpha}\frac{n!}{(n-j)!j!}p^j(1-p)^{n-j}u^jd^{n-j}
    $$

  - and

  - $$
    U_2=\sum_{j>\alpha}\frac{n!}{(n-j)!j!}p^j(1-p)^{n-j}
    $$

  - so the c is

  - $$
    c=e^{-rT}(S_0U_1-KU_2)
    $$

- The variable $U_2$ is the probability of the number of successes being more than $\alpha$. And the n approachs the infinity. We can use  *De Moivre-Laplace*  we have:

  - $$
    U_2=1-N\bigg(\frac{\alpha-np}{\sqrt{np(1-p)}}\biggl)\\
    $$

  - or

  - $$
    U_2=N\bigg(\frac{np-\alpha}{\sqrt{np(1-p)}}\biggl)
    $$

  - From the equation (8), we have:
  
  - $$
    U_2=N\bigg(\frac{\ln(S_0/K)}{2\sigma\sqrt{T}\sqrt{p(1-p)}}+\frac{\sqrt{n}(p-\frac{1}{2})}{\sqrt{p(1-p)}}\biggl)
    $$
  
- P is :

  - $$
    p=\frac{e^{-rT}-d}{u-d}
    $$

  - we have

  - $$
    p=\frac{e^{rT/n}-e^{-\sigma\sqrt{T/n}}}{e^{\sigma\sqrt{T/n}}-e^{-\sigma\sqrt{T/n}}}
    $$

- Set the $x=\sqrt{T/n}$

- So the $p(1-p)$ is

  - $$
    p(1-p)=\frac{e^{rx^2+\sigma x}-e^{2rx^2}+e^{rx^2-\sigma x}-1}{e^{2\sigma x}+e^{-2\sigma x }-2}
    $$

  - By expanding the exponential functions in a series， the top of the equation (17) can be written as 

  - $$
    \begin{align}
    top =& 1+rx^2+\sigma x +\frac{(rx^2+\sigma x)^2}{2}+o(x^2)-1-2rx^2-o(x^2)+1+rx^2-\sigma x\\
    &+\frac{(rx^2-\sigma x)^2}{2}+o(x^2)-1\\
     \space=&1+rx^2+\sigma x+\frac{\sigma^2x^2}{2}+o(x^2)-1-2rx^2-o(x^2)+rx^2-\sigma x+1+\frac{\sigma^2x^2}{2}+o(x^2)-1\\
     =&\sigma^2x^2+o(x^2)
    \end{align}
    $$

  - And the bottom of the equation can be written as:

  - $$
    \begin{align}
    bottom&=1+2\sigma x+\frac{4\sigma^2x^2}{2}+o(x^2)+1-2\sigma x+\frac{4\sigma^2x^2}{2}+o(x^2)-2\\
    &=4\sigma^2x^2
    \end{align}
    $$

  - So $p(1-p)=\frac{1}{4}$

- And the $\sqrt{n}(p-\frac{1}{2})$ is 

  - $$
    (p-\frac{1}{2})\sqrt{n}=\frac{2e^{rT/n}-e^{-\sigma\sqrt{T/n}}-e^{\sigma\sqrt{T/n}}}{2(e^{\sigma\sqrt{T/n}}-e^{-\sigma\sqrt{T/n}})}\sqrt{n}
    $$

  - Also we set $x=\sqrt{T/n}$ 

  - $$
    \begin{align}
    e^{\sigma x}&=1+\sigma x +o(x)\\
    e^{-\sigma x}&=1-\sigma x +o(x)\\
    e^{rx^2}&=1+rx^2+o(x^2)
    \end{align}
    $$

  - The top is equal to:

  - $$
    \begin{align}
    top&=2+2rx^2+o(x^2)-1+\sigma x-\frac{\sigma^2x^2}{2}
    +o(x^2)-1-\sigma x-\frac{\sigma^2x^2}{2}+o(x^2)\\
    &=(2r-\sigma^2)x^2+o(x^2)\\
    bottom&=4\sigma x+o(x)
    \end{align}
    $$

  - so the result is

  - $$
    \frac{(2r-\sigma^2)x^2}{4\sigma x}
    $$

- $U_2$ is 

  - $$
    U_2=N\bigg(\frac{\ln(S_0/K)+(r-\sigma^2/2)T}{\sigma T}\biggl)
    $$

- We now move to evaluate $U_1$ .From equation (9) ,we have

  - $$
    U_1=\sum_{j>\alpha}\frac{n!}{(n-j)!j!}(1-p)^{n-j}(pu)^j[(1-p)d]^{n-j}
    $$

  - Define

  - $$
    
    \begin{align}
    p^*&=\frac{pu}{pu+(1-p)d}\\
    \\
    1-p^*&=\frac{(1-p)d}{pu+(1-p)d}
    \end{align}
    $$

  - $U_1$ is 

  - $$
    U_1=[pu+(1-p)d]^n\sum_{j>\alpha}\frac{n!}{(n-j)!j!}(p^*)^j(1-p^*)^{n-j}
    $$

  - In the risk-neural world $pu+(1-p)d=e^{rT/n}$ so

  - $$
    U_1=e^{rT}\sum_{j>\alpha}\frac{n!}{(n-j)!j!}(p^*)^j(1-p^*)^{n-j}
    $$

  - $$
    U_1=e^{rT}N\bigg(\frac{np^*-\alpha}{\sqrt{np^*(1-p^*)}}\biggl)
    $$

  - As the $p^*$ is

  - $$
    p^*=\bigg(\frac{e^{rT/n}-e^{-\sigma\sqrt{T/n}}}{e^{\sigma\sqrt{T/n}}-e^{-\sigma\sqrt{T/n}}}\biggl)\bigg(\frac{e^{\sigma\sqrt{T/n}}}{e^{rT/n}}\biggl)
    $$

  - By expanding the exponential functions in a series we see that , as n tends to infinty $p^*(1-p^*)$ tends to $\frac{1}{4}$ and $\sqrt{n}(p^*-\frac{1}{2})$ tends to

  - $$
    \frac{(r+\sigma^2/2)\sqrt{T}}{2\sigma}
    $$

  - The result that

  - $$
    U_1=e^{rT}N\bigg(\frac{\ln(S_0/K)+(r+\sigma^2/2)T}{\sigma\sqrt{T}}\biggl)
    $$

- So we have

  - $$
    c=S_0N(d_1)-Ke^{-rT}N(d_2)
    $$

  - $d_1$ is

    - $$
      d_1=\frac{\ln(S_0/K)+(r+\sigma^2/2)T}{\sigma\sqrt{T}}
      $$

  - and $d_2$ is

    - $$
      d_2=\frac{\ln(S_0/K)+(r-\sigma^2/2)T}{\sigma T}=d_1-\sigma\sqrt{T}
      $$

    - 

