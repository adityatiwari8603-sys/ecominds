import sqlite3

DATABASE_NAME = "ecomind.db"

LESSONS = {
    "DSA Master - Introduction to Binary Search": {
        "content": """# Binary Search

Binary Search is an efficient searching algorithm for a sorted array.

Instead of checking every element one by one, Binary Search repeatedly divides the search range into half.

## Example

nums = [1, 3, 5, 7, 9, 11, 13]

Search for 9.

Middle = 7

9 > 7

Search the right half.

Then:

9 is found.

## Requirement

The data normally needs to be sorted.

## Complexity

Linear Search:

O(n)

Binary Search:

O(log n)

## Main idea

Maintain:

left
right

Find:

mid = left + (right - left) // 2

Then decide whether to search left or right.

## Pattern

Sorted data + searching

→ Think Binary Search.
""",
        "topic": "Binary Search",
        "difficulty": "Beginner",
        "keywords": "binary search,sorted,array,left,right,mid",
    },

    "DSA Master - Binary Search Iterative": {
        "content": """# Binary Search - Iterative

The iterative version uses a while loop.

Example:

nums = [1,3,5,7,9]
target = 7

Python:

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

## Logic

If nums[mid] == target:

Found.

If nums[mid] < target:

Target is on the right.

If nums[mid] > target:

Target is on the left.

## Complexity

Time: O(log n)

Space: O(1)

## Important

Use:

left <= right

when both boundary positions are valid candidates.
""",
        "topic": "Binary Search Iterative",
        "difficulty": "Beginner",
        "keywords": "binary search,iteration,while loop,array",
    },

    "DSA Master - Binary Search Recursive": {
        "content": """# Binary Search - Recursive

Binary Search can also be written recursively.

## Python

def binary_search(nums, target, left, right):

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid

    if nums[mid] < target:
        return binary_search(
            nums,
            target,
            mid + 1,
            right
        )

    return binary_search(
        nums,
        target,
        left,
        mid - 1
    )

## Base Case

If:

left > right

the target does not exist.

## Complexity

Time: O(log n)

Recursive stack space: O(log n)

## Difference

Iterative:

O(1) extra space.

Recursive:

O(log n) call stack.
""",
        "topic": "Binary Search Recursive",
        "difficulty": "Beginner",
        "keywords": "binary search,recursion,recursive,array",
    },

    "DSA Master - Lower Bound": {
        "content": """# Lower Bound

Lower Bound finds the first position where a value is greater than or equal to target.

Example:

nums = [1,2,4,4,5,7]
target = 4

Lower Bound = index 2.

## Why?

Index 2 is the first index satisfying:

nums[index] >= 4

## Python

def lower_bound(nums, target):
    left = 0
    right = len(nums)

    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left

## Important

The right boundary is exclusive.

## Complexity

Time: O(log n)

Space: O(1)

## Uses

First occurrence

Insertion position

Frequency ranges

Sorted arrays
""",
        "topic": "Lower Bound",
        "difficulty": "Intermediate",
        "keywords": "binary search,lower bound,first occurrence,insertion",
    },

    "DSA Master - Upper Bound": {
        "content": """# Upper Bound

Upper Bound finds the first position where a value is strictly greater than target.

Example:

nums = [1,2,4,4,5,7]
target = 4

Upper Bound = index 4.

Because:

nums[4] = 5

and 5 > 4.

## Python

def upper_bound(nums, target):
    left = 0
    right = len(nums)

    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left

## Frequency Trick

Number of occurrences of target:

upper_bound(target) - lower_bound(target)

## Complexity

Time: O(log n)

Space: O(1)
""",
        "topic": "Upper Bound",
        "difficulty": "Intermediate",
        "keywords": "binary search,upper bound,frequency,sorted",
    },

    "DSA Master - First and Last Position": {
        "content": """# First and Last Position

Find the first and last index of a target in a sorted array.

Example:

nums = [5,7,7,8,8,10]
target = 8

Answer:

[3,4]

## Idea

Use Binary Search twice.

First search:

find first occurrence.

Second search:

find last occurrence.

## Complexity

Time:

O(log n)

Space:

O(1)

## Pattern

Repeated values in sorted data

→ Lower Bound + Upper Bound style Binary Search.
""",
        "topic": "First and Last Position",
        "difficulty": "Intermediate",
        "keywords": "binary search,first occurrence,last occurrence,duplicates",
    },

    "DSA Master - Search Insert Position": {
        "content": """# Search Insert Position

Given a sorted array, find the index where target exists or should be inserted.

Example:

nums = [1,3,5,6]
target = 5

Answer:

2

Example:

target = 2

Answer:

1

## Idea

Find the first position where:

nums[index] >= target

This is exactly the Lower Bound concept.

## Python

def search_insert(nums, target):
    left = 0
    right = len(nums)

    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left

## Complexity

Time: O(log n)

Space: O(1)
""",
        "topic": "Search Insert Position",
        "difficulty": "Beginner",
        "keywords": "binary search,insert position,lower bound",
    },

    "DSA Master - Search in Rotated Sorted Array": {
        "content": """# Search in Rotated Sorted Array

A sorted array may be rotated.

Example:

[4,5,6,7,0,1,2]

Search for 0.

Answer:

4

## Main Idea

At every step, at least one half is sorted.

Find mid.

Then determine:

left half sorted

or

right half sorted

Check whether target belongs to the sorted half.

## Algorithm

If nums[left] <= nums[mid]:

left half is sorted.

Otherwise:

right half is sorted.

Then decide which half can contain target.

## Complexity

Time: O(log n)

Space: O(1)

## Pattern

Sorted array + rotation

→ Modified Binary Search.
""",
        "topic": "Search in Rotated Sorted Array",
        "difficulty": "Intermediate",
        "keywords": "binary search,rotated array,sorted array",
    },

    "DSA Master - Find Minimum in Rotated Sorted Array": {
        "content": """# Find Minimum in Rotated Sorted Array

Example:

nums = [3,4,5,1,2]

Minimum:

1

## Binary Search Idea

Compare:

nums[mid]

with:

nums[right]

If nums[mid] > nums[right]:

the minimum must be on the right.

Otherwise:

the minimum is on the left side including mid.

## Python

def find_min(nums):
    left = 0
    right = len(nums) - 1

    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

## Complexity

Time: O(log n)

Space: O(1)
""",
        "topic": "Find Minimum in Rotated Sorted Array",
        "difficulty": "Intermediate",
        "keywords": "binary search,rotated array,minimum",
    },

    "DSA Master - Find Peak Element": {
        "content": """# Find Peak Element

A peak element is greater than its neighbors.

Example:

[1,2,3,1]

3 is a peak.

## Binary Search Idea

Compare:

nums[mid]

with:

nums[mid + 1]

If:

nums[mid] < nums[mid + 1]

a peak exists on the right.

Otherwise:

a peak exists on the left including mid.

## Python

def find_peak(nums):
    left = 0
    right = len(nums) - 1

    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

## Complexity

Time: O(log n)

Space: O(1)

## Pattern

A problem does not always require finding an exact target.

Binary Search can also find a position where a condition changes.
""",
        "topic": "Find Peak Element",
        "difficulty": "Intermediate",
        "keywords": "binary search,peak,condition,array",
    },

    "DSA Master - Binary Search on Answer": {
        "content": """# Binary Search on Answer

Sometimes the answer itself is not an index.

Instead, we binary search over the possible answer values.

## Example

Suppose a problem asks:

"What is the minimum capacity needed?"

Possible capacities form a range:

1 ... maximum.

For a guessed capacity:

Check whether the task is possible.

If possible:

try smaller.

If impossible:

try larger.

## General Structure

left = minimum possible answer

right = maximum possible answer

while left <= right:

    mid = ...

    if feasible(mid):
        save answer
        search left
    else:
        search right

## Important

This is often called:

Binary Search on the Answer.

## Pattern

If:

answers are ordered

and feasibility changes from false to true

Binary Search may work.
""",
        "topic": "Binary Search on Answer",
        "difficulty": "Advanced",
        "keywords": "binary search,answer,feasibility,optimization",
    },

    "DSA Master - Koko Eating Bananas": {
        "content": """# Koko Eating Bananas

Koko has piles of bananas and must finish them within h hours.

Find the minimum eating speed.

## Binary Search on Answer

Possible speed:

1 to max(piles)

For each speed:

calculate whether Koko can finish within h hours.

If yes:

try a smaller speed.

If no:

increase speed.

## Python

import math

def min_eating_speed(piles, h):

    left = 1
    right = max(piles)

    while left < right:

        speed = left + (right - left) // 2

        hours = 0

        for pile in piles:
            hours += math.ceil(pile / speed)

        if hours <= h:
            right = speed
        else:
            left = speed + 1

    return left

## Complexity

Time: O(n log m)

where m = max pile size.

Space: O(1)

## Pattern

Minimum value satisfying a feasibility condition

→ Binary Search on Answer.
""",
        "topic": "Koko Eating Bananas",
        "difficulty": "Advanced",
        "keywords": "binary search,koko,feasibility,minimum speed",
    },

    "DSA Master - Capacity to Ship Packages": {
        "content": """# Capacity to Ship Packages Within D Days

Find the minimum ship capacity required to ship packages within D days.

Packages must be shipped in order.

## Binary Search on Answer

Minimum capacity:

max(weights)

Maximum capacity:

sum(weights)

For a guessed capacity:

simulate how many days are required.

If days <= D:

capacity may be smaller.

Otherwise:

increase capacity.

## Complexity

Time:

O(n log(sum(weights)))

Space:

O(1)

## Pattern

Minimum feasible capacity

→ Binary Search on Answer.
""",
        "topic": "Capacity to Ship Packages",
        "difficulty": "Advanced",
        "keywords": "binary search,shipping,capacity,days,feasibility",
    },

    "DSA Master - Split Array Largest Sum": {
        "content": """# Split Array Largest Sum

Split an array into k non-empty continuous subarrays while minimizing the largest subarray sum.

## Binary Search on Answer

Minimum possible largest sum:

max(nums)

Maximum:

sum(nums)

For a candidate maximum sum:

greedily create subarrays without exceeding that candidate.

Count how many parts are needed.

If number of parts <= k:

candidate works.

Try smaller.

Otherwise:

try larger.

## Complexity

Approximately:

O(n log(sum(nums)))

## Pattern

Minimize the maximum value

→ Binary Search on Answer.
""",
        "topic": "Split Array Largest Sum",
        "difficulty": "Advanced",
        "keywords": "binary search,subarray,split,minimize maximum",
    },

    "DSA Master - Time Based Key Value Store": {
        "content": """# Time Based Key Value Store

Store a value with a timestamp and retrieve the value for a requested time.

For get(key, timestamp), return the value stored at the largest timestamp that is less than or equal to the requested timestamp.

## Example

set("foo", "bar1", 1)
set("foo", "bar2", 4)

get("foo", 3)

Answer:

"bar1"

## Main Idea

Store timestamps in sorted order.

For each get operation, use Binary Search to find the rightmost valid timestamp.

## Pattern

Sorted timestamps + nearest valid previous value

→ Binary Search.
""",
        "topic": "Time Based Key Value Store",
        "difficulty": "Intermediate",
        "keywords": "binary search,timestamp,key value,sorted",
    },

    "DSA Master - Median of Two Sorted Arrays": {
        "content": """# Median of Two Sorted Arrays

Given two sorted arrays, find their combined median.

The challenge is to do it in:

O(log(min(n,m)))

## Main Idea

Binary Search the partition of the smaller array.

Choose how many elements belong to the left side.

The remaining elements from the other array are determined automatically.

We want:

max(left side) <= min(right side)

for both arrays.

## Important

This is a partition-based Binary Search problem.

## Complexity

Time:

O(log(min(n,m)))

Space:

O(1)

## Pattern

Two sorted arrays + partition

→ Binary Search on the smaller array.
""",
        "topic": "Median of Two Sorted Arrays",
        "difficulty": "Advanced",
        "keywords": "binary search,median,sorted arrays,partition",
    },

    "DSA Master - Binary Search Problem Recognition": {
        "content": """# Binary Search Problem Recognition

Do not only look for the words "binary search".

A problem may be a Binary Search problem when:

1. Data is sorted.
2. The search space can be divided in half.
3. There is a monotonic condition.
4. The answer space has a true/false feasibility boundary.
5. We need first or last valid position.

## Examples

Search target:

Classic Binary Search.

First position:

Lower Bound.

Last position:

Upper Bound style search.

Rotated sorted array:

Modified Binary Search.

Minimum feasible answer:

Binary Search on Answer.

## Key Question

Ask:

"Can I eliminate roughly half of the remaining possibilities after each step?"

If yes, Binary Search may be applicable.
""",
        "topic": "Binary Search Problem Recognition",
        "difficulty": "Beginner",
        "keywords": "binary search,pattern recognition,sorted,monotonic",
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

    print("EchoMind - Binary Search Lessons")
    print("Updated :", updated)
    print("Inserted:", inserted)
    print("Total   :", len(LESSONS))


if __name__ == "__main__":
    main()