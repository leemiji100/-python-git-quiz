from quiz_game import QuizGame  # 게임 진행자 클래스 가져오기


def main():
    """게임 진행자를 만들고 게임을 시작해요."""
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C를 눌러도 저장하고 안전하게 끝나요
        game.save_state()
        print("\n\n💾 저장 완료! 👋 게임을 종료합니다. 다음에 또 만나요!")


main()