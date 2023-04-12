import sys, random

log_f = open("med_log.txt", "w")
def bitwise_xnor(a, b):
    xor_result = a ^ b
    xnor_result = ~xor_result

    # Find the maximum bit length of the input numbers
    max_bits = max(a.bit_length(), b.bit_length())

    # Create a mask with only the relevant bits set to 1
    mask = (1 << max_bits) - 1

    # Apply the mask to the xnor_result to get the unsigned binary representation
    unsigned_xnor_result = xnor_result & mask

    return unsigned_xnor_result
def bitwise_not(num):
    # Find the bit length of the input number
    num_bits = num.bit_length()

    # Create a mask with only the relevant bits set to 1
    mask = (1 << num_bits) - 1

    # Apply bitwise XOR with the mask to obtain the bitwise NOT result
    not_result = num ^ mask +base_num
    return not_result



# read the instance
print("Reading SAT instance from file")
with open("large.txt", "r") as sat_file:
  n, m = map(int, sat_file.readline().split())
  clauses = [tuple(map(int, sat_file.readline().split()))[1:] for _ in range(m)]

base_num  = 1<<n
print(n,m)
# for clause in clauses:
#     for lit in clause:
#         if (lit>0):
#             print(str(lit), end=" V ")
#         else:
#             print("~"+str(abs(lit)), end=" V ")
#     print()

bitmask =[]
bitclause = []
c=0
for idx, clause in enumerate(clauses):
    # print(c)
    if(c%100==0):
        print(c)
    c+=1
    bm = base_num
    bc = base_num
    for lit in clause:
        bm|=1<<(abs(lit)-1)
        if(lit>0):
            bc|=1<<(lit-1)


print("done")

def check_satsifaction(sat):
    for idx , bc in enumerate(bitclause):
        res = bitwise_xnor(sat,bc)
        res_mask = res & bitmask[idx]
        if(res_mask-base_num==0):
            sat = local_correct(bc,bitmask[idx], sat)

    return True, sat

def local_correct(clause,mask, sat):
    # print("sat:\t\t",bin(sat+base_num))
    # print("clause:\t\t",bin(clause))
    # print("mask:\t\t",bin(mask))
    temp_sat = (base_num+random.randint(1,2**(n)-1))
    # print("temp_sat:\t",bin(temp_sat))
    # print("masked_temp:\t",bin((temp_sat & (mask))))
    # print("masked_sat:\t",bin(sat & (bitwise_not(mask))))
    sat = (sat & (bitwise_not(mask))) | (temp_sat & (mask))
    # print("new sat:\t",bin(sat))

    for idx , bc in enumerate(bitclause):
        res = bitwise_xnor(sat,bc)
        res_mask = res & bitmask[idx]

        if(res_mask-base_num==0):
            
            sat=local_correct(bc,bitmask[idx], sat)
            # return sat

    return sat



sat = base_num+2**(n)-1
# sat = 0b001010000000100111
# print(sat)
while(True):
    stat, sat= check_satsifaction(sat)
    # print("---------------------------")
    # for idx , bc in enumerate(bitclause):
    #     res = bitwise_xnor(sat,bc)
    #     res_mask = res & bitmask[idx]
    #     if idx==395:
    #         print("hi")
    #         pass
    #     print((res_mask-base_num).bit_length())
    #     if(res_mask-base_num==0):
    #         print(idx)
    #         # sat = local_correct(bc,bitmask[idx], sat)
    # print("---------------------------")
    # print(bin(sat))
    out=""
    for i in (bin(sat)[3:]):
        if i=="1":
            out+="T"
        else:
            out+="F"
    out = out[::-1]

    with open("med_sol.txt", "w") as text_file:
        text_file.write(out)
    break
