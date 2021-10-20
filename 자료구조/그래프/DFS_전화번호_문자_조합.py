"""
2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자열 출력

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

"""

# 아이디어 : 재귀 함수를 사용하여 조합 작성하기
# 첫번째 풀이
# Runtime : 50 ms
# Memory : 14.4 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        def combination(start_idx, letter):
            if len(letter) == len(digits):
                answer.append(letter)
                return
            for i in range(start_idx,len(digits)):
                for j in letters[digits[start_idx]]:
                    combination(i+1, letter+j)

        letters = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        if not digits:
            return answer
        combination(0,"")
        return answer
    
# 아이디어02 : python의 itertools.product 사용하기
# 하나의 리스트에서 조합을 구할 때 : itertools.combinations
# 두 개 이상의 리스트에서 조합을 구할 때 : itertools.product(*list)
# Runtime : 54 ms
# Memory : 13.9 MB
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        if not digits:
            return []
        return list(map(lambda x:''.join(x), product(*[letters[i] for i in digits])))
