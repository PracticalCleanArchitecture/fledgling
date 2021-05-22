# -*- coding: utf8 -*-
from typing import Union

from fledgling.app.entity.location import (
    ILocationRepository,
    Location,
    LocationRepositoryError,
)
from fledgling.repository.nest_gateway import INestGateway


class NestLocationRepository(ILocationRepository):
    def __init__(self, *, nest_client: INestGateway):
        self.nest_client = nest_client

    def get(self, *, id_) -> Union[None, Location]:
        pathname = '/location/{}'.format(id_)
        response = self.nest_client.request(
            method='GET',
            pathname=pathname,
        )
        response = response.json()
        if response['status'] == 'failure':
            raise LocationRepositoryError(response['error']['message'])

        result = response['result']
        if result is None:
            return None
        return self._dto_to_entity(result)

    def _dto_to_entity(self, dto):
        """将通过网络传输回来的对象反序列化为地点的实体对象。"""
        return Location.new(
            id_=dto['id'],
            name=dto['name'],
            user_id=dto['user_id'],
        )
