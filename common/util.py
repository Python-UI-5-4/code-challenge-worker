import re

from common import TEST_CASE_EXEC_MEM_LIMIT


def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def camel_to_snake(camel_str: str) -> str:
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_time_bonus_by_language(code_language: str, challenge_id: int=None):
    time_bonus = {
        'java17': 1.0,
        'nodejs20': 0.0,
        'nodejs20esm': 0.0
    }

    return time_bonus[code_language]


def get_memory_bonus_by_language(code_language: str, challenge_id: int):
    if code_language == "java17":
        return TEST_CASE_EXEC_MEM_LIMIT[challenge_id]
    else:
        return 0