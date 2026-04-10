import sys
from _gen.fetch import fetch_question
from _gen.write import (
    create_question_directory,
    write_question_readme,
    update_core_readme
)


def retrieve_slug() -> str:
    if len(sys.argv) >= 2:
        slug = sys.argv[1]
    else:
        slug = input('Enter question slug (like "fizz-buzz"): ')
    return slug


if __name__ == "__main__":
    slug = retrieve_slug()
    try:
        question = fetch_question(slug)
    except Exception as e:
        print(e)
        quit()
    create_question_directory(question)
    write_question_readme(question)
    update_core_readme(question)
