-- 코드를 입력하세요
SELECT R.FOOD_TYPE, R.REST_ID, R.REST_NAME, R.FAVORITES
FROM 
    REST_INFO R,
    (
        SELECT FOOD_TYPE, MAX(FAVORITES) as FAVORITES
        FROM REST_INFO
        GROUP BY FOOD_TYPE
    ) T
WHERE R.FAVORITES = T.FAVORITES AND R.FOOD_TYPE = T.FOOD_TYPE
ORDER BY R.FOOD_TYPE DESC
