# 회문 : 왼쪽에서 읽었을 때와 오른쪽에서 읽었을 때 같은 문자열
# => abcecba

a = 'abcdcba1'
print(a, ": 회문" if a==a[::-1] else ": 회문 아님")
print('-' * 20)

# if-else 사용
if a == a[::-1] : print(a, ": 회문")
else : print(a, ": 회문 아님")
    
