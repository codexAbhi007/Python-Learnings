import time 
import asyncio

async def f1():
    await asyncio.sleep(1)
    print("func 1")
    return("Abhi")

async def f2():
    await asyncio.sleep(1)
    print("func 2")

async def f3():
    await asyncio.sleep(4)
    print("func 3")

async def main():
    L  = await asyncio.gather(
        f1(),
        f2(),
        f3()
    )
    print(L)
asyncio.run(main())