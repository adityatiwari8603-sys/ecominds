import sqlite3

from database import get_connection


DE_KNOWLEDGE = [

    # ============================================================
    # UNIT I — NUMBER SYSTEMS AND BOOLEAN ALGEBRA
    # ============================================================

    {
        "title": "What is Digital Electronics?",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Digital Electronics",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "digital electronics digital signal binary logic",
        "content": """
Digital electronics is a branch of electronics that deals mainly with discrete
signals represented using digital values, commonly binary 0 and 1.

Digital circuits are used in computers, calculators, communication systems,
control systems, processors, memory devices, and embedded systems.
"""
    },

    {
        "title": "Analog vs Digital Signal",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Digital and Analog Signals",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "analog digital signal continuous discrete difference",
        "content": """
An analog signal varies continuously with time and can have many possible
values.

A digital signal uses discrete values. In binary digital systems, the two
logic values are generally represented by 0 and 1.

Analog signals are continuous, while digital signals represent information
using discrete levels.
"""
    },

    {
        "title": "Binary Number System",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Number Systems",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "binary number system base 2 0 1",
        "content": """
The binary number system has base 2 and uses only two digits: 0 and 1.

Each position represents a power of 2.

For example:

(1011)₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰
        = 8 + 0 + 2 + 1
        = 11₁₀
"""
    },

    {
        "title": "Decimal Number System",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Number Systems",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "decimal number system base 10",
        "content": """
The decimal number system has base 10 and uses digits from 0 to 9.

Each position represents a power of 10.

For example:

325 = 3×10² + 2×10¹ + 5×10⁰
"""
    },

    {
        "title": "Octal Number System",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Number Systems",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "octal number system base 8 digits",
        "content": """
The octal number system has base 8 and uses digits from 0 to 7.

Each octal digit represents three binary bits.

Example:

(25)₈ = 2×8¹ + 5×8⁰
       = 16 + 5
       = 21₁₀
"""
    },

    {
        "title": "Hexadecimal Number System",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Number Systems",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "hexadecimal base 16 digits A B C D E F",
        "content": """
The hexadecimal number system has base 16.

It uses:
0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

Here A=10, B=11, C=12, D=13, E=14 and F=15.

One hexadecimal digit represents four binary bits.
"""
    },

    {
        "title": "Binary to Decimal Conversion",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Number Conversion",
        "category": "Numerical",
        "difficulty": "Easy",
        "keywords": "binary decimal conversion powers of 2",
        "content": """
To convert binary to decimal, multiply each binary digit by its corresponding
power of 2 and add the results.

Example:

(10101)₂
= 1×2⁴ + 0×2³ + 1×2² + 0×2¹ + 1×2⁰
= 16 + 4 + 1
= 21₁₀
"""
    },

    {
        "title": "Decimal to Binary Conversion",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Number Conversion",
        "category": "Numerical",
        "difficulty": "Easy",
        "keywords": "decimal binary conversion repeated division",
        "content": """
To convert an integer decimal number to binary, repeatedly divide the number
by 2 and record the remainders.

Read the remainders from bottom to top.

Example:

13 ÷ 2 → remainder 1
6 ÷ 2  → remainder 0
3 ÷ 2  → remainder 1
1 ÷ 2  → remainder 1

Therefore:

13₁₀ = 1101₂
"""
    },

    {
        "title": "1's Complement",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Complements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "ones complement binary invert bits",
        "content": """
The 1's complement of a binary number is obtained by changing every 0 to 1
and every 1 to 0.

Example:

Binary:       10110010
1's complement: 01001101
"""
    },

    {
        "title": "2's Complement",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Complements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "twos complement binary subtraction negative number",
        "content": """
The 2's complement of a binary number is obtained by:

1. Finding its 1's complement.
2. Adding 1 to the result.

Example:

Binary:
10110010

1's complement:
01001101

Add 1:
01001110

Therefore, the 2's complement is 01001110.
"""
    },

    {
        "title": "Binary Addition",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Binary Arithmetic",
        "category": "Numerical",
        "difficulty": "Easy",
        "keywords": "binary addition rules carry",
        "content": """
Basic binary addition rules are:

0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10

When adding 1 + 1, the result is 0 with carry 1 to the next position.
"""
    },

    {
        "title": "Boolean Algebra",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Boolean Algebra",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "boolean algebra logic variables operations digital",
        "content": """
Boolean algebra is a mathematical system used to represent and simplify
logical relationships in digital circuits.

Boolean variables generally have two values:
0 and 1.

The fundamental operations are:
- AND
- OR
- NOT

Boolean algebra is useful for simplifying logic expressions and designing
digital circuits.
"""
    },

    {
        "title": "Boolean Algebra Laws",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Boolean Algebra",
        "category": "Exam Important",
        "difficulty": "Medium",
        "keywords": "boolean laws identity null idempotent complement absorption",
        "content": """
Important Boolean algebra laws include:

Identity:
A + 0 = A
A·1 = A

Null:
A + 1 = 1
A·0 = 0

Idempotent:
A + A = A
A·A = A

Complement:
A + A' = 1
A·A' = 0

Involution:
(A')' = A

Absorption:
A + AB = A
A(A+B) = A
"""
    },

    {
        "title": "De Morgan's Theorems",
        "subject": "Digital Electronics",
        "unit": "Unit I",
        "topic": "Boolean Algebra",
        "category": "Exam Important",
        "difficulty": "Medium",
        "keywords": "demorgan theorem boolean complement AND OR",
        "content": """
De Morgan's theorems are:

First theorem:
(A + B)' = A'·B'

Second theorem:
(A·B)' = A' + B'

They are widely used to simplify Boolean expressions and convert between
logic gate implementations.
"""
    },

    # ============================================================
    # UNIT II — LOGIC GATES
    # ============================================================

    {
        "title": "Logic Gate",
        "subject": "Digital Electronics",
        "unit": "Unit II",
        "topic": "Logic Gates",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "logic gate digital circuit input output",
        "content": """
A logic gate is a digital circuit that performs a logical operation on one
or more input signals and produces an output.

Basic gates include:
- AND
- OR
- NOT

Other important gates include:
- NAND
- NOR
- XOR
- XNOR
"""
    },

    {
        "title": "AND Gate",
        "subject": "Digital Electronics",
        "unit": "Unit II",
        "topic": "AND Gate",
        "category": "Logic Gate",
        "difficulty": "Easy",
        "keywords": "AND gate truth table multiplication",
        "content": """
An AND gate produces output 1 only when all inputs are 1.

For two inputs:

A B | Y
0 0 | 0
0 1 | 0
1 0 | 0
1 1 | 1

Boolean expression:

Y = A·B
"""
    },

    {
        "title": "OR Gate",
        "subject": "Digital Electronics",
        "unit": "Unit II",
        "topic": "OR Gate",
        "category": "Logic Gate",
        "difficulty": "Easy",
        "keywords": "OR gate truth table addition",
        "content": """
An OR gate produces output 1 when at least one input is 1.

For two inputs:

A B | Y
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 1

Boolean expression:

Y = A + B
"""
    },

    {
        "title": "NOT Gate",
        "subject": "Digital Electronics",
        "unit": "Unit II",
        "topic": "NOT Gate",
        "category": "Logic Gate",
        "difficulty": "Easy",
        "keywords": "NOT gate inverter complement",
        "content": """
A NOT gate is an inverter. It produces the complement of its input.

A = 0 → Y = 1
A = 1 → Y = 0

Boolean expression:

Y = A'
"""
    },

    {
        "title": "NAND Gate",
        "subject": "Digital Electronics",
        "unit": "Unit II",
        "topic": "NAND Gate",
        "category": "Logic Gate",
        "difficulty": "Easy",
        "keywords": "NAND universal gate AND NOT",
        "content": """
A NAND gate is an AND gate followed by a NOT gate.

Boolean expression:

Y = (A·B)'

The output is 0 only when all inputs are 1.

NAND is called a universal gate because basic logic functions can be
implemented using only NAND gates.
"""
    },

    {
        "title": "NOR Gate",
        "subject": "Digital Electronics",
        "unit": "Unit II",
        "topic": "NOR Gate",
        "category": "Logic Gate",
        "difficulty": "Easy",
        "keywords": "NOR universal gate OR NOT",
        "content": """
A NOR gate is an OR gate followed by a NOT gate.

Boolean expression:

Y = (A+B)'

The output is 1 only when all inputs are 0.

NOR is also a universal gate.
"""
    },

    {
        "title": "XOR Gate",
        "subject": "Digital Electronics",
        "unit": "Unit II",
        "topic": "XOR Gate",
        "category": "Logic Gate",
        "difficulty": "Easy",
        "keywords": "XOR exclusive OR truth table",
        "content": """
XOR stands for Exclusive OR.

A two-input XOR gate produces output 1 when the two inputs are different.

A B | Y
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 0

Boolean expression:

Y = A'B + AB'
"""
    },

    {
        "title": "XNOR Gate",
        "subject": "Digital Electronics",
        "unit": "Unit II",
        "topic": "XNOR Gate",
        "category": "Logic Gate",
        "difficulty": "Easy",
        "keywords": "XNOR equivalence gate truth table",
        "content": """
XNOR stands for Exclusive NOR.

A two-input XNOR gate produces output 1 when the inputs are equal.

A B | Y
0 0 | 1
0 1 | 0
1 0 | 0
1 1 | 1

XNOR is also called an equivalence gate.
"""
    },

    {
        "title": "Universal Gates",
        "subject": "Digital Electronics",
        "unit": "Unit II",
        "topic": "Universal Gates",
        "category": "Exam Important",
        "difficulty": "Easy",
        "keywords": "universal gate NAND NOR",
        "content": """
NAND and NOR are called universal gates because any basic Boolean function
can be implemented using only NAND gates or only NOR gates.

For example, NOT can be implemented using a NAND gate by connecting both
inputs together.
"""
    },

    # ============================================================
    # UNIT III — SOP, POS AND K-MAP
    # ============================================================

    {
        "title": "SOP Form",
        "subject": "Digital Electronics",
        "unit": "Unit III",
        "topic": "SOP",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "sum of products SOP minterms boolean expression",
        "content": """
SOP stands for Sum of Products.

In SOP form, product terms are ORed together.

Example:

F = AB + A'C + BC

Canonical SOP can be represented using minterms.
"""
    },

    {
        "title": "POS Form",
        "subject": "Digital Electronics",
        "unit": "Unit III",
        "topic": "POS",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "product of sums POS maxterms boolean expression",
        "content": """
POS stands for Product of Sums.

In POS form, sum terms are ANDed together.

Example:

F = (A+B)(A'+C)(B+C')

Canonical POS can be represented using maxterms.
"""
    },

    {
        "title": "Minterm",
        "subject": "Digital Electronics",
        "unit": "Unit III",
        "topic": "Minterms and Maxterms",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "minterm SOP canonical boolean",
        "content": """
A minterm is a product term containing every variable of a Boolean function
exactly once, either complemented or uncomplemented.

Minterms are associated with rows of a truth table where the output is 1.

Canonical SOP is represented as a sum of minterms.
"""
    },

    {
        "title": "Maxterm",
        "subject": "Digital Electronics",
        "unit": "Unit III",
        "topic": "Minterms and Maxterms",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "maxterm POS canonical boolean",
        "content": """
A maxterm is a sum term containing every variable exactly once, either
complemented or uncomplemented.

Maxterms are associated with rows of a truth table where the output is 0.

Canonical POS is represented as a product of maxterms.
"""
    },

    {
        "title": "K-Map Simplification",
        "subject": "Digital Electronics",
        "unit": "Unit III",
        "topic": "K-Map",
        "category": "Numerical",
        "difficulty": "Medium",
        "keywords": "K-map Karnaugh map simplification grouping minterms",
        "content": """
A Karnaugh map, or K-map, is a graphical method for simplifying Boolean
expressions.

Important rules:
- Cells are arranged in Gray-code order.
- Groups contain powers of two cells: 1, 2, 4, 8, etc.
- Groups should be as large as possible.
- Groups may wrap around edges.
- Overlapping groups are allowed when useful.
- For SOP simplification, group cells containing 1.
- For POS simplification, group cells containing 0.

The simplified expression is obtained from the variables that remain constant
within each group.
"""
    },

    # ============================================================
    # UNIT IV — COMBINATIONAL CIRCUITS
    # ============================================================

    {
        "title": "Combinational Circuit",
        "subject": "Digital Electronics",
        "unit": "Unit IV",
        "topic": "Combinational Circuits",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "combinational circuit output current input no memory",
        "content": """
A combinational circuit is a digital circuit whose output depends only on
the current input values.

It does not have memory.

Examples:
- Adders
- Subtractors
- Multiplexers
- Demultiplexers
- Encoders
- Decoders
"""
    },

    {
        "title": "Half Adder",
        "subject": "Digital Electronics",
        "unit": "Unit IV",
        "topic": "Half Adder",
        "category": "Combinational Circuit",
        "difficulty": "Medium",
        "keywords": "half adder sum carry XOR AND",
        "content": """
A half adder adds two one-bit binary numbers.

Inputs:
A, B

Outputs:
Sum, Carry

Equations:

Sum = A XOR B
Carry = A AND B

It does not have a carry input.
"""
    },

    {
        "title": "Full Adder",
        "subject": "Digital Electronics",
        "unit": "Unit IV",
        "topic": "Full Adder",
        "category": "Combinational Circuit",
        "difficulty": "Medium",
        "keywords": "full adder sum carry cin cout",
        "content": """
A full adder adds three one-bit inputs:

A, B, and Cin.

Outputs:
- Sum
- Carry-out

Equations:

Sum = A XOR B XOR Cin

Carry-out = AB + BCin + ACin

A full adder can be constructed using two half adders and an OR gate.
"""
    },

    {
        "title": "Half Subtractor",
        "subject": "Digital Electronics",
        "unit": "Unit IV",
        "topic": "Half Subtractor",
        "category": "Combinational Circuit",
        "difficulty": "Medium",
        "keywords": "half subtractor difference borrow XOR AND NOT",
        "content": """
A half subtractor subtracts one binary bit from another.

Inputs:
A, B

Outputs:
Difference and Borrow.

Equations:

Difference = A XOR B

Borrow = A'B
"""
    },

    {
        "title": "Full Subtractor",
        "subject": "Digital Electronics",
        "unit": "Unit IV",
        "topic": "Full Subtractor",
        "category": "Combinational Circuit",
        "difficulty": "Medium",
        "keywords": "full subtractor difference borrow bin",
        "content": """
A full subtractor performs subtraction using three inputs:

A, B, and Borrow-in.

Outputs:
- Difference
- Borrow-out

Difference:

D = A XOR B XOR Bin

Borrow-out:

Bout = A'B + A'Bin + BBin
"""
    },

    {
        "title": "Multiplexer",
        "subject": "Digital Electronics",
        "unit": "Unit IV",
        "topic": "Multiplexer",
        "category": "Combinational Circuit",
        "difficulty": "Medium",
        "keywords": "MUX multiplexer data selector select lines",
        "content": """
A multiplexer, or MUX, is a combinational circuit that selects one input
from multiple inputs and sends it to a single output.

For a 2^n-to-1 multiplexer:
- Number of data inputs = 2^n
- Number of select lines = n
- Number of outputs = 1

A multiplexer is also called a data selector.
"""
    },

    {
        "title": "Demultiplexer",
        "subject": "Digital Electronics",
        "unit": "Unit IV",
        "topic": "Demultiplexer",
        "category": "Combinational Circuit",
        "difficulty": "Medium",
        "keywords": "DEMUX demultiplexer data distributor select lines",
        "content": """
A demultiplexer, or DEMUX, takes one input and routes it to one of multiple
outputs according to select lines.

For a 1-to-2^n demultiplexer:
- One data input
- n select lines
- 2^n outputs

A DEMUX is a data distributor.
"""
    },

    {
        "title": "Encoder",
        "subject": "Digital Electronics",
        "unit": "Unit IV",
        "topic": "Encoder",
        "category": "Combinational Circuit",
        "difficulty": "Medium",
        "keywords": "encoder digital circuit inputs outputs binary",
        "content": """
An encoder converts one active input from a set of input lines into a binary
code at its output.

A basic 2^n-to-n encoder has:
- 2^n input lines
- n output lines

A practical encoder may require additional logic when multiple inputs can
be active.
"""
    },

    {
        "title": "Decoder",
        "subject": "Digital Electronics",
        "unit": "Unit IV",
        "topic": "Decoder",
        "category": "Combinational Circuit",
        "difficulty": "Medium",
        "keywords": "decoder binary input output lines",
        "content": """
A decoder converts an n-bit binary input into one of up to 2^n output lines.

A basic n-to-2^n decoder has:
- n input lines
- Up to 2^n output lines

For each valid input combination, a corresponding output line is activated,
depending on the circuit's enable and active-level conventions.
"""
    },

    # ============================================================
    # UNIT V — SEQUENTIAL CIRCUITS
    # ============================================================

    {
        "title": "Sequential Circuit",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "Sequential Circuits",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "sequential circuit memory clock flip flop",
        "content": """
A sequential circuit is a digital circuit whose output depends on the
current inputs and the previous state of the circuit.

Sequential circuits have memory elements.

Examples:
- Flip-flops
- Registers
- Counters
"""
    },

    {
        "title": "Combinational vs Sequential Circuit",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "Combinational and Sequential Circuits",
        "category": "Exam Important",
        "difficulty": "Easy",
        "keywords": "combinational sequential difference memory clock",
        "content": """
Combinational circuit:
- Output depends only on current inputs.
- Normally has no memory.
- Examples: adder, multiplexer, decoder.

Sequential circuit:
- Output depends on current inputs and previous state.
- Contains memory elements.
- Often uses a clock.
- Examples: flip-flop, register, counter.
"""
    },

    {
        "title": "What is a Flip-Flop?",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "Flip-Flops",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "flip flop memory one bit sequential circuit",
        "content": """
A flip-flop is a basic memory element in digital electronics capable of
storing one bit of information.

It is used in:
- Registers
- Counters
- Memory circuits
- Sequential logic systems
"""
    },

    {
        "title": "SR Flip-Flop",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "SR Flip-Flop",
        "category": "Flip-Flop",
        "difficulty": "Medium",
        "keywords": "SR flip flop set reset",
        "content": """
An SR flip-flop has two principal inputs:

S = Set
R = Reset

For a basic active-high SR latch:

S=0, R=0 → Hold
S=1, R=0 → Set
S=0, R=1 → Reset
S=1, R=1 → Invalid for the basic NOR implementation

The exact invalid condition depends on the implementation.
"""
    },

    {
        "title": "JK Flip-Flop",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "JK Flip-Flop",
        "category": "Flip-Flop",
        "difficulty": "Medium",
        "keywords": "JK flip flop toggle set reset",
        "content": """
A JK flip-flop is an improved form of the SR flip-flop.

For a typical JK flip-flop:

J=0, K=0 → Hold
J=0, K=1 → Reset
J=1, K=0 → Set
J=1, K=1 → Toggle

The toggle operation makes JK flip-flops useful in counters.
"""
    },

    {
        "title": "D Flip-Flop",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "D Flip-Flop",
        "category": "Flip-Flop",
        "difficulty": "Easy",
        "keywords": "D flip flop data delay storage",
        "content": """
A D flip-flop has a single data input D.

For a clocked edge-triggered D flip-flop, the output takes the value of D
at the active clock edge.

Thus, conceptually:

Q(next) = D

D flip-flops are widely used in registers and data storage.
"""
    },

    {
        "title": "T Flip-Flop",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "T Flip-Flop",
        "category": "Flip-Flop",
        "difficulty": "Easy",
        "keywords": "T flip flop toggle counter",
        "content": """
A T flip-flop is designed for toggle operation.

Typical behavior:

T=0 → Hold
T=1 → Toggle

T flip-flops are commonly used in counter circuits.
"""
    },

    {
        "title": "Registers",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "Registers",
        "category": "Sequential Circuit",
        "difficulty": "Medium",
        "keywords": "register shift register storage bits",
        "content": """
A register is a group of flip-flops used to store multiple bits of binary
information.

A register may also shift data from one position to another.

Common shift-register types include:
- SISO
- SIPO
- PISO
- PIPO
"""
    },

    {
        "title": "Shift Registers",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "Shift Registers",
        "category": "Sequential Circuit",
        "difficulty": "Medium",
        "keywords": "shift register SISO SIPO PISO PIPO",
        "content": """
A shift register is a register that moves stored bits from one flip-flop
position to another on clock pulses.

Types:

SISO — Serial In Serial Out
SIPO — Serial In Parallel Out
PISO — Parallel In Serial Out
PIPO — Parallel In Parallel Out

Shift registers are used for data storage and serial/parallel data conversion.
"""
    },

    {
        "title": "Counters",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "Counters",
        "category": "Sequential Circuit",
        "difficulty": "Medium",
        "keywords": "counter digital sequential binary counting flip flop",
        "content": """
A counter is a sequential circuit that moves through a predetermined sequence
of states in response to clock pulses.

Counters are used for:
- Counting events
- Frequency division
- Timing
- Digital clocks
- Control circuits

Counters may be asynchronous or synchronous.
"""
    },

    {
        "title": "Synchronous Counter",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "Synchronous Counter",
        "category": "Sequential Circuit",
        "difficulty": "Medium",
        "keywords": "synchronous counter common clock flip flop",
        "content": """
In a synchronous counter, all flip-flops receive the clock signal
simultaneously.

Advantages:
- Faster operation
- More predictable timing
- Less cumulative propagation delay than a ripple counter

The combinational logic determines which flip-flops change state.
"""
    },

    {
        "title": "Asynchronous Counter",
        "subject": "Digital Electronics",
        "unit": "Unit V",
        "topic": "Asynchronous Counter",
        "category": "Sequential Circuit",
        "difficulty": "Medium",
        "keywords": "asynchronous counter ripple counter propagation delay",
        "content": """
In an asynchronous counter, the clock is applied directly to one flip-flop
and subsequent flip-flops are triggered by outputs of preceding stages.

It is also called a ripple counter.

Its main limitation is cumulative propagation delay through the flip-flops.
"""
    },

    # ============================================================
    # EXAM REVISION
    # ============================================================

    {
        "title": "Digital Electronics Important Topics",
        "subject": "Digital Electronics",
        "unit": "All Units",
        "topic": "Exam Revision",
        "category": "Exam Strategy",
        "difficulty": "Easy",
        "keywords": "digital electronics exam important topics revision",
        "content": """
Important Digital Electronics topics for revision include:

1. Number systems
2. Binary conversions
3. 1's complement
4. 2's complement
5. Binary arithmetic
6. Boolean algebra
7. Boolean laws
8. De Morgan's theorems
9. Logic gates
10. NAND and NOR universal gates
11. XOR and XNOR
12. SOP and POS
13. Minterms and maxterms
14. K-map
15. Combinational circuits
16. Half adder
17. Full adder
18. Half subtractor
19. Full subtractor
20. Multiplexer
21. Demultiplexer
22. Encoder
23. Decoder
24. Sequential circuits
25. Flip-flops
26. Registers
27. Shift registers
28. Counters
29. Synchronous counters
30. Asynchronous counters
"""
    }
]


def add_knowledge(item):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM knowledge
        WHERE title = ?
        """,
        (item["title"],)
    )

    existing = cursor.fetchone()

    if existing:
        conn.close()
        return False

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
            item["content"].strip(),
            item["subject"],
            item["unit"],
            item["topic"],
            item["category"],
            item["difficulty"],
            item["keywords"],
            "EchoMind Academic Knowledge"
        )
    )

    conn.commit()
    conn.close()

    return True


def main():
    added = 0
    skipped = 0

    for item in DE_KNOWLEDGE:
        if add_knowledge(item):
            added += 1
        else:
            skipped += 1

    print("=" * 60)
    print("EchoMind Digital Electronics Knowledge Seed")
    print("=" * 60)
    print(f"Added:   {added}")
    print(f"Skipped: {skipped}")
    print(f"Total entries in seed: {len(DE_KNOWLEDGE)}")
    print("=" * 60)


if __name__ == "__main__":
    main()