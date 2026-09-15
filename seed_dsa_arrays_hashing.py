import sqlite3

DATABASE_NAME = "ecomind.db"

LESSONS = {
    "DSA Master - Introduction to Arrays & Hashing": {
        "content": """# Arrays & Hashing

Arrays and hashing are two of the most important foundations in problem solving.

## 1. Arrays

An array stores multiple values in an ordered structure.

Example:

arr = [10, 20, 30, 40, 50]

Indexes:

0 → 10
1 → 20
2 → 30
3 → 40
4 → 50

## 2. Array access

Accessing an element by index is usually O(1).

Example:

arr[2]

returns 30.

## 3. Common array operations

Traversal:
Visit every element.

Searching:
Find whether an element exists.

Insertion:
Add a new element.

Deletion:
Remove an element.

Updating:
Change an existing value.

## 4. Hashing

Hashing allows us to store and find values efficiently.

In Python, dictionaries and sets are commonly used.

Dictionary:

data = {
    "apple": 3,
    "banana": 5
}

Set:

seen = {2, 4, 6, 8}

## 5. Why hashing is useful

Suppose we want to check whether a number appeared before.

Using a list may require O(n) searching.

Using a set usually gives average O(1) lookup.

## 6. Common problem-solving pattern

Many array problems can be solved using:

Array + Set
Array + Dictionary
Frequency Map
Sorting
Prefix Sum

## 7. Exam tip

When a problem asks:

"Have we seen this value before?"

Think about a Set.

When a problem asks:

"How many times does this value occur?"

Think about a Dictionary / frequency map.

When a problem asks:

"What index is associated with this value?"

Think about a Dictionary.

## Complexity

Array index access: O(1)

Set lookup: Average O(1)

Dictionary lookup: Average O(1)

Full array traversal: O(n)
""",
        "topic": "Arrays & Hashing",
        "difficulty": "Beginner",
        "keywords": "array,hashing,set,dictionary,map,frequency",
    },

    "DSA Master - Contains Duplicate": {
        "content": """# Contains Duplicate

## Problem

Given an array, determine whether any value appears more than once.

Example:

nums = [1, 2, 3, 1]

Answer:

True

because 1 occurs twice.

## Approach 1: Brute Force

Compare every pair of elements.

Time Complexity:
O(n²)

Space Complexity:
O(1)

This works but becomes slow for large arrays.

## Approach 2: Set

Create a set of seen elements.

For every number:

1. Check whether it is already in the set.
2. If yes, duplicate found.
3. Otherwise add it to the set.

Python:

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

## Complexity

Time: O(n) average

Space: O(n)

## Important idea

Set = useful when we only need to know whether a value exists.
""",
        "topic": "Contains Duplicate",
        "difficulty": "Beginner",
        "keywords": "array,duplicate,set,hashing",
    },

    "DSA Master - Valid Anagram": {
        "content": """# Valid Anagram

Two strings are anagrams if they contain the same characters with the same frequencies.

Example:

"listen"
"silent"

They are anagrams.

## Frequency Map Approach

Count the frequency of every character in both strings.

Example:

"abbc"

a → 1
b → 2
c → 1

Then compare the frequency maps.

Python:

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True

## Complexity

Time: O(n)

Space: O(k)

where k is the number of distinct characters.

## Pattern

Whenever a problem asks about frequency, think:

Frequency Map / Hash Map.
""",
        "topic": "Valid Anagram",
        "difficulty": "Beginner",
        "keywords": "anagram,string,frequency,map,hashing",
    },

    "DSA Master - Two Sum": {
        "content": """# Two Sum

Given an array of integers and a target value, find two numbers whose sum equals the target.

Example:

nums = [2, 7, 11, 15]
target = 9

2 + 7 = 9

Answer:

[0, 1]

## Brute Force

Check every pair.

Time:
O(n²)

## Hash Map Approach

For every number:

current = nums[i]

We need:

needed = target - current

Check whether needed already exists in the hash map.

If yes, we found the answer.

Otherwise store the current number and its index.

Python:

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return []

## Example

nums = [2, 7, 11, 15]
target = 9

i = 0
num = 2
needed = 7

7 is not found.

Store:

2 → 0

Next:

num = 7
needed = 2

2 exists.

Therefore:

[0, 1]

## Complexity

Time: O(n) average

Space: O(n)

## Important Pattern

Instead of repeatedly searching the array,
store information that future elements may need.
""",
        "topic": "Two Sum",
        "difficulty": "Beginner",
        "keywords": "two sum,array,hash map,dictionary,target",
    },

    "DSA Master - Group Anagrams": {
        "content": """# Group Anagrams

Given a list of strings, group strings that are anagrams.

Example:

["eat", "tea", "tan", "ate", "nat", "bat"]

Output groups:

["eat", "tea", "ate"]
["tan", "nat"]
["bat"]

## Main Idea

Anagrams have the same character composition.

We can sort each word and use the sorted version as a key.

Example:

eat → aet
tea → aet
ate → aet

Therefore they belong to the same group.

## Hash Map

Dictionary structure:

key → list of anagrams

Example:

aet → ["eat", "tea", "ate"]

ant → ["tan", "nat"]

abt → ["bat"]

## Python

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())

## Complexity

Sorting each word takes O(k log k),
where k is the word length.

For n words:

Approximately O(n × k log k)

## Better idea

A frequency tuple can also be used as the key.

This can avoid sorting.

## Pattern

When multiple objects share the same normalized representation,
use that representation as a hash key.
""",
        "topic": "Group Anagrams",
        "difficulty": "Intermediate",
        "keywords": "anagram,hash map,string,frequency,grouping",
    },

    "DSA Master - Top K Frequent Elements": {
        "content": """# Top K Frequent Elements

Given an array, return the k most frequent elements.

Example:

nums = [1,1,1,2,2,3]
k = 2

Answer:

[1,2]

## Step 1: Frequency Map

Count how many times every value occurs.

1 → 3
2 → 2
3 → 1

## Step 2

Find the k values with the highest frequencies.

## Hash Map

Use a dictionary:

count[num] += 1

## Python

from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, freq in count.most_common(k)]

## Bucket Sort Idea

An efficient DSA approach is bucket sorting.

Create buckets where:

index = frequency

For example:

bucket[3] contains values occurring 3 times.

Then scan buckets from highest frequency to lowest.

## Complexity

Frequency counting:

O(n)

Bucket solution:

O(n) approximately

## Pattern

Frequency + ranking problems often use:

Hash Map + Heap

or

Hash Map + Bucket Sort.
""",
        "topic": "Top K Frequent Elements",
        "difficulty": "Intermediate",
        "keywords": "frequency,hash map,bucket sort,heap,top k",
    },

    "DSA Master - Product of Array Except Self": {
        "content": """# Product of Array Except Self

Given an array, return an array where each element is the product of all other elements except itself.

Example:

nums = [1,2,3,4]

Output:

[24,12,8,6]

## Important Restriction

Do not use division.

## Main Idea

For every index:

answer[i] =
product of elements before i
×
product of elements after i

## Prefix and Suffix

Example:

nums = [1,2,3,4]

Prefix products:

1
1
2
6

Suffix products:

24
12
4
1

Combining them:

24
12
8
6

## O(1) Extra Space Approach

First store prefix products in answer.

Then traverse from right to left using a suffix variable.

Python:

def product_except_self(nums):
    result = [1] * len(nums)

    prefix = 1

    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1

    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

## Complexity

Time: O(n)

Extra space: O(1), excluding output array.

## Pattern

Many array problems become easier when we separate:

Left information
+
Right information.
""",
        "topic": "Product of Array Except Self",
        "difficulty": "Intermediate",
        "keywords": "array,prefix,suffix,product",
    },

    "DSA Master - Longest Consecutive Sequence": {
        "content": """# Longest Consecutive Sequence

Find the length of the longest sequence of consecutive integers.

Example:

nums = [100,4,200,1,3,2]

Longest sequence:

1,2,3,4

Answer:

4

## Hash Set Approach

Put all values into a set.

Then check which numbers are starts of sequences.

A number is a sequence start when:

num - 1

does not exist.

## Python

def longest_consecutive(nums):
    values = set(nums)
    longest = 0

    for num in values:
        if num - 1 not in values:
            length = 1

            while num + length in values:
                length += 1

            longest = max(longest, length)

    return longest

## Why Set?

Set membership is average O(1).

This allows us to avoid sorting.

## Complexity

Average Time: O(n)

Space: O(n)

## Pattern

Unordered numbers + fast existence checking

→ Think Hash Set.
""",
        "topic": "Longest Consecutive Sequence",
        "difficulty": "Intermediate",
        "keywords": "array,set,hashing,consecutive",
    },

    "DSA Master - Majority Element": {
        "content": """# Majority Element

Given an array, find the element that appears more than n/2 times.

Example:

[2,2,1,1,1,2,2]

Answer:

2

## Hash Map Approach

Count every element.

Then find the element whose frequency is greater than n/2.

## Better Approach

Boyer-Moore Voting Algorithm.

Maintain:

candidate
count

When count becomes zero,
choose the current number as the new candidate.

## Python

def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        count += 1 if num == candidate else -1

    return candidate

## Complexity

Time: O(n)

Space: O(1)

## Important Idea

The majority element has more occurrences than all other elements combined.

This allows cancellation of different elements.
""",
        "topic": "Majority Element",
        "difficulty": "Intermediate",
        "keywords": "array,majority,boyer moore,voting algorithm",
    },

    "DSA Master - First Missing Positive": {
        "content": """# First Missing Positive

Find the smallest positive integer missing from an unsorted array.

Example:

[3,4,-1,1]

Answer:

2

## Simple Approach

Use a set.

Store all positive values.

Then start from 1 and find the first missing number.

## Python

def first_missing_positive(nums):
    values = set(nums)

    answer = 1

    while answer in values:
        answer += 1

    return answer

## Complexity

Time: O(n)

Space: O(n)

## Advanced Approach

An optimal solution can achieve O(n) time and O(1) extra space by placing numbers into their correct indexes.

For value x:

ideal index = x - 1

This is called cyclic placement.

## Pattern

When numbers range from 1 to n,
index-position relationships can often be exploited.
""",
        "topic": "First Missing Positive",
        "difficulty": "Advanced",
        "keywords": "array,missing positive,set,cyclic sort",
    },

    "DSA Master - Subarray Sum Equals K": {
        "content": """# Subarray Sum Equals K

Given an integer array and target k, count the number of subarrays whose sum equals k.

Example:

nums = [1,1,1]
k = 2

Answer:

2

because:

[1,1]
[1,1]

## Prefix Sum Idea

Maintain a running sum.

Suppose current prefix sum is:

sum

We need an earlier prefix sum:

sum - k

because:

current_sum - previous_sum = k

## Hash Map

Store how many times each prefix sum has appeared.

Python:

def subarray_sum(nums, k):
    count = {0: 1}
    prefix = 0
    answer = 0

    for num in nums:
        prefix += num

        needed = prefix - k

        if needed in count:
            answer += count[needed]

        count[prefix] = count.get(prefix, 0) + 1

    return answer

## Complexity

Time: O(n)

Space: O(n)

## Important Pattern

Prefix Sum + Hash Map

is one of the most important patterns for subarray problems.
""",
        "topic": "Subarray Sum Equals K",
        "difficulty": "Intermediate",
        "keywords": "subarray,prefix sum,hash map,target sum",
    },

    "DSA Master - Longest Subarray with Sum K": {
        "content": """# Longest Subarray with Sum K

Find the longest subarray whose sum equals k.

## Prefix Sum

Maintain a running sum.

For every index i:

prefix = sum from start to i

If:

prefix - k

was seen earlier,
then the portion between those indexes has sum k.

## Important Difference

For counting subarrays:

Store frequency of prefix sums.

For longest subarray:

Store the earliest index of each prefix sum.

## Python

def longest_subarray_sum_k(nums, k):
    first_index = {0: -1}
    prefix = 0
    longest = 0

    for i, num in enumerate(nums):
        prefix += num

        if prefix - k in first_index:
            longest = max(longest, i - first_index[prefix - k])

        if prefix not in first_index:
            first_index[prefix] = i

    return longest

## Complexity

Time: O(n)

Space: O(n)

## Pattern

Prefix Sum + Earliest Index
→ Longest subarray problems.
""",
        "topic": "Longest Subarray with Sum K",
        "difficulty": "Intermediate",
        "keywords": "subarray,prefix sum,longest,array,hash map",
    },

    "DSA Master - Frequency Counter Pattern": {
        "content": """# Frequency Counter Pattern

The frequency counter pattern means storing how many times values occur.

Example:

nums = [1,2,2,3,3,3]

Frequency:

1 → 1
2 → 2
3 → 3

## Python

count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

## Why Use It?

It avoids repeatedly scanning the array.

Without a frequency map:

Repeated searches can become O(n²).

With a frequency map:

Counting can usually be done in O(n).

## Common Problems

Frequency counter is useful for:

Anagrams
Duplicates
Majority Element
Top K Frequent Elements
Character counting
Most frequent values

## Pattern Recognition

Question says:

"How many times?"

"Does frequency exceed..."

"Are these characters the same?"

"Which value occurs most?"

Think:

Frequency Map.
""",
        "topic": "Frequency Counter Pattern",
        "difficulty": "Beginner",
        "keywords": "frequency,map,counting,hashing",
    },

    "DSA Master - Hash Set Pattern": {
        "content": """# Hash Set Pattern

A set stores unique values.

Example:

values = {1,2,3,4}

If we add 3 again:

values.add(3)

the set remains:

{1,2,3,4}

## Main Advantage

Fast membership checking.

Example:

if x in values:
    ...

## Common Uses

Detect duplicates.

Check whether a value exists.

Find missing values.

Track visited items.

Find consecutive sequences.

## Example

nums = [1,2,3,1]

seen = set()

for num in nums:

    if num in seen:
        print("Duplicate")

    seen.add(num)

## Complexity

Average membership lookup:

O(1)

## Pattern

Need only existence information?

Use a Set.

Need value + associated information?

Use a Dictionary.
""",
        "topic": "Hash Set Pattern",
        "difficulty": "Beginner",
        "keywords": "set,hash set,membership,duplicates",
    },

    "DSA Master - Hash Map Pattern": {
        "content": """# Hash Map Pattern

A hash map stores key-value pairs.

In Python, the dictionary is a hash map.

Example:

student = {
    "name": "Aditya",
    "marks": 85
}

## Common DSA Uses

Store:

value → index

value → frequency

character → frequency

prefix sum → index

prefix sum → frequency

## Example

nums = [2,7,11,15]

For Two Sum:

2 → index 0
7 → index 1

When we need a complement,
we can find its index quickly.

## Complexity

Average insertion:

O(1)

Average lookup:

O(1)

Average deletion:

O(1)

## Pattern

Use a Hash Map when the problem needs:

Lookup
Mapping
Counting
Index tracking
Fast association between two pieces of information.
""",
        "topic": "Hash Map Pattern",
        "difficulty": "Beginner",
        "keywords": "dictionary,hash map,key value,lookup",
    },

    "DSA Master - Prefix Sum": {
        "content": """# Prefix Sum

Prefix sum stores cumulative sums.

Example:

nums = [2,4,3,5]

Prefix:

[2,6,9,14]

Because:

2
2+4 = 6
2+4+3 = 9
2+4+3+5 = 14

## Range Sum

Suppose we want the sum from index l to r.

Using prefix sums:

range_sum = prefix[r] - prefix[l-1]

with a special case when l = 0.

## Example

nums = [2,4,3,5]

Prefix = [2,6,9,14]

Sum from index 1 to 3:

14 - 2 = 12

which is:

4 + 3 + 5 = 12

## Complexity

Building prefix:

O(n)

Each range query:

O(1)

## Important Pattern

Prefix Sum is useful when many range-sum queries are required.
""",
        "topic": "Prefix Sum",
        "difficulty": "Beginner",
        "keywords": "prefix sum,array,range sum",
    },

    "DSA Master - Array Sorting as a Pattern": {
        "content": """# Sorting as a Problem-Solving Pattern

Sorting is not only a standalone algorithmic topic.

It can simplify many problems.

Example:

nums = [7,2,9,1,5]

After sorting:

[1,2,5,7,9]

Now relationships between nearby elements become easier to analyze.

## Sorting Helps With

Two Pointers

Intervals

Duplicate detection

Greedy algorithms

Closest values

3Sum

4Sum

Meeting room problems

## Example

For duplicate detection:

[4,2,4,1]

Sort:

[1,2,4,4]

Now duplicate values become adjacent.

## Complexity

Typical efficient comparison sorting:

O(n log n)

## Pattern

When order matters or nearby values need comparison,
consider sorting first.

But remember:

Sorting may destroy the original indexes.

If indexes matter,
store them before sorting or use another technique.
""",
        "topic": "Sorting as a Problem-Solving Pattern",
        "difficulty": "Beginner",
        "keywords": "sorting,array,two pointers,greedy,duplicates",
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

        # Check whether the lesson already exists
        cursor.execute(
            "SELECT id FROM knowledge WHERE title = ?",
            (title,)
        )

        row = cursor.fetchone()

        if row:
            # Update existing lesson
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
            # Insert missing lesson
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

    print("EchoMind - Arrays & Hashing Lessons")
    print("Updated :", updated)
    print("Inserted:", inserted)
    print("Total   :", len(LESSONS))


if __name__ == "__main__":
    main()