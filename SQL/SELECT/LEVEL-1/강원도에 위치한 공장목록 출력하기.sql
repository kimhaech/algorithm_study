-- 코드를 입력하세요
-- 공장 id, 이름, 주소를 보여줌
-- 주소가 강원도인 공장
-- 정렬 : 공장 id 오름차순
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS from FOOD_FACTORY
where ADDRESS like "강원도%"
order by FACTORY_ID asc;
