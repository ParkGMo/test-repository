-- 뷰 : 가상의 테이블, 실체가 없다, ex) 바로가기 아이콘, 경로를 만들어준다.
-- 보안의 이유로 사용 
-- 쿼리를 단순하게 만들 수 있다. 
CREATE VIEW member_view
AS
	SELECT * FROM member;

SELECT * FROM member_view

-- 사용자 -> 조회 -> SELECT문 -> 테이브 쿼리 실행 -> 테이블 쿠리 결과값 -> SELECT문 -> 결과 -> 사용자

USE market_db;
SELECT mem_id, mem_name, addr FROM member;

USE market_db;
CREATE VIEW v_member
AS
    SELECT mem_id, mem_name, addr FROM member;

SELECT * FROM v_member;

-- VIEW는 조건을 걸 수 있다.
SELECT mem_name, addr FROM v_member
	WHERE addr IN ('서울', '경기');

-- UPDATE : VIEW는 UPDATE할 수 없다.

-- DROP VIEW : VIEW를 삭제

CREATE VIEW v_memberbuy
AS
	SELECT B.mem_id, M.mem_name, B.prod_name, M.addr,
		CONCAT(M.phone1, M.phone2) "연락처"
	FROM buy B
    	INNER JOIN member M ON B.mem_id = M.mem_id;

SELECT * FROM v_memberbuy;
SELECT * FROM v_memberbuy WHERE mem_name = "블랙핑크";

-- VIEW 생성 수정 삭제 

USE market_db;
DROP VIEW IF EXISTS v_viewtest1;
CREATE VIEW v_viewtest1
AS 
	SELECT B.mem_id "Member ID", 
	M.mem_name AS "Member Name", 
	B.prod_name "Product Name", 
	CONCAT(M.phone1, M.phone2) AS "Office Phone" 

	FROM buy B
		INNER JOIN member M
		ON B.mem_id = M.mem_id;

SELECT DISTINCT "Member ID", "Member Name" FROM v_viewtest1;

-- ! ⭐⭐ 띄어쓰기가 있으면 백틱으로 작성 ⭐⭐
SELECT DISTINCT `Member ID`, `Member Name` FROM v_viewtest1;

-- VIEW 수정
ALTER VIEW v_viewtest1
AS 
	SELECT B.mem_id "회원 아이디", 
	M.mem_name AS "회원 이름", 
	B.prod_name "제품 이름", 
	CONCAT(M.phone1, M.phone2) AS "연락처" 

	FROM buy B
		INNER JOIN member M
		ON B.mem_id = M.mem_id;

-- 한글을 권장하지 않는다. 
SELECT DISTINCT `회원 아이디`, `회원 이름` FROM v_viewtest1;

-- VIEW 삭제
DROP VIEW v_viewtest1;

-- VIEW 확인
USE market_db;
CREATE VIEW v_viewtest2
AS 
    SELECT mem_id, mem_name, addr FROM member;

DESCRIBE v_viewtest2;

DESCRIBE member;

SHOW CREATE VIEW v_viewtest2;


-- 업데이트
UPDATE v_member SET addr = '부산' WHERE mem_id = 'BLK';
SELECT * FROM v_member;

-- VIEW로 업테이트는 NOT NULL로 인해 입력이 안될 수도 있어서 권장하지 않는다.
INSERT  INTO v_member(mem_id, mem_name, addr) VALUES ('BTS', '방탄소년단','경기');

-- VIEW 조건 추출
CREATE VIEW v_height167
AS 
    SELECT * FROM member
    WHERE height >= 167;

SELECT * FROM v_height167;
DELETE FROM v_height167 WHERE height < 167; -- -> 삭제할 데이터가 없다.

INSERT INTO v_height167 VALUES ('TRA','티아라', 6, '서울', NULL, NULL, 159, '2005-01-01')
SELECT * FROM v_height167; -- -> 추가는 되지만 확인이 안된다. 바람직X

CREATE VIEW v_height167
AS 
    SELECT * FROM member
    WHERE height >= 167;
	WITH CHECK OPTION; 
	-- -> 위에서 추가는 되었지만 확인이 안되므로 조건이 되지 않으면 추가X

DROP TABLE IF EXISTS buy, member;

SELECT * FROM v_height167; -- 테이블을 삭제하면 VIEW 를 확인 할 수 없다.

CHECK TABLE v_height167; -- 테이블을 확인(참조하는 테이블이 없다. - form editor에서)