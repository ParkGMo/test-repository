# Quiz 1 L=[1,2,3,4,5]일때 다음 두개 코드가 어떤 결과를 내겠는가? \
# >>>L[1:3]=[100]
L=[1,2,3,4,5]
L[1:3]=100
print(L)

# Quiz 1 L=[1,2,3,4,5]일때 다음 두개 코드가 어떤 결과를 내겠는가? \
# >>>L[1:3]=[100]
L=[1,2,3,4,5]
L[1:3]=100
print(L)

# Quiz 2 다음 두 개의 치환문이 수행하는 절차를 설명하라. 두 번째 문에 의해서 a의 레퍼런스가 변경되었는가?
# >>>a=[1,2,3]
# >>>a[:]=[4,5,6,]
a=[1,2,3]
a[:]=4,5,6
print(a)  

# 다음 각 물음에 답하시오.
# >>>a=[1,2,3]
# >>>b=[a*3]
# >>>c=[a]*3
a=[1,2,3]
b=[a*3]
c=[a]*3

# 가) 다음 b,c의 차이는 무엇인가?
print(b) 
print(c)

# 나) 다음 코드를 수행한 후에 b와 c는 어떻게 변화하겠는가?
# >>>a[0]=0
a[0]=0
print(a)
# 다) 그렇게 변화한 이유를 설명하라.

# 라) 코드 >>> c=[a[:]]*3는 위의 c와 어떻게 다른가?
print(c)
c=[a[:]]*3
print(c)

# 마) 다음 코드는 또 어떻게 다른가? >>> c=[a[:],a[:],a[:]]
c=[a[:],a[:],a[:]]
print(c)

# Quiz 5 다음 리스트 L을 5로 나눈 나머지를 기준으로 정렬하라.
# L=range(10)
# result=[]
# for i in L:
#     result.append(i%5)
# L.sort(key=result)
L=list(range(10))
def a (x):
    return x%5

L.sort(key=a)
print(L)
# Quiz 6 다음 각 물음에 답하시오.
# >>> a=[1]
# >>> b=[2]
# >>> a.append(b)
# >>> b.append(a)
# 가) 위 코드의 자료 구조를 그림으로 그려 보아라.  a=[1,2] , b=[2,1]
# 나) 값을 출력해 보라. 어떤 결과가 나오는가?
a=[1]
b=[2]
a.append(b)
b.append(a)
print(a)   
print(b) 

# 다) 객체 a의 레퍼런스 카운트 값은 얼마인가?
# >>>sys.getrefcount(a)
import sys 
sys.getrefcount(a)

# 라) 객체 b를 지웠다. 객체 a의 레퍼런스 카운트 값은 얼마인가?
del b
import sys 
sys.getrefcount(a)

# 마) 객체 b를 삭제한 구조를 그림으로 그려라. a 값을 출력해 보라. 구조가 맞는가?
del b
import sys 
sys.getrefcount(a)
print(a)

# 바) a를 삭제하였다. 무슨 문제가 발생하겠는가? 설명해 보라.
del b
del a
import sys 
sys.getrefcount(a)
print(a)

# Quiz 7 문자열 리스트가 있다. 리스트의 sort 메쏘드를 이용하여 이들을 정렬하라. 단, 대 소문자 구별하지 않는다.
s=['what is the name of ', 'the function you wish to call ', 'and what is the name of the ']
a=s.sort()
print(a)

# Quiz 8 다음 문자열을 ‘:‘를 기준으로 분리하여 리스트로 만들고, 각 문자열의 좌우의 공백을 제거하라. 즉, 다음 문자열 s에서 L을 만들어라(for 문 이용)
# s=' first item : second item : third item '
# L= ['first item,second item,third item']
s='first item : second item : third item'
L=s.replace(' : ',',').replace(' f','').replace('m','')
L=[]
for i in s.split(' : '):
    L.append(i.strip())
print(L)

# Quiz 9 문제 8번을 리스트 내장을 이용하여 한 줄로 해결하라.
[i.strip() for i in s.split(':')]

# 6강
# Quiz 1 다음 코드를 수행했을 때 객체들 간의 관계를 그래프로 그려 보아라. s는 1,2,4라는 세 개의 객체를 추가로 가지는가? 메모리의 사용이 얼마나 증가하는가?
t=(1,2,3,4)
s=t[:2]+t[3:]
print(s)

# Quiz 2 다음과 같은 코드가 있다. 일요일부터 토요일까지 0-6의 값을 할당받았다. 
# Print Sun,Mon에 의해서 0과1이 출력될 것이다. Weekday에 입력된 값이 ‘Sun’,’Mon’등의 문자열일 때 
# 이것을 정수 0, 1로 변환해서 출력하도록 마지막 print 문을 완성하라.(힌트 : globals()를 이용하라.)
# Sun, Mon, Tue, Wed, Thu, Fri, Sat = range(7)
# print Sun, Mon #0, 1
# weekday = raw_input(“요일 하나를 입력하세요:“)
# print
Sun, Mon, Tue, Wed, Thu, Fri, Sat = range(7)
globals()['Sun']
globals()['Mon']

# Quiz 3 다음 코드는 10장 함수에서 설명될 가변 인수에 관한 내용이다.
# >>> def varge(*args):
#   print args

# >>> vargs(1)
# (1,)
# >>>vargs(1,3,5,7)
# (1,3,5,7)

# Quiz 3 다음 코드는 10장 함수에서 설명될 가변 인수에 관한 내용이다.
def vargs(*args):
    print (args)

vargs(1)
vargs(1,3,5,7)

# 이 코드를 수정하여 다음과 같은 연산이 가능하도록 addall()함수를 만들어라.
# >>> addall(1)
# (1)
# >>> addall(1,2,3,4)
# 10

def addall(*args):
    return sum(args)
print (addall(1))
print (addall(1,2,3,4))

# 7강
# Quiz 1 사전의 키로 사용될 수 있는 자료는 어떤 것들이 있는지 시험해 보라. 예를 들어 다음과 같이 사용할 수 있는가?
d={}
d[(1,2,3)]=10
d[[1,2,3]]=10
d[{1:2,3:4}]=10

# Quiz 2 사전의 값으로 사용될 수 있는 자료형에 어떤 제약이 있는지 조사해 보라. 다음이 모두 가능한가?
d[10]=[1,2,3]
print(d)
d[10]=(1,2,3)
print(d)
d[10]={1:2,3:4}
print(d)

# Quiz 1 다음 두개 코드의 차이를 설명하라.
a=d
a=d.copy()
# Quiz 2 다음 두개 코드의 차이를 설명하라.
del d['a']
d['a']=None


# Quiz 1 다음과 같은, if 문을 대신할 수 있는 코드를 사전을 이용해서 작성하라.
# if menuselection == 'odeng':
#   price=300
# elif menuselection == 'sundae':
#   price=400
# elif menuselection == 'mandu':
#   price=500
# else:
#   price=0

menu = {'odeng': 300, 'sundae': 400, 'mandu':500}
menu.get('odeng',0)
menu.get('bread',0)

# Quiz 3 다음 코드를 수행했을 경우에 e와 f의 출력 결과를 예측해 보아라.
L1=[1,2,3]
L2={4,5,6}
d={'low':L1, 'high':L2}
e=d
f=d.copy()
d['low']=[10,20,30]
d['high'][1]=500
print(e)
print(f)
