import sqlite3

DATABASE_NAME = "ecomind.db"

LESSONS = {
    "DSA Master - Introduction to Sliding Window": {
        "content": """# Sliding Window

Sliding Window is a technique used mainly for array and string problems involving contiguous subarrays or substrings.

Instead of repeatedly calculating the same range, we maintain a window and move its boundaries.

## Basic idea

A window is usually represented by:

left
right

Example:

[2, 1, 5, 1, 3, 2]

A window could be:

[1, 5, 1]

When the window moves, remove the old left value and add the new right value.

## Why use Sliding Window?

Brute-force solutions often examine every possible subarray.

That can take O(n²).

Sliding Window can often reduce this to O(n).

## Types

There are two common forms:

1. Fixed-size window
2. Variable-size window

## Fixed-size example

Find the maximum sum of any subarray of size k.

## Variable-size example

Find the smallest subarray whose sum is at least a target.

## Pattern recognition

Think Sliding Window when the problem contains:

subarray
substring
contiguous
longest
shortest
maximum
minimum
at most k
exactly k

and the elements being considered form a continuous range.
""",
        "topic": "Sliding Window",
        "difficulty": "Beginner",
        "keywords": "sliding window,array,substring,subarray,contiguous",
    },

    "DSA Master - Maximum Sum Subarray of Size K": {
        "content": """# Maximum Sum Subarray of Size K

Given an array and integer k, find the maximum sum of any contiguous subarray of size k.

Example:

nums = [2,1,5,1,3,2]
k = 3

Windows:

2 + 1 + 5 = 8
1 + 5 + 1 = 7
5 + 1 + 3 = 9
1 + 3 + 2 = 6

Answer:

9

## Brute Force

Calculate every window from scratch.

Time Complexity:

O(nk)

## Sliding Window

First calculate the sum of the first k elements.

Then move the window:

new sum = old sum - outgoing element + incoming element

Python:

def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    answer = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        answer = max(answer, window_sum)

    return answer

## Complexity

Time: O(n)

Space: O(1)

## Key idea

Do not recalculate the entire window.
Reuse the previous window's result.
""",
        "topic": "Maximum Sum Subarray of Size K",
        "difficulty": "Beginner",
        "keywords": "sliding window,fixed window,subarray,maximum sum",
    },

    "DSA Master - Average of Subarrays of Size K": {
        "content": """# Average of Subarrays of Size K

Find the average of every contiguous subarray of size k.

Example:

nums = [1,3,2,6,-1,4,1,8,2]
k = 5

For every window, calculate its average.

## Sliding Window

Maintain a running sum.

When the window moves:

remove nums[left]
add nums[right]

Then:

average = window_sum / k

Python:

def averages(nums, k):
    result = []
    window_sum = sum(nums[:k])

    result.append(window_sum / k)

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        result.append(window_sum / k)

    return result

## Complexity

Time: O(n)

Space: O(n) for the output

## Pattern

Fixed-size contiguous range

→ Fixed Sliding Window.
""",
        "topic": "Average of Subarrays of Size K",
        "difficulty": "Beginner",
        "keywords": "sliding window,average,fixed window,array",
    },

    "DSA Master - Longest Substring Without Repeating Characters": {
        "content": """# Longest Substring Without Repeating Characters

Find the length of the longest substring containing no repeated characters.

Example:

s = "abcabcbb"

Longest substring:

"abc"

Answer:

3

## Sliding Window

Maintain:

left
right

and a set of characters currently inside the window.

When a duplicate appears, move left until the duplicate is removed.

## Python

def length_of_longest_substring(s):
    seen = set()
    left = 0
    answer = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        answer = max(answer, right - left + 1)

    return answer

## Complexity

Time: O(n)

Space: O(k)

where k is the number of distinct characters.

## Pattern

Longest substring + uniqueness

→ Variable Sliding Window + Set.
""",
        "topic": "Longest Substring Without Repeating Characters",
        "difficulty": "Intermediate",
        "keywords": "sliding window,string,substring,set,longest",
    },

    "DSA Master - Minimum Size Subarray Sum": {
        "content": """# Minimum Size Subarray Sum

Given positive integers and a target, find the minimum length of a contiguous subarray whose sum is at least the target.

Example:

nums = [2,3,1,2,4,3]
target = 7

Possible answer:

[4,3]

Length:

2

## Variable Sliding Window

Expand the right side until the sum is at least target.

Then shrink from the left while the condition remains true.

This finds the smallest valid window.

## Python

def min_subarray_len(target, nums):
    left = 0
    window_sum = 0
    answer = float("inf")

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            answer = min(answer, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return 0 if answer == float("inf") else answer

## Complexity

Time: O(n)

Space: O(1)

## Important

This standard approach depends on positive numbers.

With negative numbers, the window behavior changes and other techniques may be required.
""",
        "topic": "Minimum Size Subarray Sum",
        "difficulty": "Intermediate",
        "keywords": "sliding window,minimum,subarray,target,variable window",
    },

    "DSA Master - Longest Repeating Character Replacement": {
        "content": """# Longest Repeating Character Replacement

Given a string and k replacements, find the longest substring that can be changed into the same character.

Example:

s = "AABABBA"
k = 1

Answer:

4

because a substring such as "AABA" can become all A using one replacement.

## Sliding Window

Maintain:

left
right
frequency map
maximum frequency in current window

A window is valid when:

window_size - max_frequency <= k

If it becomes invalid, move left.

## Python

def character_replacement(s, k):
    count = {}
    left = 0
    max_freq = 0
    answer = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        answer = max(answer, right - left + 1)

    return answer

## Complexity

Time: O(n)

Space: O(k)

## Pattern

Longest substring with a limited number of changes

→ Variable Sliding Window + Frequency Map.
""",
        "topic": "Longest Repeating Character Replacement",
        "difficulty": "Intermediate",
        "keywords": "sliding window,string,frequency,longest substring",
    },

    "DSA Master - Permutation in String": {
        "content": """# Permutation in String

Given two strings s1 and s2, determine whether some permutation of s1 appears as a substring of s2.

Example:

s1 = "ab"
s2 = "eidbaooo"

"ba" appears in s2.

Answer:

True

## Sliding Window

The required window size is:

len(s1)

Maintain character frequencies inside that window.

When the window moves:

remove the outgoing character
add the incoming character

Compare frequencies.

## Python

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    need = [0] * 26
    window = [0] * 26

    for char in s1:
        need[ord(char) - ord('a')] += 1

    for i, char in enumerate(s2):
        window[ord(char) - ord('a')] += 1

        if i >= len(s1):
            old = s2[i - len(s1)]
            window[ord(old) - ord('a')] -= 1

        if window == need:
            return True

    return False

## Complexity

Time: O(n)

Space: O(1)

for a fixed alphabet.

## Pattern

Permutation/anagram substring

→ Fixed-size Sliding Window + Frequency Map.
""",
        "topic": "Permutation in String",
        "difficulty": "Intermediate",
        "keywords": "sliding window,permutation,string,frequency,anagram",
    },

    "DSA Master - Find All Anagrams in a String": {
        "content": """# Find All Anagrams in a String

Find all starting indexes of anagrams of pattern p inside string s.

Example:

s = "cbaebabacd"
p = "abc"

Answer:

[0, 6]

because:

"cba" and "bac" are anagrams of "abc".

## Main Idea

Every valid window has:

window size = len(p)

and the same frequency distribution as p.

## Sliding Window

Add the incoming character.

Remove the outgoing character.

Compare the frequency state.

## Complexity

Time: O(n)

Space: O(1) with a fixed alphabet.

## Pattern

Fixed substring length + anagram matching

→ Sliding Window + Frequency Map.
""",
        "topic": "Find All Anagrams in a String",
        "difficulty": "Intermediate",
        "keywords": "sliding window,anagram,string,frequency",
    },

    "DSA Master - Max Consecutive Ones III": {
        "content": """# Max Consecutive Ones III

Given a binary array and integer k, find the longest subarray containing at most k zeros.

Example:

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

We may flip at most two zeros.

## Sliding Window

Maintain a window containing at most k zeros.

Expand right.

When zeros become greater than k:

move left
until zeros <= k

Track the maximum window length.

## Python

def longest_ones(nums, k):
    left = 0
    zeros = 0
    answer = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1

            left += 1

        answer = max(answer, right - left + 1)

    return answer

## Complexity

Time: O(n)

Space: O(1)

## Pattern

Longest contiguous section with at most k violations

→ Variable Sliding Window.
""",
        "topic": "Max Consecutive Ones III",
        "difficulty": "Intermediate",
        "keywords": "sliding window,binary array,longest,k zeros",
    },

    "DSA Master - Fruit Into Baskets": {
        "content": """# Fruit Into Baskets

Given an array representing fruit types, find the longest contiguous subarray containing at most two distinct types.

Example:

[1,2,1,2,3]

Longest valid window:

[1,2,1,2]

Length:

4

## Sliding Window

Maintain a frequency dictionary.

Expand right.

If the number of distinct values becomes greater than 2:

remove values from the left until only two types remain.

## Python

def total_fruit(fruits):
    count = {}
    left = 0
    answer = 0

    for right, fruit in enumerate(fruits):
        count[fruit] = count.get(fruit, 0) + 1

        while len(count) > 2:
            count[fruits[left]] -= 1

            if count[fruits[left]] == 0:
                del count[fruits[left]]

            left += 1

        answer = max(answer, right - left + 1)

    return answer

## Complexity

Time: O(n)

Space: O(1) effectively because the window contains at most three tracked types at a time.

## Pattern

Longest subarray with at most k distinct values

→ Variable Sliding Window + Frequency Map.
""",
        "topic": "Fruit Into Baskets",
        "difficulty": "Intermediate",
        "keywords": "sliding window,frequency,map,two distinct",
    },

    "DSA Master - Minimum Window Substring": {
        "content": """# Minimum Window Substring

Given strings s and t, find the smallest substring of s containing all characters of t.

Example:

s = "ADOBECODEBANC"
t = "ABC"

Answer:

"BANC"

## Sliding Window

Maintain:

required character counts
current window counts
number of satisfied requirements

Expand right until the window contains everything needed.

Then shrink from the left to make the window as small as possible.

## General Structure

1. Add right character.
2. Check whether the window became valid.
3. While valid, update the answer.
4. Remove left character.
5. Continue.

## Complexity

Time: O(n)

Space: O(k)

where k is the number of required characters.

## Pattern

Smallest substring containing required information

→ Variable Sliding Window + Frequency Map.
""",
        "topic": "Minimum Window Substring",
        "difficulty": "Advanced",
        "keywords": "sliding window,minimum substring,frequency,map",
    },

    "DSA Master - Longest Subarray with At Most K Distinct": {
        "content": """# Longest Subarray with At Most K Distinct

Find the longest contiguous subarray containing at most k distinct values.

Example:

nums = [1,2,1,2,3]
k = 2

Answer:

4

because [1,2,1,2] contains only two distinct values.

## Sliding Window

Use a frequency map.

Expand right.

If the map contains more than k distinct values:

move left
decrease frequencies
remove zero-frequency values

Then update the maximum length.

## Complexity

Time: O(n)

Space: O(k)

## Pattern

Longest subarray + at most k distinct

→ Variable Sliding Window.
""",
        "topic": "Longest Subarray with At Most K Distinct",
        "difficulty": "Intermediate",
        "keywords": "sliding window,distinct,array,frequency",
    },

    "DSA Master - Subarrays with K Different Integers": {
        "content": """# Subarrays with K Different Integers

Count subarrays containing exactly k distinct integers.

The useful identity is:

Exactly K
=
At Most K
-
At Most K-1

## At Most K

Use a sliding window with a frequency map.

For each right position, once the window is valid:

number of new valid subarrays = right - left + 1

Then calculate:

atMost(k) - atMost(k - 1)

## Why this works

Every subarray with fewer than or equal to k distinct values is counted by atMost(k).

Subtract those with at most k-1.

The remaining subarrays have exactly k.

## Complexity

Each atMost computation is O(n).

Total:

O(n)

Space:

O(k)

## Pattern

Exactly K often becomes:

At Most K - At Most K-1
""",
        "topic": "Subarrays with K Different Integers",
        "difficulty": "Advanced",
        "keywords": "sliding window,exactly k,at most k,distinct",
    },

    "DSA Master - Binary Subarrays With Sum": {
        "content": """# Binary Subarrays With Sum

Given a binary array and goal, count the number of non-empty subarrays whose sum equals goal.

Example:

nums = [1,0,1,0,1]
goal = 2

Answer:

4

## Sliding Window Insight

For binary arrays, one useful approach is:

number of subarrays with sum exactly goal
=
atMost(goal)
-
atMost(goal - 1)

## At Most Goal

Maintain a running sum and sliding window.

If sum becomes greater than goal, move left.

For each right position:

valid subarrays ending at right
=
right - left + 1

## Complexity

Time: O(n)

Space: O(1)

## Pattern

Exact sum in a binary array

→ At Most difference + Sliding Window.
""",
        "topic": "Binary Subarrays With Sum",
        "difficulty": "Advanced",
        "keywords": "sliding window,binary array,sum,at most",
    },

    "DSA Master - Sliding Window Maximum": {
        "content": """# Sliding Window Maximum

Given an array and window size k, find the maximum value in every window.

Example:

nums = [1,3,-1,-3,5,3,6,7]
k = 3

Output:

[3,3,5,5,6,7]

## Challenge

A naive solution scans every window.

That can take O(nk).

## Efficient Approach

Use a monotonic deque.

The deque stores indexes.

Values in the deque are maintained in decreasing order.

The front always contains the index of the maximum value for the current window.

## Algorithm

For each right index:

1. Remove indexes outside the window.
2. Remove smaller values from the back.
3. Add the current index.
4. Once the first full window is reached, record the front value.

## Complexity

Time: O(n)

Space: O(k)

## Pattern

Need maximum/minimum in every moving window?

Think:

Monotonic Deque.
""",
        "topic": "Sliding Window Maximum",
        "difficulty": "Advanced",
        "keywords": "sliding window,deque,monotonic queue,maximum",
    },
}


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


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

    print("EchoMind - Sliding Window Lessons")
    print("Updated :", updated)
    print("Inserted:", inserted)
    print("Total   :", len(LESSONS))


if __name__ == "__main__":
    main()