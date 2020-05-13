import asyncio
from .connect import Generator


class CloudflareWarpPlus(Generator):
    def __init__(self):
        super().__init__()

    @staticmethod
    async def is_successful(status_code):
        if status_code == 200:
            return True
        else:
            return False

    async def data_generator(self, referrer: str, n_count: int):
        counter = 0
        n = 1
        error_count = 0
        while counter < n_count:
            status_code = await self.warp_data_generate(referrer=referrer)
            if await self.is_successful(status_code):
                result = {
                    "status": True,
                    "result": {
                        "message": "Data successfully generated",
                        "generated_data": n,
                        "error_count": error_count
                    }
                }
                yield result
                n += 1
                counter += 1
                await asyncio.sleep(20)
            else:
                if error_count > 3:
                    res = {
                        "status": False,
                        "result": {
                            "message": "data generation failed. This session closed.",
                            "generated_data": n,
                            "error_count": error_count
                        }
                    }
                    yield res
                result = {
                    "status": False,
                    "result": {
                        "message": "data generation failed. Repeat this error 3 times and this session ends.",
                        "generated_data": n,
                        "error_count": error_count
                    }
                }
                yield result
                error_count += 1