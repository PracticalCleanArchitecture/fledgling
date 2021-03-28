# -*- coding: utf8 -*-
from abc import ABC, abstractmethod
from typing import Union


class Task:
    def __init__(self, *, brief, id):
        self.brief = brief
        self.id = id


class ITaskRepository(ABC):
    @abstractmethod
    def get_by_id(self, id_) -> Union[None, Task]:
        """
        查询指定的任务。
        """
        pass