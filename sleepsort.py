import asyncio

async def pause_then_print(integer):
    await asyncio.sleep(integer)
    print(integer)

async def sleepsort(integers):
    await asyncio.gather(*[pause_then_print(integer) for integer in integers])


if __name__ == "__main__":
    asyncio.run(sleepsort([10,15,5,4,22]))
