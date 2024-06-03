import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2) # simulate an I/O operation with a delay
    if value == "Future is to be ready":
        future.set_result("We are ready")
        print("Set the future's result to be ready")
    else:
        future.set_result("We are not ready")
        print("Set the future's result to be not ready")


async def main():
    # Create a future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    # Schedule the future running
    asyncio.create_task(set_future_result(future, "Future is to be ready"))

    # Wait for the future to complete
    result = await future

    print(f"Received the future's result: {result}")

# Running the main coroutine
asyncio.run(main())