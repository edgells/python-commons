import asyncio


# 获取事件循环
import time

loop = asyncio.get_event_loop()


async def main():
    await asyncio.sleep(10)
    print("main coroutine running")


print(time.time_ns())
# 运行一个协程函数
loop.run_until_complete(main())
print(time.time_ns())

# 在线程池中运行一个协程函数
# loop.run_in_executor()

# 运行一个事件循环
loop.run_forever()