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

    def to_dict(self):
        """퀴즈를 파일에 저장할 수 있는 딕셔너리 모양으로 바꿔요."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }


def make_quiz_from_dict(data):
    """파일에서 읽은 딕셔너리로 퀴즈를 다시 만들어요. 모양이 이상하면 에러를 내요."""
    question = data["question"]
    choices = data["choices"]
    answer = data["answer"]

    if not isinstance(question, str) or not isinstance(choices, list) or len(choices) != 4:
        raise ValueError("퀴즈 모양이 이상해요")
    if not isinstance(answer, int) or answer < 1 or answer > 4:
        raise ValueError("정답 번호가 이상해요")

    return Quiz(question, choices, answer)


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