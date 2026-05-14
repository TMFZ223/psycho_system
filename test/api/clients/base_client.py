import httpx


class BaseClient:

    def __init__(self, client: httpx.AsyncClient):
        self.client = client