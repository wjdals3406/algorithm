-- �ڵ带 �Է��ϼ���
SELECT 
    HISTORY_ID, CAR_ID, DATE_FORMAT (START_DATE, "%Y-%m-%d") AS START_DATE, DATE_FORMAT (END_DATE, "%Y-%m-%d") AS END_DATE,
    CASE
        WHEN DATEDIFF(END_DATE, START_DATE) >= 29 THEN '��� �뿩'
        ELSE '�ܱ� �뿩'
    END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09-%'
ORDER BY HISTORY_ID DESC;

-- ��� ��
-- DATE_FORMAT�Լ�
-- DATEDIFF() �Լ��� �ΰ��� ��¥���� ���̸� int�� ��ȯ�ϴ� �����Լ�
-- "%Y-%m-%d" != "%Y-%M-%D"