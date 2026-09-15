from database import init_database, get_connection


LESSONS = {

    "DSA Master - Introduction to Two Pointers": """
Two Pointers is a problem-solving technique in which two indexes or
references move through a data structure.

It is commonly used with:
- arrays
- strings
- sorted sequences
- linked lists

The main purpose is to avoid unnecessary repeated scanning.

Common patterns:

1. Left and Right Pointers
One pointer starts at the beginning and another at the end.

2. Same-Direction Pointers
Two pointers move from left to right at different speeds.

3. Fast and Slow Pointers
One pointer moves faster than the other.

General example:

left = 0
right = n - 1

while left < right:
    process the current elements
    move one or both pointers

Two Pointers can often reduce a brute-force O(n²) solution to O(n).

Important:
The pointer movement must be based on the problem's logic.
""",

    "DSA Master - Two Sum II": """
Two Sum II:

Given a sorted array and a target value, find two numbers whose sum
equals the target.

Example:

numbers = [2, 7, 11, 15]
target = 9

Answer:
2 + 7 = 9

Approach:

left = 0
right = len(numbers) - 1

Calculate:

current_sum = numbers[left] + numbers[right]

If current_sum == target:
    pair found

If current_sum < target:
    move left forward

If current_sum > target:
    move right backward

Why does this work?

The array is sorted.

Moving left to the right increases the selected value.
Moving right to the left decreases the selected value.

Complexity:
Time: O(n)
Space: O(1)

Brute-force pair checking would take O(n²), so Two Pointers gives a
major improvement.
""",

    "DSA Master - Valid Palindrome": """
Valid Palindrome:

A palindrome reads the same from both directions.

Examples:
madam
level
racecar

For the common problem version, spaces, punctuation and letter case
may be ignored.

Two Pointer approach:

left = 0
right = len(string) - 1

While left < right:

1. Ignore invalid characters from the left.
2. Ignore invalid characters from the right.
3. Compare the two valid characters.
4. If they are different, return false.
5. Otherwise:
   left += 1
   right -= 1

Example:

"Madam"

M is compared with m.
a is compared with a.
d is compared with d.

All characters match, so it is a palindrome.

Complexity:
Time: O(n)
Space: O(1) when processed without constructing another cleaned string.

Common mistake:
Comparing the original raw string without applying the required
normalization rules.
""",

    "DSA Master - 3Sum": """
3Sum:

The 3Sum problem asks us to find three values whose sum equals zero.

Example:

[-1, 0, 1, 2, -1, -4]

Valid triplets:

[-1, -1, 2]
[-1, 0, 1]

Efficient approach:

1. Sort the array.
2. Fix one element at index i.
3. Use two pointers for the remaining range.

left = i + 1
right = n - 1

Calculate:

total = nums[i] + nums[left] + nums[right]

If total == 0:
    record the triplet
    move both pointers
    skip duplicates

If total < 0:
    left += 1

If total > 0:
    right -= 1

Why does sorting help?

It makes pointer movement logical and allows duplicate values to be
skipped.

Typical complexity:
Time: O(n²)

Common mistakes:
- forgetting to sort
- returning duplicate triplets
- moving the wrong pointer
- not skipping duplicate values
""",

    "DSA Master - Container With Most Water": """
Container With Most Water:

You are given vertical lines represented by heights.
Choose two lines that contain the maximum possible amount of water.

For positions left and right:

width = right - left

area =
min(height[left], height[right]) * width

Two Pointer approach:

left = 0
right = n - 1

Calculate the current area.

Then move the pointer with the smaller height.

Why?

The width decreases whenever a pointer moves.
If the shorter boundary remains unchanged, moving the taller boundary
cannot increase the limiting height.

Therefore, the shorter side is the side that must be moved.

Complexity:
Time: O(n)
Space: O(1)

This is an important example of finding an O(n) solution instead of
checking every pair in O(n²).
""",

    "DSA Master - Valid Triangle Number": """
Valid Triangle Number:

Given side lengths, count how many triples can form a valid triangle.

For sorted sides:

a <= b <= c

A valid triangle requires:

a + b > c

Approach:

1. Sort the array.
2. Fix the largest side using index k.
3. Set:
   left = 0
   right = k - 1
4. If nums[left] + nums[right] > nums[k]:
   all values between left and right with nums[right] can form
   valid triangles with nums[k].
5. Count those combinations.
6. Move right.
7. Otherwise move left.

Sorting makes it possible to count multiple valid combinations without
checking every triplet independently.

Typical complexity:
Time: O(n²)

Important:
The largest side is the critical value for the triangle inequality.
""",

    "DSA Master - Remove Duplicates from Sorted Array": """
Remove Duplicates from Sorted Array:

The array is already sorted.
The goal is to keep each unique value once.

Example:

[1, 1, 2, 2, 3]

Required valid prefix:

[1, 2, 3]

Use two same-direction pointers:

slow:
Points to the next position where a new unique value should be placed.

fast:
Scans through the array.

When nums[fast] differs from the last kept value:
place it at the slow position and advance slow.

Complexity:
Time: O(n)
Space: O(1)

This is an important example of the slow/fast pointer pattern.

Important:
Only the first k positions normally represent the final unique result.
Elements after that prefix may remain unchanged.
""",

    "DSA Master - Merge Sorted Array": """
Merge Sorted Array:

Two arrays are already sorted.
The goal is to merge them into the first array.

For an in-place solution with enough empty positions at the end,
start from the back.

Pointers:

i -> last valid element of the first array
j -> last element of the second array
k -> last position of the combined array

Compare nums1[i] and nums2[j].

Place the larger value at nums1[k].

Then move the corresponding pointer backward.

Why merge from the back?

If we merge from the front, we may overwrite elements of the first
array that still need to be processed.

Complexity:
Time: O(m + n)
Space: O(1) extra

Common mistake:
Processing from the beginning in an in-place merge.
""",

    "DSA Master - Move Zeroes": """
Move Zeroes:

Move all zero values to the end of the array while maintaining the
relative order of the non-zero values.

Example:

[0, 1, 0, 3, 12]

Result:

[1, 3, 12, 0, 0]

Two Pointer approach:

slow:
Position where the next non-zero value should be written.

fast:
Scans the complete array.

When nums[fast] is non-zero:
1. place it at slow
2. increase slow

After all non-zero values are processed, fill the remaining positions
with zeroes.

Complexity:
Time: O(n)
Space: O(1)

Important:
Relative order of non-zero elements must remain unchanged.
""",

    "DSA Master - Sort Colors": """
Sort Colors:

The array contains only three values:
0, 1 and 2.

The goal is to sort them in one pass using constant extra space.

This is commonly solved using the Dutch National Flag algorithm.

Maintain:

low:
end of the 0 region

mid:
current element being examined

high:
beginning of the 2 region

Rules:

If nums[mid] == 0:
swap nums[low] and nums[mid]
low += 1
mid += 1

If nums[mid] == 1:
mid += 1

If nums[mid] == 2:
swap nums[mid] and nums[high]
high -= 1

Important:
After swapping a 2 with nums[high], do not immediately increment mid.
The new value at mid has not been examined yet.

Complexity:
Time: O(n)
Space: O(1)

This is a classic three-pointer partitioning problem.
""",

    "DSA Master - Rotate Array": """
Rotate Array:

Rotating an array moves elements circularly.

Example:

[1, 2, 3, 4, 5, 6, 7]

Rotate right by 3:

[5, 6, 7, 1, 2, 3, 4]

Efficient in-place method:

1. k = k % n
2. Reverse the whole array.
3. Reverse the first k elements.
4. Reverse the remaining n-k elements.

Example:

Original:
1 2 3 4 5 6 7

Reverse all:
7 6 5 4 3 2 1

Reverse first 3:
5 6 7 4 3 2 1

Reverse remaining:
5 6 7 1 2 3 4

Complexity:
Time: O(n)
Space: O(1)

Important:
Use k % n because rotating by n positions gives the same array.
""",

    "DSA Master - 4Sum": """
4Sum:

The goal is to find four values whose sum equals a target.

Approach:

1. Sort the array.
2. Fix the first element.
3. Fix the second element.
4. Use two pointers for the remaining two values.

Structure:

for i:
    for j:
        left = j + 1
        right = n - 1

Calculate:

nums[i] + nums[j] + nums[left] + nums[right]

If the sum is too small:
    left += 1

If the sum is too large:
    right -= 1

If equal:
    store the quadruplet
    move both pointers
    skip duplicates

Typical complexity:
Time: O(n³)

Sorting is especially important because duplicate quadruplets need
to be avoided.

Common mistakes:
- duplicate answers
- incorrect pointer movement
- not handling repeated values
""",

    "DSA Master - Trapping Rain Water": """
Trapping Rain Water:

Given heights of bars, determine how much rainwater can be trapped.

For an index i:

water[i] =
min(max height on left, max height on right) - height[i]

A brute-force method calculates left and right maximum for every
position, which can take O(n²).

Two Pointer solution:

Maintain:
left
right
leftMax
rightMax

If height[left] <= height[right]:
    update leftMax
    calculate possible water using leftMax
    move left

Otherwise:
    update rightMax
    calculate possible water using rightMax
    move right

Why this works:
When one side is lower, the lower boundary determines how much water
can safely be calculated.

Complexity:
Time: O(n)
Space: O(1)

This is one of the most important advanced Two Pointer problems.
"""
}


def update_lessons():

    init_database()

    connection = get_connection()

    updated = 0
    missing = 0

    for title, content in LESSONS.items():

        row = connection.execute(
            """
            SELECT id
            FROM knowledge
            WHERE title = ?
            LIMIT 1
            """,
            (title,)
        ).fetchone()

        if row:

            connection.execute(
                """
                UPDATE knowledge
                SET content = ?
                WHERE id = ?
                """,
                (
                    content.strip(),
                    row["id"]
                )
            )

            updated += 1

        else:
            missing += 1

    connection.commit()
    connection.close()

    print("=" * 60)
    print("EchoMind - Two Pointers Lessons Updated")
    print("=" * 60)
    print("Updated:", updated)
    print("Missing:", missing)
    print("=" * 60)


if __name__ == "__main__":
    update_lessons()