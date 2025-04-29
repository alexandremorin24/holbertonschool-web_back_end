# Python - Pagination

This project is part of the Holberton School curriculum and focuses on learning **pagination techniques** for datasets. It covers basic pagination, hypermedia pagination, and how to make pagination **resilient to deletions**.

---

## 📄 Summary of Tasks

### `0-simple_helper_function.py`
Defines a helper function `index_range(page, page_size)` that:
- Calculates and returns a tuple `(start, end)` of indexes
- Used to slice datasets for pagination

```python
# Example usage:
start, end = index_range(2, 10)
# start = 10, end = 20
```

### `1-simple_pagination.py`
Defines a `Server` class that:
- Loads a dataset from `Popular_Baby_Names.csv`
- Implements `get_page(page, page_size)` to return a page of data
- Uses assertions to validate input
- Uses `index_range()` to fetch the correct slice

```python
# Example usage:
server = Server()
page = server.get_page(1, 5)
```

### `2-hypermedia_pagination.py`
Adds a method `get_hyper(page, page_size)` to `Server`, which:
- Returns metadata alongside the data slice
- Metadata includes: page size, current page, next page, previous page, total pages

```python
# Example usage:
data = server.get_hyper(1, 10)
```

Sample output:
```python
{
  'page_size': 10,
  'page': 1,
  'data': [...],
  'next_page': 2,
  'prev_page': None,
  'total_pages': 971
}
```

### `3-hypermedia_del_pagination.py`
Implements `get_hyper_index(index, page_size)` for deletion-resilient pagination:
- Returns a **page of valid records** even if records were deleted
- Handles missing indexes without breaking pagination

```python
# Example usage:
data = server.get_hyper_index(0, 10)
```

Sample output:
```python
{
  'index': 0,
  'next_index': 10,
  'page_size': 10,
  'data': [...]
}
```

---

## 🧠 Key Concepts

### ✨ What is Pagination?
Pagination is splitting a large dataset into smaller, manageable chunks (pages) that can be requested individually.

### 👀 Why Hypermedia Metadata?
Hypermedia metadata makes APIs **self-descriptive**. Clients don't need to guess "what is the next page?" or "how many pages total?".

### 🚫 Deletion-Resilient Pagination
When records are deleted, naive pagination would skip or break. Resilient pagination ensures:
- No missing data
- Smooth experience for clients

### ⏱️ Time Complexity
Efficient pagination ensures that accessing any page is **O(1)** or very close, especially important on large datasets.

---

## 🚀 Final Insights
- Pagination is critical for building **scalable APIs**.
- Hypermedia makes navigation between pages **easy and dynamic**.
- Resilient pagination is necessary in **real-world systems** where data can be updated/deleted anytime.
