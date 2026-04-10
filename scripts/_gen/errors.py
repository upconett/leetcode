class NoCookies(ValueError):
    def __init__(self, cookies_path: str):
        schema = (
            '{\n'
            '    "LEETCODE_SESSION": "...",\n'
            '    "csrftoken": "..."\n'
            '}'
        )
        super().__init__(
            f'No {cookies_path} file, create please with the following data:\n{schema}'
        )
