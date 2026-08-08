# 프롬프트 데이터
prompts = [
    {
        "title": "블로그 글 작성",
        "content": "SEO 최적화 블로그 글 작성",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "이미지 생성",
        "content": "귀여운 고양이 이미지를 생성해줘",
        "category": "이미지 생성",
        "favorite": True
    },
    {
        "title": "뉴스 요약",
        "content": "오늘 AI 뉴스를 요약해줘",
        "category": "텍스트 생성",
        "favorite": False
    }
]


def show_menu():
    print()
    print("=" * 40)
    print("        나만의 프롬프트 관리")
    print("=" * 40)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 추가/해제")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("=" * 40)


def add_prompt():
    print()
    print("=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()

        if title:
            break

        print("제목은 비워둘 수 없습니다.")

    while True:
        content = input("내용: ").strip()

        if content:
            break

        print("내용은 비워둘 수 없습니다.")

    while True:
        category = input("카테고리: ").strip()

        if category:
            break

        print("카테고리는 비워둘 수 없습니다.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("프롬프트가 추가되었습니다.")


def show_list():
    print()
    print("=== 프롬프트 목록 ===")

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = "⭐" if prompt["favorite"] else ""

        print(
            f'{index}. {prompt["title"]} '
            f'[{prompt["category"]}] {favorite_mark}'
        )

def show_by_category():
    print()
    print("=== 카테고리별 조회 ===")
    print("1. 텍스트 생성")
    print("2. 이미지 생성")
    print("3. 영상 생성")
    print("4. 페르소나")
    print("5. 자동화")
    print("6. 기타")

    choice = input("카테고리 선택: ")

    categories = {
        "1": "텍스트 생성",
        "2": "이미지 생성",
        "3": "영상 생성",
        "4": "페르소나",
        "5": "자동화",
        "6": "기타"
    }

    if choice not in categories:
        print("잘못된 카테고리 번호입니다.")
        return

    selected_category = categories[choice]

    print()
    print(f"=== {selected_category} 프롬프트 ===")

    found = False

    for index, prompt in enumerate(prompts, start=1):
        if prompt["category"] == selected_category:
            favorite_mark = "⭐" if prompt["favorite"] else ""

            print(
                f'{index}. {prompt["title"]} '
                f'[{prompt["category"]}] {favorite_mark}'
            )

            found = True

    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")

def search_prompt():
    print()
    print("=== 프롬프트 검색 ===")

    keyword = input("검색어: ").strip()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    print()
    print("=== 검색 결과 ===")

    found = False

    for index, prompt in enumerate(prompts, start=1):
        if (
            keyword.lower() in prompt["title"].lower()
            or keyword.lower() in prompt["content"].lower()
        ):
            favorite_mark = "⭐" if prompt["favorite"] else ""

            print(
                f'{index}. {prompt["title"]} '
                f'[{prompt["category"]}] {favorite_mark}'
            )

            found = True

    if not found:
        print("검색 결과가 없습니다.")

def main():
    while True:
        show_menu()

        choice = input("메뉴 선택: ")

        if choice == "1":
            add_prompt()

        elif choice == "2":
            show_list()

        elif choice == "3":
            show_by_category()

        elif choice == "4":
            search_prompt()

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("아직 구현되지 않은 메뉴입니다.")


if __name__ == "__main__":
    main()