import json

# 프로그램에서 관리하는 모든 프롬프트를 저장하는 전역 리스트입니다.
# 프롬프트 하나는 title, content, category, favorite 키를 가진 딕셔너리 형태로 저장합니다.
# 여러 개의 프롬프트를 순서대로 관리하기 위해 리스트 자료구조를 사용합니다.
prompts = []


def load_prompts():
    """
    JSON 파일에 저장된 프롬프트 데이터를 메모리로 불러옵니다.

    프로그램 시작 시 호출되며, prompts.json 파일이 존재하면
    해당 파일의 내용을 읽어 전역 리스트 prompts에 저장합니다.

    반환값:
        없음
    """
    # 함수 내부에서 전역 변수 prompts 자체를 새 리스트로 다시 할당하므로
    # global 키워드를 사용합니다.
    global prompts

    try:
        # 한글이 포함된 JSON 파일을 UTF-8 인코딩으로 읽습니다.
        with open("prompts.json", "r", encoding="utf-8") as file:
            prompts = json.load(file)

    # 프로그램을 처음 실행하면 prompts.json 파일이 없을 수 있습니다.
    # 이 경우 오류로 종료하지 않고 빈 리스트 상태로 프로그램을 계속 실행합니다.
    except FileNotFoundError:
        pass


def save_prompts():
    """
    현재 메모리에 있는 프롬프트 목록을 JSON 파일에 저장합니다.

    프롬프트 추가 또는 즐겨찾기 변경처럼 데이터가 수정된 후 호출하여
    프로그램을 종료해도 데이터가 유지되도록 합니다.

    반환값:
        없음
    """
    # "w" 모드는 파일을 새로 작성하거나 기존 내용을 덮어씁니다.
    with open("prompts.json", "w", encoding="utf-8") as file:
        json.dump(
            prompts,
            file,
            # 한글을 \uXXXX 형태로 변환하지 않고 그대로 저장합니다.
            ensure_ascii=False,
            # JSON 내용을 보기 좋게 들여쓰기합니다.
            indent=4
        )


def show_menu():
    """
    프로그램의 메인 메뉴를 화면에 출력합니다.

    반환값:
        없음
    """
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
    """
    사용자에게 제목, 내용, 카테고리를 입력받아 새 프롬프트를 추가합니다.

    제목과 내용은 빈 값이 입력되지 않도록 검증하고,
    카테고리는 미리 정의된 6개 항목 중 하나만 선택하도록 제한합니다.
    새 프롬프트는 기본적으로 즐겨찾기 False 상태로 생성됩니다.

    반환값:
        없음
    """
    print()
    print("=== 프롬프트 추가 ===")

    # 제목은 반드시 입력되어야 하므로 유효한 값이 들어올 때까지 반복합니다.
    while True:
        # strip()으로 앞뒤 공백을 제거하여 공백만 입력한 경우도 빈 값으로 처리합니다.
        title = input("제목: ").strip()

        if title:
            break

        print("제목은 비워둘 수 없습니다.")

    # 내용도 제목과 동일하게 빈 값 입력을 허용하지 않습니다.
    while True:
        content = input("내용: ").strip()

        if content:
            break

        print("내용은 비워둘 수 없습니다.")

    # 메뉴 번호와 실제 카테고리명을 연결하기 위해 딕셔너리를 사용합니다.
    # 사용자가 입력한 문자열 번호를 키로 조회하면 카테고리명을 쉽게 얻을 수 있습니다.
    categories = {
        "1": "텍스트 생성",
        "2": "이미지 생성",
        "3": "영상 생성",
        "4": "페르소나",
        "5": "자동화",
        "6": "기타"
    }

    # 허용된 카테고리 번호가 입력될 때까지 반복합니다.
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

        # 딕셔너리의 키에 존재하는 번호인지 확인하여 잘못된 입력을 방지합니다.
        if category_choice in categories:
            category = categories[category_choice]
            break

        print("1~6 사이의 번호를 입력해주세요.")

    # 하나의 프롬프트와 관련된 여러 속성을 한 묶음으로 관리하기 위해
    # 딕셔너리 형태로 데이터를 구성합니다.
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    # 새 프롬프트 딕셔너리를 전체 프롬프트 리스트의 마지막에 추가합니다.
    prompts.append(new_prompt)

    # 데이터가 변경되었으므로 즉시 JSON 파일에 저장합니다.
    save_prompts()

    print()
    print("프롬프트가 추가되었습니다.")


def show_list():
    """
    저장된 모든 프롬프트를 번호와 함께 출력합니다.

    즐겨찾기 상태가 True인 프롬프트에는 별(⭐) 표시를 추가합니다.
    프롬프트가 없으면 안내 메시지를 출력합니다.
    
    반환값:
        없음
    """
    print()
    print("=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # enumerate()를 사용하면 리스트를 순회하면서 번호와 데이터를 함께 얻을 수 있습니다.
    # start=1을 지정하여 사용자에게 익숙한 1번부터 번호를 표시합니다.
    for index, prompt in enumerate(prompts, start=1):
        # 조건 표현식을 이용하여 즐겨찾기 여부에 따라 표시 문자열을 결정합니다.
        favorite_mark = "⭐" if prompt["favorite"] else ""

        print(
            f'{index}. {prompt["title"]} '
            f'[{prompt["category"]}] {favorite_mark}'
        )


def show_by_category():
    """
    사용자가 선택한 카테고리에 해당하는 프롬프트만 조회합니다.

    잘못된 카테고리 번호가 입력되면 안내 메시지를 출력하고
    함수를 종료합니다.

    반환값:
        없음
    """
    print()
    print("=== 카테고리별 조회 ===")
    print("1. 텍스트 생성")
    print("2. 이미지 생성")
    print("3. 영상 생성")
    print("4. 페르소나")
    print("5. 자동화")
    print("6. 기타")

    choice = input("카테고리 선택: ")

    # 메뉴 번호와 실제 카테고리명을 연결하는 매핑 정보입니다.
    categories = {
        "1": "텍스트 생성",
        "2": "이미지 생성",
        "3": "영상 생성",
        "4": "페르소나",
        "5": "자동화",
        "6": "기타"
    }

    # 존재하지 않는 번호라면 이후 처리를 수행하지 않습니다.
    if choice not in categories:
        print("잘못된 카테고리 번호입니다.")
        return

    # 선택된 번호를 실제 카테고리 문자열로 변환합니다.
    selected_category = categories[choice]

    print()
    print(f"=== {selected_category} 프롬프트 ===")

    # 검색 결과가 한 건이라도 있었는지 확인하기 위한 플래그 변수입니다.
    found = False

    # 전체 프롬프트를 순회하며 선택한 카테고리와 일치하는 항목만 출력합니다.
    for index, prompt in enumerate(prompts, start=1):
        if prompt["category"] == selected_category:
            favorite_mark = "⭐" if prompt["favorite"] else ""

            print(
                f'{index}. {prompt["title"]} '
                f'[{prompt["category"]}] {favorite_mark}'
            )

            found = True

    # 일치하는 데이터가 한 건도 없는 경우 사용자에게 알려줍니다.
    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")


def search_prompt():
    """
    제목 또는 내용에 검색어가 포함된 프롬프트를 찾습니다.

    영어 검색 시 대소문자 차이를 무시하기 위해
    검색어와 대상 문자열을 모두 소문자로 변환하여 비교합니다.

    반환값:
        없음
    """
    print()
    print("=== 프롬프트 검색 ===")

    # 앞뒤 공백을 제거하여 빈 검색어가 입력되지 않도록 검사합니다.
    keyword = input("검색어: ").strip()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    print()
    print("=== 검색 결과 ===")

    found = False

    # 전체 프롬프트의 제목과 내용을 순차적으로 검사합니다.
    for index, prompt in enumerate(prompts, start=1):
        # in 연산자를 사용하여 검색어가 제목 또는 내용의 일부로 포함되는지 검사합니다.
        # lower()를 사용하므로 영어 검색 시 AI, ai 등의 대소문자를 구분하지 않습니다.
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
    """
    사용자가 선택한 프롬프트의 상세 정보를 출력합니다.

    번호 입력 시 숫자가 아닌 값, 존재하지 않는 번호 등을 검사하여
    프로그램이 비정상 종료되지 않도록 예외 및 범위 검증을 수행합니다.

    반환값:
        없음
    """
    print()
    print("=== 프롬프트 상세 보기 ===")

    # 저장된 데이터가 없는 경우 번호 입력을 받을 필요가 없으므로 즉시 종료합니다.
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 사용자가 선택할 수 있도록 먼저 전체 목록을 보여줍니다.
    show_list()

    try:
        # input()은 문자열을 반환하므로 정수 번호로 변환합니다.
        number = int(input("상세히 볼 프롬프트 번호: "))

    # 숫자로 변환할 수 없는 값을 입력했을 때 발생하는 오류를 처리합니다.
    except ValueError:
        print("숫자를 입력해주세요.")
        return

    # 실제 리스트 범위를 벗어나는 번호가 입력되었는지 검사합니다.
    if number < 1 or number > len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    # 사용자에게 보이는 번호는 1부터 시작하지만 리스트 인덱스는 0부터 시작하므로
    # number - 1을 사용하여 실제 항목에 접근합니다.
    prompt = prompts[number - 1]

    # Boolean 값을 사용자 친화적인 문자열로 변환합니다.
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
    """
    선택한 프롬프트의 즐겨찾기 상태를 추가 또는 해제합니다.

    현재 Boolean 값을 not 연산자로 반전시켜
    True는 False로, False는 True로 변경합니다.
    변경 후 JSON 파일에 즉시 저장합니다.

    반환값:
        없음
    """
    print()
    print("=== 즐겨찾기 추가/해제 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 사용자가 변경할 항목의 번호를 쉽게 확인하도록 전체 목록을 출력합니다.
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

    # not 연산자를 사용하여 현재 즐겨찾기 상태를 반전시킵니다.
    prompt["favorite"] = not prompt["favorite"]

    # 변경된 즐겨찾기 상태를 프로그램 종료 후에도 유지하기 위해 저장합니다.
    save_prompts()

    # 변경 결과를 사용자에게 알립니다.
    if prompt["favorite"]:
        print(f'"{prompt["title"]}"을(를) 즐겨찾기에 추가했습니다.')
    else:
        print(f'"{prompt["title"]}"을(를) 즐겨찾기에서 해제했습니다.')


def show_favorites():
    """
    즐겨찾기로 지정된 프롬프트만 모아서 출력합니다.

    favorite 값이 True인 데이터만 필터링하며,
    해당 항목이 하나도 없으면 안내 메시지를 출력합니다.

    반환값:
        없음
    """
    print()
    print("=== 즐겨찾기 목록 ===")

    found = False

    # 전체 목록을 순회하면서 favorite 값이 True인 항목만 출력합니다.
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
    """
    프로그램의 전체 실행 흐름을 관리하는 진입점 함수입니다.

    프로그램 시작 시 저장 데이터를 불러오고,
    사용자가 0번을 선택할 때까지 메뉴를 반복해서 보여줍니다.
    입력된 메뉴 번호에 따라 각 기능 함수를 호출합니다.

    반환값:
        없음
    """
    # 프로그램이 시작되면 가장 먼저 기존 JSON 데이터를 불러옵니다.
    load_prompts()

    # 사용자가 종료 메뉴를 선택할 때까지 계속 프로그램을 실행합니다.
    while True:
        show_menu()

        choice = input("메뉴 선택: ")

        # 메뉴 번호별로 담당 함수를 호출하여 기능을 분리합니다.
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

        # 정의되지 않은 번호가 입력된 경우 다시 메뉴를 표시합니다.
        else:
            print("잘못된 메뉴 번호입니다.")


# 이 파일이 다른 모듈에서 import된 경우에는 main()을 자동 실행하지 않고,
# main.py 파일을 직접 실행했을 때만 프로그램을 시작합니다.
if __name__ == "__main__":
    main()
