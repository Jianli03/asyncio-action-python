# asyncio-action-python
a tutorial pratice project for asyncio in Python

asyncio is a Python library used to write concurrent code using the async/await syntax. It provides a framework for asynchronous programming, enabling you to write code that can perform non-blocking I/O operations and other tasks concurrently, improving the efficiency of programs that involve waiting for external resources.

There are 7 different scenarios simulated by those scripts.
1. simple tasks
2. gather
3. group
4. Futre
5. lock
6. semaphore
7. event


**asyncio.TaskGroup**
is a high-level API introduced in Python 3.11 to manage and run multiple asynchronous tasks concurrently. It provides a way to group tasks together and ensures that all tasks are properly awaited, even if some of them fail.


**asyncio.Future**
is a fundamental part of the asyncio module, providing a way to manage and work with the results of asynchronous operations. It acts as a placeholder for a value that will be available at some point in the future.


**asyncio.Lock**
protects access to a shared resource in an asynchronous environment. This ensures that only one coroutine can modify the shared resource at a time, preventing race conditions. This script demonstrats the proper use of asyncio.Lock to manage concurrent access to a shared resource.

**asyncoi.Semaphore**
A semaphore is another synchronization primitive that can be used to control access to a shared resource. Unlike a lock, which allows only one coroutine to access a resource at a time, a semaphore allows a specified number of coroutines to access the resource concurrently.


**asyncio.Event** is another synchronization primitive used for signaling between coroutines. An Event object manages an internal flag that can be set or cleared, allowing coroutines to wait for certain conditions to be met. The script shows a scenario where one or more coroutines wait for an event to be set before proceeding.



## Additional reading

### Benefits of asyncio
Non-Blocking I/O: Handles I/O-bound tasks efficiently without blocking the main thread, improving performance in network and disk I/O operations.
Concurrency: Runs multiple coroutines concurrently, allowing better resource utilization.
Scalability: Scales well with many I/O-bound tasks compared to multi-threading, which can be limited by the Global Interpreter Lock (GIL) in Python.

### Use Cases
Web Scraping: Fetching multiple web pages concurrently.
Networking: Building asynchronous servers and clients.
Background Tasks: Running background operations, such as sending emails or processing data.
Real-Time Data: Handling real-time data streams, such as WebSockets or telemetry data.
