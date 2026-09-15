import sqlite3

DATABASE_NAME = "ecomind.db"

python_knowledge = [

    # ============================================================
    # UNIT I — PYTHON BASICS, CONTROL FLOW, STRINGS AND FILES
    # ============================================================

    {
        "title": "Installing Python",
        "content": "Python is installed from the official Python distribution or another approved Python distribution. During installation on Windows, adding Python to PATH allows Python commands to be used from the terminal. Installation should be verified by running python --version.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Installing Python",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "Python installation, Python, PATH, version",
        "author": "EchoMind"
    },
    {
        "title": "Python Installation Exam Tip",
        "content": "After installing Python, verify that Python is available from the terminal. A common mistake is installing Python without configuring PATH and then assuming Python itself is not installed.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Installing Python",
        "category": "Exam Tip",
        "difficulty": "Easy",
        "keywords": "installation, PATH, terminal, Python",
        "author": "EchoMind"
    },

    {
        "title": "Python Basic Syntax",
        "content": "Python syntax defines how Python programs are written. Python uses indentation to represent blocks of code. Statements are generally written one per line, and Python uses keywords, identifiers, operators and expressions to construct programs.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Basic Syntax",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "syntax, statements, indentation, keywords",
        "author": "EchoMind"
    },
    {
        "title": "Python Indentation",
        "content": "Indentation is significant in Python because it defines the beginning and end of blocks such as if statements, loops and functions. Statements belonging to the same block must normally have consistent indentation.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Python Indentation",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "indentation, blocks, Python syntax",
        "author": "EchoMind"
    },
    {
        "title": "Python Indentation Common Mistake",
        "content": "A common Python mistake is inconsistent indentation. Statements that belong to the same block must use consistent indentation. Incorrect indentation can produce an IndentationError or change the intended program structure.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Python Indentation",
        "category": "Common Mistake",
        "difficulty": "Easy",
        "keywords": "indentation, IndentationError, common mistake",
        "author": "EchoMind"
    },

    {
        "title": "Python Interactive Shell",
        "content": "The Python interactive shell allows Python statements and expressions to be executed immediately. It is useful for experimenting with syntax, testing small expressions and learning Python behavior without creating a complete script.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Interactive Shell",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "interactive shell, interpreter, Python",
        "author": "EchoMind"
    },

    {
        "title": "Python Scripts",
        "content": "A Python script is a file containing Python statements that can be saved and executed later. Python source files normally use the .py extension. Scripts are useful for developing complete programs instead of entering statements one at a time.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Python Scripts",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "script, .py, Python file, execution",
        "author": "EchoMind"
    },
    {
        "title": "Editing Saving and Running Python Scripts",
        "content": "A Python program can be written in an editor, saved as a .py file and executed using the Python interpreter. The basic workflow is edit the source code, save the file, run the program and inspect the output or errors.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Python Scripts",
        "category": "Exam Tip",
        "difficulty": "Easy",
        "keywords": "edit, save, run, script",
        "author": "EchoMind"
    },

    {
        "title": "Python Data Types",
        "content": "A data type describes the kind of value represented by an object. Python provides built-in types for different kinds of data, including numerical values, Boolean values, strings and collection objects.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Data Types",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "data types, objects, Python",
        "author": "EchoMind"
    },
    {
        "title": "Python Numerical Types",
        "content": "Python supports numerical types including integers and floating-point values. Python also provides complex numbers. Numerical values can be used in arithmetic expressions and calculations.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Numerical Types",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "int, float, complex, numerical types",
        "author": "EchoMind"
    },
    {
        "title": "Python Boolean Values",
        "content": "Boolean values represent logical truth values. Python uses True and False as Boolean values. They are commonly used with selection statements and logical expressions.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Data Types",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "Boolean, True, False, logical",
        "author": "EchoMind"
    },

    {
        "title": "Python Variables",
        "content": "A variable name refers to an object stored by a Python program. Python variables do not require a separate type declaration before assignment. The type of the value associated with a variable determines the object's data type.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Variables and Assignment",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "variables, assignment, objects",
        "author": "EchoMind"
    },
    {
        "title": "Python Assignment",
        "content": "Assignment associates a variable name with a value or object. For example, x = 10 associates the name x with the integer value 10. Assignment can also be performed using expressions.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Variables and Assignment",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "assignment, variable, expression",
        "author": "EchoMind"
    },

    {
        "title": "Python Arithmetic Operators",
        "content": "Arithmetic operators perform numerical calculations. Common arithmetic operations include addition, subtraction, multiplication, division, floor division, remainder and exponentiation.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Arithmetic Operators",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "arithmetic, operators, addition, subtraction, multiplication, division",
        "author": "EchoMind"
    },
    {
        "title": "Python Expressions",
        "content": "An expression is a combination of values, variables, operators and function calls that produces a value. Python evaluates expressions according to operator rules and precedence.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Expressions",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "expressions, operators, precedence",
        "author": "EchoMind"
    },

    {
        "title": "Python Selection Statements",
        "content": "Selection statements allow a program to choose between different execution paths based on conditions. Python provides if, elif and else constructs for conditional execution.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Selection Statements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "if, elif, else, selection",
        "author": "EchoMind"
    },
    {
        "title": "Python If Statement",
        "content": "The if statement executes its indented block when its condition evaluates to true. The condition controls whether the block should execute.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Selection Statements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "if statement, condition",
        "author": "EchoMind"
    },
    {
        "title": "Python If Else",
        "content": "The if-else structure provides two possible execution paths. The if block executes when its condition is true; otherwise the else block executes.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Selection Statements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "if else, condition, selection",
        "author": "EchoMind"
    },
    {
        "title": "Python Elif",
        "content": "The elif construct allows additional conditions to be checked after an if condition. Multiple elif branches can be used before an optional else branch.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Selection Statements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "elif, conditions, selection",
        "author": "EchoMind"
    },

    {
        "title": "Python Loops",
        "content": "Loops repeatedly execute a block of statements. Python provides for loops and while loops. Loops are useful when an operation must be performed repeatedly.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Loops",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "loops, for, while, iteration",
        "author": "EchoMind"
    },
    {
        "title": "Python For Loop",
        "content": "A for loop iterates over items supplied by an iterable. During each iteration, the loop variable refers to the current item and the loop body is executed.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "For Loop",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "for loop, iteration, iterable",
        "author": "EchoMind"
    },
    {
        "title": "Python While Loop",
        "content": "A while loop repeatedly executes its body while its condition remains true. The condition should eventually become false when the loop is intended to terminate normally.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "While Loop",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "while loop, condition, iteration",
        "author": "EchoMind"
    },

    {
        "title": "Python Strings",
        "content": "A string represents a sequence of characters. Strings can be created using quotes and support operations such as indexing, slicing and other string manipulation operations.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "String Manipulation",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "strings, characters, string manipulation",
        "author": "EchoMind"
    },
    {
        "title": "Python String Indexing",
        "content": "String indexing accesses an individual character using its position. Python sequence indexing starts from zero, so the first character is at index 0.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "String Indexing",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "string indexing, index, character",
        "author": "EchoMind"
    },
    {
        "title": "Python Subscript Operator",
        "content": "The subscript operator uses square brackets to access an element of a sequence such as a string or list. The index identifies the position of the requested element.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Subscript Operator",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "subscript operator, square brackets, indexing",
        "author": "EchoMind"
    },
    {
        "title": "Python String Slicing",
        "content": "Slicing extracts a portion of a sequence using start, stop and optional step positions. The stop position is normally excluded from the resulting slice.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "String Slicing",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "slicing, start, stop, step, strings",
        "author": "EchoMind"
    },

    {
        "title": "Python Text Files",
        "content": "Python can work with text files by opening a file, reading or writing data and then closing the file. File operations allow programs to store and retrieve information from persistent files.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Text Files",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "text files, file handling, read, write",
        "author": "EchoMind"
    },
    {
        "title": "Reading Text Files in Python",
        "content": "A text file can be opened for reading and its contents can be read using appropriate file operations. Reading can retrieve the entire content or process file data incrementally.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Reading Text Files",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "read file, text file, file handling",
        "author": "EchoMind"
    },
    {
        "title": "Writing Text Files in Python",
        "content": "Python can open a text file in a writing mode and write character data to it. Writing should use the appropriate file mode so that existing content is handled as intended.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Writing Text Files",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "write file, text file, file handling",
        "author": "EchoMind"
    },
    {
        "title": "Reading and Writing Numbers in Files",
        "content": "Numbers can be stored in text files by converting numerical values into text when writing. When reading them back, the text can be converted into the required numerical type before calculations.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Text Files",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "numbers, text files, conversion, read, write",
        "author": "EchoMind"
    },
    {
        "title": "Formatted Files in Python",
        "content": "Formatted file data stores information in a structured textual representation so that it can be written and read consistently. Formatting is important when multiple values must be represented clearly in a file.",
        "subject": "Python Programming",
        "unit": "Unit I",
        "topic": "Formatted Files",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "formatted files, text, data formatting",
        "author": "EchoMind"
    },


    # ============================================================
    # UNIT II — LISTS, DICTIONARIES, FUNCTIONS AND RECURSION
    # ============================================================

    {
        "title": "Python Lists",
        "content": "A list is a mutable sequence used to store multiple values. List elements are ordered and can be accessed using indexes. Lists support replacing, inserting and removing elements.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Lists",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "lists, mutable, sequence, indexing",
        "author": "EchoMind"
    },
    {
        "title": "Python List Replacement",
        "content": "An element in a list can be replaced by assigning a new value to its indexed position. Because lists are mutable, changing an existing element modifies the list.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "List Replacement",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "list, replacement, assignment, mutable",
        "author": "EchoMind"
    },
    {
        "title": "Python List Insertion",
        "content": "List insertion adds an element to a list. Python provides list operations such as append and insert for adding elements at appropriate positions.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "List Insertion",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "list insertion, append, insert",
        "author": "EchoMind"
    },
    {
        "title": "Python List Removal",
        "content": "Elements can be removed from a list using list removal operations. The selected removal operation determines whether an element is removed by value or by position.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "List Removal",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "list removal, remove, pop, delete",
        "author": "EchoMind"
    },
    {
        "title": "Python List Index Common Mistake",
        "content": "Python list indexing starts from zero. Attempting to access a position outside the valid index range can produce an IndexError.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Lists",
        "category": "Common Mistake",
        "difficulty": "Easy",
        "keywords": "list, indexing, IndexError, common mistake",
        "author": "EchoMind"
    },

    {
        "title": "Searching a Python List",
        "content": "Searching a list means checking whether a required value occurs in the list and, when necessary, determining its position. A sequential scan can examine list elements one by one.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Searching Lists",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "list searching, search, sequential",
        "author": "EchoMind"
    },
    {
        "title": "Sorting a Python List",
        "content": "Sorting arranges list elements according to an ordering. Python provides list sorting operations that can arrange values into ascending or another specified ordering.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Sorting Lists",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "list sorting, sort, ordering",
        "author": "EchoMind"
    },

    {
        "title": "Python Dictionaries",
        "content": "A dictionary stores data as key-value associations. Keys are used to access corresponding values. Dictionaries can be modified by adding, replacing and removing key-value entries.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Dictionaries",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "dictionary, keys, values, mapping",
        "author": "EchoMind"
    },
    {
        "title": "Python Dictionary Literals",
        "content": "A dictionary literal creates a dictionary by specifying key-value pairs. The pairs are written using dictionary syntax with keys associated with their values.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Dictionary Literals",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "dictionary literal, key, value",
        "author": "EchoMind"
    },
    {
        "title": "Adding Keys to Python Dictionary",
        "content": "A new key-value association can be added to a dictionary by assigning a value to a key that is not already present.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Dictionary Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "dictionary, add key, key value",
        "author": "EchoMind"
    },
    {
        "title": "Removing Keys from Python Dictionary",
        "content": "A key-value association can be removed from a dictionary using an appropriate dictionary removal operation. After removal, that key is no longer associated with the dictionary.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Dictionary Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "dictionary, remove key, delete",
        "author": "EchoMind"
    },
    {
        "title": "Accessing Dictionary Values",
        "content": "Dictionary values are accessed using their corresponding keys. A key must be available in the dictionary when direct key-based access is used.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Dictionary Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "dictionary, access, values, keys",
        "author": "EchoMind"
    },
    {
        "title": "Replacing Dictionary Values",
        "content": "A dictionary value can be replaced by assigning a new value to an existing key. The key remains associated with the dictionary while its value changes.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Dictionary Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "dictionary, replace, update, value",
        "author": "EchoMind"
    },
    {
        "title": "Traversing a Python Dictionary",
        "content": "Dictionary traversal means visiting dictionary keys, values or key-value pairs so that the stored information can be processed.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Dictionary Traversal",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "dictionary traversal, keys, values, iteration",
        "author": "EchoMind"
    },

    {
        "title": "Functions in Python",
        "content": "A function is a reusable block of code designed to perform a particular task. Functions help divide a program into smaller logical components and reduce repeated code.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Functions",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "functions, reusable, program structure",
        "author": "EchoMind"
    },
    {
        "title": "Defining Python Functions",
        "content": "A Python function is defined using the def keyword followed by a function name, parameters when required and an indented function body.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Functions",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "def, function definition, parameters",
        "author": "EchoMind"
    },
    {
        "title": "Python Function Arguments",
        "content": "Arguments are values supplied when a function is called. They provide input data to the parameters defined by the function.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Function Arguments",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "arguments, parameters, functions",
        "author": "EchoMind"
    },
    {
        "title": "Python Function Parameters",
        "content": "Parameters are names defined in a function declaration that receive values when the function is called. They allow a function to operate on supplied input.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Function Parameters",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "parameters, arguments, functions",
        "author": "EchoMind"
    },
    {
        "title": "Python Return Values",
        "content": "The return statement sends a value from a function back to the code that called the function. Returning a value allows the result of a function to be stored or used in another expression.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Return Values",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "return, function, return value",
        "author": "EchoMind"
    },
    {
        "title": "Python Function Common Mistake",
        "content": "A common mistake is forgetting to return a required result from a function. If the caller needs the function's computed result, the function should explicitly return that result.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Functions",
        "category": "Common Mistake",
        "difficulty": "Easy",
        "keywords": "function, return, common mistake",
        "author": "EchoMind"
    },

    {
        "title": "Program Structure in Python",
        "content": "Program structure refers to organizing a program into logical components so that its behavior is easier to understand, test and maintain. Functions can be used to separate related tasks.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Program Structure",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "program structure, functions, design",
        "author": "EchoMind"
    },
    {
        "title": "Design with Functions",
        "content": "Designing with functions means dividing a larger problem into smaller tasks and implementing those tasks as reusable functions. This reduces redundancy and makes program organization clearer.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Program Design",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "program design, functions, modularity",
        "author": "EchoMind"
    },
    {
        "title": "Hiding Redundancy and Complexity",
        "content": "Functions and suitable data structures can hide implementation details from the rest of a program. This allows other parts of the program to use an operation without depending on every implementation detail.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Program Design",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "redundancy, complexity, abstraction, functions",
        "author": "EchoMind"
    },

    {
        "title": "Python Recursion",
        "content": "Recursion occurs when a function calls itself to solve a problem through smaller versions of the same problem. A recursive design requires a condition that stops further recursive calls.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Recursive Functions",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "recursion, recursive function, base condition",
        "author": "EchoMind"
    },
    {
        "title": "Recursive Function Base Case",
        "content": "A base case is the stopping condition of a recursive function. Without an appropriate base case, recursive calls may continue indefinitely until Python encounters a recursion-related error.",
        "subject": "Python Programming",
        "unit": "Unit II",
        "topic": "Recursive Functions",
        "category": "Common Mistake",
        "difficulty": "Medium",
        "keywords": "recursion, base case, stopping condition",
        "author": "EchoMind"
    },


    # ============================================================
    # UNIT III — TURTLE, IMAGE PROCESSING AND GUI
    # ============================================================

    {
        "title": "Python Turtle Graphics",
        "content": "The turtle module provides a simple graphics environment in which a turtle cursor can move around a screen and draw shapes. It is useful for learning programming through visual output.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Turtle Graphics",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "turtle, graphics, drawing",
        "author": "EchoMind"
    },
    {
        "title": "Turtle Basic Operations",
        "content": "Turtle graphics supports operations for moving the turtle, changing its direction and controlling whether movement produces visible drawing. These operations can be combined to construct graphical patterns.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Turtle Operations",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "turtle operations, movement, direction",
        "author": "EchoMind"
    },
    {
        "title": "Manipulating Turtle Screen",
        "content": "The turtle screen provides the drawing environment. Screen properties and behavior can be controlled to create a suitable graphics window for a turtle program.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Turtle Screen",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "turtle screen, graphics window",
        "author": "EchoMind"
    },
    {
        "title": "Drawing 2D Shapes with Turtle",
        "content": "Two-dimensional shapes can be drawn using repeated turtle movement and turning operations. Different combinations of movement distance and turning angle can create shapes such as squares, triangles and polygons.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "2D Shapes",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "turtle, 2D shapes, polygon, drawing",
        "author": "EchoMind"
    },
    {
        "title": "Turtle Object Attributes",
        "content": "Objects used in turtle graphics have attributes and state information describing properties such as position, direction and drawing settings. Examining object attributes helps understand the current state of a graphics object.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Object Attributes",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "turtle, attributes, object state",
        "author": "EchoMind"
    },
    {
        "title": "Random Walk with Python Turtle",
        "content": "A random walk repeatedly chooses movement directions or steps using random choices. Turtle graphics can visualize the resulting path on the screen.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Random Walk",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "random walk, turtle, random",
        "author": "EchoMind"
    },
    {
        "title": "RGB Color Scheme",
        "content": "The RGB color scheme represents colors using three components: red, green and blue. Different component values can be combined to produce different colors in graphics and image processing.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "RGB Color Scheme",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "RGB, red, green, blue, colors",
        "author": "EchoMind"
    },

    {
        "title": "Python Image Processing",
        "content": "Image processing involves loading images and applying operations that modify or analyze their visual information. Python image-processing tools can be used for tasks such as copying, blurring and reducing images.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Image Processing",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "image processing, Python, images",
        "author": "EchoMind"
    },
    {
        "title": "Image Properties in Python",
        "content": "Image properties describe characteristics of an image such as its dimensions and other information associated with its representation. Examining properties helps a program understand the image before processing it.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Image Properties",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "image properties, dimensions, image processing",
        "author": "EchoMind"
    },
    {
        "title": "Python Image Module",
        "content": "An image module provides functionality for working with image objects and image-processing operations. The module can be used to load images and perform supported transformations.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Image Module",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "image module, image processing",
        "author": "EchoMind"
    },
    {
        "title": "Copying Images in Python",
        "content": "Copying an image creates another image representation that can be manipulated separately from the original according to the capabilities of the image-processing module.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Image Manipulation",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "image copy, image manipulation",
        "author": "EchoMind"
    },
    {
        "title": "Blurring Images in Python",
        "content": "Blurring is an image-processing operation that reduces fine detail and produces a smoother appearance. It can be applied using image-processing functionality that supports blur operations.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Image Manipulation",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "image blur, image processing",
        "author": "EchoMind"
    },
    {
        "title": "Reducing Images in Python",
        "content": "Reducing an image changes its size so that it occupies fewer pixels or less visual space. Image-processing tools can provide operations for creating a smaller representation.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "Image Manipulation",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "reduce image, resize, image processing",
        "author": "EchoMind"
    },

    {
        "title": "Terminal Programs and GUI Programs",
        "content": "A terminal-based program interacts with users through text input and output in a command-line environment. A GUI-based program interacts through graphical components such as windows, buttons and input fields.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "GUI Programming",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "terminal, GUI, graphical user interface",
        "author": "EchoMind"
    },
    {
        "title": "GUI Windows and Components",
        "content": "A GUI application uses a window containing interface components. Components provide controls or display information and allow users to interact with the application.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "GUI Components",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "GUI, windows, components",
        "author": "EchoMind"
    },
    {
        "title": "GUI Entry Fields",
        "content": "Entry fields allow users to provide textual input in a GUI application. A program can read the value entered by the user and use it as input for processing.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "GUI Input Output",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "GUI, entry field, input, output",
        "author": "EchoMind"
    },
    {
        "title": "GUI Input and Output",
        "content": "GUI input and output are performed through graphical components. Input components collect information from the user while output components display information or results.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "GUI Input Output",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "GUI input, GUI output, components",
        "author": "EchoMind"
    },
    {
        "title": "GUI Instance Variables",
        "content": "Instance variables can store data associated with an individual GUI object. They allow an object to maintain state that can be accessed by its methods.",
        "subject": "Python Programming",
        "unit": "Unit III",
        "topic": "GUI Programming",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "GUI, instance variables, object state",
        "author": "EchoMind"
    },


    # ============================================================
    # UNIT IV — OOP, EXCEPTIONS, THREADING AND NETWORKING
    # ============================================================

    {
        "title": "Python Object Oriented Programming",
        "content": "Object-oriented programming organizes software around objects that combine data and behavior. Python supports classes, objects, attributes, methods, inheritance and polymorphism.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Object Oriented Programming",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "OOP, object oriented programming, classes, objects",
        "author": "EchoMind"
    },
    {
        "title": "Python Classes",
        "content": "A class defines the structure and behavior that objects created from the class can have. It can contain attributes and methods that describe the state and behavior of its objects.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Classes",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "class, OOP, attributes, methods",
        "author": "EchoMind"
    },
    {
        "title": "Python Objects",
        "content": "An object is an instance of a class. Objects contain state represented through attributes and behavior represented through methods defined by their class.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Objects",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "objects, class, instance",
        "author": "EchoMind"
    },
    {
        "title": "Python Attributes",
        "content": "Attributes store data associated with an object or class. They represent aspects of an object's state and can be accessed or modified according to the program design.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Attributes",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "attributes, object state, OOP",
        "author": "EchoMind"
    },
    {
        "title": "Python Methods",
        "content": "Methods are functions defined inside a class that describe behavior associated with objects of that class. They can operate on the object's state.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Methods",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "methods, class, functions, OOP",
        "author": "EchoMind"
    },
    {
        "title": "Defining Python Classes",
        "content": "A Python class is defined using the class keyword followed by a class name and an indented class body. The class body can contain attributes and methods.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Defining Classes",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "class keyword, class definition, Python",
        "author": "EchoMind"
    },

    {
        "title": "Design with Python Classes",
        "content": "Designing with classes means identifying entities in a problem and representing their relevant data and behavior as objects. Good class design separates responsibilities into appropriate objects.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Design with Classes",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "class design, objects, OOP",
        "author": "EchoMind"
    },
    {
        "title": "Data Modelling with Python Classes",
        "content": "Data modelling with classes represents real or conceptual entities using objects. Attributes represent properties of an entity and methods represent operations or behavior associated with it.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Data Modelling",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "data modelling, classes, objects, attributes",
        "author": "EchoMind"
    },

    {
        "title": "Python Inheritance",
        "content": "Inheritance allows a class to derive characteristics and behavior from another class. A derived class can reuse or extend functionality provided by its base class.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Inheritance",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "inheritance, base class, derived class, OOP",
        "author": "EchoMind"
    },
    {
        "title": "Python Polymorphism",
        "content": "Polymorphism allows a common operation or interface to work with objects of different types according to the behavior provided by those objects.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Polymorphism",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "polymorphism, OOP, objects",
        "author": "EchoMind"
    },
    {
        "title": "Python Operator Overloading",
        "content": "Operator overloading allows a class to define how supported operators behave for its objects. Special methods can provide class-specific behavior for operators.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Operator Overloading",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "operator overloading, special methods, OOP",
        "author": "EchoMind"
    },
    {
        "title": "Python Abstract Classes",
        "content": "An abstract class provides a design for related classes and can specify behavior that derived classes are expected to implement. Abstract classes are useful when a common conceptual interface is required.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Abstract Classes",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "abstract class, abstraction, OOP",
        "author": "EchoMind"
    },

    {
        "title": "Python Exception Handling",
        "content": "Exception handling allows a program to respond to runtime errors and exceptional situations without necessarily terminating unexpectedly. Python provides constructs such as try and except for handling exceptions.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Exception Handling",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "exceptions, exception handling, try, except",
        "author": "EchoMind"
    },
    {
        "title": "Python Try Block",
        "content": "The try block contains statements that may raise an exception. Exception-handling code can respond to an exception raised while the protected statements execute.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Try Block",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "try block, exception, Python",
        "author": "EchoMind"
    },
    {
        "title": "Python Exception Handling Common Mistake",
        "content": "Exception handling should be designed around the errors a program is expected to handle. Using overly broad exception handling can hide programming errors and make debugging more difficult.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Exception Handling",
        "category": "Common Mistake",
        "difficulty": "Medium",
        "keywords": "exception, errors, debugging, common mistake",
        "author": "EchoMind"
    },

    {
        "title": "Python Multithreading",
        "content": "Multithreading allows a program to manage multiple threads of execution within a process. Threads can be used when a program needs multiple activities to progress concurrently.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Multithreading",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "multithreading, threads, concurrency",
        "author": "EchoMind"
    },
    {
        "title": "Python Thread",
        "content": "A thread represents an execution path within a program. A multithreaded application can have multiple threads performing different tasks under the program's execution model.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Multithreading",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "thread, multithreading, execution",
        "author": "EchoMind"
    },

    {
        "title": "Python Networking",
        "content": "Networking allows programs to communicate across a network. Python provides networking capabilities that can be used to build programs that send and receive information between systems.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Networking",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "networking, communication, Python",
        "author": "EchoMind"
    },
    {
        "title": "Client Server Programming",
        "content": "Client-server programming separates communication roles between a client and a server. The client requests a service or resource while the server receives requests and provides an appropriate response.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Client Server Programming",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "client server, networking, communication",
        "author": "EchoMind"
    },
    {
        "title": "Python Client Server Communication",
        "content": "A client-server application requires communication between the client and server. The client sends a request or data, and the server processes the communication and provides a response according to the application's protocol.",
        "subject": "Python Programming",
        "unit": "Unit IV",
        "topic": "Client Server Programming",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "client, server, request, response, networking",
        "author": "EchoMind"
    }

]


def seed_python():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    added = 0
    skipped = 0

    for item in python_knowledge:

        cursor.execute(
            """
            SELECT id
            FROM knowledge
            WHERE title = ?
              AND subject = ?
              AND topic = ?
            """,
            (
                item["title"],
                item["subject"],
                item["topic"]
            )
        )

        existing = cursor.fetchone()

        if existing:
            skipped += 1
            continue

        cursor.execute(
            """
            INSERT INTO knowledge (
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
                item["title"],
                item["content"],
                item["subject"],
                item["unit"],
                item["topic"],
                item["category"],
                item["difficulty"],
                item["keywords"],
                item["author"]
            )
        )

        added += 1

    connection.commit()
    connection.close()

    print(f"Added {added} Python knowledge entries.")
    print(f"Skipped {skipped} existing Python entries.")


if __name__ == "__main__":
    seed_python()