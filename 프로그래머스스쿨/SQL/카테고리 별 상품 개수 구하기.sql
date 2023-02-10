SELECT LEFT(PRODUCT_CODE,2) AS CATEGORY, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE,2)

-- 배운 점 : 
-- LEFT(문자열, 길이) : 왼쪽부터 길이만큼 문자열 잘라냄
-- RIGHT(문자열, 길이) : 오른쪽부터 길이만큼 문자열 잘라냄
-- SUBSTRING(문자열, 시작위치, 길이) : 시작위치부터 길이만큼 문자열 잘라냄