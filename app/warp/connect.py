import datetime
import aiohttp
import asyncio
import ujson
from .util import Utils


class Generator(Utils):
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'api.cloudflareclient.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'
        }
    
    async def generate_url(self):
        url = f'https://api.cloudflareclient.com/v0a{await self.digitString(3)}/reg'
        return url
    
    async def generate_payload(self, referrer):
        install_id = await self.genString(11)
        payload = {
            "key": "{}=".format(await self.genString(42)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, await self.genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+09:00",
            "type": "Android",
            "locale": "ko-KR"
        }
        payloadString = ujson.dumps(payload)
        return payloadString
    
    async def warp_data_generate(self, referrer):
        x = 1
        while True:
            await asyncio.sleep(20)
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.post(url=await self.generate_url(), data=await self.generate_payload(referrer=referrer), headers=self.headers) as resp:
                    status_code = resp.status
            if status_code == 200:
                result = {
                    "status": True,
                    "message": f"{x} GB"
                }
                yield result
                x = x + 1
            else:
                result = {
                    "status": False,
                    "message": "ERROR"
                }
                yield result