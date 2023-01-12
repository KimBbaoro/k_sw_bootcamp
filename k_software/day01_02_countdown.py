import time
#snake : '_' 의 사용 -> 평소 내가 쓰던 방식.
#cammel : 단어가 달라질 때 대문자를 사용하는거 -> 김승환 교수님이 쓰던 방식
countdown_snake = [5,4,3,2,1,'Hey!']
countdownCammel = [5,4,3,2,1,'Hey!']

for countdown in 5,4,3,2,1,'Hey!':
    #time.sleep(1)
    print(countdown)

print(countdown_snake[3])
print(countdown_snake[-1])

print('program over')

