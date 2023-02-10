SELECT MCDP_CD AS "진료과코드", COUNT(*) AS "5월예약건수"
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY COUNT(*) ASC, MCDP_CD ASC

-- order by 할 때 "5월예약건수"로 적어서 틀렸었음
-- order by 할 때 따옴표 없이, 5월예약건수로 적어야 함