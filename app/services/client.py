from openai import AsyncOpenAI
import httpx

class Client:
  def __init__(self):
    self.client = AsyncOpenAI(
      http_client=httpx.AsyncClient(
        limits=httpx.Limits(
          max_connections=1000,
          max_keepalive_connections=100
        )
      )
    )