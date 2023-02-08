--round(, 반올림할 자리 값) / 0:소숫점 첫째 자리, 1: 소수점 둘째 자리
SELECT round(avg(DAILY_FEE)) as AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'