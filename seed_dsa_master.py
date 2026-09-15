from database import init_database, get_connection


DSA_TOPICS = {

    "Two Pointers": [
        "Introduction to Two Pointers",
        "Two Sum II",
        "Valid Palindrome",
        "3Sum",
        "Container With Most Water",
        "Valid Triangle Number",
        "Remove Duplicates from Sorted Array",
        "Merge Sorted Array",
        "Move Zeroes",
        "Sort Colors",
        "Rotate Array",
        "4Sum",
        "Trapping Rain Water",
    ],

    "Arrays & Hashing": [
        "Arrays and Hash Tables",
        "Two Sum",
        "Contains Duplicate",
        "Valid Anagram",
        "Group Anagrams",
        "Top K Frequent Elements",
        "Product of Array Except Self",
        "Longest Consecutive Sequence",
        "Encode and Decode Strings",
        "Majority Element",
        "Plus One",
        "Intersection of Two Arrays",
        "Distribute Candies",
        "Count Inversions",
    ],

    "Sliding Window": [
        "Sliding Window Introduction",
        "Maximum Sum Subarray of Size K",
        "Maximum Sum of Distinct Subarrays",
        "Max Points From Cards",
        "Variable Size Sliding Window",
        "Longest Substring Without Repeating Characters",
        "Longest Repeating Character Replacement",
        "Minimum Window Substring",
        "Permutation in String",
        "Sliding Window Maximum",
    ],

    "Stack": [
        "Stack Introduction",
        "Valid Parentheses",
        "Baseball Game",
        "Decode String",
        "Longest Valid Parentheses",
        "Monotonic Stack",
        "Daily Temperatures",
        "Largest Rectangle in Histogram",
        "Min Stack",
        "Evaluate Reverse Polish Notation",
    ],

    "Linked List": [
        "Linked List Introduction",
        "Reverse Linked List",
        "Merge Two Sorted Lists",
        "Add Two Numbers",
        "Linked List Cycle",
        "Palindrome Linked List",
        "Remove Nth Node From End",
        "Reorder List",
        "Swap Nodes in Pairs",
        "LRU Cache",
    ],

    "Heap": [
        "Heap Introduction",
        "Kth Largest Element in an Array",
        "K Closest Points to Origin",
        "K Closest Elements",
        "Merge K Sorted Lists",
        "Median from Data Stream",
        "Task Scheduler",
        "Relative Ranks",
    ],

    "Binary Search": [
        "Binary Search Introduction",
        "Binary Search",
        "Search Insert Position",
        "Peak Index in a Mountain Array",
        "Binary Search on the Answer",
        "Koko Eating Bananas",
        "Search in Rotated Sorted Array",
        "Find Minimum in Rotated Sorted Array",
        "Search a 2D Matrix",
        "Split Array Largest Sum",
        "Kth Smallest in a Sorted Matrix",
        "Minimum Shipping Capacity",
    ],

    "Depth-First Search": [
        "DFS Introduction",
        "DFS Fundamentals",
        "DFS Return Values",
        "Maximum Depth of Binary Tree",
        "Path Sum",
        "DFS Passing Values Down and Up",
        "Validate Binary Search Tree",
        "Binary Tree Tilt",
        "Diameter of a Binary Tree",
        "Path Sum II",
        "Longest Univalue Path",
        "Invert Binary Tree",
        "Same Tree",
        "Lowest Common Ancestor",
        "Binary Tree Maximum Path Sum",
        "Serialize and Deserialize Binary Tree",
    ],

    "Graphs": [
        "Graph Introduction",
        "Course Schedule",
        "Course Schedule II",
        "Shortest Path Algorithms",
        "Network Delay Time",
        "Cheapest Flights Within K Stops",
        "Path With Minimum Effort",
        "Find the City With Fewest Reachable",
        "Union-Find DSU",
        "Number of Connected Components",
        "Redundant Connection",
        "Word Ladder",
    ],

    "Greedy Algorithms": [
        "Greedy Algorithm Introduction",
        "Best Time to Buy and Sell Stock",
        "Gas Station",
        "Jump Game",
        "Jump Game II",
        "Partition Labels",
    ],

    "Dynamic Programming": [
        "Dynamic Programming Fundamentals",
        "Solving Problems with Dynamic Programming",
        "Pascal's Triangle",
        "Climbing Stairs",
        "Dice Combinations",
        "Maximum Subarray",
        "House Robber",
        "Coin Change",
        "Longest Common Subsequence",
        "Edit Distance",
        "Counting Bits",
        "Decode Ways",
        "Unique Paths",
        "Maximal Square",
        "Longest Increasing Subsequence",
        "Word Break",
        "Maximum Profit in Job Scheduling",
        "Paint House",
        "Paint House II",
        "Minimum Window Subsequence",
    ],

    "Backtracking": [
        "Backtracking Introduction",
        "Solution Space Trees",
        "Word Search",
        "Subsets",
        "Permutations",
        "Letter Combinations of a Phone Number",
        "Generate Parentheses",
        "Combination Sum",
        "Palindrome Partitioning",
        "N-Queens",
    ],

    "Breadth-First Search": [
        "BFS Introduction",
        "BFS Fundamentals",
        "Level Order Sum",
        "Rightmost Node",
        "Zigzag Level Order",
        "Maximum Width of Binary Tree",
        "BFS on Graphs",
        "Minimum Knight Moves",
        "Rotting Oranges",
        "01 Matrix",
        "Bus Routes",
    ],

    "Trie": [
        "Trie Introduction",
        "Implement Trie",
        "Prefix Matching",
    ],

    "Prefix Sum": [
        "Prefix Sum Introduction",
        "Count Vowels in Substrings",
        "Subarray Sum Equals K",
    ],

    "Matrices": [
        "Spiral Matrix",
        "Rotate Image",
        "Set Matrix Zeroes",
        "Island Perimeter",
        "Find Missing and Repeated Values",
    ],

    "Intervals": [
        "Intervals Introduction",
        "Merge Intervals",
        "Insert Interval",
        "Non-overlapping Intervals",
        "Meeting Rooms",
        "Meeting Rooms II",
    ],

    "Bit Manipulation": [
        "Bit Manipulation Introduction",
        "Single Number",
        "Number of 1 Bits",
        "Missing Number",
        "Reverse Bits",
        "Sum of Two Integers",
    ],
}


def seed_dsa_master():
    init_database()

    connection = get_connection()

    inserted = 0
    skipped = 0

    for pattern, topics in DSA_TOPICS.items():

        for topic in topics:

            title = f"DSA Master - {topic}"

            content = f"""
DSA Topic: {topic}

Pattern:
{pattern}

This topic is part of the EchoMind Data Structures & Algorithms learning library.

The detailed EchoMind lesson for this topic will contain:
- concept explanation
- problem-solving approach
- step-by-step algorithm
- example
- edge cases
- time complexity
- space complexity
- common mistakes
- interview questions
- practice problems

This entry is part of the DSA Master roadmap.
"""

            existing = connection.execute(
                """
                SELECT id
                FROM knowledge
                WHERE title = ?
                LIMIT 1
                """,
                (title,)
            ).fetchone()

            if existing:
                skipped += 1
                continue

            connection.execute(
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
                    content.strip(),
                    "Data Structures & Algorithms",
                    "CS Core",
                    topic,
                    "DSA Master Library",
                    "Medium",
                    f"DSA, {pattern}, {topic}",
                    "EchoMind"
                )
            )

            inserted += 1

    connection.commit()
    connection.close()

    total_topics = sum(
        len(topics)
        for topics in DSA_TOPICS.values()
    )

    print("=" * 60)
    print("EchoMind DSA Master Library")
    print("=" * 60)
    print("Patterns:", len(DSA_TOPICS))
    print("Topics:", total_topics)
    print("Inserted:", inserted)
    print("Skipped:", skipped)
    print("=" * 60)


if __name__ == "__main__":
    seed_dsa_master()