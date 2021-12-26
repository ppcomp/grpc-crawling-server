from typing import List

from crawling.src.database import session
from crawling.src.entity.Notice import Notice


def find_all_by_code(code: str) -> List[Notice]:
    query_result = session.query(Notice)
    return query_result.filter_by(code=code).all()
