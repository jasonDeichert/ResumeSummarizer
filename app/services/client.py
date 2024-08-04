from openai import AsyncOpenAI
import httpx
from functools import lru_cache

class Client:
  def __init__(self) -> None:
    self.client = AsyncOpenAI(
      http_client=httpx.AsyncClient(
        limits=httpx.Limits(
          max_connections=1000,
          max_keepalive_connections=100
        )
      )
    )
    print("Client created")
  @classmethod
  @lru_cache
  def get_client(cls) -> 'Client':
    return cls()