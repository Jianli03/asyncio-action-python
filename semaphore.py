import asyncio
from os import access


async def access_resource(semaphore, resource_id):
    async with semaphore:
        # Critical section starts
        print(f"Resouce before modification: {resource_id}")
        await asyncio.sleep(1) # Simulate an IO operation
        print(f"Resource after modification: {resource_id}")
        # Critical section ends

async def main():
    semaphore = asyncio.Semaphore(2) # All 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

asyncio.run(main())


