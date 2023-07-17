import numpy as np
import csv
import random
import math

# laplaceMechanism(img, length, width, epsilon)
# epsilon
#   The privacy budget of the laplace Mechanism.
#   The smaller the value is, the better privacy protection.
def laplaceMechanism(num, n,max, epsilon=1,div=True):
    # Generate laplace noise mask
    dp_noise = np.random.laplace(0, 1.0/epsilon, n).round() % max # round
    if div:
        num_out = (num + dp_noise) % max # round
    else:
        num_out = (num + dp_noise)# round
    # Reshape to origin form
    return num_out
def score(x, y, ox, oy):
    sc=0
    for i in range(0,3000):
        sc+=math.hypot(x[i]-ox[i],y[i]-oy[i])
    return sc
#X=20K,Y=27K
with open('DP_FixGrid.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    X=67
    Y=90
    ep=[1,0.1,0.05,0.02,0.01]
    case_num=3000
    # parameter setting
    numx = []
    numy = []
    num_id=range(0,case_num)
    for i in range(0,case_num):
        numx.append(random.randint(0,X))
        numy.append(random.randint(0,Y))
    writer.writerow(['cases', 'FixGrid', 'Unfix'])
    #case 1
    for b in ep:
        epsilon=b # epsilon 1 -> 0.1 -> 0.05 -> 0.02 -> 0.01
        # Check original data
        #print(num)
        num_outx = laplaceMechanism(numx, case_num, X, epsilon)
        num_outy = laplaceMechanism(numy, case_num, Y, epsilon)
        # Check sorted DP data
        #print(num_ans)
        # Count score
        n1=score(numx,numy,num_outx,num_outy)
        #case 2
        num_outx = laplaceMechanism(numx, case_num, X, epsilon,False)
        num_outy = laplaceMechanism(numy, case_num, Y, epsilon,False)
        # Check unsort DP data
        #print(num_out)
        # Count score
        n2=score(numx,numy,num_outx,num_outy)
        # Check scores
        caseStr=''
        caseStr+='epsilon = '+str(b)
        print(caseStr)
        print('DP with fix: ',n1)
        print('DP without fix: ',n2)
        writer.writerow([caseStr, n1, n2])