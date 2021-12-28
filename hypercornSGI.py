import asyncio

from hypercorn.config import Config
from hypercorn.asyncio import serve

from api import myApp

asyncio.run(serve(myApp, Config()))