# Python - Async Comprehension

This project is part of the Holberton School curriculum and focuses on mastering **asynchronous generators** and **async comprehensions** in Python. It introduces how to yield values asynchronously, how to collect them efficiently, and how to measure performance when executing multiple asynchronous tasks.

---

## 📄 Summary of Tasks

### `0-async_generator.py`
Defines an **async generator** called `async_generator` that:
- Waits asynchronously (`await asyncio.sleep(1)`) for 1 second
- Yields a random float between 0 and 10
- Repeats the process 10 times

```python
# Example usage:
async for value in async_generator():
    print(value)
```

### `1-async_comprehension.py`
Defines `async_comprehension()`, a coroutine that:
- Uses an **async comprehension** to collect all values from `async_generator()`
- Returns a list of the 10 random floats

```python
# Example usage:
result = await async_comprehension()
print(result)
```

### `2-measure_runtime.py`
Defines `measure_runtime()`, a coroutine that:
- Runs `async_comprehension()` **four times concurrently** using `asyncio.gather`
- Measures and returns the **total runtime**
- The runtime is roughly 10 seconds, not 40, because the tasks run in parallel.

```python
# Example usage:
time_taken = await measure_runtime()
print(time_taken)
```

---

## 🧠 Key Concepts

### ✨ Async Generator
An **async generator** is a coroutine that yields values one by one over time, instead of returning all values at once. You use `yield` inside an `async def` function and `await` whenever needed.

```python
async def my_async_gen():
    for i in range(5):
        await asyncio.sleep(1)
        yield i
```

### ✨ Async Comprehension
An **async comprehension** is similar to a list comprehension, but for asynchronous iterators:

```python
[i async for i in async_generator()]
```

This allows you to quickly collect or transform values from an async generator without manually writing an `async for` loop.

### 👩‍💻 Running Coroutines Concurrently
Using `asyncio.gather`, you can run multiple async operations **in parallel**:

```python
await asyncio.gather(async_func1(), async_func2(), async_func3())
```

This is much faster than running them one after the other.

### ⏱️ Measuring Runtime
Use `time.perf_counter()` to measure how long async operations take with high precision.

```python
import time
start = time.perf_counter()
await some_async_function()
end = time.perf_counter()
print(f"Execution took {end - start:.2f} seconds")
```

---

## 🚀 Final Insights
- Async generators allow you to **yield data progressively** over time.
- Async comprehensions let you **collect async data** efficiently into a list.
- Running async comprehensions in parallel shows the **power of concurrency**, saving lots of time!
