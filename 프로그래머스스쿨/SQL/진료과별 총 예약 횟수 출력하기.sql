SELECT MCDP_CD AS "������ڵ�", COUNT(*) AS "5������Ǽ�"
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY COUNT(*) ASC, MCDP_CD ASC

-- order by �� �� "5������Ǽ�"�� ��� Ʋ�Ⱦ���
-- order by �� �� ����ǥ ����, 5������Ǽ��� ����� ��