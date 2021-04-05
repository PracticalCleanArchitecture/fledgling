# -*- coding: utf8 -*-
from fledgling.app.use_case.create_task import CreateTaskUseCase, IParams
from fledgling.cli.config import IniFileConfig
from fledgling.cli.repository_factory import RepositoryFactory


class Params(IParams):
    def __init__(self, *, brief):
        self.brief = brief

    def get_brief(self) -> str:
        return self.brief


def create_task(*, brief):
    """
    创建一个任务。
    """
    config = IniFileConfig()
    config.load()
    params = Params(
        brief=brief,
    )
    repository_factory = RepositoryFactory(
        config=config,
    )
    task_repository = repository_factory.for_task()
    use_case = CreateTaskUseCase(
        params=params,
        task_repository=task_repository,
    )
    use_case.run()