from app.warp.connect import Generator
import asyncio

code = ""

app = Generator()


async def run():
    async for x in app.warp_data_generate(referrer=code):
        print(x)

asyncio.run(run())