'''
백준 2149 암호 해독

문제 해석
입력 - 키 | 암호문 모두 영어 대문자, len(암호문) = len(키)*n
출력 - 평문(암호화 전 문장) 출력

문제 풀이 절차
아이디어
키와 평문으로 암호문을 만든것을 반대 순서로 해주면 됨

평문을 암호문으로 바꾸는 과정
키를 정렬하여 나열 동일 문자의 경우 원래 키에서 먼저 나온 문자가 앞에 위치
키를 행으로 평문을 열을 맞춰 나열한다.
열순으로 평문을 뽑으면 암호문이 된다.


'''
key = input()
code = input()

def decrypted(key, code):
    length = len(code)
    keylen = len(key)
    sortkey = sorted(key)
    
    keydict = {sortkey[i] : i for i in range(keylen)}
    
    decryptedcode = ''
    
    for i in range(keylen):
        x = keydict[key[i]]
        decryptedcode += code[x : length : keylen]
    
    return decryptedcode

decryptedcode = decrypted(key, code)

'''
역순으로 잘 한것 같은데 안돌아 간다.
어디서 틀렸는지 감도 안오는'''