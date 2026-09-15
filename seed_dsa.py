import sqlite3

DATABASE_NAME = "ecomind.db"

DSA_ENTRIES = [

    # =========================================================
    # UNIT I — INTRODUCTION, ALGORITHMS, COMPLEXITY, SEARCHING
    # =========================================================

    {
        "title": "Data Structures",
        "content": "A data structure is a method of organizing and storing data so that it can be accessed and modified efficiently. Common data structures include arrays, linked lists, stacks, queues, trees, graphs, and hash tables.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Data Structures Basics",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "data structure, data, organization, storage, array, linked list, stack, queue, tree, graph",
        "author": "Senior Student"
    },

    {
        "title": "Why Data Structures Are Needed",
        "content": "Data structures are needed to organize data efficiently and to make operations such as searching, insertion, deletion, traversal, and sorting more efficient. The choice of data structure affects the time and space required by an algorithm.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Data Structures Basics",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "need data structures, efficiency, searching, insertion, deletion, traversal, sorting",
        "author": "Senior Student"
    },

    {
        "title": "Choosing the Right Data Structure",
        "content": "The appropriate data structure should be selected according to the operations required by the application. Arrays are useful for direct indexing, linked lists for flexible insertion and deletion, stacks for LIFO operations, queues for FIFO operations, trees for hierarchical data, graphs for relationships, and hash tables for fast key-based lookup.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Choice of Data Structure",
        "category": "Exam Strategy",
        "difficulty": "Medium",
        "keywords": "choose data structure, array, linked list, stack, queue, tree, graph, hash table",
        "author": "Senior Student"
    },

    {
        "title": "Algorithm",
        "content": "An algorithm is a finite sequence of well-defined steps used to solve a problem or perform a computation. A good algorithm should have clear input, output, definiteness, finiteness, and effectiveness.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Algorithms",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "algorithm, definition, input, output, definiteness, finiteness, effectiveness",
        "author": "Senior Student"
    },

    {
        "title": "Characteristics of an Algorithm",
        "content": "Important characteristics of an algorithm include input, output, definiteness, finiteness, and effectiveness. The steps should be unambiguous, the algorithm should terminate after a finite number of steps, and every operation should be practically executable.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Algorithms",
        "category": "Exam Tip",
        "difficulty": "Easy",
        "keywords": "algorithm characteristics, input, output, definiteness, finiteness, effectiveness",
        "author": "Senior Student"
    },

    {
        "title": "Algorithm Design",
        "content": "Algorithm design is the process of developing a sequence of steps to solve a problem. A typical approach is to understand the problem, identify inputs and outputs, design the solution, write pseudocode or a flowchart, analyze complexity, implement the algorithm, and test it.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Algorithm Design",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "algorithm design, problem solving, pseudocode, flowchart, implementation, testing",
        "author": "Senior Student"
    },

    {
        "title": "Pseudocode",
        "content": "Pseudocode is an informal representation of an algorithm written using structured natural-language statements. It describes the logic without depending on a specific programming language.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Algorithms",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "pseudocode, algorithm, logic, programming language",
        "author": "Senior Student"
    },

    {
        "title": "Flowchart",
        "content": "A flowchart is a graphical representation of an algorithm. Common symbols include an oval for start or end, a rectangle for processing, a parallelogram for input or output, and a diamond for decisions.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Flowcharts",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "flowchart, algorithm, process, decision, input, output",
        "author": "Senior Student"
    },

    {
        "title": "Time Complexity",
        "content": "Time complexity describes how the running time of an algorithm grows as the input size increases. It is commonly expressed using asymptotic notation such as Big O, Big Omega, and Big Theta.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Complexity Analysis",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "time complexity, running time, input size, Big O, Big Omega, Big Theta",
        "author": "Senior Student"
    },

    {
        "title": "Space Complexity",
        "content": "Space complexity describes how much memory an algorithm requires as the input size increases. It includes memory used for input data and additional memory required during execution.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Complexity Analysis",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "space complexity, memory, input, auxiliary space",
        "author": "Senior Student"
    },

    {
        "title": "Big O Notation",
        "content": "Big O notation describes an asymptotic upper bound on the growth of an algorithm's running time or space requirement. Common complexities include O(1), O(log n), O(n), O(n log n), O(n²), O(n³), O(2ⁿ), and O(n!).",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Big O",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "Big O, upper bound, complexity, O(1), O(log n), O(n), O(n log n), O(n2)",
        "author": "Senior Student"
    },

    {
        "title": "Big Omega Notation",
        "content": "Big Omega notation describes an asymptotic lower bound on the growth of an algorithm's running time or space requirement.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Big Omega",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "Big Omega, lower bound, complexity",
        "author": "Senior Student"
    },

    {
        "title": "Big Theta Notation",
        "content": "Big Theta notation describes an asymptotically tight bound. It indicates that an algorithm grows at the same asymptotic rate from both an upper-bound and lower-bound perspective.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Big Theta",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "Big Theta, tight bound, upper bound, lower bound, complexity",
        "author": "Senior Student"
    },

    {
        "title": "Common Complexity Classes",
        "content": "Common algorithmic complexity classes include constant O(1), logarithmic O(log n), linear O(n), linearithmic O(n log n), quadratic O(n²), cubic O(n³), exponential O(2ⁿ), and factorial O(n!).",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Complexity Analysis",
        "category": "Exam Tip",
        "difficulty": "Medium",
        "keywords": "complexity classes, constant, logarithmic, linear, linearithmic, quadratic, cubic, exponential, factorial",
        "author": "Senior Student"
    },

    {
        "title": "Traversal Operation",
        "content": "Traversal means visiting or processing each element of a data structure according to a defined order. Traversal is commonly used for arrays, linked lists, trees, and graphs.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Data Structure Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "traversal, operations, array, linked list, tree, graph",
        "author": "Senior Student"
    },

    {
        "title": "Insertion Operation",
        "content": "Insertion means adding a new element to a data structure. The time required for insertion depends on the structure and the location where the new element is inserted.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Data Structure Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "insertion, insert, data structure operation",
        "author": "Senior Student"
    },

    {
        "title": "Deletion Operation",
        "content": "Deletion means removing an element from a data structure. The procedure and complexity depend on the type of data structure and the location of the element.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Data Structure Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "deletion, delete, data structure operation",
        "author": "Senior Student"
    },

    {
        "title": "Updating Operation",
        "content": "Updating means changing the value or information stored in an existing element of a data structure.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Data Structure Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "update, updating, data structure operation",
        "author": "Senior Student"
    },

    {
        "title": "Searching Operation",
        "content": "Searching is the operation of locating an element with a particular value or key in a data structure. Linear search and binary search are important searching techniques.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Searching",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "searching, search, linear search, binary search",
        "author": "Senior Student"
    },

    {
        "title": "Linear Search",
        "content": "Linear search checks elements one by one from the beginning until the target is found or the data structure is exhausted. Its worst-case time complexity is O(n), and its best-case time complexity is O(1).",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Linear Search",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "linear search, sequential search, O(n), searching",
        "author": "Senior Student"
    },

    {
        "title": "Linear Search Common Mistake",
        "content": "A common mistake in linear search is stopping before checking the final element or returning an incorrect position. The algorithm should continue until the target is found or all elements have been checked.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Linear Search",
        "category": "Common Mistake",
        "difficulty": "Easy",
        "keywords": "linear search mistake, searching error, final element",
        "author": "Senior Student"
    },

    {
        "title": "Binary Search",
        "content": "Binary search repeatedly divides a sorted search range into two halves. It compares the target with the middle element and continues in the half that may contain the target. Its worst-case time complexity is O(log n).",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Binary Search",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "binary search, sorted array, middle element, divide, O(log n)",
        "author": "Senior Student"
    },

    {
        "title": "Binary Search Requirement",
        "content": "Binary search requires the data to be sorted according to the ordering used by the search. Applying binary search directly to unsorted data can produce incorrect results.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Binary Search",
        "category": "Common Mistake",
        "difficulty": "Easy",
        "keywords": "binary search, sorted data, unsorted array, common mistake",
        "author": "Senior Student"
    },

    {
        "title": "Iterative Binary Search",
        "content": "Iterative binary search uses a loop and maintains low, high, and middle positions. The search range is repeatedly reduced until the target is found or the range becomes empty.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Binary Search",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "iterative binary search, low, high, mid, loop",
        "author": "Senior Student"
    },

    {
        "title": "Recursive Binary Search",
        "content": "Recursive binary search solves the search problem by calling itself on the appropriate half of the sorted data. The recursion stops when the target is found or the search interval becomes invalid.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit I",
        "topic": "Binary Search",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "recursive binary search, recursion, sorted data, base condition",
        "author": "Senior Student"
    },

    # =========================================================
    # UNIT II — STACKS AND QUEUES
    # =========================================================

    {
        "title": "Stack",
        "content": "A stack is a linear data structure that follows the LIFO principle, meaning Last In, First Out. The main operations are push, pop, and peek or top.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Stack",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "stack, LIFO, push, pop, peek, top",
        "author": "Senior Student"
    },

    {
        "title": "Stack Push Operation",
        "content": "Push is the operation of inserting an element at the top of a stack. In an array-based stack, insertion is possible only when there is available space.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Stack Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "stack push, push operation, top",
        "author": "Senior Student"
    },

    {
        "title": "Stack Pop Operation",
        "content": "Pop is the operation of removing the element from the top of a stack. If the stack contains no element, attempting to pop causes stack underflow.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Stack Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "stack pop, pop operation, underflow",
        "author": "Senior Student"
    },

    {
        "title": "Stack Overflow and Underflow",
        "content": "Stack overflow occurs when an insertion is attempted on a full array-based stack. Stack underflow occurs when a deletion is attempted on an empty stack.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Stack Operations",
        "category": "Common Mistake",
        "difficulty": "Easy",
        "keywords": "stack overflow, stack underflow, full stack, empty stack",
        "author": "Senior Student"
    },

    {
        "title": "Stack Complexity",
        "content": "For a standard array-based stack, push, pop, and peek operations take O(1) time when performed at the top.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Stack Operations",
        "category": "Exam Tip",
        "difficulty": "Medium",
        "keywords": "stack complexity, push O(1), pop O(1), peek O(1)",
        "author": "Senior Student"
    },

    {
        "title": "Stack Applications",
        "content": "Stacks are commonly used for expression conversion and evaluation, function-call management, recursion, undo operations, and backtracking.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Stack Applications",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "stack applications, expression, recursion, backtracking, undo",
        "author": "Senior Student"
    },

    {
        "title": "Infix Expression",
        "content": "In an infix expression, the operator is written between its operands. For example, A + B places the plus operator between A and B.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Expression Conversion",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "infix, expression, operator, operand",
        "author": "Senior Student"
    },

    {
        "title": "Postfix Expression",
        "content": "In a postfix expression, the operator is written after its operands. Postfix expressions can be evaluated efficiently using a stack.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Expression Conversion",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "postfix, expression, stack, evaluation",
        "author": "Senior Student"
    },

    {
        "title": "Prefix Expression",
        "content": "In a prefix expression, the operator is written before its operands. Prefix expressions are also called Polish notation.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Expression Conversion",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "prefix, Polish notation, expression",
        "author": "Senior Student"
    },

    {
        "title": "Expression Conversion Using Stack",
        "content": "Stacks are used during conversion between infix, postfix, and prefix expressions because operators can be temporarily stored while respecting precedence and associativity rules.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Expression Conversion",
        "category": "Exam Strategy",
        "difficulty": "Medium",
        "keywords": "expression conversion, stack, infix, postfix, prefix, precedence, associativity",
        "author": "Senior Student"
    },

    {
        "title": "Queue",
        "content": "A queue is a linear data structure that follows the FIFO principle, meaning First In, First Out. Elements are generally inserted at the rear and removed from the front.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Queue",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "queue, FIFO, front, rear, insertion, deletion",
        "author": "Senior Student"
    },

    {
        "title": "Queue Enqueue Operation",
        "content": "Enqueue is the operation of inserting an element into a queue, normally at the rear.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Queue Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "enqueue, queue insertion, rear",
        "author": "Senior Student"
    },

    {
        "title": "Queue Dequeue Operation",
        "content": "Dequeue is the operation of removing an element from a queue, normally from the front.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Queue Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "dequeue, queue deletion, front",
        "author": "Senior Student"
    },

    {
        "title": "Simple Queue",
        "content": "A simple queue is a FIFO data structure in which insertion occurs at the rear and deletion occurs at the front. In a basic array implementation, freed positions at the front may not be reused efficiently.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Simple Queue",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "simple queue, FIFO, array queue, front, rear",
        "author": "Senior Student"
    },

    {
        "title": "Circular Queue",
        "content": "A circular queue treats the final array position as connected to the first position. It allows previously freed positions to be reused and avoids the space-wastage problem of a simple array queue.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Circular Queue",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "circular queue, FIFO, array, wrap around, front, rear",
        "author": "Senior Student"
    },

    {
        "title": "Priority Queue",
        "content": "A priority queue stores elements with associated priorities. Removal is based on priority rather than simply following the order of arrival.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Priority Queue",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "priority queue, priority, insertion, deletion",
        "author": "Senior Student"
    },

    {
        "title": "Stack and Queue Difference",
        "content": "A stack follows LIFO, while a queue follows FIFO. Stack insertion and deletion occur at the same end, while a standard queue inserts at the rear and deletes from the front.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit II",
        "topic": "Stack and Queue Comparison",
        "category": "Exam Tip",
        "difficulty": "Easy",
        "keywords": "stack vs queue, LIFO, FIFO, push, pop, enqueue, dequeue",
        "author": "Senior Student"
    },

    # =========================================================
    # UNIT III — LINKED LISTS
    # =========================================================

    {
        "title": "Linked List",
        "content": "A linked list is a dynamic linear data structure consisting of nodes. Each node contains data and one or more links that connect it to other nodes.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Linked List",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "linked list, node, data, pointer, dynamic",
        "author": "Senior Student"
    },

    {
        "title": "Singly Linked List",
        "content": "A singly linked list contains nodes where each node stores data and a link to the next node. The last node points to NULL.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Singly Linked List",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "singly linked list, node, next, NULL",
        "author": "Senior Student"
    },

    {
        "title": "Linked List Traversal",
        "content": "Traversal of a singly linked list starts from the head node and follows the next links until NULL is reached. Each node is visited in sequence.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Singly Linked List",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "linked list traversal, head, next, NULL",
        "author": "Senior Student"
    },

    {
        "title": "Linked List Searching",
        "content": "Searching in a singly linked list generally involves starting at the head and comparing each node's data with the target until the target is found or the end of the list is reached.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Singly Linked List",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "linked list search, sequential search, node",
        "author": "Senior Student"
    },

    {
        "title": "Linked List Insertion",
        "content": "Insertion in a linked list can be performed at the beginning, end, or a specified position by creating a node and adjusting the appropriate links.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Linked List Insertion",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "linked list insertion, beginning, end, position, links",
        "author": "Senior Student"
    },

    {
        "title": "Linked List Deletion",
        "content": "Deletion from a linked list removes a node and adjusts the links so that the remaining nodes stay connected correctly.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Linked List Deletion",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "linked list deletion, remove node, links",
        "author": "Senior Student"
    },

    {
        "title": "Linked List Common Mistake",
        "content": "A common linked-list mistake is losing the reference to the remaining nodes while changing links. Before changing a link, ensure that the required next-node reference is preserved.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Linked List",
        "category": "Common Mistake",
        "difficulty": "Medium",
        "keywords": "linked list mistake, pointer, reference, next",
        "author": "Senior Student"
    },

    {
        "title": "Linked Representation of Stack",
        "content": "A stack can be implemented using a linked list. The head node can represent the top, allowing insertion and deletion at the beginning of the list.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Linked Stack",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "linked stack, stack, linked list, top",
        "author": "Senior Student"
    },

    {
        "title": "Linked Representation of Queue",
        "content": "A queue can be implemented using a linked list with front and rear references. Enqueue can be performed at the rear and dequeue at the front.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Linked Queue",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "linked queue, queue, front, rear, linked list",
        "author": "Senior Student"
    },

    {
        "title": "Header Linked List",
        "content": "A header linked list contains a special header node at the beginning. The header can store list-related information or provide a convenient starting point for list operations.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Header Linked List",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "header linked list, header node, linked list",
        "author": "Senior Student"
    },

    {
        "title": "Doubly Linked List",
        "content": "A doubly linked list contains nodes with two links: one to the previous node and one to the next node. It supports traversal in both directions.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Doubly Linked List",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "doubly linked list, previous, next, bidirectional",
        "author": "Senior Student"
    },

    {
        "title": "Circular Linked List",
        "content": "In a circular linked list, the final node links back to the first node instead of pointing to NULL. This creates a circular structure.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Circular Linked List",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "circular linked list, last node, first node, circular",
        "author": "Senior Student"
    },

    {
        "title": "Linked List vs Array",
        "content": "Arrays generally provide direct indexed access, while linked lists require traversal to reach a particular position. Linked lists allow flexible node insertion and deletion without requiring contiguous storage.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Linked List Comparison",
        "category": "Exam Tip",
        "difficulty": "Medium",
        "keywords": "array vs linked list, indexing, insertion, deletion, contiguous memory",
        "author": "Senior Student"
    },

    # =========================================================
    # UNIT III — TREES
    # =========================================================

    {
        "title": "Tree",
        "content": "A tree is a non-linear hierarchical data structure consisting of nodes connected by edges. A tree has a root and can contain parent-child relationships.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Trees",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "tree, root, node, edge, parent, child, hierarchy",
        "author": "Senior Student"
    },

    {
        "title": "Tree Terminology",
        "content": "Important tree terms include root, parent, child, sibling, leaf, internal node, degree, depth, height, subtree, and level.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Tree Terminology",
        "category": "Exam Tip",
        "difficulty": "Easy",
        "keywords": "tree terminology, root, parent, child, leaf, degree, depth, height",
        "author": "Senior Student"
    },

    {
        "title": "Binary Tree",
        "content": "A binary tree is a tree in which each node has at most two children, commonly called the left child and right child.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Binary Tree",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "binary tree, left child, right child, tree",
        "author": "Senior Student"
    },

    {
        "title": "Binary Search Tree",
        "content": "A binary search tree is a binary tree in which values in the left subtree follow the ordering rule relative to the node and values in the right subtree follow the opposite ordering rule. This ordering supports efficient searching when the tree is suitably balanced.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Binary Search Tree",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "BST, binary search tree, left subtree, right subtree, searching",
        "author": "Senior Student"
    },

    {
        "title": "BST Searching",
        "content": "Searching in a binary search tree compares the target with the current node and moves to the left or right subtree according to the ordering property. The average performance can be efficient when the tree is balanced, while a highly skewed tree can degrade toward linear behavior.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "BST Operations",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "BST search, binary search tree, balanced, skewed",
        "author": "Senior Student"
    },

    {
        "title": "BST Insertion",
        "content": "BST insertion compares the new value with nodes starting from the root and follows the appropriate subtree until a suitable empty position is reached.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "BST Operations",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "BST insertion, binary search tree, insert node",
        "author": "Senior Student"
    },

    {
        "title": "BST Deletion",
        "content": "BST deletion depends on the node's situation: a leaf node can be removed directly, a node with one child can be replaced by its child, and a node with two children is handled using a suitable replacement such as an inorder successor or predecessor.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "BST Operations",
        "category": "Exam Strategy",
        "difficulty": "Hard",
        "keywords": "BST deletion, leaf, one child, two children, inorder successor, predecessor",
        "author": "Senior Student"
    },

    {
        "title": "AVL Tree",
        "content": "An AVL tree is a self-balancing binary search tree. It maintains a balance condition so that the height remains controlled after insertions and deletions.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "AVL Tree",
        "category": "Concept Explanation",
        "difficulty": "Hard",
        "keywords": "AVL tree, self balancing, binary search tree, height",
        "author": "Senior Student"
    },

    {
        "title": "AVL Rotations",
        "content": "AVL trees use rotations to restore balance after updates. Common rotation cases are LL, RR, LR, and RL.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "AVL Tree",
        "category": "Exam Tip",
        "difficulty": "Hard",
        "keywords": "AVL rotations, LL, RR, LR, RL, balancing",
        "author": "Senior Student"
    },

    {
        "title": "M-Way Tree",
        "content": "An M-way tree is a search tree in which a node can have multiple children, with the maximum number determined by the order of the tree.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "M-Way Trees",
        "category": "Concept Explanation",
        "difficulty": "Hard",
        "keywords": "M-way tree, multiway tree, search tree",
        "author": "Senior Student"
    },

    {
        "title": "B Tree",
        "content": "A B-tree is a balanced multiway search tree designed to keep its height small and support efficient search, insertion, and deletion. It is commonly associated with secondary-storage systems.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "B Tree",
        "category": "Concept Explanation",
        "difficulty": "Hard",
        "keywords": "B tree, balanced tree, multiway, search, insertion, deletion",
        "author": "Senior Student"
    },

    {
        "title": "B Plus Tree",
        "content": "A B+ tree is a balanced multiway tree in which records are stored at leaf level and leaf nodes are typically linked for efficient sequential and range access.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "B Plus Tree",
        "category": "Concept Explanation",
        "difficulty": "Hard",
        "keywords": "B+ tree, leaf nodes, range search, balanced tree, database",
        "author": "Senior Student"
    },

    {
        "title": "Tree Applications",
        "content": "Trees are used for hierarchical data representation, searching, indexing, expression representation, file-system organization, and other applications where parent-child relationships are useful.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit III",
        "topic": "Tree Applications",
        "category": "Exam Tip",
        "difficulty": "Medium",
        "keywords": "tree applications, hierarchy, indexing, file system, expression",
        "author": "Senior Student"
    },

    # =========================================================
    # UNIT IV — SORTING
    # =========================================================

    {
        "title": "Sorting",
        "content": "Sorting is the process of arranging data according to a specified order, such as ascending or descending order. Sorting can make searching and data processing easier.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Sorting Basics",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "sorting, ascending, descending, data arrangement",
        "author": "Senior Student"
    },

    {
        "title": "Selection Sort",
        "content": "Selection sort repeatedly selects the smallest or largest remaining element and places it in its correct position. Its typical time complexity is O(n²).",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Selection Sort",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "selection sort, minimum, O(n2), sorting",
        "author": "Senior Student"
    },

    {
        "title": "Bubble Sort",
        "content": "Bubble sort repeatedly compares adjacent elements and swaps them when they are in the wrong order. In its common optimized form, the best case can be O(n) when the data is already sorted, while the typical worst-case time complexity is O(n²).",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Bubble Sort",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "bubble sort, adjacent, swap, O(n2), sorting",
        "author": "Senior Student"
    },

    {
        "title": "Bubble Sort Common Mistake",
        "content": "A common bubble-sort mistake is using an incorrect loop boundary or forgetting to swap adjacent elements only when they are out of order. The largest unsorted element should move toward the end after each pass.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Bubble Sort",
        "category": "Common Mistake",
        "difficulty": "Easy",
        "keywords": "bubble sort mistake, loop, adjacent swap, passes",
        "author": "Senior Student"
    },

    {
        "title": "Insertion Sort",
        "content": "Insertion sort builds the sorted portion one element at a time by inserting each new element into its appropriate position. Its worst-case time complexity is O(n²), while its best case can be O(n) for already sorted data.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Insertion Sort",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "insertion sort, sorted portion, O(n2), sorting",
        "author": "Senior Student"
    },

    {
        "title": "Quick Sort",
        "content": "Quick sort is a divide-and-conquer sorting algorithm. It chooses a pivot, partitions the data around the pivot, and recursively sorts the resulting partitions. Its average time complexity is O(n log n), while its worst case can be O(n²).",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Quick Sort",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "quick sort, pivot, partition, divide and conquer, O(n log n)",
        "author": "Senior Student"
    },

    {
        "title": "Merge Sort",
        "content": "Merge sort is a divide-and-conquer sorting algorithm that divides the data into smaller parts, recursively sorts them, and merges the sorted parts. Its time complexity is O(n log n).",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Merge Sort",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "merge sort, divide and conquer, merge, O(n log n)",
        "author": "Senior Student"
    },

    {
        "title": "Heap Sort",
        "content": "Heap sort uses a heap data structure to repeatedly select the next element for the sorted sequence. Its time complexity is O(n log n).",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Heap Sort",
        "category": "Concept Explanation",
        "difficulty": "Hard",
        "keywords": "heap sort, heap, O(n log n), sorting",
        "author": "Senior Student"
    },

    {
        "title": "Sorting Algorithm Comparison",
        "content": "Selection sort, bubble sort, and insertion sort generally have quadratic worst-case time complexity. Merge sort and heap sort have O(n log n) time complexity. Quick sort has average O(n log n) performance but can have O(n²) worst-case performance.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Sorting Comparison",
        "category": "Exam Tip",
        "difficulty": "Medium",
        "keywords": "sorting comparison, selection, bubble, insertion, quick, merge, heap, complexity",
        "author": "Senior Student"
    },

    # =========================================================
    # UNIT IV — HASHING
    # =========================================================

    {
        "title": "Hashing",
        "content": "Hashing is a technique for mapping a key to a location in a hash table using a hash function. It is used to support efficient key-based insertion, searching, and deletion.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Hashing",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "hashing, hash table, hash function, key, searching",
        "author": "Senior Student"
    },

    {
        "title": "Hash Function",
        "content": "A hash function transforms a key into a hash value or table index. A good hash function should distribute keys effectively across the available table positions.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Hashing",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "hash function, hash value, table index, key",
        "author": "Senior Student"
    },

    {
        "title": "Hash Collision",
        "content": "A collision occurs when two or more different keys produce the same hash-table location. Collision-resolution techniques are used to store and retrieve the affected keys.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Hashing",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "hash collision, collision, hash table, keys",
        "author": "Senior Student"
    },

    {
        "title": "Hashing Common Mistake",
        "content": "A common hashing mistake is assuming that a hash function always gives a unique location. Different keys can map to the same location, so collision handling is important.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Hashing",
        "category": "Common Mistake",
        "difficulty": "Easy",
        "keywords": "hashing mistake, collision, duplicate index, hash table",
        "author": "Senior Student"
    },

    # =========================================================
    # UNIT IV — GRAPHS
    # =========================================================

    {
        "title": "Graph",
        "content": "A graph is a non-linear data structure consisting of vertices and edges. Edges represent relationships or connections between vertices.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Graphs",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "graph, vertex, edge, vertices, relationships",
        "author": "Senior Student"
    },

    {
        "title": "Graph Terminology",
        "content": "Important graph terms include vertex, edge, degree, path, cycle, connected graph, directed graph, undirected graph, weighted graph, and adjacent vertices.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Graph Terminology",
        "category": "Exam Tip",
        "difficulty": "Easy",
        "keywords": "graph terminology, vertex, edge, degree, path, cycle, directed, undirected",
        "author": "Senior Student"
    },

    {
        "title": "Adjacency Matrix",
        "content": "An adjacency matrix represents a graph using a two-dimensional matrix. The entry at a pair of vertex positions indicates whether an edge exists and can also represent an edge weight in a weighted graph.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Graph Representation",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "adjacency matrix, graph representation, matrix, edge",
        "author": "Senior Student"
    },

    {
        "title": "Adjacency List",
        "content": "An adjacency list represents each vertex together with a list of vertices connected to it. It can be more space-efficient than an adjacency matrix for sparse graphs.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Graph Representation",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "adjacency list, graph representation, sparse graph, vertex",
        "author": "Senior Student"
    },

    {
        "title": "Graph Traversal",
        "content": "Graph traversal means systematically visiting vertices of a graph. Breadth-first search and depth-first search are fundamental graph traversal techniques.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Graph Traversal",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "graph traversal, BFS, DFS, vertices",
        "author": "Senior Student"
    },

    {
        "title": "Breadth First Search",
        "content": "Breadth-first search explores a graph level by level, generally using a queue. It visits neighboring vertices before moving to the next level.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "BFS",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "BFS, breadth first search, queue, graph traversal",
        "author": "Senior Student"
    },

    {
        "title": "Depth First Search",
        "content": "Depth-first search explores as far as possible along one path before backtracking. It can be implemented using recursion or an explicit stack.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "DFS",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "DFS, depth first search, stack, recursion, graph traversal",
        "author": "Senior Student"
    },

    {
        "title": "Graph Traversal Complexity",
        "content": "With an appropriate adjacency-list representation, BFS and DFS can traverse a graph in O(V + E) time, where V is the number of vertices and E is the number of edges.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Graph Traversal",
        "category": "Exam Tip",
        "difficulty": "Hard",
        "keywords": "BFS complexity, DFS complexity, O(V+E), vertices, edges",
        "author": "Senior Student"
    },

    # =========================================================
    # UNIT IV — MINIMUM SPANNING TREE
    # =========================================================

    {
        "title": "Minimum Spanning Tree",
        "content": "A minimum spanning tree is a spanning tree of a connected weighted undirected graph whose total edge weight is minimum among all spanning trees.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Minimum Spanning Tree",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "MST, minimum spanning tree, weighted graph, spanning tree",
        "author": "Senior Student"
    },

    {
        "title": "Kruskal Algorithm",
        "content": "Kruskal's algorithm constructs a minimum spanning tree by considering edges in increasing order of weight and adding an edge when it does not create a cycle in the selected edges.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Kruskal Algorithm",
        "category": "Concept Explanation",
        "difficulty": "Hard",
        "keywords": "Kruskal, MST, minimum spanning tree, edge sorting, cycle",
        "author": "Senior Student"
    },

    {
        "title": "Prim Algorithm",
        "content": "Prim's algorithm constructs a minimum spanning tree by starting from a vertex and repeatedly adding the minimum-weight edge that connects the growing tree to a vertex outside it.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "Prim Algorithm",
        "category": "Concept Explanation",
        "difficulty": "Hard",
        "keywords": "Prim, MST, minimum spanning tree, vertex, minimum edge",
        "author": "Senior Student"
    },

    {
        "title": "Kruskal vs Prim",
        "content": "Kruskal's algorithm selects edges globally in increasing weight order while avoiding cycles. Prim's algorithm grows one tree from a starting vertex by repeatedly selecting the cheapest connecting edge.",
        "subject": "Data Structures and Algorithms",
        "unit": "Unit IV",
        "topic": "MST Comparison",
        "category": "Exam Tip",
        "difficulty": "Medium",
        "keywords": "Kruskal vs Prim, MST, edge, vertex, comparison",
        "author": "Senior Student"
    },

    {
        "title": "DSA Exam Strategy",
        "content": "For DSA theory questions, first write the definition, then explain the working or algorithm, followed by important operations and time complexity where applicable. For algorithms, use clear steps or pseudocode and mention complexity.",
        "subject": "Data Structures and Algorithms",
        "unit": "All Units",
        "topic": "DSA Exam Strategy",
        "category": "Exam Strategy",
        "difficulty": "Easy",
        "keywords": "DSA exam strategy, definition, algorithm, pseudocode, complexity",
        "author": "Senior Student"
    }
]


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def seed_database():
    connection = get_connection()

    added = 0
    skipped = 0

    for entry in DSA_ENTRIES:

        existing = connection.execute(
            """
            SELECT id
            FROM knowledge
            WHERE title = ?
              AND subject = ?
            """,
            (entry["title"], entry["subject"])
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
                entry["title"],
                entry["content"],
                entry["subject"],
                entry["unit"],
                entry["topic"],
                entry["category"],
                entry["difficulty"],
                entry["keywords"],
                entry["author"]
            )
        )

        added += 1

    connection.commit()
    connection.close()

    print(f"Added {added} Data Structures and Algorithms knowledge entries.")
    print(f"Skipped {skipped} existing Data Structures and Algorithms entries.")


if __name__ == "__main__":
    seed_database()