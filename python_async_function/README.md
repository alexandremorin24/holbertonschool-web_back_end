# Python - Async

This project is part of the Holberton School curriculum and is focused on learning **asynchronous programming** in Python using `async` and `await`, along with the `asyncio` module. It explores running multiple coroutines concurrently and using tasks to manage asynchronous execution efficiently.

---

## 📄 Summary of Tasks

### `0-basic_async_syntax.py`
Defines an **asynchronous coroutine** `wait_random` that waits for a random time between 0 and `max_delay`, then returns it. Uses `random.uniform()` and `await asyncio.sleep()` to simulate a variable delay.

```python
# Example:
delay = await wait_random(5)
print(f"Waited {delay:.2f} seconds")
```

### `1-concurrent_coroutines.py`
Defines `wait_n(n, max_delay)` that launches `wait_random()` **n times concurrently** using `asyncio.create_task()`. The results are gathered using `asyncio.as_completed()` so the returned list is **in the order the tasks complete**.

```python
# Example:
result = await wait_n(3, 5)
print(result)  # Might output: [0.5, 1.8, 3.2]
```

### `2-measure_runtime.py`
Defines `measure_time(n, max_delay)` that uses `time.perf_counter()` to measure how long it takes to run `wait_n(n, max_delay)`, and returns the **average execution time** per coroutine.

```python
# Example:
avg = measure_time(5, 9)
print(f"Average time per coroutine: {avg:.2f} seconds")
```

### `3-tasks.py`
Defines a normal (non-async) function `task_wait_random(max_delay)` that creates and returns an `asyncio.Task` from the `wait_random()` coroutine. This schedules the coroutine to start running immediately in the event loop.

```python
# Example:
task = task_wait_random(5)
await task
print(f"Task result: {task.result()}")
```

### `4-tasks.py`
Defines `task_wait_n(n, max_delay)`, a variation of `wait_n` that uses `task_wait_random()` to create and manage tasks directly. The function returns a list of delays, in the order they complete.

```python
# Example:
results = await task_wait_n(5, 6)
print(results)  # Example: [0.3, 1.1, 1.9, 3.5, 4.7]
```

---

## 🧠 Key Concepts

### ✨ Coroutine vs Task
- A **coroutine** is a function declared with `async def` and needs to be **awaited** to run.
- A **task** is a coroutine **wrapped** with `asyncio.create_task()`, which starts running immediately in the background.

```python
# Coroutine
coro = wait_random(5)     # Just created, not running
result = await coro        # Now it runs

# Task
task = asyncio.create_task(wait_random(5))  # Scheduled to run now
await task  # Waits for the task to finish
```

### ⌚ Measuring Execution Time
Use `time.perf_counter()` to measure precise time:

```python
import time
start = time.perf_counter()
await wait_n(5, 10)
end = time.perf_counter()
print(f"Total time: {end - start:.2f}s")
```

### ⏳ Running Multiple Coroutines
`asyncio.as_completed()` lets you process results **as soon as each task finishes**, without waiting for all of them to complete:

```python
tasks = [asyncio.create_task(wait_random(5)) for _ in range(5)]

for task in asyncio.as_completed(tasks):
    result = await task
    print(f"One task finished after {result:.2f} seconds")
```

You can also use `asyncio.gather()` if you want to wait for all tasks at once and get the results in order of submission:

```python
results = await asyncio.gather(*(wait_random(5) for _ in range(5)))
print(results)  # Order matches how they were started
```

---

## 🌟 Why Async is Powerful
- Traditional (synchronous) code runs one thing at a time and **waits**.
- Async code allows many I/O operations to be in progress **simultaneously** without blocking each other.

### Example:
```python
# Synchronous (takes 10 seconds total)
for _ in range(5):
    time.sleep(2)

# Asynchronous (takes ~2 seconds total)
await asyncio.gather(*(asyncio.sleep(2) for _ in range(5)))
```
