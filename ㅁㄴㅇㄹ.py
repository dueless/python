import random

def number_guessing_game():
    # 1부터 100까지의 숫자 중 무작위로 하나를 선택합니다.
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("1부터 100까지의 숫자 중 하나를 맞춰보세요!")

    # 사용자가 정답을 맞출 때까지 반복합니다.
    while guess != secret_number:
        try:
            # 사용자로부터 입력을 받습니다.
            guess = int(input("숫자를 입력하세요: "))
            attempts += 1

            # 입력한 숫자가 정답보다 높은지 낮은지 알려줍니다.
            if guess < secret_number:
                print("더 큰 숫자입니다.")
            elif guess > secret_number:
                print("더 작은 숫자입니다.")
        except ValueError:
            # 숫자가 아닌 값을 입력했을 때의 예외 처리
            print("유효한 숫자를 입력하세요.")

    # 정답을 맞췄을 때의 메시지
    print(f"정답입니다! {attempts}번 만에 맞췄어요.")

# 게임을 시작합니다.
if __name__ == "__main__":
    number_guessing_game()