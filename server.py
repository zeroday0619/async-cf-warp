import asyncio
from app.warp import CloudflareWarpPlus

code = ""

app = CloudflareWarpPlus()


async def run():
    async for x in app.data_generator(referrer=code, n_count=10):
        print(x)

asyncio.run(run())