import asyncio


async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay) # simulate an I/O operation with a delay
    print("Data fetched...")
    return {"data": "some data", "id": id}  # return some data

# couroutin function
async def  main():
    print("Start of main coroutine")
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)
    # Awat the fetch_data function, pausing execution of main thread
    result = await task1
    print(f"Received task1's result: {result}")

    result = await task2
    print(f"Received task2's result: {result}")

    print("main coroutine finished")

# Run the coroutine in a event loop
asyncio.run(main())
print("End of main coroutine")
