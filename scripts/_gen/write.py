from io import StringIO
from pathlib import Path

from mako.runtime import Context
from mako.template import Template
from datetime import date

from .models import Question


DIFFICULTY_EMOJIS = { 'EASY': '🟩', 'MEDIUM': '🟨', 'HARD': '🟥' }


def update_core_readme(question: Question):
    q = question
    today = date.today().strftime('%d.%m.%Y')
    difficulty = DIFFICULTY_EMOJIS[q.difficulty]
    newline = f'- `{today}` {difficulty} [{q.id}. {q.title}](./{__dir_name(q)})\n'
    with open("README.md", 'a') as file:
        file.write(newline)


def create_question_directory(question: Question):
    dir_name = __dir_name(question)
    Path(dir_name).mkdir(exist_ok=True)


def write_question_readme(question: Question):
    dir_name = __dir_name(question)
    readme_path = Path(dir_name) / 'README.md'
    readme = Template(filename='scripts/_gen/README.mako')
    buffer = StringIO()
    context = Context(buffer,
        id=question.id,
        title=question.title,
        link=f'https://leetcode.com/problems/{question.slug}',
        difficulty=question.difficulty,
        difficulty_emoji=DIFFICULTY_EMOJIS[question.difficulty],
        topics=' '.join(f'`{t}`' for t in question.topics)
    )
    readme.render_context(context)
    with readme_path.open('w') as file:
        file.write(buffer.getvalue())


def __dir_name(question: Question):
    return f'{question.id}-{question.slug}'
