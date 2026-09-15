from database import init_database, get_connection

AUTHOR = "EchoMind Full Knowledge Pack"

KNOWLEDGE = [
    # =========================
    # SEMESTER 1 — PPS
    # =========================

    {
        "title": "PPS - Algorithms and Problem Solving",
        "content": """An algorithm is a finite, ordered set of unambiguous steps for solving a problem.
Important characteristics include finiteness, definiteness, input, output and effectiveness.
A good solution normally follows:
problem understanding -> algorithm -> pseudocode/flowchart -> implementation -> testing -> debugging.""",
        "subject": "PPS",
        "unit": "Unit I",
        "topic": "Programming Fundamentals",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "algorithm, problem solving, pseudocode, flowchart"
    },

    {
        "title": "PPS - Python Variables and Data Types",
        "content": """A variable is a name bound to a value.
Common Python data types include int, float, str, bool, list, tuple, set and dict.
Python uses dynamic typing, so the type of a variable is determined at runtime.

Example:
marks = 85
name = "Aditya".""",
        "subject": "PPS",
        "unit": "Unit I",
        "topic": "Python Basics",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "python, variables, data types, int, float, string, boolean"
    },

    {
        "title": "PPS - If, Elif and Else",
        "content": """Conditional statements allow a program to choose different execution paths.

if checks a condition.
elif checks another condition.
else handles the remaining case.

Python uses indentation to define the block belonging to each condition.""",
        "subject": "PPS",
        "unit": "Unit II",
        "topic": "Control Statements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "if, elif, else, conditional statement"
    },

    {
        "title": "PPS - For and While Loops",
        "content": """A for loop iterates over an iterable such as a range or list.
A while loop continues while a condition is true.

break terminates a loop.
continue skips the current iteration.
pass is a placeholder statement.""",
        "subject": "PPS",
        "unit": "Unit II",
        "topic": "Loops",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "for loop, while loop, break, continue, pass"
    },

    {
        "title": "PPS - Python Functions",
        "content": """A function is a reusable block of code.
Functions can accept parameters and may return a value using return.

Benefits:
- code reuse
- modularity
- testing
- readability

A Python function is defined using def.""",
        "subject": "PPS",
        "unit": "Unit III",
        "topic": "Functions",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "function, def, parameters, return, modular programming"
    },

    {
        "title": "PPS - Lists, Tuples, Sets and Dictionaries",
        "content": """A list is ordered and mutable.
A tuple is ordered and immutable.
A set stores unique elements.
A dictionary stores key-value pairs.

The appropriate collection depends on ordering, mutability and lookup requirements.""",
        "subject": "PPS",
        "unit": "Unit IV",
        "topic": "Collections",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "list, tuple, set, dictionary, collection"
    },

    {
        "title": "PPS - File Handling and Exceptions",
        "content": """Python file handling commonly uses open() with modes such as r, w and a.
Exceptions can be handled using try, except, else and finally.

Exception handling prevents expected runtime problems from terminating the entire program unexpectedly.""",
        "subject": "PPS",
        "unit": "Unit V",
        "topic": "Exceptions and Files",
        "category": "Practical Tip",
        "difficulty": "Medium",
        "keywords": "file handling, open, read, write, exception, try except"
    },

    # =========================
    # SEMESTER 1 — PHYSICS
    # =========================

    {
        "title": "Physics - SI Units and Dimensions",
        "content": """The SI system contains seven base units:
metre, kilogram, second, ampere, kelvin, mole and candela.

Derived units are formed from base units.
Dimensional analysis can be used to check the consistency of physical equations.""",
        "subject": "Physics",
        "unit": "Unit I",
        "topic": "Units and Measurement",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "SI units, dimensions, measurement, derived units"
    },

    {
        "title": "Physics - Wave Motion",
        "content": """Important wave terms are:
amplitude
wavelength
frequency
time period
phase

Frequency is the number of cycles per second.

For a travelling wave:
v = f lambda""",
        "subject": "Physics",
        "unit": "Unit II",
        "topic": "Wave Motion",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "wave, wavelength, frequency, amplitude, time period"
    },

    {
        "title": "Physics - Reflection and Refraction",
        "content": """Reflection is the return of light into the same medium after striking a surface.

Refraction is the change in direction of light when it enters a different medium because its speed changes.

Snell's law relates the angles and refractive indices of the two media.""",
        "subject": "Physics",
        "unit": "Unit III",
        "topic": "Optics",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "reflection, refraction, Snell law, optics"
    },

    {
        "title": "Physics - Photoelectric Effect",
        "content": """The photoelectric effect is the emission of electrons from a material when electromagnetic radiation of suitable frequency falls on it.

Important ideas include:
threshold frequency
work function
stopping potential""",
        "subject": "Physics",
        "unit": "Unit IV",
        "topic": "Modern Physics",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "photoelectric effect, threshold frequency, work function"
    },

    {
        "title": "Physics - Laser Characteristics",
        "content": """LASER stands for Light Amplification by Stimulated Emission of Radiation.

Laser light is:
highly coherent
highly directional
narrow in spectral width

Applications include communication, medicine, measurement and manufacturing.""",
        "subject": "Physics",
        "unit": "Unit V",
        "topic": "Lasers",
        "category": "Viva Question",
        "difficulty": "Medium",
        "keywords": "laser, stimulated emission, coherence, applications"
    },

    # =========================
    # SEMESTER 1 — AI
    # =========================

    {
        "title": "AI - Intelligent Agents",
        "content": """An intelligent agent perceives its environment through sensors and acts through actuators.

A rational agent selects actions that maximize expected performance according to its performance measure.""",
        "subject": "Artificial Intelligence",
        "unit": "Unit I",
        "topic": "AI Fundamentals",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "AI, intelligent agent, sensors, actuators, rational agent"
    },

    {
        "title": "AI - Breadth First Search",
        "content": """Breadth First Search explores nodes level by level using a queue.

For an unweighted graph, BFS can find shortest paths in terms of number of edges.

Its commonly stated graph complexity is O(V + E).""",
        "subject": "Artificial Intelligence",
        "unit": "Unit II",
        "topic": "Search",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "AI, BFS, breadth first search, graph search, queue"
    },

    {
        "title": "AI - Depth First Search",
        "content": """Depth First Search explores as far as possible along one branch before backtracking.

It can be implemented using recursion or an explicit stack.

DFS is useful for traversal, connectivity and search problems.""",
        "subject": "Artificial Intelligence",
        "unit": "Unit II",
        "topic": "Search",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "AI, DFS, depth first search, stack, recursion"
    },

    {
        "title": "AI - Machine Learning Types",
        "content": """Supervised learning uses labelled examples.
Unsupervised learning finds structure in unlabelled data.
Reinforcement learning learns through interaction with an environment using rewards and penalties.""",
        "subject": "Artificial Intelligence",
        "unit": "Unit III",
        "topic": "Machine Learning",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "machine learning, supervised, unsupervised, reinforcement"
    },

    {
        "title": "AI - Neural Network Basics",
        "content": """A neural network is built from connected computational units.

A basic neuron computes a weighted sum, adds a bias and applies an activation function.

Networks learn parameters from data using an optimization procedure.""",
        "subject": "Artificial Intelligence",
        "unit": "Unit IV",
        "topic": "Neural Networks",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "neural network, neuron, activation, weights, bias"
    },

    # =========================
    # SEMESTER 1 — MATHEMATICS-I
    # =========================

    {
        "title": "Mathematics-I - Matrix Operations",
        "content": """Matrix operations include:
addition
subtraction
scalar multiplication
matrix multiplication

Matrix multiplication is defined only when the number of columns of the first matrix equals the number of rows of the second matrix.""",
        "subject": "Mathematics-I",
        "unit": "Unit I",
        "topic": "Matrices",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "matrix, matrices, multiplication, determinant"
    },

    {
        "title": "Mathematics-I - Differentiation",
        "content": """Differentiation measures instantaneous rate of change.

Important rules include:
power rule
product rule
quotient rule
chain rule

Derivatives are used for slope, optimization and related rates.""",
        "subject": "Mathematics-I",
        "unit": "Unit II",
        "topic": "Differential Calculus",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "differentiation, derivative, product rule, chain rule"
    },

    {
        "title": "Mathematics-I - Integration",
        "content": """Integration can be viewed as anti-differentiation and accumulation.

Important methods include:
substitution
integration by parts
partial fractions

Definite integrals can represent accumulated quantities such as area.""",
        "subject": "Mathematics-I",
        "unit": "Unit III",
        "topic": "Integral Calculus",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "integration, integral, definite integral, area"
    },

    {
        "title": "Mathematics-I - First Order Differential Equations",
        "content": """A differential equation relates an unknown function to its derivatives.

First-order equations include separable and linear forms.

For a linear first-order equation, an integrating factor can convert the equation into a directly integrable form.""",
        "subject": "Mathematics-I",
        "unit": "Unit IV",
        "topic": "Differential Equations",
        "category": "Important Question",
        "difficulty": "Hard",
        "keywords": "differential equation, first order, integrating factor"
    },

    {
        "title": "Mathematics-I - Laplace Transform Basics",
        "content": """The Laplace transform converts a function of time into a function of a complex variable.

It is especially useful for solving differential equations with initial conditions.""",
        "subject": "Mathematics-I",
        "unit": "Unit V",
        "topic": "Transforms",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "Laplace transform, differential equations, transform"
    },

    # =========================
    # SEMESTER 1 — BME
    # =========================

    {
        "title": "BME - Engineering Materials",
        "content": """Engineering materials include:
metals
polymers
ceramics
composites

Important properties include strength, hardness, toughness, ductility and conductivity.""",
        "subject": "BME",
        "unit": "Unit I",
        "topic": "Engineering Materials",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "BME, materials, metals, polymers, ceramics"
    },

    {
        "title": "BME - Mechanical Properties",
        "content": """Strength is the ability to resist failure under load.
Hardness is resistance to indentation or wear.
Toughness is the ability to absorb energy before fracture.
Ductility is the ability to undergo plastic deformation in tension.""",
        "subject": "BME",
        "unit": "Unit II",
        "topic": "Mechanical Properties",
        "category": "Viva Question",
        "difficulty": "Medium",
        "keywords": "strength, hardness, toughness, ductility"
    },

    {
        "title": "BME - Manufacturing Processes",
        "content": """Casting uses molten material and a mould.
Forging shapes material by compressive force.
Rolling reduces thickness or changes cross-section using rotating rolls.

Process selection depends on geometry, material and production volume.""",
        "subject": "BME",
        "unit": "Unit III",
        "topic": "Manufacturing",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "casting, forging, rolling, manufacturing"
    },

    {
        "title": "BME - Gears, Shafts and Bearings",
        "content": """Gears transfer motion and torque between rotating shafts.
Shafts transmit torque and support rotating components.
Bearings reduce friction and support relative motion.""",
        "subject": "BME",
        "unit": "Unit IV",
        "topic": "Machine Elements",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "gear, shaft, bearing, machine elements"
    },

    # =========================
    # SEMESTER 2 — BEEE
    # =========================

    {
        "title": "BEEE - KCL and KVL",
        "content": """Kirchhoff's Current Law states that the algebraic sum of currents at a node is zero.

Kirchhoff's Voltage Law states that the algebraic sum of voltages around a closed loop is zero.

Both laws are fundamental tools for circuit analysis.""",
        "subject": "BEEE",
        "unit": "Unit I",
        "topic": "Circuit Laws",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "KCL, KVL, Kirchhoff, circuit analysis"
    },

    {
        "title": "BEEE - RMS Average and Peak Values",
        "content": """For a sinusoidal waveform, the RMS value represents the equivalent DC heating effect.

Peak value is the maximum magnitude.

Average value over a complete symmetric cycle is zero, while rectified waveforms have non-zero average values.""",
        "subject": "BEEE",
        "unit": "Unit II",
        "topic": "AC Fundamentals",
        "category": "Numerical Problem",
        "difficulty": "Medium",
        "keywords": "RMS, average value, peak value, sinusoidal"
    },

    {
        "title": "BEEE - AC Power and Power Factor",
        "content": """Real power is measured in watts.
Reactive power is measured in VAR.
Apparent power is measured in VA.

For sinusoidal AC:
Power Factor = cos(phi)

A low power factor can increase current and losses for a given real power.""",
        "subject": "BEEE",
        "unit": "Unit III",
        "topic": "AC Power",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "real power, reactive power, apparent power, power factor"
    },

    {
        "title": "BEEE - Transformer Principle",
        "content": """A transformer transfers AC electrical energy between circuits using electromagnetic induction.

For an ideal transformer:
V1 / V2 = N1 / N2

A step-up transformer increases voltage.
A step-down transformer decreases voltage.""",
        "subject": "BEEE",
        "unit": "Unit IV",
        "topic": "Transformers",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "transformer, induction, turns ratio, step up, step down"
    },

    {
        "title": "BEEE - Diode BJT and MOSFET",
        "content": """A diode is primarily a one-way semiconductor device.

A BJT has emitter, base and collector terminals and can operate as an amplifier or switch.

A MOSFET is a voltage-controlled field-effect transistor with gate, source and drain terminals.""",
        "subject": "BEEE",
        "unit": "Unit V",
        "topic": "Semiconductors",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "diode, BJT, MOSFET, transistor, semiconductor"
    },

    # =========================
    # CHEMISTRY
    # =========================

    {
        "title": "Chemistry - Corrosion Mechanism",
        "content": """Corrosion can occur through electrochemical processes involving anodic metal oxidation and cathodic reduction reactions.

Prevention methods include coatings, inhibitors, cathodic protection and material selection.""",
        "subject": "Chemistry",
        "unit": "Unit I",
        "topic": "Corrosion",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "corrosion, electrochemical, anode, cathode, protection"
    },

    {
        "title": "Chemistry - Crystal Field Splitting",
        "content": """Crystal Field Theory describes splitting of d orbitals under the electric field of ligands.

In an octahedral complex the five d orbitals split into:
t2g - lower energy
eg - higher energy

The energy difference is crystal field splitting energy.""",
        "subject": "Chemistry",
        "unit": "Unit II",
        "topic": "CFT",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "CFT, crystal field, d orbitals, octahedral"
    },

    {
        "title": "Chemistry - Molecular Orbital Theory",
        "content": """Molecular Orbital Theory explains bonding using molecular orbitals formed from atomic orbitals.

Molecular orbitals are bonding or antibonding.

Bond order is related to the difference between bonding and antibonding electron populations.""",
        "subject": "Chemistry",
        "unit": "Unit II",
        "topic": "MO Theory",
        "category": "Exam Strategy",
        "difficulty": "Hard",
        "keywords": "MO theory, bonding, antibonding, bond order"
    },

    {
        "title": "Chemistry - Water Hardness and EDTA",
        "content": """Hardness of water is mainly associated with dissolved calcium and magnesium ions.

EDTA complexometric titration can estimate total hardness.
Eriochrome Black T is commonly used as an indicator.""",
        "subject": "Chemistry",
        "unit": "Unit III",
        "topic": "Water Treatment",
        "category": "Practical Tip",
        "difficulty": "Medium",
        "keywords": "water hardness, EDTA, EBT, calcium, magnesium"
    },

    {
        "title": "Chemistry - IR and NMR Spectroscopy",
        "content": """Infrared spectroscopy is associated with molecular vibrations and functional-group identification.

NMR spectroscopy provides information about nuclei in a magnetic field and is useful in structure determination.""",
        "subject": "Chemistry",
        "unit": "Unit IV",
        "topic": "Spectroscopy",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "IR, NMR, spectroscopy, functional groups"
    },

    {
        "title": "Chemistry - Isomerism and Stereochemistry",
        "content": """Isomers have the same molecular formula but different arrangements.

Structural isomerism changes connectivity.
Stereoisomerism changes spatial arrangement without changing connectivity.

R/S configuration is used for certain chiral centres.""",
        "subject": "Chemistry",
        "unit": "Unit V",
        "topic": "Organic Chemistry",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "isomerism, stereochemistry, R S configuration, chirality"
    },

    # =========================
    # MATHEMATICS-II
    # =========================

    {
        "title": "Mathematics-II - Conditional Probability and Bayes Theorem",
        "content": """Conditional probability measures the probability of an event given that another event has occurred.

Bayes theorem updates the probability of a hypothesis using evidence.""",
        "subject": "Mathematics-II",
        "unit": "Unit I",
        "topic": "Probability",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "conditional probability, Bayes theorem, probability"
    },

    {
        "title": "Mathematics-II - Binomial and Poisson Distributions",
        "content": """The binomial distribution models a fixed number of independent Bernoulli trials.

The Poisson distribution models counts of events occurring at a constant average rate over a fixed interval.""",
        "subject": "Mathematics-II",
        "unit": "Unit II",
        "topic": "Distributions",
        "category": "Numerical Problem",
        "difficulty": "Medium",
        "keywords": "binomial, Poisson, distribution, lambda"
    },

    {
        "title": "Mathematics-II - Normal Distribution and Z Score",
        "content": """The normal distribution is symmetric and bell-shaped.

Standardization:
Z = (X - mu) / sigma

A Z-table can then be used to find probabilities and areas under the standard normal curve.""",
        "subject": "Mathematics-II",
        "unit": "Unit III",
        "topic": "Normal Distribution",
        "category": "Numerical Problem",
        "difficulty": "Medium",
        "keywords": "normal distribution, z score, z table, standard deviation"
    },

    {
        "title": "Mathematics-II - Hypothesis Testing",
        "content": """Hypothesis testing starts with:
H0 = null hypothesis
H1 = alternative hypothesis

A test statistic is calculated and compared with a critical value or p-value criterion.""",
        "subject": "Mathematics-II",
        "unit": "Unit IV",
        "topic": "Hypothesis Testing",
        "category": "Concept Explanation",
        "difficulty": "Hard",
        "keywords": "hypothesis testing, null hypothesis, alternative hypothesis, p value"
    },

    {
        "title": "Mathematics-II - Chi Square and F Test",
        "content": """Chi-square tests are commonly used for categorical data, goodness of fit and independence.

The F test is commonly used for comparing variances and in ANOVA-related situations.""",
        "subject": "Mathematics-II",
        "unit": "Unit IV",
        "topic": "Tests",
        "category": "Important Question",
        "difficulty": "Hard",
        "keywords": "chi square, F test, variance, hypothesis testing"
    },

    {
        "title": "Mathematics-II - Regression Lines",
        "content": """Regression models describe relationships between variables.

The regression line of y on x is used to estimate y from x.

Correlation measures linear association while regression is used mainly for prediction.""",
        "subject": "Mathematics-II",
        "unit": "Unit V",
        "topic": "Regression",
        "category": "Study Notes",
        "difficulty": "Hard",
        "keywords": "regression, regression line, correlation, prediction"
    },

    # =========================
    # WORKSHOP TECHNOLOGY
    # =========================

    {
        "title": "Workshop - Casting and Pattern",
        "content": """A pattern is used to create the mould cavity in casting.

Pattern allowances account for shrinkage, machining and other dimensional effects.

Casting is useful for producing complex geometries.""",
        "subject": "Workshop Technology",
        "unit": "Unit I",
        "topic": "Casting",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "casting, pattern, mould, allowance"
    },

    {
        "title": "Workshop - Arc Welding",
        "content": """Arc welding uses an electric arc to provide heat for joining metals.

Important considerations include electrode selection, current, polarity, joint preparation and safety equipment.""",
        "subject": "Workshop Technology",
        "unit": "Unit II",
        "topic": "Welding",
        "category": "Practical Tip",
        "difficulty": "Medium",
        "keywords": "welding, arc welding, electrode, fabrication"
    },

    {
        "title": "Workshop - Lathe Operations",
        "content": """Common lathe operations include:
turning
facing
drilling
boring
threading
knurling

The workpiece rotates while the cutting tool removes material.""",
        "subject": "Workshop Technology",
        "unit": "Unit III",
        "topic": "Machining",
        "category": "Practical Tip",
        "difficulty": "Medium",
        "keywords": "lathe, turning, facing, drilling, threading"
    },

    {
        "title": "Workshop - Drilling Milling and Shaping",
        "content": """A drilling machine produces holes using a rotating drill.

A milling machine removes material using a rotating multi-point cutter.

A shaper commonly uses reciprocating motion for machining flat surfaces.""",
        "subject": "Workshop Technology",
        "unit": "Unit IV",
        "topic": "Machine Tools",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "drilling, milling, shaping, machine tools"
    },

    # =========================
    # CS CORE — DSA
    # =========================

    {
        "title": "DSA - Data Information and Data Structures",
        "content": """Data are raw facts.
Information is processed data with meaning.

A data structure organizes data so required operations can be performed efficiently.

Classifications include:
primitive/non-primitive
linear/non-linear
static/dynamic""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit I",
        "topic": "Introduction",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "data, information, data structure, primitive, non primitive, linear, non linear"
    },

    {
        "title": "DSA - Abstract Data Type",
        "content": """An Abstract Data Type specifies what operations are supported and what behaviour they provide without requiring a specific implementation.

Example:
A Stack ADT supports push, pop and peek.""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit I",
        "topic": "ADT",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "ADT, abstract data type, stack, operations"
    },

    {
        "title": "DSA - Basic Data Structure Operations",
        "content": """Common operations include:
Traversal
Searching
Insertion
Deletion
Updating
Sorting
Merging
Splitting

The cost of an operation depends on the data structure used.""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit I",
        "topic": "Operations",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "traversal, searching, insertion, deletion, sorting, merging"
    },

    {
        "title": "DSA - Big O Big Omega and Big Theta",
        "content": """Big O describes an asymptotic upper bound.
Big Omega describes an asymptotic lower bound.
Big Theta describes a tight asymptotic bound.

Common complexities:
O(1)
O(log n)
O(n)
O(n log n)
O(n^2)
O(n^3)
O(2^n)
O(n!)""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit I",
        "topic": "Complexity",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "Big O, Big Omega, Big Theta, asymptotic analysis"
    },

    {
        "title": "DSA - Linear Search",
        "content": """Linear search checks elements one by one until a match is found or the data ends.

It works on sorted and unsorted data.

Complexity:
Best case O(1)
Worst case O(n)""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit I",
        "topic": "Linear Search",
        "category": "Exam Strategy",
        "difficulty": "Easy",
        "keywords": "linear search, sequential search, O(n)"
    },

    {
        "title": "DSA - Binary Search",
        "content": """Binary search requires sorted data.

The search range is repeatedly divided into two halves.

Worst-case complexity is O(log n).

It can be implemented iteratively or recursively.""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit I",
        "topic": "Binary Search",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "binary search, iterative, recursive, O(log n)"
    },

    {
        "title": "DSA - Stack",
        "content": """A stack follows LIFO:
Last In, First Out.

Operations:
push
pop
peek

Applications include function calls, undo operations, backtracking and expression evaluation.""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit II",
        "topic": "Stack",
        "category": "Viva Question",
        "difficulty": "Medium",
        "keywords": "stack, push, pop, peek, LIFO"
    },

    {
        "title": "DSA - Queue and Circular Queue",
        "content": """A queue follows FIFO:
First In, First Out.

Operations:
enqueue
dequeue

A circular queue reuses positions by treating storage as cyclic.""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit II",
        "topic": "Queue",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "queue, FIFO, enqueue, dequeue, circular queue"
    },

    {
        "title": "DSA - Singly Linked List",
        "content": """A singly linked list consists of nodes connected using next references.

Each node normally stores:
data
next reference

Insertion and deletion can be efficient when the correct position is already known, while random indexing is slower than arrays.""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit II",
        "topic": "Linked List",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "linked list, node, pointer, singly linked list"
    },

    {
        "title": "DSA - Sorting Techniques",
        "content": """Sorting arranges data according to an ordering criterion.

Common algorithms:
Bubble Sort
Selection Sort
Insertion Sort
Merge Sort
Quick Sort

Different algorithms have different time and space complexity.""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit III",
        "topic": "Sorting",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "sorting, bubble sort, selection sort, insertion sort, merge sort, quicksort"
    },

    {
        "title": "DSA - Binary Trees",
        "content": """A tree is a hierarchical non-linear structure.

A binary tree allows at most two children per node.

Common traversals:
preorder
inorder
postorder""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit III",
        "topic": "Trees",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "tree, binary tree, preorder, inorder, postorder"
    },

    {
        "title": "DSA - Graph Basics and Traversal",
        "content": """A graph contains vertices and edges.

Graphs may be:
directed or undirected
weighted or unweighted

BFS generally uses a queue.
DFS generally uses recursion or a stack.""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit IV",
        "topic": "Graphs",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "graph, vertex, edge, BFS, DFS"
    },

    {
        "title": "DSA - Choosing the Right Data Structure",
        "content": """The right data structure depends on required operations.

Arrays provide fast indexing.
Linked lists support flexible structural changes.
Stacks provide LIFO behaviour.
Queues provide FIFO behaviour.

The choice should consider time, space and operation requirements.""",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit V",
        "topic": "Algorithm Design",
        "category": "Exam Strategy",
        "difficulty": "Medium",
        "keywords": "data structure selection, arrays, linked lists, stack, queue"
    },

    # =========================
    # CS CORE — OOP
    # =========================

    {
        "title": "OOP - Classes and Objects",
        "content": """A class defines attributes and behaviour.
An object is an instance of a class.

Classes provide a blueprint for creating objects and organizing data with related methods.""",
        "subject": "OOP",
        "unit": "Unit I",
        "topic": "Class and Object",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "class, object, constructor, attributes, methods"
    },

    {
        "title": "OOP - Encapsulation",
        "content": """Encapsulation combines data and behaviour and controls how internal state is accessed.

It supports modularity, maintainability and controlled access.""",
        "subject": "OOP",
        "unit": "Unit II",
        "topic": "Encapsulation",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "encapsulation, access control, data hiding"
    },

    {
        "title": "OOP - Inheritance",
        "content": """Inheritance allows a new class to reuse or extend another class.

Common conceptual forms include:
single inheritance
multilevel inheritance
hierarchical inheritance""",
        "subject": "OOP",
        "unit": "Unit II",
        "topic": "Inheritance",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "inheritance, base class, derived class, multilevel"
    },

    {
        "title": "OOP - Polymorphism",
        "content": """Polymorphism means one interface can represent different behaviours.

Compile-time forms may include overloading.
Run-time polymorphism commonly involves method overriding and dynamic dispatch.""",
        "subject": "OOP",
        "unit": "Unit III",
        "topic": "Polymorphism",
        "category": "Important Question",
        "difficulty": "Hard",
        "keywords": "polymorphism, overloading, overriding, dynamic dispatch"
    },

    # =========================
    # CS CORE — OPERATING SYSTEMS
    # =========================

    {
        "title": "OS - Generations and Types",
        "content": """Operating systems evolved from early batch systems to multiprogramming, time-sharing and modern distributed and mobile systems.

Types include:
batch
multiprogramming
multitasking
real-time
distributed
network OS""",
        "subject": "Operating Systems",
        "unit": "Unit I",
        "topic": "Basics",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "operating system, generations, batch, multiprogramming, real time"
    },

    {
        "title": "OS - Functions of Operating System",
        "content": """Major OS functions include:
process management
memory management
file management
device management
security
resource allocation""",
        "subject": "Operating Systems",
        "unit": "Unit I",
        "topic": "Functions",
        "category": "Important Question",
        "difficulty": "Easy",
        "keywords": "OS functions, process management, memory management, file management"
    },

    {
        "title": "OS - Process States and PCB",
        "content": """A process is a program in execution.

Typical process states:
new
ready
running
waiting or blocked
terminated

The PCB stores information required by the operating system to manage the process.""",
        "subject": "Operating Systems",
        "unit": "Unit I",
        "topic": "Process",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "process, process state, PCB, ready, running, blocked"
    },

    {
        "title": "OS - FCFS Scheduling",
        "content": """First Come First Serve schedules processes in arrival order and is generally non-preemptive.

Important formulas:
Turnaround Time = Completion Time - Arrival Time
Waiting Time = Turnaround Time - Burst Time""",
        "subject": "Operating Systems",
        "unit": "Unit I",
        "topic": "Scheduling",
        "category": "Numerical Problem",
        "difficulty": "Medium",
        "keywords": "FCFS, scheduling, completion time, turnaround time, waiting time"
    },

    {
        "title": "OS - SJF and SRTF Scheduling",
        "content": """SJF chooses the shortest burst among available processes in the non-preemptive version.

SRTF is the preemptive version and may switch to a newly arrived process with a shorter remaining time.""",
        "subject": "Operating Systems",
        "unit": "Unit I",
        "topic": "Scheduling",
        "category": "Numerical Problem",
        "difficulty": "Hard",
        "keywords": "SJF, SRTF, shortest job first, preemptive, non preemptive"
    },

    {
        "title": "OS - Round Robin Scheduling",
        "content": """Round Robin gives each ready process a fixed time quantum.

If the process does not finish within that quantum, it is moved to the back of the ready queue.""",
        "subject": "Operating Systems",
        "unit": "Unit I",
        "topic": "Scheduling",
        "category": "Numerical Problem",
        "difficulty": "Medium",
        "keywords": "Round Robin, time quantum, ready queue, preemptive"
    },

    {
        "title": "OS - Inter Process Communication",
        "content": """IPC provides ways for processes to exchange information and coordinate execution.

Common mechanisms include:
shared memory
message passing""",
        "subject": "Operating Systems",
        "unit": "Unit II",
        "topic": "IPC",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "IPC, inter process communication, shared memory, message passing"
    },

    {
        "title": "OS - Critical Section and Race Condition",
        "content": """A race condition occurs when concurrent execution allows the result to depend on timing.

The critical-section problem requires:
mutual exclusion
progress
bounded waiting""",
        "subject": "Operating Systems",
        "unit": "Unit II",
        "topic": "Synchronization",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "critical section, race condition, mutual exclusion, synchronization"
    },

    {
        "title": "OS - Semaphores",
        "content": """A semaphore is a synchronization primitive commonly supporting wait/P and signal/V operations.

Binary semaphores can help provide mutual exclusion.
Counting semaphores can manage multiple resource instances.""",
        "subject": "Operating Systems",
        "unit": "Unit II",
        "topic": "Semaphores",
        "category": "Viva Question",
        "difficulty": "Medium",
        "keywords": "semaphore, wait, signal, synchronization, mutex"
    },

    {
        "title": "OS - Producer Consumer and Reader Writer",
        "content": """Producer-consumer coordinates producers and consumers sharing a bounded buffer.

Reader-writer problems coordinate concurrent readers and writers accessing shared data.

Synchronization mechanisms are used to prevent inconsistent state.""",
        "subject": "Operating Systems",
        "unit": "Unit II",
        "topic": "Classic Problems",
        "category": "Important Question",
        "difficulty": "Hard",
        "keywords": "producer consumer, reader writer, synchronization, semaphore"
    },

    {
        "title": "OS - Deadlock Conditions",
        "content": """The four necessary conditions for deadlock are:
1. Mutual Exclusion
2. Hold and Wait
3. No Preemption
4. Circular Wait

Breaking one of these conditions is part of deadlock prevention.""",
        "subject": "Operating Systems",
        "unit": "Unit II",
        "topic": "Deadlock",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "deadlock, mutual exclusion, hold and wait, no preemption, circular wait"
    },

    {
        "title": "OS - Banker's Algorithm",
        "content": """Banker's algorithm is a deadlock-avoidance method.

It checks whether granting a request would leave the system in a safe state.

A safe sequence provides an ordering in which all processes can complete under the model assumptions.""",
        "subject": "Operating Systems",
        "unit": "Unit II",
        "topic": "Deadlock",
        "category": "Numerical Problem",
        "difficulty": "Hard",
        "keywords": "Banker algorithm, safe state, safe sequence, deadlock avoidance"
    },

    {
        "title": "OS - Memory Management",
        "content": """Memory management keeps track of memory usage and allocates memory to processes.

Important concepts:
contiguous allocation
paging
segmentation
virtual memory
page replacement""",
        "subject": "Operating Systems",
        "unit": "Unit III",
        "topic": "Memory",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "memory management, paging, segmentation, virtual memory"
    },

    {
        "title": "OS - Paging and Page Fault",
        "content": """Paging divides logical memory into fixed-size pages and physical memory into frames.

A page fault occurs when a referenced page is not currently in physical memory and must be loaded.""",
        "subject": "Operating Systems",
        "unit": "Unit III",
        "topic": "Virtual Memory",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "paging, page, frame, page fault, virtual memory"
    },

    {
        "title": "OS - FIFO and LRU Page Replacement",
        "content": """Page replacement chooses which page to remove when a new page must be loaded.

FIFO replaces the oldest page.
LRU replaces the page that has not been used for the longest time.""",
        "subject": "Operating Systems",
        "unit": "Unit III",
        "topic": "Page Replacement",
        "category": "Numerical Problem",
        "difficulty": "Hard",
        "keywords": "page replacement, FIFO, LRU, page fault"
    },

    # =========================
    # CS CORE — DBMS
    # =========================

    {
        "title": "DBMS - Database Schema and Instance",
        "content": """A database is an organized collection of related data.

A schema describes the structure of the database.

An instance is the actual data stored at a particular time.""",
        "subject": "DBMS",
        "unit": "Unit I",
        "topic": "Database Concepts",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "database, schema, instance, DBMS"
    },

    {
        "title": "DBMS - Primary Candidate Foreign and Composite Keys",
        "content": """A candidate key can uniquely identify a row.
The primary key is the selected candidate key used as the main identifier.
A foreign key references a key in another table.
A composite key uses multiple attributes together.""",
        "subject": "DBMS",
        "unit": "Unit II",
        "topic": "Keys",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "primary key, candidate key, foreign key, composite key"
    },

    {
        "title": "DBMS - SELECT INSERT UPDATE DELETE",
        "content": """SELECT retrieves rows.
INSERT adds rows.
UPDATE changes existing rows.
DELETE removes rows.
WHERE restricts affected or returned rows.""",
        "subject": "DBMS",
        "unit": "Unit III",
        "topic": "SQL",
        "category": "Practical Tip",
        "difficulty": "Easy",
        "keywords": "SQL, SELECT, INSERT, UPDATE, DELETE, WHERE"
    },

    {
        "title": "DBMS - 1NF 2NF and 3NF",
        "content": """Normalization reduces redundancy and update anomalies.

1NF requires atomic values and removes repeating groups.
2NF removes partial dependency on a composite key.
3NF removes transitive dependency under the standard formulation.""",
        "subject": "DBMS",
        "unit": "Unit IV",
        "topic": "Normalization",
        "category": "Important Question",
        "difficulty": "Hard",
        "keywords": "normalization, 1NF, 2NF, 3NF, dependency"
    },

    {
        "title": "DBMS - ACID Properties",
        "content": """Transactions should satisfy ACID properties:

Atomicity
Consistency
Isolation
Durability

These properties support reliable database operations.""",
        "subject": "DBMS",
        "unit": "Unit V",
        "topic": "Transactions",
        "category": "Viva Question",
        "difficulty": "Medium",
        "keywords": "transaction, ACID, atomicity, consistency, isolation, durability"
    },

    # =========================
    # CS CORE — COMPUTER NETWORKS
    # =========================

    {
        "title": "CN - Seven OSI Layers",
        "content": """The OSI model contains seven layers:

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application""",
        "subject": "Computer Networks",
        "unit": "Unit I",
        "topic": "OSI Model",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "OSI, physical, data link, network, transport, application"
    },

    {
        "title": "CN - TCP vs UDP",
        "content": """TCP is connection-oriented and focuses on reliable ordered delivery.

UDP is connectionless with lower overhead and does not provide the same delivery guarantees.""",
        "subject": "Computer Networks",
        "unit": "Unit II",
        "topic": "TCP/IP",
        "category": "Viva Question",
        "difficulty": "Medium",
        "keywords": "TCP, UDP, transport layer, reliable"
    },

    {
        "title": "CN - IPv4 and IPv6",
        "content": """IPv4 addresses are 32 bits.
IPv6 addresses are 128 bits.

IPv6 provides a much larger address space and other protocol improvements.""",
        "subject": "Computer Networks",
        "unit": "Unit III",
        "topic": "IP",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "IPv4, IPv6, IP address, network"
    },

    {
        "title": "CN - Routing and Routers",
        "content": """Routers forward packets between networks using routing information.

Routing can use static or dynamic approaches.

The network layer is responsible for logical addressing and routing.""",
        "subject": "Computer Networks",
        "unit": "Unit IV",
        "topic": "Routing",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "router, routing, packets, network layer"
    },

    {
        "title": "CN - Basic Network Security",
        "content": """Basic network security concepts include:
authentication
confidentiality
integrity
availability
encryption
access control

Common threats include phishing, malware, spoofing and denial-of-service attacks.""",
        "subject": "Computer Networks",
        "unit": "Unit V",
        "topic": "Security",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "network security, authentication, encryption, CIA, attacks"
    },

    # =========================
    # COMPUTER FUNDAMENTALS
    # =========================

    {
        "title": "CF - CPU ALU Control Unit and Registers",
        "content": """The CPU executes instructions.
The ALU performs arithmetic and logical operations.
The Control Unit directs instruction execution.
Registers provide very fast temporary storage inside the processor.""",
        "subject": "Computer Fundamentals",
        "unit": "Unit I",
        "topic": "Computer Organization",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "CPU, ALU, control unit, registers"
    },

    {
        "title": "CF - RAM ROM and Cache",
        "content": """RAM is volatile working memory.
ROM is generally non-volatile.
Cache is small and fast memory used to reduce average memory-access time by keeping frequently used data and instructions closer to the CPU.""",
        "subject": "Computer Fundamentals",
        "unit": "Unit II",
        "topic": "Memory",
        "category": "Viva Question",
        "difficulty": "Easy",
        "keywords": "RAM, ROM, cache, memory"
    },

    {
        "title": "CF - Number Systems",
        "content": """Binary is base 2.
Octal is base 8.
Decimal is base 10.
Hexadecimal is base 16.

Number-system conversion is fundamental in computer representation.""",
        "subject": "Computer Fundamentals",
        "unit": "Unit III",
        "topic": "Number Systems",
        "category": "Numerical Problem",
        "difficulty": "Medium",
        "keywords": "binary, decimal, octal, hexadecimal, number system"
    },

    {
        "title": "CF - Logic Gates and Boolean Algebra",
        "content": """Basic logic gates include AND, OR and NOT.

Derived gates include:
NAND
NOR
XOR
XNOR

Boolean algebra provides laws for simplifying logical expressions.""",
        "subject": "Computer Fundamentals",
        "unit": "Unit IV",
        "topic": "Digital Logic",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "logic gates, Boolean algebra, NAND, NOR, XOR, XNOR"
    },

    {
        "title": "CF - Authentication and Access Control",
        "content": """Authentication verifies identity.

Authorization determines what an authenticated user is allowed to do.

Strong passwords, multi-factor authentication and least privilege improve security.""",
        "subject": "Computer Fundamentals",
        "unit": "Unit V",
        "topic": "Computer Security",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "authentication, authorization, access control, security"
    },
]


def seed_knowledge():
    init_database()

    connection = get_connection()

    inserted = 0
    skipped = 0

    for item in KNOWLEDGE:

        existing = connection.execute(
            """
            SELECT id
            FROM knowledge
            WHERE title = ? AND subject = ?
            LIMIT 1
            """,
            (
                item["title"],
                item["subject"]
            )
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
                item["title"],
                item["content"],
                item["subject"],
                item["unit"],
                item["topic"],
                item["category"],
                item["difficulty"],
                item["keywords"],
                AUTHOR
            )
        )

        inserted += 1

    connection.commit()
    connection.close()

    print("==============================================")
    print("EchoMind Full Junior Knowledge Pack")
    print("==============================================")
    print("New entries inserted :", inserted)
    print("Existing entries     :", skipped)
    print("Pack entries         :", len(KNOWLEDGE))
    print("==============================================")


if __name__ == "__main__":
    seed_knowledge()