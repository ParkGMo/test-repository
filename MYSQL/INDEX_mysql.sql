-- select version()
-- 스키마 == datadase 
-- 직접 테이블 CRUD 
-- SELECT * FROM member
SELECT * FROM member WHERE member_name ="아이유";

CREATE INDEX idx_member_name ON member(member_name); 
-- 인덱스 : 전체 페이지에서 찾는게 아닌 인덱스에서 찾으므로써 빠르게 찾는다 - execution plan 이 달라짐 
-- 인텍스가 많으면 찾기가 많아지는 것처럼 비효율적이다.
-- 인덱스는 공긴을 차지하여 테이터베이스의 추가적인 공간이 필요
-- 처음에 인덱스는 만드는데 시간이 오래 걸린다.

-- 인덱스 2가지
--  1.clustered index  ex) 한영사전, 국어사전
--  2.secondary index  ex) 책 맨뒤 찾아보기 
--  자동 생성되는 인덱스는 두가지 중 하나로 만들어진다. 

--  PK는 자동으로 클러스터형 인덱스 생성 --> 자동으로 PK를 정렬

USE market_db;
CREATE TABLE table1 (
    col1 INT PRIMARY KEY,
    col2 INT,
    col3 INT,
)
SHOW INDEX FROM table1;
-- -> key name 열에 PRIMARY써 있으면 클러스터형 인덱스이다.

CREATE TABLE table2 (
    col1 INT PRIMARY KEY,
    col2 INT UNIQUE,
    col3 INT UNIQUE,
);
SHOW INDEX FROM table2;
-- -> key name 열에 PRIMARY써 있으면 클러스터형 인덱스이다. * 클러스터 인덱스는 하나만 만들어짐
-- -> key name 열에 col2과 col3 보조 인덱스이다. * 보조인덱스는 여러개 가능


-- 클러스터 인덱스
USE market_db;
DROP TABLE IF EXISTS buy, member;

CREATE TABLE member (
    mem_id CHAR(8),
    mem_name VARCHAR(10),
    mem_number INT,
    addr CHAR(2)
);

INSERT INTO member VALUES ('TWC', '트와이스', 9, '서울');
INSERT INTO member VALUES ('BLK', '블랙핑크', 4, '경남');
INSERT INTO member VALUES ('WMN', '여자친구', 6, '경기');
INSERT INTO member VALUES ('OMY', '오마이걸', 7, '서울');
SELECT * FROM member;

-- PRIMARY KEY가 지정되면 정렬된다. (클러스터 인덱스)
ALTER TABLE member 
    ADD CONSTRAINT
    PRIMARY KEY (mem_id);
SELECT * FROM member;

-- 정렬이 되어서 추가된다.
INSERT INTO member VALUES ('GRL', '소녀시대', 8,'서울');
SELECT * FROM member;


-- 보조 인덱스
USE market_db;
DROP TABLE IF EXISTS buy, member;

CREATE TABLE member (
    mem_id CHAR(8),
    mem_name VARCHAR(10),
    mem_number INT,
    addr CHAR(2)
);
INSERT INTO member VALUES ('TWC', '트와이스', 9, '서울');
INSERT INTO member VALUES ('BLK', '블랙핑크', 4, '경남');
INSERT INTO member VALUES ('WMN', '여자친구', 6, '경기');
INSERT INTO member VALUES ('OMY', '오마이걸', 7, '서울');
SELECT * FROM member;

-- UNIQUE가 지정되면 자동 정렬X (보조 인덱스)
ALTER TABLE member 
    ADD CONSTRAINT
    UNIQUE (mem_id);
SELECT * FROM member;

ALTER TABLE member 
    ADD CONSTRAINT
    UNIQUE (mem_name);
SELECT * FROM member;

-- 추가하더라도 정렬 되지 않는다.
INSERT INTO member VALUES ('GRL', '소녀시대', 8,'서울');
SELECT * FROM member;


-- 균형 트리 : 뿌리(루트) -> 줄기(중간) -> 잎(리프)
-- 루트 노드 : 가장 상위 노드
-- 리프 노드 : 제일 마지막 노드   
--  단계는 3단계 이지만 그이상 일 수 있다  --> 중간 노드는 여러번 가능

--  인덱스가 없다면 리프 페이지에서 전체를 원하는 값을 찾아나간다. *노드에서 하나의 테이블을 페이지라 한다.
--  인덱스가 있다면 루트 페이지에서 해당 리프 페이지를 찾아가서 원하는 값을 찾는다.

-- 균형 트리 페이지 분할
--  인덱스로 인해 페이지를 분할 하기 때문에 C.R.U.D.가 느려진다.
--  노드 페이지에서 INSERT 
--  1. 노드 페이지 추가 - 문제 X

--  그러나 루트 페이지에서 INSERT할 때 
--  1. 추가된 루트 페이지 데이터
--  2. 새로운 노드 페이지 생성 추가

--  만약 루트페이지의 마지막에 INSERT되면 
--  1. 루트 페이지 분할로 전체 데이터를 가진 새로운 루트페이지 생성
--  2. 기존 루트페이지는 중간 페이지 이동 (기존 루트페이지 + 새로은 페이지)
--  3. 새로운 중간 페이지로 인해 하위에 새로운 노드 페이지가 만들어진다.


-- 두개의 인덱스 중 뭐가 다른가?
USE market_db;
DROP TABLE IF EXISTS cluster;
CREATE TABLE cluster (
    mem_id  CHAR(8),
    mem_name VARCHAR(10)
);
INSERT INTO cluster VALUES ('TWC', '트와이스');
INSERT INTO cluster VALUES ('BLK', '블랙핑크');
INSERT INTO cluster VALUES ('WMN', '여자친구');
INSERT INTO cluster VALUES ('OMY', '오마이걸');
INSERT INTO cluster VALUES ('GRL', '소녀시대');
INSERT INTO cluster VALUES ('ITZ', '잇지');
INSERT INTO cluster VALUES ('RED', '레드벨벳');
INSERT INTO cluster VALUES ('APN', '에이핑크');
INSERT INTO cluster VALUES ('SPC', '우주소녀');
INSERT INTO cluster VALUES ('MMU', '마마무');
SELECT * FROM cluster;

ALTER TABLE cluster
    ADD CONSTRAINT
    PRIMARY KEY (mem_id);
--  -> 리프 페이지가 정렬 되어 생성


-- secondary index
DROP TABLE IF EXISTS second;
CREATE TABLE second (
    mem_id  CHAR(8),
    mem_name VARCHAR(10)
);
INSERT INTO second VALUES ('TWC', '트와이스');
INSERT INTO second VALUES ('BLK', '블랙핑크');
INSERT INTO second VALUES ('WMN', '여자친구');
INSERT INTO second VALUES ('OMY', '오마이걸');
INSERT INTO second VALUES ('GRL', '소녀시대');
INSERT INTO second VALUES ('ITZ', '잇지');
INSERT INTO second VALUES ('RED', '레드벨벳');
INSERT INTO second VALUES ('APN', '에이핑크');
INSERT INTO second VALUES ('SPC', '우주소녀');
INSERT INTO second VALUES ('MMU', '마마무');
SELECT * FROM second;

ALTER TABLE second
    ADD CONSTRAINT
   UNIQUE (mem_id);
-- -> 데이터 페이지(찾아보기 기능)가 변화 X (정렬 X) , 루트페이지 생성, 리프 페이지는 데이터 페이지를 정렬, 

-- 두개의 인덱스는 어떻게 검색하는가?
--  클러스터 인덱스 (영어 사전)
--      1. 루트 페이지에서 검색
--      2. 리프 페이지(데이터 페이지)에서 검색

--  보조 인덱스 (사전의 찾아보기)
--      1. 루트 페이지에서 검색
--      2. 리프 페이지(찾아보기)에서 검색
--      3. 데이터 페이지에서 검색

-- 효율 : 클러스터 > 보조