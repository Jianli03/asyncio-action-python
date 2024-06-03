import asyncio

async def fetch_data(id, sleep_time):
    print("Fetching data... id:", id)
    await asyncio.sleep(sleep_time) # simulate an I/O operation with a delay
    print(f"Data {id} fetched...")
    return {"data": f"some data from coroutine {id}", "id": id}  # return some data

async def main():
    tasks = []
    async with asyncio.TaskGroup() as group:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = group.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")

    print("main coroutine finished")

# Running the main coroutine
asyncio.run(main())