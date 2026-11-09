class Quiz:
    """퀴즈 한 문제를 담는 클래스(붕어빵 틀)예요."""

    def __init__(self, question, choices, answer):
        """퀴즈를 처음 만들 때 실행돼요."""
        self.question = question  # 문제
        self.choices = choices    # 보기 4개 (리스트)
        self.answer = answer      # 정답 번호 (1~4)

    def show(self, number):
        """문제와 보기를 화면에 보여줘요."""
        print(f"[문제 {number}]")
        print(self.question)
        print()
        # enumerate: 보기에 1, 2, 3, 4 번호를 붙여줘요
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
        print()

    def is_correct(self, user_answer):
        """정답이면 True, 틀리면 False를 돌려줘요."""
        return user_answer == self.answer


# 이 파일만 따로 실행했을 때 테스트해보는 부분이에요
if __name__ == "__main__":
    test_quiz = Quiz(
        "Python에서 화면에 글자를 보여주는 함수는?",
        ["input", "print", "len", "int"],
        2,
    )
    test_quiz.show(1)
    print("2번을 고르면:", test_quiz.is_correct(2))
    print("3번을 고르면:", test_quiz.is_correct(3))
    