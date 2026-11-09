from quiz import Quiz  # quiz.py에 있는 Quiz 틀을 가져와요


def get_default_quizzes():
    """처음 실행할 때 쓰는 기본 퀴즈 목록을 돌려줘요."""
    return [
        Quiz(
            "Python에서 화면에 글자를 보여주는 함수는?",
            ["input", "print", "len", "int"],
            2,
        ),
        Quiz(
            "True와 False, 두 가지 값만 가지는 자료형은?",
            ["int", "str", "list", "bool"],
            4,
        ),
        Quiz(
            "몇 번 반복할지 정해져 있을 때 주로 쓰는 반복문은?",
            ["for", "while", "if", "def"],
            1,
        ),
        Quiz(
            "Python에서 함수를 만들 때 쓰는 키워드는?",
            ["class", "def", "return", "import"],
            2,
        ),
        Quiz(
            "클래스로 객체를 만들 때 자동으로 실행되는 메서드는?",
            ["__init__", "__main__", "__str__", "__call__"],
            1,
        ),
        Quiz(
            "작업한 내용을 사진처럼 기록하는 Git 명령어는?",
            ["git add", "git commit", "git push", "git clone"],
            2,
        ),
        Quiz(
            "GitHub에 있는 변경사항을 내 컴퓨터로 가져오는 명령어는?",
            ["git push", "git pull", "git init", "git status"],
            2,
        ),
        Quiz(
            "새 Git 저장소를 처음 만드는 명령어는?",
            ["git start", "git new", "git make", "git init"],
            4,
        ),
    ]


# 이 파일만 따로 실행했을 때 테스트해보는 부분이에요
if __name__ == "__main__":
    quizzes = get_default_quizzes()
    print(f"기본 퀴즈는 모두 {len(quizzes)}개예요!\n")
    for number, quiz in enumerate(quizzes, start=1):
        quiz.show(number)