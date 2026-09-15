import sqlite3

DATABASE_NAME = "ecomind.db"

LESSONS = {
    "DSA Master - Introduction to Linked List": {
        "content": """# Linked List

A Linked List is a linear data structure made of nodes.

Each node usually contains:

1. Data
2. A reference to the next node

## Example

10 -> 20 -> 30 -> None

Here:

10 is the first node.
20 is the second node.
30 is the last node.
None means the list has ended.

## Why use Linked List?

Arrays store elements in contiguous memory.

Linked Lists connect nodes using references.

Insertion and deletion can be efficient when the correct node position is already known.

## Types

1. Singly Linked List
2. Doubly Linked List
3. Circular Linked List

## Important terms

Head:
First node.

Tail:
Last node.

Next:
Reference to the next node.

## Complexity

Access by position: O(n)

Search: O(n)

Insert at head: O(1)

Delete at head: O(1)

## Pattern

When a problem involves nodes connected through references:

Think Linked List.
""",
        "topic": "Linked List",
        "difficulty": "Beginner",
        "keywords": "linked list,node,head,tail,next",
    },

    "DSA Master - Singly Linked List": {
        "content": """# Singly Linked List

A Singly Linked List contains nodes where every node points to the next node.

Example:

10 -> 20 -> 30 -> None

## Node Structure

In Python:

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

## Creating Nodes

first = Node(10)
second = Node(20)
third = Node(30)

Connect them:

first.next = second
second.next = third

Now:

first -> second -> third -> None

## Head

The first node is called head.

head = first

## Traversal

Start from head and repeatedly follow next.

current = head

while current:
    print(current.value)
    current = current.next

## Complexity

Traversal: O(n)

Search: O(n)

Insert at head: O(1)
""",
        "topic": "Singly Linked List",
        "difficulty": "Beginner",
        "keywords": "linked list,singly,node,head,next",
    },

    "DSA Master - Linked List Traversal": {
        "content": """# Linked List Traversal

Traversal means visiting every node in a linked list.

Example:

10 -> 20 -> 30 -> None

Start at head.

Then repeatedly move to:

current.next

## Python

def print_list(head):
    current = head

    while current:
        print(current.value)
        current = current.next

## Step-by-step

current = 10

print 10

move to 20

print 20

move to 30

print 30

move to None

stop

## Complexity

Time: O(n)

Space: O(1)

## Pattern

Linked Lists do not provide direct index access like arrays.

To reach a position, we normally traverse from the head.
""",
        "topic": "Linked List Traversal",
        "difficulty": "Beginner",
        "keywords": "linked list,traversal,node,pointer",
    },

    "DSA Master - Insert Node at Head": {
        "content": """# Insert Node at Head

Adding a node at the beginning of a singly linked list is O(1).

Example:

Before:

20 -> 30 -> None

Insert 10.

After:

10 -> 20 -> 30 -> None

## Algorithm

1. Create new node.
2. Point new node to current head.
3. Make new node the new head.

## Python

def insert_at_head(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node

## Complexity

Time: O(1)

Space: O(1) extra excluding the new node.

## Important

The head changes after insertion.
""",
        "topic": "Insert Node at Head",
        "difficulty": "Beginner",
        "keywords": "linked list,insertion,head,node",
    },

    "DSA Master - Insert Node at Tail": {
        "content": """# Insert Node at Tail

Adding a node at the end of a singly linked list requires reaching the last node when no tail pointer is available.

Example:

10 -> 20 -> None

Insert 30:

10 -> 20 -> 30 -> None

## Algorithm

1. Create a new node.
2. If list is empty, return new node.
3. Traverse to the last node.
4. Set last.next = new node.

## Python

def insert_at_tail(head, value):
    new_node = Node(value)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node

    return head

## Complexity

Time: O(n)

With a tail pointer, insertion can be O(1).
""",
        "topic": "Insert Node at Tail",
        "difficulty": "Beginner",
        "keywords": "linked list,insertion,tail,node",
    },

    "DSA Master - Delete Node from Linked List": {
        "content": """# Delete Node from Linked List

To delete a node from a singly linked list, the previous node must point to the deleted node's next node.

Example:

10 -> 20 -> 30 -> None

Delete 20.

Result:

10 -> 30 -> None

## Algorithm

1. Find the previous node.
2. Skip the target node.
3. Connect previous.next to target.next.

## Python

def delete_value(head, value):

    if head is None:
        return None

    if head.value == value:
        return head.next

    current = head

    while current.next:

        if current.next.value == value:
            current.next = current.next.next
            break

        current = current.next

    return head

## Complexity

Search + deletion:

O(n)

## Important

Deleting the head is a special case because head itself changes.
""",
        "topic": "Delete Node from Linked List",
        "difficulty": "Beginner",
        "keywords": "linked list,deletion,node,head,next",
    },

    "DSA Master - Reverse Linked List": {
        "content": """# Reverse Linked List

Reverse a linked list.

Example:

1 -> 2 -> 3 -> None

becomes:

3 -> 2 -> 1 -> None

## Three Variables

Use:

previous
current
next_node

## Algorithm

current.next = previous

Then move forward.

## Python

def reverse_list(head):
    previous = None
    current = head

    while current:

        next_node = current.next

        current.next = previous

        previous = current
        current = next_node

    return previous

## Example

Initially:

previous = None
current = 1

After first iteration:

1 -> None

Then process 2:

2 -> 1 -> None

Then 3:

3 -> 2 -> 1 -> None

## Complexity

Time: O(n)

Space: O(1)

## Pattern

Reverse pointers one node at a time.
""",
        "topic": "Reverse Linked List",
        "difficulty": "Beginner",
        "keywords": "linked list,reverse,pointers,iteration",
    },

    "DSA Master - Find Middle of Linked List": {
        "content": """# Find Middle of Linked List

Find the middle node of a linked list.

Example:

1 -> 2 -> 3 -> 4 -> 5

Middle:

3

## Slow and Fast Pointers

Use two pointers:

slow
fast

Move:

slow = slow.next

fast = fast.next.next

When fast reaches the end, slow is at the middle.

## Python

def middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

## Why does it work?

Fast moves twice as quickly as slow.

Therefore when fast finishes,
slow has traveled approximately half the distance.

## Complexity

Time: O(n)

Space: O(1)

## Pattern

Middle of Linked List

→ Slow and Fast Pointers.
""",
        "topic": "Find Middle of Linked List",
        "difficulty": "Beginner",
        "keywords": "linked list,middle,slow fast pointers",
    },

    "DSA Master - Detect Cycle in Linked List": {
        "content": """# Detect Cycle in Linked List

A cycle occurs when a node eventually points back to an earlier node.

Example:

1 -> 2 -> 3 -> 4
     ^         |
     |_________|

There is no None at the end.

## Floyd's Cycle Detection

Use:

slow
fast

slow moves one step.

fast moves two steps.

If they meet, a cycle exists.

## Python

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

## Complexity

Time: O(n)

Space: O(1)

## Important

This is also called the Tortoise and Hare algorithm.
""",
        "topic": "Detect Cycle in Linked List",
        "difficulty": "Intermediate",
        "keywords": "linked list,cycle,floyd,slow fast,tortoise hare",
    },

    "DSA Master - Linked List Cycle II": {
        "content": """# Linked List Cycle II

Instead of only detecting a cycle, find the node where the cycle begins.

## Floyd's Algorithm

First use slow and fast pointers.

When they meet:

Move one pointer back to head.

Then move both pointers one step at a time.

Their next meeting point is the cycle entrance.

## Python

def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

## Complexity

Time: O(n)

Space: O(1)

## Pattern

Cycle detection + entrance

→ Floyd's algorithm.
""",
        "topic": "Linked List Cycle II",
        "difficulty": "Intermediate",
        "keywords": "linked list,cycle,cycle entrance,floyd",
    },

    "DSA Master - Merge Two Sorted Linked Lists": {
        "content": """# Merge Two Sorted Linked Lists

Given two sorted linked lists, merge them into one sorted linked list.

Example:

1 -> 3 -> 5

2 -> 4 -> 6

Result:

1 -> 2 -> 3 -> 4 -> 5 -> 6

## Two Pointer Approach

Maintain pointers:

a
b

Compare their current values.

Attach the smaller node to the result.

## Python

def merge_two_lists(list1, list2):

    dummy = Node(0)
    current = dummy

    while list1 and list2:

        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next

## Complexity

Time: O(n + m)

Space: O(1) extra.
""",
        "topic": "Merge Two Sorted Linked Lists",
        "difficulty": "Intermediate",
        "keywords": "linked list,merge,sorted,two pointers",
    },

    "DSA Master - Remove Nth Node From End": {
        "content": """# Remove Nth Node From End

Remove the nth node counting from the end.

Example:

1 -> 2 -> 3 -> 4 -> 5

Remove 2nd node from end.

Answer:

1 -> 2 -> 3 -> 5

## Two Pointer Approach

Use:

fast
slow

Move fast n steps ahead.

Then move both until fast reaches the end.

The slow pointer will be just before the target node.

## Python

def remove_nth_from_end(head, n):

    dummy = Node(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next

## Complexity

Time: O(n)

Space: O(1)

## Pattern

Need the nth node from the end?

Think two pointers.
""",
        "topic": "Remove Nth Node From End",
        "difficulty": "Intermediate",
        "keywords": "linked list,two pointers,nth from end,delete",
    },

    "DSA Master - Palindrome Linked List": {
        "content": """# Palindrome Linked List

Determine whether the linked list reads the same forward and backward.

Example:

1 -> 2 -> 2 -> 1

True

Example:

1 -> 2 -> 3

False

## Efficient Approach

1. Find the middle.
2. Reverse the second half.
3. Compare both halves.
4. Optionally restore the list.

## Why?

A linked list cannot be accessed from the end efficiently.

Reversing the second half gives us forward access to the backward portion.

## Complexity

Time: O(n)

Space: O(1)

## Pattern

Palindrome + Linked List

→ Middle + Reverse + Compare.
""",
        "topic": "Palindrome Linked List",
        "difficulty": "Intermediate",
        "keywords": "linked list,palindrome,middle,reverse",
    },

    "DSA Master - Intersection of Two Linked Lists": {
        "content": """# Intersection of Two Linked Lists

Find the node where two linked lists intersect.

Example:

A: 1 -> 2 -> 3
             \
              7 -> 8

B:     4 -> 5
             \
              7 -> 8

The intersection starts at node 7.

## Two Pointer Trick

Use pointers:

a = headA
b = headB

When a reaches the end, move it to headB.

When b reaches the end, move it to headA.

Eventually they align at the intersection or both become None.

## Python

def get_intersection_node(headA, headB):

    a = headA
    b = headB

    while a != b:

        a = headB if a is None else a.next
        b = headA if b is None else b.next

    return a

## Complexity

Time: O(n + m)

Space: O(1)

## Pattern

Two lists with a shared tail

→ Two-pointer switching heads.
""",
        "topic": "Intersection of Two Linked Lists",
        "difficulty": "Intermediate",
        "keywords": "linked list,intersection,two pointers",
    },

    "DSA Master - Reorder Linked List": {
        "content": """# Reorder Linked List

Reorder:

1 -> 2 -> 3 -> 4 -> 5

into:

1 -> 5 -> 2 -> 4 -> 3

## Main Steps

1. Find the middle.
2. Reverse the second half.
3. Merge the two halves alternately.

## Example

First half:

1 -> 2 -> 3

Second half:

4 -> 5

Reverse:

5 -> 4

Merge:

1 -> 5 -> 2 -> 4 -> 3

## Complexity

Time: O(n)

Space: O(1)

## Pattern

Reordering a linked list often combines:

Middle finding
+
Reverse
+
Merge
""",
        "topic": "Reorder Linked List",
        "difficulty": "Advanced",
        "keywords": "linked list,reorder,middle,reverse,merge",
    },

    "DSA Master - Add Two Numbers": {
        "content": """# Add Two Numbers

Each linked list represents a number in reverse digit order.

Example:

2 -> 4 -> 3

means:

342

and:

5 -> 6 -> 4

means:

465

Sum:

807

Output:

7 -> 0 -> 8

## Algorithm

Traverse both lists simultaneously.

Add:

digit1 + digit2 + carry

Store:

sum % 10

Move carry:

sum // 10

## Python

def add_two_numbers(l1, l2):

    dummy = Node(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:

        a = l1.value if l1 else 0
        b = l2.value if l2 else 0

        total = a + b + carry

        carry = total // 10
        digit = total % 10

        current.next = Node(digit)
        current = current.next

        if l1:
            l1 = l1.next

        if l2:
            l2 = l2.next

    return dummy.next

## Complexity

Time: O(max(n,m))

Space: O(max(n,m)) for the output.
""",
        "topic": "Add Two Numbers",
        "difficulty": "Intermediate",
        "keywords": "linked list,addition,carry,math",
    },

    "DSA Master - Copy List with Random Pointer": {
        "content": """# Copy List with Random Pointer

Each node contains:

next

and an additional random pointer.

The random pointer may point to any node or None.

## Main Challenge

A simple copy of values is not enough.

We must correctly connect every random pointer to the corresponding copied node.

## Hash Map Approach

Create a mapping:

original node -> copied node

First pass:

Create all copied nodes.

Second pass:

Set:

copy.next

copy.random

using the mapping.

## Complexity

Time: O(n)

Space: O(n)

## Advanced Approach

An O(1) auxiliary-space technique inserts copied nodes between original nodes and then separates the two lists.

## Pattern

When objects have arbitrary references to other objects:

Think mapping original objects to their copies.
""",
        "topic": "Copy List with Random Pointer",
        "difficulty": "Advanced",
        "keywords": "linked list,random pointer,copy,hash map",
    },

    "DSA Master - Rotate Linked List": {
        "content": """# Rotate Linked List

Rotate a linked list to the right by k positions.

Example:

1 -> 2 -> 3 -> 4 -> 5

Rotate by 2:

4 -> 5 -> 1 -> 2 -> 3

## Main Idea

First find the length.

Then connect the tail to the head to form a cycle.

Find the new tail.

Break the cycle there.

## Steps

1. Find length n.
2. k = k % n.
3. Connect tail.next = head.
4. Move to the new tail.
5. Set new head = new_tail.next.
6. Break new_tail.next.

## Complexity

Time: O(n)

Space: O(1)

## Pattern

Rotation of a linked list

→ Make a temporary circular list, then cut it.
""",
        "topic": "Rotate Linked List",
        "difficulty": "Intermediate",
        "keywords": "linked list,rotate,circular list,k positions",
    },

    "DSA Master - Doubly Linked List": {
        "content": """# Doubly Linked List

A Doubly Linked List stores references in both directions.

Each node contains:

prev
data
next

Example:

None <- 10 <-> 20 <-> 30 -> None

## Advantage

We can move:

forward using next

backward using prev

## Node

class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

## Complexity

Access: O(n)

Search: O(n)

Insert/delete when node is known: O(1)

## Use Cases

Browser history

Undo/redo

LRU Cache

Deque implementations

## Important

Doubly linked lists use more memory because each node stores two references.
""",
        "topic": "Doubly Linked List",
        "difficulty": "Beginner",
        "keywords": "doubly linked list,prev,next,node",
    },

    "DSA Master - Circular Linked List": {
        "content": """# Circular Linked List

In a Circular Linked List, the last node points back to the first node.

Example:

1 -> 2 -> 3
^         |
|_________|

There is no None at the end.

## Types

Singly Circular

Doubly Circular

## Important

Traversal must stop using a condition based on returning to the starting node.

Do not blindly use:

while current:

because current never becomes None.

## Use Cases

Round Robin Scheduling

Circular buffers

Repeated turn systems

## Complexity

Search: O(n)

Insert at head/tail depends on implementation and whether a tail pointer is maintained.
""",
        "topic": "Circular Linked List",
        "difficulty": "Beginner",
        "keywords": "circular linked list,round robin,cycle",
    },

    "DSA Master - Merge Sort on Linked List": {
        "content": """# Merge Sort on Linked List

Merge Sort is especially useful for linked lists.

## Why?

Linked lists do not provide efficient random access.

Merge Sort only needs sequential traversal.

## Steps

1. Find the middle.
2. Split the list.
3. Recursively sort both halves.
4. Merge the sorted halves.

## Complexity

Time: O(n log n)

Extra recursion space: O(log n)

## Pattern

Linked List + Sorting

→ Merge Sort is usually a strong choice.
""",
        "topic": "Merge Sort on Linked List",
        "difficulty": "Advanced",
        "keywords": "linked list,merge sort,sorting,middle",
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

    print("EchoMind - Linked List Lessons")
    print("Updated :", updated)
    print("Inserted:", inserted)
    print("Total   :", len(LESSONS))


if __name__ == "__main__":
    main()