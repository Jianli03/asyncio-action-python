#gather function to run tasks in parallel

import asyncio

# create task for running simutanously
async def fetch_data(id, sleep_time):
    print("Fetching data... id:", id)
    await asyncio.sleep(sleep_time) # simulate an I/O operation with a delay
    print(f"Data {id} fetched...")
    return {"data": f"some data from coroutine {id}", "id": id}  # return some data

# couroutin function
async def  main():

    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 3), fetch_data(3, 1))

    for result in results:
        print(f"Received result: {result}")

    print("main coroutine finished")

# Run the coroutine in a event loop
asyncio.run(main())

