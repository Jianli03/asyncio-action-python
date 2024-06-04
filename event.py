import asyncio
from unittest import async_case

async def waiter(event):
    print('waiter for event: %s to be set' % event )
    await event.wait()
    print("event: %s has been set" % event)

async def setter(event):
    print("start doing something with event: %s" % event)
    await asyncio.sleep(2) # Simulate doing something
    print("job is done with the event: %s" % event)
    event.set()
    print("event: %s is set" % event)

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())

