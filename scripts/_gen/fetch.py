from pathlib import Path
import json
from gql import Client
from gql.transport.requests import RequestsHTTPTransport

from .models import Question
from .queries import QUERY_TITLE, QUERY_TOPICS
from .errors import NoCookies


LEETCODE_URL = 'https://leetcode.com/graphql'
COOKIES_PATH = Path('cookies.json')


def fetch_question(slug: str) -> Question:
    cookies = __load_cookies()
    transport = RequestsHTTPTransport(LEETCODE_URL, cookies=cookies)
    client = Client(transport=transport)
    data = __fetch_data(client, slug)
    return Question(slug=slug, **data)


def __load_cookies() -> dict:
    if not COOKIES_PATH.exists():
        raise NoCookies(str(COOKIES_PATH))
    with COOKIES_PATH.open() as file:
        return json.load(file)


def __fetch_data(client: Client, slug: str) -> dict:
    title_result = client.execute(QUERY_TITLE, variable_values={"titleSlug": slug})['question']
    topics_result = client.execute(QUERY_TOPICS, variable_values={"titleSlug": slug})['question']
    if not title_result:
        raise LookupError(f'Question "{slug}" not found')
    title_result['difficulty'] = title_result['difficulty'].upper()
    topics = [t['name'] for t in topics_result['topicTags']]
    return {**title_result, 'topics': topics}
