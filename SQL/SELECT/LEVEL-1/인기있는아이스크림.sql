-- 보여줄 정보 : 아이스크림의 맛
-- 정렬 기준 : 1. 총 주문량 2. 같은 주문량 -> 출하 번호
SELECT FLAVOR FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;
