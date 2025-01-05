-- select version()
-- 스키마 == datadase 
-- 직접 테이블 CRUD 
-- SELECT * FROM member
SELECT * FROM member WHERE member_name ="아이유";

-- 인덱스 : 전체 페이지에서 찾는게 아닌 인덱스에서 찾으므로써 빠르게 찾는다 - execution plan 이 달라짐 
CREATE INDEX idx_member_name ON member(member_name); 
