--round(, �ݿø��� �ڸ� ��) / 0:�Ҽ��� ù° �ڸ�, 1: �Ҽ��� ��° �ڸ�
SELECT round(avg(DAILY_FEE)) as AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'