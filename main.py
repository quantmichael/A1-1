import json

prompts = []

def load_prompts():
    global prompts

    try:
        with open("prompts.json", "r", encoding="utf-8") as file:
            prompts = json.load(file)

    except FileNotFoundError:
        pass

def save_prompts():
    with open("prompts.json", "w", encoding="utf-8") as file:
        json.dump(
            prompts,
            file,
            ensure_ascii=False,
            indent=4
        )

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

    categories = {
        "1": "텍스트 생성",
        "2": "이미지 생성",
        "3": "영상 생성",
        "4": "페르소나",
        "5": "자동화",
        "6": "기타"
    }

    while True:
        print()
        print("=== 카테고리 선택 ===")
        print("1. 텍스트 생성")
        print("2. 이미지 생성")
        print("3. 영상 생성")
        print("4. 페르소나")
        print("5. 자동화")
        print("6. 기타")

        category_choice = input("카테고리 번호: ").strip()

        if category_choice in categories:
            category = categories[category_choice]
            break

        print("1~6 사이의 번호를 입력해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    save_prompts()

    print()
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

def show_detail():
    print()
    print("=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    try:
        number = int(input("상세히 볼 프롬프트 번호: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        return

    if number < 1 or number > len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[number - 1]

    favorite_text = "예" if prompt["favorite"] else "아니오"

    print()
    print("=" * 40)
    print(f'제목       : {prompt["title"]}')
    print(f'카테고리   : {prompt["category"]}')
    print(f'즐겨찾기   : {favorite_text}')
    print("-" * 40)
    print("내용")
    print(prompt["content"])
    print("=" * 40)

def toggle_favorite():
    print()
    print("=== 즐겨찾기 추가/해제 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    try:
        number = int(input("즐겨찾기를 변경할 프롬프트 번호: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        return

    if number < 1 or number > len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[number - 1]

    prompt["favorite"] = not prompt["favorite"]

    save_prompts()
    
    if prompt["favorite"]:
        print(f'"{prompt["title"]}"을(를) 즐겨찾기에 추가했습니다.')
    else:
        print(f'"{prompt["title"]}"을(를) 즐겨찾기에서 해제했습니다.')
        

def show_favorites():
    print()
    print("=== 즐겨찾기 목록 ===")

    found = False

    for index, prompt in enumerate(prompts, start=1):
        if prompt["favorite"]:
            print(
                f'{index}. {prompt["title"]} '
                f'[{prompt["category"]}] ⭐'
            )

            found = True

    if not found:
        print("즐겨찾기한 프롬프트가 없습니다.")
        
def main():
    load_prompts()

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

        elif choice == "5":
            show_detail()

        elif choice == "6":
            toggle_favorite()

        elif choice == "7":
            show_favorites()

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 메뉴 번호입니다.")

if __name__ == "__main__":
    main()