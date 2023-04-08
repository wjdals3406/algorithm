import math
from collections import defaultdict
def solution(fees, records):
    answer = []
    basic_time, basic_fee, mtime, mmfee = fees
    car_dic = defaultdict(list)
    last_time = 23*60 + 59

    for record in records:
        t, car, in_out = record.split()
        car_dic[car].append((t,in_out))

    for car in car_dic.keys():
        stack = []
        total_time = 0

        for t,in_out in car_dic[car]:
            if in_out == "IN":
                stack.append((t,in_out))
            else:
                in_t, IN = stack.pop()

                INh, INminute = in_t.split(":")
                OUTh, OUTminute = t.split(":")
                IN_time = int(INh) * 60 + int(INminute)
                OUT_time = int(OUTh) * 60 + int(OUTminute)
                total_time += (OUT_time - IN_time)

        if stack:
            in_t, IN = stack.pop()
            INh, INminute = in_t.split(":")
            IN_time = int(INh) * 60 + int(INminute)
            total_time += (last_time - IN_time)

        if total_time <= basic_time:
            fee = basic_fee
        else:
            fee = basic_fee + math.ceil((total_time - basic_time)/mtime)*mmfee

        answer.append((car, fee))

    answer.sort(key = lambda x : x[0])    
    #차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
    return [i[1] for i in answer]