-- 뷰 : 가사의 테이블, 실체가 없다, ex) 바로가기 아이콘, 경로를 만들어준다.
-- 보안의 이유로 사용 
CREATE VIEW member_view
AS
	SELECT * FROM member;

SELECT * FROM member_view