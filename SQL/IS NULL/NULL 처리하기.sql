-- 코드를 입력하세요
-- 종, 이름, 성별, 중성화 여부 / 아이디 순 / 이름 없는 경우 No name으로 표시
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
