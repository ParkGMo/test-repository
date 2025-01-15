# import pymysql

# 1. MYSQL 연결하기
# conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='soloDB', charset='utf8')

# 2. 커서 생성하기 -  커서이름 = 연결자.cursor()
# cur = conn.cursor()

# 3. 테이블 만들기 - 커서이름.execute('CREATE TABLE 문장)
# cur.execute('CREATE TABLE userTable (id CHAR(4), userName CHAR(15), email CHAR(20), brithYear INT)') 
# # 0이 나오면 성공

# 4. 데이터 입력 - 커서이름.execute('INSERT 문장')
# cur.execute("INSERT INTO userTable VALUES ('hong', '홍지윤', 'hong@naver.com', 1996)")
# # 1이 나오면 한개의 행이 들어갔다!

# cur.execute("INSERT INTO userTable VALUES ('kim', '김태연', 'kim@daum.net', 2011)")
# cur.execute("INSERT INTO userTable VALUES ('star', '별사랑', 'star@paran.com', 1990)")
# cur.execute("INSERT INTO userTable VALUES ('yang', '양지은', 'yang@gmail.com', 1993)")

# 5. 입력한 데이터 저장하기 - 연결자.commit()
# conn.commit()

# 6. MYSQL 연결 종료하기 - 연결자.close()
# conn.close()


# 완전한 입력프로그램 제작
import pymysql

# 전역변수 선언부
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='soloDB', charset='utf8')
cur = conn.cursor()

while (True):
    data1 = input("사용자 ID ==> ")
    if data1 == "" :
        break;
    
    data2 = input("사용자 이름 ==> ")
    data3 = input("사용자 이메일 ==> ")
    data4 = input("사용자 출생연도 ==> ")

    sql = f"INSERT INTO userTable VALUES ('{data1}', '{data2}', '{data3}', '{data4}')"

    cur.execute(sql)

conn.commit()

cur.close()