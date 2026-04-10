from dataclasses import dataclass

from typing import Literal


@dataclass
class Question:
    slug: str
    id: str
    title: str
    difficulty: Literal['EASY', 'MEDIUM', 'HARD']
    topics: list[str]
