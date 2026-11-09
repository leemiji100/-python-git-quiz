import json  # JSON 파일을 읽고 쓰는 도구
from pathlib import Path  # 파일 위치를 다루는 도구

from quiz import Quiz, make_quiz_from_dict
from default_quizzes import get_default_quizzes

# 프로젝트 폴더(이 파일이 있는 곳)에 있는 state.json
STATE_FILE = Path(__file__).parent / "state.json"


class QuizGame:
    """게임 전체를 관리하는 클래스(게임 진행자)예요."""

    def __init__(self):
        """게임을 처음 만들 때 실행돼요."""
        self.quizzes = []        # 퀴즈 목록
        self.best_score = None   # 최고 점수 (None = 아직 안 풀었음)
        self.load_state()        # 저장 파일에서 불러오기

    # ========== 파일 저장/불러오기 ==========

    def load_state(self):
        """state.json에서 퀴즈와 최고 점수를 불러와요."""
        # 1) 파일이 없을 때 (처음 실행)
        if not STATE_FILE.exists():
            print("📂 저장된 데이터가 없어서 기본 퀴즈로 시작해요.")
            self.quizzes = get_default_quizzes()
            self.best_score = None
            return

        # 2) 파일이 있으면 읽어보기 (망가져 있으면 except로!)
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            quizzes = []
            for item in data["quizzes"]:
                quizzes.append(make_quiz_from_dict(item))

            best_score = data["best_score"]
            if best_score is not None and not isinstance(best_score, int):
                raise ValueError("최고 점수가 이상해요")

        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("⚠️ 저장 파일이 망가져 있어요. 기본 퀴즈로 다시 시작할게요.")
            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.save_state()  # 깨끗한 파일로 다시 저장
            return

        # 3) 잘 읽었으면 게임에 넣기
        self.quizzes = quizzes
        self.best_score = best_score
        score_text = "없음" if best_score is None else f"{best_score}점"
        print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, 최고점수 {score_text})")

    def save_state(self):
        """퀴즈와 최고 점수를 state.json에 저장해요."""
        quiz_list = []
        for quiz in self.quizzes:
            quiz_list.append(quiz.to_dict())

        data = {
            "quizzes": quiz_list,
            "best_score": self.best_score,
        }

        try:
            with open(STATE_FILE, "w", encoding="utf-8") as file:
                # ensure_ascii=False: 한글이 깨지지 않게 / indent=4: 보기 좋게 줄 맞추기
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError:
            print("⚠️ 파일에 저장하지 못했어요.")

    # ========== 입력 도우미 (문지기들) ==========

    def get_number(self, message, min_num, max_num):
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

    def get_text(self, message):
        """빈칸이 아닌 글자를 받을 때까지 계속 물어봐요."""
        while True:
            text = input(message).strip()

            if text == "":
                print("⚠️ 아무것도 입력하지 않았어요. 다시 입력하세요.")
                continue

            return text

    # ========== 화면 ==========

    def show_menu(self):
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

    # ========== 기능들 ==========

    def play_quiz(self):
        """퀴즈를 하나씩 내고, 최고 점수와 비교해요."""
        # 퀴즈가 하나도 없을 때
        if len(self.quizzes) == 0:
            print("\n📭 아직 등록된 퀴즈가 없어요. 먼저 퀴즈를 추가해 주세요!\n")
            return

        total = len(self.quizzes)
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)\n")
        correct_count = 0  # 맞힌 개수를 세는 변수

        for number, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            quiz.show(number)
            user_answer = self.get_number("정답 입력: ", 1, 4)

            if quiz.is_correct(user_answer):
                print("✅ 정답입니다!\n")
                correct_count += 1
            else:
                right_text = quiz.choices[quiz.answer - 1]
                print(f"❌ 아쉬워요! 정답은 {quiz.answer}번 ({right_text})이에요.\n")

        score = correct_count * 100 // total  # 100점 만점으로 바꾸기
        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")

        # 최고 점수보다 높으면 바꾸고 저장해요
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
            self.save_state()
        print("=" * 40 + "\n")

    def add_quiz(self):
        """사용자에게 새 퀴즈를 입력받아 목록에 추가하고 저장해요."""
        print("\n📌 새로운 퀴즈를 추가합니다.\n")

        question = self.get_text("문제를 입력하세요: ")

        # 보기 4개를 하나씩 받아서 리스트에 담아요
        choices = []
        for i in range(1, 5):
            choice = self.get_text(f"선택지 {i}: ")
            choices.append(choice)

        answer = self.get_number("정답 번호 (1-4): ", 1, 4)

        # 붕어빵 틀로 새 퀴즈를 찍어내서 목록에 넣고 저장해요
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print(f"\n✅ 퀴즈가 추가되었습니다! (지금 퀴즈는 모두 {len(self.quizzes)}개)\n")

    def list_quizzes(self):
        """등록된 퀴즈 문제들을 번호와 함께 보여줘요."""
        if len(self.quizzes) == 0:
            print("\n📭 아직 등록된 퀴즈가 없어요.\n")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40 + "\n")

    def show_score(self):
        """최고 점수를 보여줘요."""
        if self.best_score is None:
            print("\n🙈 아직 퀴즈를 풀지 않았어요. 1번을 눌러 도전해 보세요!\n")
        else:
            print(f"\n🏆 최고 점수: {self.best_score}점\n")

    # ========== 게임 진행 ==========

    def run(self):
        """메뉴를 보여주고, 고른 번호에 맞는 일을 해요."""
        while True:
            self.show_menu()
            choice = self.get_number("선택: ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                self.save_state()
                print("\n💾 저장 완료! 👋 게임을 종료합니다. 다음에 또 만나요!")
                break