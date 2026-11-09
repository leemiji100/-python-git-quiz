# 🎯 Python & Git 기초 퀴즈 게임

## 프로젝트 개요

터미널에서 동작하는 퀴즈 게임입니다. 메뉴에서 번호를 골라 퀴즈를 풀고, 새 퀴즈를 추가하고, 목록과 최고 점수를 확인할 수 있습니다.
추가한 퀴즈와 최고 점수는 `state.json` 파일에 저장되어, 프로그램을 껐다 켜도 그대로 남아 있습니다.

## 퀴즈 주제와 선정 이유

**주제: Python & Git 기초 상식**

이번 미션에서 배우는 내용(자료형, 반복문, 함수, 클래스, Git 명령어)을 직접 퀴즈로 만들면,
퀴즈를 만드는 과정과 푸는 과정 모두가 복습이 된다고 생각해서 이 주제를 골랐습니다.

## 실행 방법

Python 3.10 이상이 필요합니다. 외부 라이브러리는 사용하지 않습니다.

```bash
git clone https://github.com/leemiji100/-python-git-quiz.git
cd ./-python-git-quiz
python3 main.py
```

> Windows에서는 `python3` 대신 `python main.py`로 실행할 수도 있습니다.

## 기능 목록

| 번호 | 기능 | 설명 |
|---|---|---|
| 1 | 퀴즈 풀기 | 저장된 퀴즈를 순서대로 풀고, 정답/오답과 최종 점수를 보여줍니다. 최고 점수를 넘으면 갱신합니다. |
| 2 | 퀴즈 추가 | 문제, 선택지 4개, 정답 번호를 입력받아 새 퀴즈를 등록하고 파일에 저장합니다. |
| 3 | 퀴즈 목록 | 등록된 퀴즈의 문제를 번호와 함께 보여줍니다. |
| 4 | 점수 확인 | 최고 점수를 보여줍니다. 아직 풀지 않았으면 안내 메시지를 보여줍니다. |
| 5 | 종료 | 데이터를 저장하고 프로그램을 끝냅니다. |

### 입력 및 예외 처리

- 입력 앞뒤 공백을 지우고 처리합니다.
- 숫자가 아닌 입력(`abc`), 범위 밖 숫자(`9`, `0`), 빈 입력(그냥 Enter)은 안내 메시지를 보여주고 다시 입력받습니다.
- `Ctrl+C`나 입력 종료(EOF)가 발생해도 데이터를 저장하고 안전하게 종료합니다.
- `state.json`이 없으면 기본 퀴즈로 시작하고, 손상되었으면 안내 후 기본 퀴즈로 복구합니다.

## 파일 구조

```
python-git-quiz/
├── main.py              # 프로그램 시작 파일 (QuizGame 실행, Ctrl+C 처리)
├── quiz_game.py         # QuizGame 클래스: 메뉴, 게임 진행, 파일 저장/불러오기
├── quiz.py              # Quiz 클래스: 퀴즈 한 문제 (문제, 선택지, 정답)
├── default_quizzes.py   # 기본 퀴즈 8개
├── state.json           # 저장 데이터 (실행하면 자동 생성)
├── .gitignore
└── README.md
```

### 클래스 설계

| 클래스 | 역할 | 주요 속성 | 주요 메서드 |
|---|---|---|---|
| `Quiz` | 퀴즈 한 문제 | `question`, `choices`, `answer` | `show()`, `is_correct()`, `to_dict()` |
| `QuizGame` | 게임 전체 관리 | `quizzes`, `best_score` | `run()`, `play_quiz()`, `add_quiz()`, `list_quizzes()`, `show_score()`, `load_state()`, `save_state()` |

## 데이터 파일 설명 (state.json)

- **경로:** 프로젝트 루트의 `state.json`
- **역할:** 퀴즈 목록과 최고 점수를 저장해서, 프로그램을 다시 실행해도 데이터가 유지되게 합니다.
- **인코딩:** UTF-8
- **저장 시점:** 퀴즈 추가 후, 최고 점수 갱신 후, 프로그램 종료 시

### 스키마

| 키 | 자료형 | 설명 |
|---|---|---|
| `quizzes` | list | 퀴즈 목록 |
| `quizzes[].question` | str | 문제 |
| `quizzes[].choices` | list (str 4개) | 선택지 4개 |
| `quizzes[].answer` | int (1~4) | 정답 번호 |
| `best_score` | int 또는 null | 최고 점수 (100점 만점, 아직 안 풀었으면 null) |

### 예시

```json
{
    "quizzes": [
        {
            "question": "Python에서 화면에 글자를 보여주는 함수는?",
            "choices": ["input", "print", "len", "int"],
            "answer": 2
        }
    ],
    "best_score": 75
}
```

## Git 작업 기록

- 기능 단위로 커밋했습니다. (메뉴 → Quiz 클래스 → 기본 퀴즈 → 퀴즈 풀기 → 추가 → 목록 → 점수 → 구조 정리 → 파일 저장 → README)
- 퀴즈 풀기 기능은 `feature/play-quiz` 브랜치에서 작업한 뒤 `main`에 병합했습니다.
- 사용한 Git 명령어: `init`, `add`, `commit`, `push`, `checkout`, `merge`, `clone`, `pull`- clone한 저장소에서 추가한 줄입니다. (clone/pull 실습)
