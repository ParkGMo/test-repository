# 3.7 연습문제: 문자열 출력하기
print('Hello, world!')
print('Python Programming')

# 5.5 연습문제: 아파트에서 소음이 가장 심한 층수 출력하기
# 국립환경과학원에서는 아파트에서 소음이 가장 심한 층수를 구하는 계산식을 발표했습니다. 
# 소음이 가장 심한 층은 0.2467 * 도로와의 거리(m) + 4.159입니다. 
# 다음 소스 코드를 완성하여 소음이 가장 심한 층수가 출력되게 만드세요. 
# 단, 층수를 출력할 때는 소수점 이하 자리는 버립니다(정수로 출력).
print(int(0.2467 * 12 + 4.159))

# 6.6 연습문제: 정수 세 개를 입력받고 합계 출력하기
# 다음 소스 코드를 완성하여 정수 세 개를 입력받고 합계가 출력되게 만드세요.
# -10 20 30 (입력)
# 40
a=-10
b=20
c=30
print(a + b + c)
a, b, c = map(int, input().split())

# 7.4 연습문제: 날짜와 시간 출력하기
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
 
print(f'{year}/{month}/{day} {hour}:{minute}:{second}')

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')
# 결과 : 2000/10/27 11:43:59

# 8.4 연습문제: 합격 여부 출력하기
# 국어, 영어, 수학, 과학 점수가 있을 때 한 과목이라도 50점 미만이면 불합격이라고 정했습니다. 
# 다음 소스 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되게 만드세요.
korean = 92
english = 47
mathematics = 86
science = 81
 
print(korean > 50 and english > 50 and mathematics > 50 and science > 50)
# 정답 false

# 9.3 연습문제: 여러 줄로 된 문자열 사용하기
# 다음 소스 코드를 완성하여 실행 결과대로 문자열이 출력되게 만드세요.
s='''
Python is a programming language that lets you work quickly
and
integrate systems more effectively.
'''

# 10.4 연습문제: range로 리스트 만들기
# 다음 소스 코드를 완성하여 리스트 [5, 3, 1, -1, -3, -5, -7, -9]가 출력되게 만드세요. 
# 리스트를 만들 때는 range를 사용해야 합니다.
a=range(5,-10,-2)
aList=list(a)
print(aList)
# 결과 [5, 3, 1, -1, -3, -5, -7, -9]

# 11.6 연습문제: 최근 3년간 인구 출력하기
# 리스트 year에 연도, population에 서울시 인구수가 저장되어 있습니다. 
# 다음 소스 코드를 완성하여 최근 3년간 연도와 인구수가 리스트로 출력되게 만드세요.
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[5:])
print(population[-3:])
# 결과 [2016, 2017, 2018] [9930616, 9857426, 9838892]

# 11.7 연습문제: 인덱스가 홀수인 요소 출력하기
# 다음 소스 코드를 완성하여 튜플 n에서 인덱스가 홀수인 요소들이 출력되게 만드세요.
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])
print(tuple(n[i] for i in range(len(n)) if i % 2 == 1))
# 결과 (75, -10, 32, -15, 76, 2)

# 12.4 연습문제: 딕셔너리에 게임 캐릭터 능력치 저장하기
# 다음 소스 코드를 완성하여 게임 캐릭터의 체력(health)과 이동 속도(movement speed)가 출력되게 만드세요
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print(camille['health'])
print(camille['movement_speed'])

# 결과 
# 575.6
# 340

# 13.6 연습문제: if 조건문 사용하기
# 다음 소스 코드를 완성하여 x의 값이 10이 아닐 때 'ok'가 출력되게 만드세요.
x = 5
if x!= 10:
    print('ok')

# 결과 ok

# 14.6 연습문제: 합격 여부 판단하기
# A 기업의 입사 시험은 필기 시험 점수가 80점 이상이면서 코딩 시험을 통과해야 합격이라고 정했습니다(코딩 시험 통과 여부는 True, False로 구분). 
# 다음 소스 코드를 완성하여 '합격', '불합격'이 출력되게 만드세요.
written_test = 75
coding_test = True

if written_test >= 80 and coding_test:
    print('합격')
else:
    print('불합격')

# 결과 불합격

# 15.3 연습문제: if, elif, else 모두 사용하기
# 다음 소스 코드를 완성하여 변수 x가 11과 20 사이면 '11~20', 21과 30 사이면 '21~30', 
# 아무것도 해당하지 않으면 '아무것도 해당하지 않음'이 출력되게 만드세요.
x = int(input())
if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

# 결과 
# 5 (입력)
# 아무것도 해당하지 않음

# 16.5 연습문제: 리스트의 요소에 10을 곱해서 출력하기
# 다음 소스 코드를 완성하여 리스트 x에 들어있는 각 숫자(요소)에 10을 곱한 값이 출력되게 만드세요. 
# 모든 숫자는 공백으로 구분하여 한 줄로 출력되어야 합니다.
x = [49, -17, 25, 102, 8, 62, 21]

for num in x:
    print(num * 10, end=" ")
    # print(num * 10)

# 결과 490 -170 250 1020 80 620 210 

# 17.5 연습문제: 변수 두 개를 다르게 반복하기
# 다음 소스 코드를 완성하여 정수 2 5, 4 4, 8 3, 16 2, 32 1이 각 줄에 출력되게 만드세요. 
# while에 조건식은 두 개 지정하고, 두 변수를 모두 변화시켜야 합니다.
i = 2
j = 5

while i <= 32 and j >= 1:
    print(i, j)
    i += 2
    j -= 1


# 결과 
# 2 5
# 4 4
# 8 3
# 16 2
# 32 1
