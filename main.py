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


def main():
    """게임을 시작해요."""
    while True:
        show_menu()
        choice = get_number("선택: ", 1, 5)

        if choice == 1:
            print("\n📝 퀴즈 풀기는 곧 만들 거예요!\n")
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