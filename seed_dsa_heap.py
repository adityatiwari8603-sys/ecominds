import sqlite3
import heapq

DATABASE_NAME = "ecomind.db"

LESSONS = {
    "DSA Master - Introduction to Heap": {
        "content": """# Heap

A Heap is a special tree-based data structure that satisfies the heap property.

There are two main types:

1. Min Heap
2. Max Heap

## Min Heap

The smallest element is always at the root.

Example:

        1
       / \\
      3   5
     / \\
    7   9

The root is the minimum element.

## Max Heap

The largest element is always at the root.

Example:

        9
       / \\
      7   5
     / \\
    3   1

The root is the maximum element.

## Important

A heap is usually implemented using an array.

For a zero-based array:

left child:
2 * i + 1

right child:
2 * i + 2

parent:
(i - 1) // 2

## Complexity

Peek min/max: O(1)

Insert: O(log n)

Delete root: O(log n)

Build heap: O(n)

## Uses

Priority Queue

Top K problems

Scheduling

Dijkstra's Algorithm

Heap Sort

Finding minimum/maximum efficiently
""",
        "topic": "Heap",
        "difficulty": "Beginner",
        "keywords": "heap,min heap,max heap,priority queue,tree",
    },

    "DSA Master - Min Heap": {
        "content": """# Min Heap

In a Min Heap, every parent is less than or equal to its children.

Therefore the smallest element is always at the root.

## Python

Python's heapq module provides a Min Heap.

Example:

import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heapq.heappop(heap))

Output:

1

## Operations

Push:

heapq.heappush(heap, value)

Pop minimum:

heapq.heappop(heap)

Peek:

heap[0]

## Complexity

Push: O(log n)

Pop: O(log n)

Peek: O(1)

## Pattern

Need the smallest item repeatedly?

Think Min Heap.
""",
        "topic": "Min Heap",
        "difficulty": "Beginner",
        "keywords": "min heap,heapq,priority queue,minimum",
    },

    "DSA Master - Max Heap": {
        "content": """# Max Heap

In a Max Heap, the largest element is always at the root.

Python's heapq is a Min Heap, so a common trick is to store negative values.

## Example

nums = [5, 2, 8, 1]

Use:

heapq.heappush(heap, -value)

The smallest negative value corresponds to the largest original value.

## Python

import heapq

heap = []

for num in [5, 2, 8, 1]:
    heapq.heappush(heap, -num)

maximum = -heapq.heappop(heap)

print(maximum)

Output:

8

## Complexity

Push: O(log n)

Pop: O(log n)

Peek maximum: O(1)

## Pattern

Need the largest item repeatedly?

Think Max Heap / Priority Queue.
""",
        "topic": "Max Heap",
        "difficulty": "Beginner",
        "keywords": "max heap,heapq,priority queue,maximum",
    },

    "DSA Master - Priority Queue": {
        "content": """# Priority Queue

A Priority Queue removes elements according to priority instead of insertion order.

A heap is commonly used to implement a priority queue.

## Example

Suppose smaller numbers have higher priority:

5
1
3
2

The removal order is:

1
2
3
5

## Python

import heapq

pq = []

heapq.heappush(pq, (2, "Task B"))
heapq.heappush(pq, (1, "Task A"))
heapq.heappush(pq, (3, "Task C"))

print(heapq.heappop(pq))

Output:

(1, "Task A")

## Why tuples?

The first tuple value is compared first.

So:

(priority, data)

is a common pattern.

## Complexity

Insert: O(log n)

Remove highest-priority item: O(log n)

Peek: O(1)

## Uses

CPU scheduling

Network processing

Event systems

Shortest path algorithms

Task management
""",
        "topic": "Priority Queue",
        "difficulty": "Beginner",
        "keywords": "priority queue,heap,scheduling,heapq",
    },

    "DSA Master - Kth Largest Element": {
        "content": """# Kth Largest Element

Find the kth largest element in an array.

Example:

nums = [3,2,1,5,6,4]
k = 2

Sorted:

[1,2,3,4,5,6]

2nd largest = 5

## Min Heap Approach

Maintain a heap of size k.

For every number:

push it into the heap.

If heap size becomes greater than k:

remove the smallest.

At the end, the heap contains the k largest elements.

The root is the kth largest.

## Python

def find_kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

## Complexity

Time: O(n log k)

Space: O(k)

## Pattern

Top K / Kth largest

→ Small Min Heap of size K.
""",
        "topic": "Kth Largest Element",
        "difficulty": "Intermediate",
        "keywords": "heap,kth largest,top k,min heap",
    },

    "DSA Master - Kth Smallest Element": {
        "content": """# Kth Smallest Element

Find the kth smallest element.

Example:

nums = [7,4,6,3,9,1]
k = 3

Sorted:

[1,3,4,6,7,9]

Answer:

4

## Heap Idea

One approach is to use a Max Heap of size k.

Keep the k smallest values.

If the heap becomes larger than k,
remove the largest value.

At the end, the root is the kth smallest.

## Complexity

Time: O(n log k)

Space: O(k)

## Pattern

Kth smallest

→ Max Heap of size K.
""",
        "topic": "Kth Smallest Element",
        "difficulty": "Intermediate",
        "keywords": "heap,kth smallest,max heap,top k",
    },

    "DSA Master - Top K Frequent Elements Using Heap": {
        "content": """# Top K Frequent Elements Using Heap

Find the k most frequent values.

Example:

nums = [1,1,1,2,2,3]
k = 2

Frequency:

1 -> 3
2 -> 2
3 -> 1

Answer:

[1,2]

## Approach

First create a frequency map.

Then maintain a Min Heap of size k.

Store:

(frequency, value)

When heap size exceeds k:

remove the lowest frequency.

## Python

from collections import Counter
import heapq

def top_k_frequent(nums, k):

    count = Counter(nums)
    heap = []

    for value, freq in count.items():

        heapq.heappush(heap, (freq, value))

        if len(heap) > k:
            heapq.heappop(heap)

    return [value for freq, value in heap]

## Complexity

Approximately:

O(n log k)

## Pattern

Frequency + Top K

→ Hash Map + Heap.
""",
        "topic": "Top K Frequent Elements Using Heap",
        "difficulty": "Intermediate",
        "keywords": "heap,top k,frequency,hash map,priority queue",
    },

    "DSA Master - K Closest Points to Origin": {
        "content": """# K Closest Points to Origin

Given points on a 2D plane, find the k points closest to the origin.

Distance:

x² + y²

We do not need the square root because comparing squared distances gives the same ordering.

Example:

[1,3]

distance squared:

1² + 3² = 10

## Heap Approach

Use a heap to keep the k closest or farthest points depending on the implementation.

A Max Heap of size k is useful:

If a new point is closer than the farthest point currently stored,
replace it.

## Complexity

Time:

O(n log k)

Space:

O(k)

## Important

Compare:

x*x + y*y

not:

sqrt(x*x + y*y)

The square root is unnecessary for comparison.
""",
        "topic": "K Closest Points to Origin",
        "difficulty": "Intermediate",
        "keywords": "heap,priority queue,points,distance,top k",
    },

    "DSA Master - Merge K Sorted Lists": {
        "content": """# Merge K Sorted Lists

Given k sorted linked lists, merge them into one sorted linked list.

Example:

List 1:

1 -> 4 -> 5

List 2:

1 -> 3 -> 4

List 3:

2 -> 6

Result:

1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

## Heap Approach

Put the first node of every list into a Min Heap.

Remove the smallest node.

Add it to the result.

Then push that node's next node into the heap.

Repeat.

## Complexity

If N is the total number of nodes:

Time:

O(N log k)

Space:

O(k)

## Pattern

Multiple sorted sources

→ Min Heap containing one candidate from each source.
""",
        "topic": "Merge K Sorted Lists",
        "difficulty": "Advanced",
        "keywords": "heap,linked list,merge k sorted,priority queue",
    },

    "DSA Master - Find Median from Data Stream": {
        "content": """# Find Median from Data Stream

Numbers arrive one at a time.

After each insertion, we need the median.

## Two Heap Approach

Use:

Max Heap for the smaller half.

Min Heap for the larger half.

Maintain the sizes so they differ by at most one.

## Example

Numbers:

1, 2, 3, 4

Smaller half:

[1,2]

Larger half:

[3,4]

Median:

(2 + 3) / 2 = 2.5

## Python Idea

Use two heaps.

In Python, represent the Max Heap using negative values.

## Complexity

Insertion:

O(log n)

Median:

O(1)

Space:

O(n)

## Pattern

Dynamic median

→ Two Heaps.
""",
        "topic": "Find Median from Data Stream",
        "difficulty": "Advanced",
        "keywords": "heap,median,two heaps,data stream",
    },

    "DSA Master - Heap Sort": {
        "content": """# Heap Sort

Heap Sort uses a heap to sort an array.

## Main Idea

For ascending order:

Build a Max Heap.

Repeatedly remove the maximum.

Place it at the end of the array.

## Complexity

Time:

O(n log n)

Space:

O(1) for an in-place implementation.

## Comparison

Merge Sort:

O(n log n)

Quick Sort:

Average O(n log n)

Heap Sort:

O(n log n)

## Advantages

Guaranteed O(n log n) time.

Does not require recursion for the standard iterative heap operations.

## Disadvantage

Usually less cache-friendly than some other sorting algorithms.
""",
        "topic": "Heap Sort",
        "difficulty": "Intermediate",
        "keywords": "heap sort,sorting,heap,max heap",
    },

    "DSA Master - Build Heap": {
        "content": """# Build Heap

Building a heap means converting an unordered array into a valid heap.

A simple approach inserts elements one by one.

That takes:

O(n log n)

But bottom-up heap construction can be done in:

O(n)

## Idea

Start from the last non-leaf node.

Perform heapify downward.

Continue toward the root.

## Why O(n)?

Although some nodes may move many levels,
most nodes are near the leaves and require very little work.

The total work sums to O(n).

## Important Formula

For a zero-based array:

last non-leaf index:

(n // 2) - 1

## Pattern

Need to construct a heap from an entire array?

Use bottom-up heapify for O(n).
""",
        "topic": "Build Heap",
        "difficulty": "Intermediate",
        "keywords": "heap,heapify,build heap,array",
    },

    "DSA Master - Heapify": {
        "content": """# Heapify

Heapify restores the heap property.

For a Min Heap:

The parent should be <= its children.

For a Max Heap:

The parent should be >= its children.

## Down Heapify

Start from a node.

Compare it with its children.

Swap with the appropriate child if necessary.

Continue downward until the heap property is restored.

## Complexity

Heapify one node:

O(log n)

Build heap using bottom-up heapify:

O(n)

## Important

Heapify is one of the core operations behind:

Heap Sort

Priority Queues

Build Heap
""",
        "topic": "Heapify",
        "difficulty": "Intermediate",
        "keywords": "heapify,heap,max heap,min heap,tree",
    },

    "DSA Master - Task Scheduler Using Heap": {
        "content": """# Task Scheduler Using Heap

A priority queue can be used to choose the next task to process.

Suppose tasks have different priorities.

Always process the highest-priority task first.

## Example

Tasks:

A -> priority 5
B -> priority 2
C -> priority 8

Processing order:

C
A
B

## Heap

Store:

(-priority, task)

for a Max Heap using Python heapq.

## Why Heap?

We repeatedly need the highest-priority remaining task.

Heap gives:

Insertion: O(log n)

Remove highest priority: O(log n)

Peek: O(1)

## Pattern

Repeatedly choose best available option

→ Priority Queue / Heap.
""",
        "topic": "Task Scheduler Using Heap",
        "difficulty": "Intermediate",
        "keywords": "heap,priority queue,scheduling,tasks",
    },

    "DSA Master - Heap Based Greedy Pattern": {
        "content": """# Heap-Based Greedy Pattern

Many greedy problems repeatedly require the best currently available choice.

A heap makes this efficient.

## General Pattern

1. Insert available choices into heap.
2. Select the smallest or largest.
3. Process it.
4. Add newly available choices.
5. Repeat.

## Examples

Kth Largest

Top K Frequent

Merge K Sorted Lists

Task Scheduling

Dijkstra

Minimum Cost problems

## Why?

Without a heap, repeatedly finding the best option may require O(n) scanning.

With a heap:

O(log n)

per insertion/removal.

## Pattern

Repeatedly choose minimum or maximum

→ Heap.
""",
        "topic": "Heap-Based Greedy Pattern",
        "difficulty": "Intermediate",
        "keywords": "heap,greedy,priority queue,minimum,maximum",
    },

    "DSA Master - Smallest Range Covering K Lists": {
        "content": """# Smallest Range Covering K Lists

Given k sorted lists, find the smallest range that contains at least one number from every list.

## Main Idea

Maintain one current element from each list inside a Min Heap.

The heap tells us the smallest current value.

We also track the maximum current value.

Current range:

minimum -> maximum

Then move forward in the list containing the minimum value.

## Why Heap?

We need to quickly know which list currently has the smallest candidate.

## Complexity

If N is the total number of elements:

Approximately O(N log k)

## Pattern

Multiple sorted lists + repeatedly advance the smallest candidate

→ Min Heap.
""",
        "topic": "Smallest Range Covering K Lists",
        "difficulty": "Advanced",
        "keywords": "heap,sorted lists,range,priority queue",
    },

    "DSA Master - IPO Maximum Capital": {
        "content": """# IPO Maximum Capital Pattern

Some problems give projects with:

capital requirement
profit

You can only choose a project when you have enough capital.

Among currently affordable projects, choose the one with maximum profit.

## Two Heap Approach

Use:

Min Heap for projects ordered by capital requirement.

Max Heap for currently affordable projects ordered by profit.

## Process

1. Add all projects whose capital requirement is affordable.
2. Pick the maximum-profit available project.
3. Increase capital.
4. Repeat.

## Complexity

O(n log n)

## Pattern

Choose the best option among currently available choices

→ Min Heap + Max Heap.
""",
        "topic": "IPO Maximum Capital",
        "difficulty": "Advanced",
        "keywords": "heap,greedy,capital,profit,two heaps",
    },

    "DSA Master - Sliding Window Median": {
        "content": """# Sliding Window Median

Find the median of every window of size k.

Example:

nums = [1,3,-1,-3,5,3,6,7]
k = 3

Each window has a median.

## Main Idea

Use two heaps:

Max Heap for the smaller half.

Min Heap for the larger half.

As the window moves:

insert new value
remove old value
rebalance the heaps

## Challenge

Removing arbitrary elements from a heap is not always O(log n) with basic heapq.

A common technique is lazy deletion.

## Complexity

Approximately:

O(n log k)

## Pattern

Moving window + median

→ Two Heaps + Sliding Window.
""",
        "topic": "Sliding Window Median",
        "difficulty": "Advanced",
        "keywords": "heap,median,sliding window,two heaps",
    },

    "DSA Master - Heap Problem Recognition": {
        "content": """# Heap Problem Recognition

Recognizing when to use a heap is more important than memorizing heap operations.

Think Heap when the problem repeatedly asks for:

smallest element
largest element
k smallest
k largest
highest priority
lowest priority
next best choice
merge sorted sources
dynamic median

## Examples

"Kth largest"

→ Min Heap of size K.

"Kth smallest"

→ Max Heap of size K.

"Top K frequent"

→ Hash Map + Heap.

"Merge K sorted lists"

→ Min Heap.

"Median from stream"

→ Two Heaps.

## General Rule

If repeatedly scanning for the best available element seems necessary:

Ask whether a Heap can maintain that best element automatically.
""",
        "topic": "Heap Problem Recognition",
        "difficulty": "Beginner",
        "keywords": "heap,pattern recognition,priority queue,top k",
    },
}


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def main():
    connection = get_connection()
    cursor = connection.cursor()

    updated = 0
    inserted = 0

    for title, data in LESSONS.items():

        cursor.execute(
            "SELECT id FROM knowledge WHERE title = ?",
            (title,)
        )

        row = cursor.fetchone()

        if row:
            cursor.execute(
                """
                UPDATE knowledge
                SET content = ?,
                    subject = ?,
                    unit = ?,
                    topic = ?,
                    category = ?,
                    difficulty = ?,
                    keywords = ?,
                    author = ?
                WHERE title = ?
                """,
                (
                    data["content"],
                    "Data Structures & Algorithms",
                    "CS Core",
                    data["topic"],
                    "DSA Master Library",
                    data["difficulty"],
                    data["keywords"],
                    "EchoMind",
                    title,
                ),
            )

            updated += 1

        else:
            cursor.execute(
                """
                INSERT INTO knowledge
                (
                    title,
                    content,
                    subject,
                    unit,
                    topic,
                    category,
                    difficulty,
                    keywords,
                    author
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    title,
                    data["content"],
                    "Data Structures & Algorithms",
                    "CS Core",
                    data["topic"],
                    "DSA Master Library",
                    data["difficulty"],
                    data["keywords"],
                    "EchoMind",
                ),
            )

            inserted += 1

    connection.commit()
    connection.close()

    print("EchoMind - Heap Lessons")
    print("Updated :", updated)
    print("Inserted:", inserted)
    print("Total   :", len(LESSONS))


if __name__ == "__main__":
    main()