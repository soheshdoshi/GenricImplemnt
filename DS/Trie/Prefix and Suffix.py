from collections import defaultdict
def mySolution(A,B):
    m_lenth=len(B[0])
    new_arr=[]
    for i in A:
        if len(i)>=m_lenth:
            new_arr.append(i)
    #print(new_arr)
    pre=defaultdict(list)
    for i in new_arr:
        pre[i[:m_lenth]].append(i)
    count_arr=[]
    for i in B:
        coun=0
        arr_list=pre[i]
        for i in arr_list:
            lenth=len(i)
            if i[:m_lenth]==i[lenth-m_lenth:]:
                coun+=1
        count_arr.append(coun)
    return count_arr


A = ["cazqzqcaz", "cadssac", "caz"]
B = ["caz", "cad"]
mySolution(A,B)