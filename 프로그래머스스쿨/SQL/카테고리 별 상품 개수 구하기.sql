SELECT LEFT(PRODUCT_CODE,2) AS CATEGORY, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE,2)

-- ��� �� : 
-- LEFT(���ڿ�, ����) : ���ʺ��� ���̸�ŭ ���ڿ� �߶�
-- RIGHT(���ڿ�, ����) : �����ʺ��� ���̸�ŭ ���ڿ� �߶�
-- SUBSTRING(���ڿ�, ������ġ, ����) : ������ġ���� ���̸�ŭ ���ڿ� �߶�