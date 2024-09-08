from tests.pytest.test.test import test_standardize_and_summarize_resume
import asyncio

async def main() -> None:
    await test_standardize_and_summarize_resume()

if __name__ == '__main__':
    asyncio.run(main())