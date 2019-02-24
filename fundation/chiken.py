for m in range(1,21):
    for n in range(1,35):
        for x in range(1,301):
            s=5*m+3*n+x*(1/3)
            if s==100:
                print(m,n,x)


