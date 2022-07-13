import sys

n = int(sys.stdin.readline())
house = list(map(int,sys.stdin.readline().split()))
house.sort()
if len(house) % 2 == 0:
    print(house[len(house)//2-1])
else:
    print(house[len(house)//2])
    
# (n-1)//2 ÀÌ°Å »ç¿ëÇÏ¸é È¦Â¦ ¾È³ª´²µµµÊ