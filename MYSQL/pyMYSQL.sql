-- 세팅!
-- ctrl + R
-- cmd
-- pip install pymysql

-- IDLE Shell 열기

CREATE DATABASE soloDB;

-- 파이썬 IDLE 실행 - 연결자 = pymysql.connect(연결옵션)

-- 1. MYSQL 연결하기 

-- 2. 커서 생성하기 -  커서이름 = 연결자.cursor()

-- 3. 테이블 만들기 - 커서이름.execute('CREATE TABLE 문장)

-- 4. 데이터 입력 - 커서이름.execute('INSERT 문장')

-- 5. 입력한 데이터 저장하기 - 연결자.commit()

-- 6. MYSQL 연결 종료하기 - 연결자.close()

USE soloDB;
SELECT * FROM userTable;