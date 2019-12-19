#로또 번호를 랜덤으로 뽑아주는 프로그램
import random

number = range(1,46)
# 마치 [1,2,3,.....,45] 과 비슷하다

# 6개의 숫자를 뽑아 출력해주는 프로그램 작성
lotto = random.sample(number, 6)  #중복없이 범위내에서 출력
print(sorted(lotto))

# alt + shift + 위 or 아래 방향키 : 복사
# alt + 위 or 아래 방향키 : 해당 문장 이동

