import sqlite3

DATABASE_NAME = "ecomind.db"

LESSONS = {
    "DSA Master - Introduction to Stack": {
        "content": """# Stack

A Stack is a linear data structure that follows:

LIFO = Last In, First Out

The element inserted last is removed first.

## Real-life example

Imagine a stack of plates.

You put a new plate on top.

You also remove the top plate first.

## Main operations

### Push

Adds an element to the top.

### Pop

Removes the top element.

### Peek

Returns the top element without removing it.

### isEmpty

Checks whether the stack contains elements.

## Example

Stack:

[10, 20, 30]

Top = 30

Push 40:

[10, 20, 30, 40]

Pop:

40 is removed.

Stack becomes:

[10, 20, 30]

## Complexity

Push: O(1)

Pop: O(1)

Peek: O(1)

isEmpty: O(1)

## Important

Stack is used in:

Function calls
Undo operations
Browser history
Expression evaluation
Parentheses checking
DFS
Backtracking
Monotonic stack problems

## Pattern

When the latest item must be processed first:

Think Stack.
""",
        "topic": "Stack",
        "difficulty": "Beginner",
        "keywords": "stack,lifo,push,pop,peek,data structure",
    },

    "DSA Master - Stack Implementation Using Array": {
        "content": """# Stack Implementation Using Array

A stack can be implemented using an array or Python list.

## Python

stack = []

Push:

stack.append(10)

stack.append(20)

stack.append(30)

Stack:

[10, 20, 30]

## Pop

value = stack.pop()

The removed value is 30.

## Peek

top = stack[-1]

## Check Empty

if not stack:
    print("Stack is empty")

## Complete example

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack[-1])

print(stack.pop())

print(stack)

## Complexity

append(): O(1) amortized

pop(): O(1)

peek using [-1]: O(1)

## Important

Python list provides an efficient implementation for a basic stack.
""",
        "topic": "Stack Implementation Using Array",
        "difficulty": "Beginner",
        "keywords": "stack,array,list,push,pop,python",
    },

    "DSA Master - Valid Parentheses": {
        "content": """# Valid Parentheses

Given a string containing:

()
{}
[]

determine whether the brackets are correctly matched.

Example:

"()[]{}"

True

Example:

"([)]"

False

## Stack Approach

Whenever an opening bracket appears:

Push it.

Whenever a closing bracket appears:

Check the top of the stack.

It must contain the matching opening bracket.

## Python

def is_valid(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:

        if char in "([{":
            stack.append(char)

        else:
            if not stack:
                return False

            if stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

## Example

Input:

"{[]}".

Process:

{ → push
[ → push
] → matches [
} → matches {

Stack becomes empty.

Answer:

True

## Complexity

Time: O(n)

Space: O(n)

## Pattern

Nested matching structures

→ Stack.
""",
        "topic": "Valid Parentheses",
        "difficulty": "Beginner",
        "keywords": "stack,parentheses,brackets,matching",
    },

    "DSA Master - Min Stack": {
        "content": """# Min Stack

Design a stack that supports:

push
pop
top
getMin

and getMin must work in O(1).

## Problem

Normal stack gives O(1) push and pop.

But finding the minimum by scanning the entire stack takes O(n).

We need another idea.

## Two Stack Approach

Maintain:

main stack
minimum stack

Example:

Push 5

main = [5]
min = [5]

Push 3

main = [5,3]
min = [5,3]

Push 7

main = [5,3,7]
min = [5,3,3]

The minimum stack keeps track of the smallest value seen so far.

## Python

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(
                min(value, self.min_stack[-1])
            )

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]

## Complexity

Push: O(1)

Pop: O(1)

Top: O(1)

Get Min: O(1)

Space: O(n)

## Pattern

Need stack operations + constant-time minimum?

Think auxiliary minimum stack.
""",
        "topic": "Min Stack",
        "difficulty": "Intermediate",
        "keywords": "stack,min stack,auxiliary stack,minimum",
    },

    "DSA Master - Evaluate Reverse Polish Notation": {
        "content": """# Evaluate Reverse Polish Notation

Reverse Polish Notation places operators after operands.

Example:

["2","1","+","3","*"]

means:

(2 + 1) * 3

Answer:

9

## Stack Approach

If token is a number:

Push it.

If token is an operator:

Pop the second operand.

Pop the first operand.

Apply the operator.

Push the result.

## Python

def eval_rpn(tokens):
    stack = []

    for token in tokens:

        if token not in "+-*/":
            stack.append(int(token))
            continue

        b = stack.pop()
        a = stack.pop()

        if token == '+':
            result = a + b
        elif token == '-':
            result = a - b
        elif token == '*':
            result = a * b
        else:
            result = int(a / b)

        stack.append(result)

    return stack[-1]

## Important

Order matters.

For subtraction:

a - b

For division:

a / b

Do not reverse them.

## Complexity

Time: O(n)

Space: O(n)

## Pattern

Expression evaluation

→ Stack.
""",
        "topic": "Evaluate Reverse Polish Notation",
        "difficulty": "Intermediate",
        "keywords": "stack,rpn,expression,evaluation,postfix",
    },

    "DSA Master - Daily Temperatures": {
        "content": """# Daily Temperatures

Given temperatures, determine how many days must pass before a warmer temperature appears.

Example:

[73,74,75,71,69,72,76,73]

Output:

[1,1,4,2,1,1,0,0]

## Monotonic Stack

Store indexes whose temperatures have not yet found a warmer day.

When current temperature is greater than the temperature at the top index:

A warmer day has been found.

Pop the old index.

Calculate the distance.

## Python

def daily_temperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):

        while stack and temperatures[stack[-1]] < temp:
            previous = stack.pop()
            answer[previous] = i - previous

        stack.append(i)

    return answer

## Why Stack?

The unresolved temperatures need to wait.

When a warmer temperature appears, resolve them in reverse order.

## Complexity

Time: O(n)

Space: O(n)

## Pattern

Next greater element

→ Monotonic Stack.
""",
        "topic": "Daily Temperatures",
        "difficulty": "Intermediate",
        "keywords": "stack,monotonic stack,next greater,daily temperatures",
    },

    "DSA Master - Next Greater Element": {
        "content": """# Next Greater Element

For every element, find the next element to its right that is greater.

Example:

nums = [2,1,2,4,3]

Output:

[4,2,4,-1,-1]

## Monotonic Stack

Traverse from right to left.

Maintain a stack of possible greater elements.

Before using the top:

Remove values smaller than or equal to the current value.

Then:

top = next greater element

Push current value.

## Python

def next_greater(nums):
    answer = [-1] * len(nums)
    stack = []

    for i in range(len(nums) - 1, -1, -1):

        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            answer[i] = stack[-1]

        stack.append(nums[i])

    return answer

## Complexity

Time: O(n)

Space: O(n)

## Pattern

Looking for the next larger value

→ Monotonic Stack.
""",
        "topic": "Next Greater Element",
        "difficulty": "Intermediate",
        "keywords": "stack,next greater,monotonic stack,array",
    },

    "DSA Master - Largest Rectangle in Histogram": {
        "content": """# Largest Rectangle in Histogram

Given bar heights, find the largest rectangle that can be formed.

Example:

[2,1,5,6,2,3]

Answer:

10

The rectangle using heights 5 and 6 has area:

5 × 2 = 10

## Main Idea

For each bar, determine how far it can extend left and right while maintaining its height.

A brute-force solution is slow.

## Monotonic Increasing Stack

Maintain indexes of bars in increasing height order.

When a smaller bar appears:

bars are popped because their right boundary has been found.

Calculate:

area = height × width

## Python

def largest_rectangle(heights):
    stack = []
    max_area = 0

    for i in range(len(heights) + 1):

        current = 0 if i == len(heights) else heights[i]

        while stack and heights[stack[-1]] > current:
            height = heights[stack.pop()]

            left = stack[-1] if stack else -1
            width = i - left - 1

            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area

## Complexity

Time: O(n)

Space: O(n)

## Pattern

Rectangle boundaries in histograms

→ Monotonic Stack.
""",
        "topic": "Largest Rectangle in Histogram",
        "difficulty": "Advanced",
        "keywords": "stack,histogram,monotonic stack,rectangle",
    },

    "DSA Master - Trapping Rain Water Using Stack": {
        "content": """# Trapping Rain Water Using Stack

Given elevation heights, determine how much rainwater can be trapped.

Example:

[0,1,0,2,1,0,1,3,2,1,2,1]

Answer:

6

## Stack Approach

Use a decreasing stack of indexes.

When the current height is greater than the height at the stack top:

A valley has been closed.

Pop the bottom of the valley.

Then calculate:

height = min(left_wall, right_wall) - valley_height

width = current_index - left_index - 1

water = height × width

## Python

def trap(height):
    stack = []
    water = 0

    for right in range(len(height)):

        while stack and height[right] > height[stack[-1]]:

            bottom = stack.pop()

            if not stack:
                break

            left = stack[-1]

            bounded_height = min(
                height[left],
                height[right]
            ) - height[bottom]

            width = right - left - 1

            water += bounded_height * width

        stack.append(right)

    return water

## Complexity

Time: O(n)

Space: O(n)

## Pattern

Water trapped between boundaries

→ Monotonic Stack.
""",
        "topic": "Trapping Rain Water Using Stack",
        "difficulty": "Advanced",
        "keywords": "stack,rain water,monotonic stack,trapping water",
    },

    "DSA Master - Remove Adjacent Duplicates": {
        "content": """# Remove Adjacent Duplicates

Given a string, repeatedly remove adjacent equal characters.

Example:

"abbaca"

First:

abbaca

Remove bb:

aaca

Remove aa:

ca

Answer:

"ca"

## Stack Approach

Traverse the string.

If current character equals the stack top:

pop

Otherwise:

push

## Python

def remove_duplicates(s):
    stack = []

    for char in s:

        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)

## Complexity

Time: O(n)

Space: O(n)

## Pattern

When a new element may cancel the most recent unresolved element:

Think Stack.
""",
        "topic": "Remove Adjacent Duplicates",
        "difficulty": "Beginner",
        "keywords": "stack,string,duplicates,cancellation",
    },

    "DSA Master - Asteroid Collision": {
        "content": """# Asteroid Collision

Asteroids move either right or left.

Positive number = moving right.

Negative number = moving left.

When a right-moving asteroid meets a left-moving asteroid, they collide.

Example:

[5,10,-5]

10 survives.

Example:

[8,-8]

Both disappear.

## Stack Approach

Add asteroids to a stack.

For a negative asteroid, compare it with positive asteroids currently at the top.

Cases:

top < abs(current)

Pop top.

top == abs(current)

Pop top and destroy current.

top > abs(current)

Destroy current.

## Python

def asteroid_collision(asteroids):
    stack = []

    for asteroid in asteroids:

        alive = True

        while (
            alive
            and asteroid < 0
            and stack
            and stack[-1] > 0
        ):
            if stack[-1] < -asteroid:
                stack.pop()
            elif stack[-1] == -asteroid:
                stack.pop()
                alive = False
            else:
                alive = False

        if alive:
            stack.append(asteroid)

    return stack

## Complexity

Time: O(n) amortized

Space: O(n)

## Pattern

Objects interact with the most recent unresolved object

→ Stack.
""",
        "topic": "Asteroid Collision",
        "difficulty": "Intermediate",
        "keywords": "stack,asteroid,collision,array",
    },

    "DSA Master - Decode String": {
        "content": """# Decode String

Decode encoded strings such as:

3[a2[c]]

which becomes:

accaccacc

## Stack Approach

Use stacks for:

numbers
strings

When an opening bracket appears, save the current state.

When a closing bracket appears:

1. Get the previous string.
2. Get the multiplier.
3. Repeat the current string.
4. Combine them.

## Example

2[ab]

Save empty string.

Read 2.

Read [.

Build "ab".

At ]:

repeat "ab" twice.

Result:

"abab"

## Python

def decode_string(s):
    stack = []
    current = ""
    number = 0

    for char in s:

        if char.isdigit():
            number = number * 10 + int(char)

        elif char == '[':
            stack.append((current, number))
            current = ""
            number = 0

        elif char == ']':
            previous, repeat = stack.pop()
            current = previous + current * repeat

        else:
            current += char

    return current

## Complexity

Approximately O(n) relative to the produced output, although repeated expansion can make the actual output much larger than the encoded input.

## Pattern

Nested structures that must be reconstructed in reverse order

→ Stack.
""",
        "topic": "Decode String",
        "difficulty": "Intermediate",
        "keywords": "stack,string,decode,nested brackets",
    },

    "DSA Master - Basic Calculator": {
        "content": """# Basic Calculator

Evaluate an arithmetic expression containing numbers, +, -, parentheses, and spaces.

Example:

"1 + (2 - 3)"

Answer:

0

## Stack Idea

Parentheses create nested calculations.

When "(" appears:

save the current result and sign.

When ")" appears:

finish the current expression.

Then combine it with the saved result.

## General Logic

Maintain:

result
number
sign
stack

## Example

For:

1 + (2 - 3)

The parenthesized expression is evaluated separately.

Its result is then combined with the outside expression.

## Complexity

Time: O(n)

Space: O(n)

## Pattern

Nested arithmetic expressions

→ Stack.
""",
        "topic": "Basic Calculator",
        "difficulty": "Advanced",
        "keywords": "stack,calculator,expression,parentheses",
    },

    "DSA Master - Stack and DFS Connection": {
        "content": """# Stack and DFS Connection

Depth-First Search can be implemented using recursion or an explicit stack.

## Recursive DFS

The programming language's call stack keeps track of the nodes.

## Iterative DFS

We create our own stack.

Example:

stack = [start]

while stack:

    node = stack.pop()

    process(node)

    for neighbor in graph[node]:
        stack.append(neighbor)

## Why does this work?

DFS always explores one path deeply before returning.

LIFO behavior naturally matches this requirement.

## Complexity

For a graph:

Time: O(V + E)

Space: O(V)

## Important Connection

Recursion often hides a stack.

Whenever you replace recursion with iteration,
you frequently use an explicit stack.
""",
        "topic": "Stack and DFS Connection",
        "difficulty": "Intermediate",
        "keywords": "stack,dfs,graph,recursion,iterative",
    },

    "DSA Master - Monotonic Stack Pattern": {
        "content": """# Monotonic Stack Pattern

A monotonic stack maintains elements in increasing or decreasing order.

## Increasing Stack

Values remain increasing from bottom to top.

## Decreasing Stack

Values remain decreasing from bottom to top.

## Why?

This helps solve problems involving:

Next Greater Element
Next Smaller Element
Previous Greater Element
Largest Rectangle
Daily Temperatures
Stock Span

## Typical Algorithm

For each element:

while the stack violates the required order:

    pop

then:

push current element

## Important Observation

Each element is pushed once and popped at most once.

Therefore the total work is O(n).

## Complexity

Time: O(n)

Space: O(n)

## Pattern

Need nearest greater/smaller information?

Think:

Monotonic Stack.
""",
        "topic": "Monotonic Stack Pattern",
        "difficulty": "Intermediate",
        "keywords": "monotonic stack,next greater,next smaller",
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

    print("EchoMind - Stack Lessons")
    print("Updated :", updated)
    print("Inserted:", inserted)
    print("Total   :", len(LESSONS))


if __name__ == "__main__":
    main()