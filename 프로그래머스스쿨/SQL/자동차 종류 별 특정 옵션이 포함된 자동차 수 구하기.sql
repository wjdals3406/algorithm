-- �ڵ带 �Է��ϼ���
SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE "%��Ʈ%"
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE
-- ��� �� : CAR_RENTAL_COMPANY_CAR ���̺��� '��ǳ��Ʈ', '������Ʈ', '���׽�Ʈ' �� 
-- �ϳ� �̻��� �ɼ��� ���Ե� �ڵ����� �ڵ��� ���� ���� �� ������ ���
-- -> %��Ʈ%�� �ϸ� �ذ� ��