-- 코드를 입력하세요
SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE "%시트%"
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE
-- 배운 점 : CAR_RENTAL_COMPANY_CAR 테이블에서 '통풍시트', '열선시트', '가죽시트' 중 
-- 하나 이상의 옵션이 포함된 자동차가 자동차 종류 별로 몇 대인지 출력
-- -> %시트%로 하면 해결 됨