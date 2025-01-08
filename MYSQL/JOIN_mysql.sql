-- JOIN
--  두개 테이블을 하나의 결과를 만들어 내는 것

-- 내부 조인
-- one to many(일대다)
--  PK(primary key) : 중복 x, NULL X
--  FK(foreign key) : 왜래키는 다른 테이블에서 PK 
-- ex) 회원(PK) -> 구매내역의 회원(FK)

-- SELECT <열 이름>
-- FROM <첫 번째 테이블>
--  INNER JOIN <두 번쨰 테이블>
--  ON <조인될 조건>
-- [WHERE 검색 조건]

USE market_db;
SELECT * 
    FROM buy
        INNER JOIN member
        ON buy.mem_id = member.mem_id
    WHERE buy.mem_id ="GRL";

SELECT * 
    FROM buy
        INNER JOIN member
        ON buy.mem_id = member.mem_id ;

-- 두개의 테이블에서 mem_id 가 있으므로 직접 지정
-- SELECT mem_id, mem_name, prod_name, addr, CONCAT(phone1, phone2) AS '연락처'
SELECT buy.mem_id, mem_name, prod_name, addr, CONCAT(phone1, phone2) AS '연락처'
    FROM buy
        INNER JOIN member
        ON buy.mem_id = member.mem_id

-- B. M. 별명 부여 가능
SELECT B.mem_id, M.mem_name, M.addr, CONCAT(M.phone1, M.phone2) AS '연락처'
    FROM buy B
        LEFT JOIN member M
        ON B.mem_id = M.mem_id;

-- 내부 조인의 한계 == 해당하는 조건만 추출 가능

-- 외부 조인
-- 조인이 안되는 것들도 추출!
-- SELECT <열 목록>
--  FROM <첫번째 테이블(LEFT 테이블)>
--      <LEFT : RIGHT : FULL> OUTER JOIN <두 번째 테이블(RIGHT 테이블)>
--      ON <조인 될 조건>
--  [WHERE <검색 조건>]

-- LEFT 값은 전부 출력된다.
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr
    FROM member M
        LEFT OUTER JOIN buy B
        ON M.mem_id = B.mem_id
    ORDER BY M.mem_id;

-- RIGHT 값은 전부 출력된다.
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr
    FROM member M
        RIGHT OUTER JOIN buy B
        ON M.mem_id = B.mem_id
    ORDER BY M.mem_id;

-- 상호 조인
-- 대용량의 데이터를 만들 떄 사용

--  1. ON 구문이 없다.
--  2. 결과의 내용은 의미가 없다. 랜덤으로 조인하기 떄문
--  3. 상호 조인의 주용도는 테스트하기 위해 대용량의 테이터를 생성할 때

SELECT *
    FROM buy
        CROSS JOIN member;

SELECT COUNT(*) "데이터 개수"
    FROM sakila.inventory
        CROSS JOIN world.city;

-- 자체 조인

-- SELECT <열 목록>
--  FROM <테이블> 별칭A
--      INNER JOIN <테이블> 별칭B
--      ON <조인 될 조건>
-- [WHERE 검색 조건]

--  -> 같은 테이블이므로 별칭을 부여하여 조인한다.

USE market_db;
CREATE TABLE emp_table (emp CHAR(4), manager CHAR(4), phone VARCHAR(8));

INSERT INTO emp_table VALUES('대표', NULL, '0000');
INSERT INTO emp_table VALUES('영업이사', '대표', '1111');
INSERT INTO emp_table VALUES('관리이사', '대표', '2222');
INSERT INTO emp_table VALUES('정보이사', '대표', '3333');
INSERT INTO emp_table VALUES('영업과장', '영업이사', '1111-1');
INSERT INTO emp_table VALUES('경리부장', '관리이사', '2222-1');
INSERT INTO emp_table VALUES('인사부장', '관리이사', '2222-2');
INSERT INTO emp_table VALUES('개발팀장', '정보이사', '3333-1');
INSERT INTO emp_table VALUES('개발주임', '정보이사', '3333-1-1');

SELECT A.emp "직원", B.emp "직속상관", B.phone "직속상관연락처"
    FROM emp_table A
        INNER JOIN emp_table B
        ON A.manager = B.emp
    WHERE A.emp ="경리부장"