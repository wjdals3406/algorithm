# -*- coding: utf-8 -*-
import copy
def pick( items, n, picked, picked_size, toPick , comblist) :
    #m = picked_size
    if toPick == 0 : 
        newitem = copy.deepcopy(picked)
        for i in range(len(newitem)):
            newitem[i] = items[picked[i]]
            
        comblist.append(newitem)
        return comblist
    lastIndex = picked_size - toPick - 1 # ���� �ֱٿ� ���� ���� ����� ��ġ index
    if picked_size == toPick :
        smallest = 0; 
    else :
        smallest = picked[lastIndex] + 1
    for i in range(smallest, n):
        picked[lastIndex + 1] = i
        comblist= pick(items, n, picked, picked_size, toPick - 1, comblist) 
    
    return comblist

if __name__ == "__main__":
    item = [[1, 2], [4, 1], [5, 1], [5, 2], [5, 5]]
    picked = [0 for _ in range(3)]
    comblist = []
    comblist=pick( item, len(item),  picked, 3, 3 , comblist)
    print(comblist)
#�� �Լ��� ��ȯ���� [(10,20,30), (20,30,40), ....]

