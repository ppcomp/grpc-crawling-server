import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean

from .data import data

Base = declarative_base()

class Notice(Base):
    # id = models.CharField(max_length=200, primary_key=True)
    # site = models.CharField(max_length=30)
    # is_fixed = models.BooleanField(default=False)
    # title = models.CharField(max_length=100)
    # link = models.CharField(max_length=500)
    # date = models.DateField(null=True)
    # author = models.CharField(max_length=30, null=True)
    # reference = models.CharField(max_length=50, null=True)

    __tablename__ = 'notices'
    id = Column(String(200), primary_key=True)
    site = Column(String(30))
    is_fixed = Column(Boolean, default=False)
    title = Column(String(100))
    link = Column(String(500))
    date = Column(Date, nullable=True)
    author = Column(String(30), nullable=True)
    reference = Column(String(50), nullable=True)

    # __mapper_args__ = {
    #     "order_by":(is_fixed.desc(), date.desc())
    # }

    # class Meta:
    #     ordering = ['-is_fixed', '-date']  # 기본 정렬: 고정 공지 우선, 시간 내림차순(최신 우선)

    def __str__(self):
        return self.title

    def __repr__(self):
        return "<Notice(id='%s', site='%s', is_fixed=%s, title=%s, link=%s, date=%s, author=%s, reference=%s)>" % (
            self.id,
            self.site,
            self.is_fixed,
            self.title,
            self.link,
            self.date,
            self.author,
            self.reference
        )

"""
class Main(Notice):
    pass
"""
# 위와 같은 형식의 모델이 data로부터 자동 생성
for key, item in data.items():
    txt = f"""
class {key.capitalize()}(Notice):
    def __repr__(self):
        return "<{key.capitalize()}(id='%s', site='%s', is_fixed=%s, title=%s, link=%s, date=%s, author=%s, reference=%s)>" % (
            self.id,
            self.site,
            self.is_fixed,
            self.title,
            self.link,
            self.date,
            self.author,
            self.reference
        )
"""
    exec(compile(txt,"<string>","exec"))
