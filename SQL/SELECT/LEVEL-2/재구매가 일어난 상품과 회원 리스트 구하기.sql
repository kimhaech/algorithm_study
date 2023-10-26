-- 코드를 입력하세요
SELECT DISTINCT A.USER_ID, A.PRODUCT_ID FROM ONLINE_SALE AS A, ONLINE_SALE AS B
WHERE (A.USER_ID = B.USER_ID AND A.PRODUCT_ID = B.PRODUCT_ID) AND A.SALES_DATE != B.SALES_DATE
ORDER BY A.USER_ID, A.PRODUCT_ID DESC
# 같은 유저가 같은상품을 2번 이상 구매한 것 - 일자, 유저의 아이디, 상품의 아이디 세가지가 모두 같은 경우는 없다. -> 해당 경우를 조건으로 두자.
