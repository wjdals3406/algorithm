#배달할 재활용 택배 상자의 개수
#수거할 빈 재활용 택배 상자의 개수
#트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리
#각 집에 원하는 개수만큼 택배를 배달 및 수거 가능

def to_visit_house(data, s, cap):
    item = 0
    while s >= 0:
        if item + data[s] > cap:
            data[s] = item + data[s] - cap
            break
        item += data[s]
        data[s] = 0
        s -= 1
    return s

def solution(cap, n, deliveries, pickups):
    de, pe, total = n-1, n-1, 0

    while de > -1 and pe > -1 and deliveries[de] == 0 and pickups[pe] == 0:
        de -= 1
        pe -= 1
    total += (max(de, pe)+1) * 2

    while de > -1 or pe > -1:
        de = to_visit_house(deliveries, de, cap)
        pe = to_visit_house(pickups, pe, cap)
        total += (max(de, pe)+1) * 2 

    return total

cap=2	
n=7
deliveries=[1, 0, 2, 0, 1, 0, 2]
pickups	= [0, 2, 0, 1, 0, 2, 0]
print(solution(cap, n, deliveries, pickups))
