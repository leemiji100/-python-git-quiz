from default_quizzes import get_default_quizzes  # 기본 퀴즈 8개 가져오기


def show_menu():
    """메뉴 화면을 보여줘요."""
    print("=" * 40)
    print("     🎯 Python & Git 기초 퀴즈 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def get_number(message, min_num, max_num):
    """min_num부터 max_num 사이의 숫자를 받을 때까지 계속 물어봐요."""
    while True:
        text = input(message).strip()  # strip(): 앞뒤 빈칸 지우기

        # 그냥 Enter만 눌렀을 때
        if text == "":
            print(f"⚠️ 아무것도 입력하지 않았어요. {min_num}-{max_num} 사이의 숫자를 입력하세요.")
            continue

        # 글자를 숫자로 바꿔보기 (abc처럼 숫자가 아니면 실패!)
        try:
            number = int(text)
        except ValueError:
            print(f"⚠️ 숫자만 입력할 수 있어요. {min_num}-{max_num} 사이의 숫자를 입력하세요.")
            continue

        # 숫자이긴 한데 범위 밖일 때 (예: 9)
        if number < min_num or number > max_num:
            print(f"⚠️ 잘못된 번호예요. {min_num}-{max_num} 사이의 숫자를 입력하세요.")
            continue

        return number  # 통과! 숫자를 돌려줘요


def play_quiz(quizzes):
    """퀴즈를 하나씩 내고, 맞힌 개수를 세요."""
    # 퀴즈가 하나도 없을 때
    if len(quizzes) == 0:
        print("\n📭 아직 등록된 퀴즈가 없어요. 먼저 퀴즈를 추가해 주세요!\n")
        return

    print(f"\n📝 퀴즈를 시작합니다! (총 {len(quizzes)}문제)\n")
    correct_count = 0  # 맞힌 개수를 세는 변수

    for number, quiz in enumerate(quizzes, start=1):
        print("-" * 40)
        quiz.show(number)
        user_answer = get_number("정답 입력: ", 1, 4)  # 문지기 함수 재활용!

        if quiz.is_correct(user_answer):
            print("✅ 정답입니다!\n")
            correct_count += 1  # 맞힌 개수 1 늘리기
        else:
            right_text = quiz.choices[quiz.answer - 1]
            print(f"❌ 아쉬워요! 정답은 {quiz.answer}번 ({right_text})이에요.\n")

    score = correct_count * 100 // len(quizzes)  # 100점 만점으로 바꾸기
    print("=" * 40)
    print(f"🏆 결과: {len(quizzes)}문제 중 {correct_count}문제 정답! ({score}점)")
    print("=" * 40 + "\n")


def main():
    """게임을 시작해요."""
    quizzes = get_default_quizzes()  # 퀴즈 목록 준비

    while True:
        show_menu()
        choice = get_number("선택: ", 1, 5)

        if choice == 1:
            play_quiz(quizzes)
        elif choice == 2:
            print("\n📌 퀴즈 추가는 곧 만들 거예요!\n")
        elif choice == 3:
            print("\n📋 퀴즈 목록은 곧 만들 거예요!\n")
        elif choice == 4:
            print("\n🏆 점수 확인은 곧 만들 거예요!\n")
        elif choice == 5:
            print("\n👋 게임을 종료합니다. 다음에 또 만나요!")
            break  # while 반복 멈추기


# Ctrl+C를 눌러도 에러 없이 끝나게 해줘요
try:
    main()
except (KeyboardInterrupt, EOFError):
    print("\n\n👋 게임을 종료합니다. 다음에 또 만나요!")