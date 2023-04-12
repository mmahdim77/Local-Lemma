import random
from pprint import pprint

# kSAT(c) : 10SAT(9)
k = 9
c = 10
print("Reading SAT instance from file")
with open("large.txt", "r") as sat_file:
    n, m = map(int, sat_file.readline().split())
    clauses = [tuple(map(int, sat_file.readline().split()))[1:] for _ in range(m)]
base_num  = 1<<k+1
print(n,m)

pool = [[] for _ in range(n)]
for idx , clause in enumerate(clauses):
    for lit in clause:
        pool[abs(lit)-1].append(idx)
pprint("PoolDone")

vars = [random.randint(0,1) for _ in range(n)]
# print("vars:\t",vars)

def vars_resampling(clause):
    var_resample =  [random.randint(0,1) for _ in range(k)]
    for idx, lit in enumerate(clause):
        vars[abs(lit)-1] = int(var_resample[idx])

def check_satisfaction():
    for idx ,  clause in enumerate(clauses):
        satisfied_vars_num = 0
        for lit in clause:
            if lit>0:
                if vars[lit-1] == 1:
                    satisfied_vars_num+=1
                    break
            else:
                if vars[abs(lit)-1] == 0:
                    satisfied_vars_num+=1
                    break
        if(satisfied_vars_num==0):
            return 0 , clause
    return 1 , []

i=0
while (True):
    print(i)
    i+=1
    stat, clause = check_satisfaction()
    if stat == 0:
        vars_resampling(clause)
    else:
        print("satisfied: ", vars)
        out=""
        for i in vars:
            if i==1:
                out+="T"
            else:
                out+="F"
        

        with open("med_sol.txt", "w") as text_file:
            text_file.write(out)
        break
    
                    


