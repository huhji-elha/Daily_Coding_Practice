"""
https://programmers.co.kr/learn/courses/30/lessons/72410


카카오 아이디의 규칙입니다.

아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.


1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

"""
import re

# 나의 풀이 01
def solution(new_id):
    def _is_name_ok(new_id):
        _ok = 1
        if len(new_id) < 3 or len(new_id) > 15:
            _ok = 0
        if len(re.sub("[a-z0-9._\-]","",new_id)) > 0:
            _ok = 0
        if ".." in new_id or "." in [new_id[0], new_id[-1]]:
            _ok = 0
        return _ok
    
    if _is_name_ok(new_id):
        return new_id
    else:
        # 1
        new_id = new_id.lower()
        # 2
        new_id = re.sub("[^a-z0-9._\-]","",new_id)
        # 3
        new_id = re.sub(r"((\.)\2+)",".",new_id)

        # 4
        if new_id[-1] == ".":
            new_id = new_id[:-1]
        if len(new_id) > 0 and new_id[0] == ".":
            new_id = new_id[1:]
        
        # 5번과 6번 조건은 결합할 수 있다.
        # 5
        if len(new_id) == 0:
            new_id = "a"

        # 6
        if len(new_id) > 15:
            new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
        
        # 7
        if len(new_id) < 3:
            new_id = new_id + (3 - len(new_id))*new_id[-1]
    return new_id

# 정규표현식을 더 사용하여 코드 줄이기
# 신규 아이디가 성립되는 규칙은 변환 규칙에 포함되어 있으므로 따로 함수화하지 않기. (중복 코드 제거)
# 나의 풀이 02
def solution(new_id):
    new_id = new_id.lower() 
    new_id = re.sub("[^a-z0-9._\-]","",new_id)
    new_id = re.sub("\.+",".",new_id)
    new_id = re.sub("^[.]|[.]$","", new_id)
    new_id = "a" if len(new_id) == 0 else new_id[:15]
    new_id = re.sub("^[.]|[.]$","", new_id)
    new_id = new_id if len(new_id) > 2 else new_id + (3 - len(new_id))*new_id[-1]
    return new_id 