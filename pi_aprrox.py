import numpy as np
from matplotlib import pyplot as plt
import math

actualpi=math.pi

pivalues=[]
pi=0

x=np.arange(0,1000,1)

for i in range(1000):
    pi=pi+(1/(2*i+1))*((-1)**i)
    pi_calc=4*pi
    print(pi_calc)
    pivalues.append(pi_calc)
    if actualpi>pi_calc:
        error=actualpi-pi_calc
        errorprc=(error/actualpi)*100
    elif actualpi<pi_calc:
        error=pi_calc-actualpi
        errorprc=(error/actualpi)*100

    print("error - "+str(errorprc)+" %")

        
    
plt.scatter(x,pivalues,s=0.9)
plt.ylabel("approximated pi value")
plt.show()

