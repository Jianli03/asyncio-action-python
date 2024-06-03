import asyncio

# create task for running simutanously
async def fetch_data(id, sleep_time):
    print("Fetching data... id:", id)
    await asyncio.sleep(sleep_time) # simulate an I/O operation with a delay
    print(f"Data {id} fetched...")
    return {"data": f"some data from coroutine {id}", "id": id}  # return some data

# couroutin function
async def  main():
    # Create tasks for running concurrently with different sleep times
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

    print("main coroutine finished")

# Run the coroutine in a event loop
asyncio.run(main())

