import sqlite3

from database import get_connection


SE_KNOWLEDGE = [

    # ============================================================
    # UNIT I — INTRODUCTION TO SOFTWARE ENGINEERING
    # ============================================================

    {
        "title": "What is Software?",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Software",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software definition program data documentation",
        "content": """
Software is a collection of programs, procedures, data, and related documentation
that instructs a computer system to perform specific tasks.

Software is different from hardware because software is intangible and can be
modified, copied, and maintained without physically changing computer components.
"""
    },

    {
        "title": "What is Software Engineering?",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Software Engineering",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software engineering definition engineering principles development",
        "content": """
Software engineering is the systematic, disciplined, and measurable application
of engineering principles to the development, operation, maintenance, and testing
of software.

Its goal is to produce reliable, maintainable, efficient, and high-quality
software within required time and cost constraints.
"""
    },

    {
        "title": "Characteristics of Software",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Software Characteristics",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software characteristics intangible engineered maintenance",
        "content": """
Important characteristics of software include:

1. Software is developed or engineered rather than manufactured.
2. Software does not physically wear out like hardware.
3. Software is intangible.
4. Most software is custom-built or highly configurable.
5. Software maintenance can continuously change and improve the system.
6. Software complexity can increase as features are added.
"""
    },

    {
        "title": "Software Crisis",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Software Crisis",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "software crisis cost schedule quality failure complexity",
        "content": """
Software crisis refers to the problems experienced in software development when
software projects became increasingly large and complex.

Common problems include:
- Cost overruns
- Schedule delays
- Poor quality
- Difficult maintenance
- Unreliable software
- Increasing complexity
- Failure to satisfy user requirements

Software engineering practices were developed to address these problems.
"""
    },

    {
        "title": "Need for Software Engineering",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Need for Software Engineering",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "need importance software engineering quality cost maintenance",
        "content": """
Software engineering is needed to manage large and complex software projects.

It helps organizations:
- Develop reliable software
- Control project cost
- Meet deadlines
- Manage complexity
- Improve software quality
- Reduce development risks
- Make maintenance easier
- Satisfy customer requirements
"""
    },

    {
        "title": "Software Engineering Layers",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Software Engineering Layers",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "quality process methods tools software engineering layers",
        "content": """
Software engineering can be viewed as a layered technology.

The major layers are:

1. Quality focus
2. Process
3. Methods
4. Tools

Quality focus provides the foundation. Process provides the framework for
development. Methods provide technical procedures for building software.
Tools provide automated or semi-automated support for the process and methods.
"""
    },

    {
        "title": "Software Process",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Software Process",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software process activities development framework",
        "content": """
A software process is a structured set of activities used to develop, deliver,
and maintain software.

Common activities include:
- Communication
- Planning
- Modeling
- Construction
- Deployment

A defined process helps developers organize work and control project progress.
"""
    },

    {
        "title": "Generic Software Process Framework",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Generic Process Framework",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "communication planning modeling construction deployment framework",
        "content": """
The generic software process framework contains five major activities:

1. Communication — understand customer requirements.
2. Planning — estimate resources, cost, schedule, and risks.
3. Modeling — analyze requirements and design the software.
4. Construction — coding and testing.
5. Deployment — deliver the software and collect customer feedback.
"""
    },

    # ============================================================
    # SOFTWARE PROCESS MODELS
    # ============================================================

    {
        "title": "Waterfall Model",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Waterfall Model",
        "category": "Process Model",
        "difficulty": "Easy",
        "keywords": "waterfall sequential requirements design coding testing deployment",
        "content": """
The Waterfall model is a sequential software development model.

Typical phases are:

Requirements → Design → Implementation → Testing → Deployment → Maintenance

Each phase is generally completed before the next phase begins.

Advantages:
- Simple and easy to understand
- Clear documentation
- Easy project management

Disadvantages:
- Difficult to accommodate changing requirements
- Customer feedback comes late
- Working software is delivered relatively late
"""
    },

    {
        "title": "Incremental Model",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Incremental Model",
        "category": "Process Model",
        "difficulty": "Medium",
        "keywords": "incremental development iterations product increments",
        "content": """
The Incremental model develops software through multiple increments.

Each increment adds useful functionality to the previous version.

Advantages:
- Early delivery of useful software
- Easier testing
- Customer feedback can influence later increments
- Lower risk compared with a single large delivery

Disadvantage:
The system must be designed carefully so that increments can be integrated.
"""
    },

    {
        "title": "Prototyping Model",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Prototyping Model",
        "category": "Process Model",
        "difficulty": "Medium",
        "keywords": "prototype requirements customer feedback",
        "content": """
The Prototyping model creates an early working model of the software to
understand unclear or changing requirements.

Basic process:

Requirements → Quick Design → Prototype → Customer Evaluation → Refinement

It is especially useful when customers cannot clearly describe their requirements.
"""
    },

    {
        "title": "Spiral Model",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Spiral Model",
        "category": "Process Model",
        "difficulty": "Medium",
        "keywords": "spiral model risk analysis iterative development",
        "content": """
The Spiral model is an iterative software process model that strongly emphasizes
risk analysis.

Each spiral cycle generally involves:
1. Planning
2. Risk analysis
3. Engineering/development
4. Customer evaluation

The model is suitable for large, complex, and high-risk projects.

Its main disadvantage is that it can be expensive and requires expertise in
risk assessment.
"""
    },

    {
        "title": "Agile Model",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Agile Model",
        "category": "Process Model",
        "difficulty": "Medium",
        "keywords": "agile iterative incremental customer collaboration flexibility",
        "content": """
Agile software development emphasizes iterative development, customer
collaboration, frequent delivery, and responding to changing requirements.

Important Agile ideas include:
- Frequent working software
- Continuous customer feedback
- Small iterations
- Team collaboration
- Adaptation to changing requirements

Agile is useful when requirements are expected to change frequently.
"""
    },

    # ============================================================
    # UNIT II — REQUIREMENTS ENGINEERING
    # ============================================================

    {
        "title": "Requirements Engineering",
        "subject": "Software Engineering",
        "unit": "Unit II",
        "topic": "Requirements Engineering",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "requirements engineering elicitation analysis specification validation",
        "content": """
Requirements engineering is the systematic process of discovering, documenting,
analyzing, validating, and managing what users and stakeholders expect from
a software system.

Major activities include:
- Requirements elicitation
- Requirements analysis
- Requirements specification
- Requirements validation
- Requirements management
"""
    },

    {
        "title": "Functional Requirements",
        "subject": "Software Engineering",
        "unit": "Unit II",
        "topic": "Functional Requirements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "functional requirements system functions behavior services",
        "content": """
Functional requirements describe what a software system must do.

Examples:
- User can log in.
- System can calculate marks.
- User can search products.
- Administrator can add or delete users.

They describe required services, inputs, outputs, and system behavior.
"""
    },

    {
        "title": "Non-Functional Requirements",
        "subject": "Software Engineering",
        "unit": "Unit II",
        "topic": "Non-Functional Requirements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "non functional requirements performance security reliability usability",
        "content": """
Non-functional requirements describe constraints and quality attributes of a
software system rather than specific functions.

Examples include:
- Performance
- Security
- Reliability
- Usability
- Scalability
- Availability
- Maintainability

Example:
The system should respond to a request within two seconds.
"""
    },

    {
        "title": "Requirements Elicitation",
        "subject": "Software Engineering",
        "unit": "Unit II",
        "topic": "Requirements Elicitation",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "elicitation interview questionnaire observation stakeholder requirements",
        "content": """
Requirements elicitation is the process of collecting requirements from
customers, users, and other stakeholders.

Common techniques include:
- Interviews
- Questionnaires
- Observation
- Workshops
- Brainstorming
- Document analysis
- Prototyping

The objective is to understand the real needs of stakeholders.
"""
    },

    {
        "title": "Requirements Analysis",
        "subject": "Software Engineering",
        "unit": "Unit II",
        "topic": "Requirements Analysis",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "requirements analysis conflicts feasibility prioritization",
        "content": """
Requirements analysis examines collected requirements to identify ambiguity,
conflicts, missing information, feasibility issues, and priorities.

The goal is to transform raw stakeholder requirements into clear, consistent,
complete, and feasible requirements.
"""
    },

    {
        "title": "What is SRS?",
        "subject": "Software Engineering",
        "unit": "Unit II",
        "topic": "SRS",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "SRS software requirements specification document",
        "content": """
SRS stands for Software Requirements Specification.

An SRS is a formal document that describes the functional and non-functional
requirements of a software system.

It acts as an agreement between stakeholders and the development team and
provides a basis for design, development, testing, and maintenance.
"""
    },

    {
        "title": "Characteristics of Good SRS",
        "subject": "Software Engineering",
        "unit": "Unit II",
        "topic": "SRS Characteristics",
        "category": "Exam Important",
        "difficulty": "Medium",
        "keywords": "SRS characteristics correct complete consistent unambiguous verifiable",
        "content": """
A good SRS should be:

1. Correct
2. Unambiguous
3. Complete
4. Consistent
5. Verifiable
6. Modifiable
7. Traceable
8. Prioritized

These characteristics improve communication between customers, developers,
testers, and other stakeholders.
"""
    },

    {
        "title": "Requirements Validation",
        "subject": "Software Engineering",
        "unit": "Unit II",
        "topic": "Requirements Validation",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "requirements validation errors consistency completeness feasibility",
        "content": """
Requirements validation checks whether documented requirements correctly
represent the needs of stakeholders.

Validation checks include:
- Validity
- Consistency
- Completeness
- Realism or feasibility
- Verifiability

The purpose is to find requirement errors before software development becomes
expensive.
"""
    },

    {
        "title": "Requirements Management",
        "subject": "Software Engineering",
        "unit": "Unit II",
        "topic": "Requirements Management",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "requirements management change control traceability version",
        "content": """
Requirements management is the process of controlling and tracking requirements
throughout the software lifecycle.

It deals with:
- Requirement changes
- Version control
- Requirement priorities
- Traceability
- Impact analysis
- Stakeholder communication
"""
    },

    # ============================================================
    # UNIT III — SOFTWARE DESIGN
    # ============================================================

    {
        "title": "Software Design",
        "subject": "Software Engineering",
        "unit": "Unit III",
        "topic": "Software Design",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software design architecture modules interfaces data",
        "content": """
Software design converts analyzed requirements into a blueprint for constructing
the software.

It identifies:
- Software architecture
- Modules/components
- Data structures
- Interfaces
- Relationships between components

Good design improves maintainability, reliability, and understandability.
"""
    },

    {
        "title": "Modularity",
        "subject": "Software Engineering",
        "unit": "Unit III",
        "topic": "Modularity",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "modularity modules decomposition software design",
        "content": """
Modularity is the division of a software system into smaller independent
modules.

A module performs a specific responsibility.

Benefits:
- Easier understanding
- Easier testing
- Easier maintenance
- Reusability
- Reduced complexity
"""
    },

    {
        "title": "Cohesion",
        "subject": "Software Engineering",
        "unit": "Unit III",
        "topic": "Cohesion",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "cohesion module functional cohesion software design",
        "content": """
Cohesion measures how strongly the responsibilities inside a module are related.

High cohesion is desirable because a highly cohesive module focuses on a small,
well-defined responsibility.

Generally, functional cohesion is considered stronger than weaker forms such
as coincidental cohesion.
"""
    },

    {
        "title": "Coupling",
        "subject": "Software Engineering",
        "unit": "Unit III",
        "topic": "Coupling",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "coupling modules dependency software design",
        "content": """
Coupling measures the degree of dependency between software modules.

Low coupling is desirable because changes in one module are less likely to
cause problems in other modules.

Good software design generally aims for:
High cohesion + Low coupling.
"""
    },

    {
        "title": "Software Architecture",
        "subject": "Software Engineering",
        "unit": "Unit III",
        "topic": "Software Architecture",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "software architecture components connectors system structure",
        "content": """
Software architecture describes the high-level structure of a software system.

It identifies major components, their responsibilities, relationships, and
communication mechanisms.

Architecture helps developers reason about system organization, scalability,
performance, and maintainability.
"""
    },

    {
        "title": "Data Design",
        "subject": "Software Engineering",
        "unit": "Unit III",
        "topic": "Data Design",
        "category": "Design",
        "difficulty": "Medium",
        "keywords": "data design database data structures software",
        "content": """
Data design defines how data is organized, stored, accessed, and managed by
the software system.

It may involve:
- Data structures
- Database schemas
- Data relationships
- Data storage
- Data access methods

Good data design improves consistency, performance, and maintainability.
"""
    },

    {
        "title": "Interface Design",
        "subject": "Software Engineering",
        "unit": "Unit III",
        "topic": "Interface Design",
        "category": "Design",
        "difficulty": "Medium",
        "keywords": "interface design user interface module interface API",
        "content": """
Interface design defines how users and software components interact with
the system.

It may include:
- User interface
- Module interfaces
- External system interfaces
- APIs

A good interface should be understandable, consistent, and easy to use.
"""
    },

    {
        "title": "UML",
        "subject": "Software Engineering",
        "unit": "Unit III",
        "topic": "UML",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "UML unified modeling language software diagrams",
        "content": """
UML stands for Unified Modeling Language.

It is a standard visual modeling language used to represent, design, and
document software systems.

UML provides diagrams such as:
- Use Case Diagram
- Class Diagram
- Sequence Diagram
- Activity Diagram
- State Diagram
"""
    },

    {
        "title": "Use Case Diagram",
        "subject": "Software Engineering",
        "unit": "Unit III",
        "topic": "Use Case Diagram",
        "category": "UML",
        "difficulty": "Easy",
        "keywords": "use case actor system UML interaction requirements",
        "content": """
A Use Case Diagram represents interactions between users or external systems
and a software system.

Main elements:
- Actor
- Use case
- System boundary
- Relationships

An actor represents an external entity interacting with the system.
A use case represents a function or service provided by the system.
"""
    },

    # ============================================================
    # UNIT IV — SOFTWARE TESTING
    # ============================================================

    {
        "title": "Software Testing",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Software Testing",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software testing defects errors quality testing",
        "content": """
Software testing is the process of evaluating software to find defects and
verify that it satisfies specified requirements.

Testing helps improve confidence in software quality and can reveal incorrect
behavior before or after deployment.
"""
    },

    {
        "title": "Verification and Validation",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Verification and Validation",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "verification validation V and V software testing",
        "content": """
Verification asks whether the software is being built correctly according to
specified requirements and design.

Validation asks whether the correct software is being built for the user's
actual needs.

Simple distinction:
Verification → Are we building the product right?
Validation → Are we building the right product?
"""
    },

    {
        "title": "Unit Testing",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Unit Testing",
        "category": "Testing",
        "difficulty": "Easy",
        "keywords": "unit testing individual module component",
        "content": """
Unit testing tests individual modules or components of a software system.

The objective is to verify that each small unit works correctly in isolation
before it is combined with other components.
"""
    },

    {
        "title": "Integration Testing",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Integration Testing",
        "category": "Testing",
        "difficulty": "Easy",
        "keywords": "integration testing modules interfaces components",
        "content": """
Integration testing combines individual modules and tests their interactions.

Its main purpose is to discover problems in communication and interfaces
between integrated components.
"""
    },

    {
        "title": "System Testing",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "System Testing",
        "category": "Testing",
        "difficulty": "Easy",
        "keywords": "system testing complete software system",
        "content": """
System testing evaluates the complete integrated software system.

It checks whether the complete system satisfies specified functional and
non-functional requirements.
"""
    },

    {
        "title": "Acceptance Testing",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Acceptance Testing",
        "category": "Testing",
        "difficulty": "Easy",
        "keywords": "acceptance testing customer user requirements",
        "content": """
Acceptance testing determines whether the software is acceptable to the
customer or intended users.

It is performed against customer requirements and business needs before
final acceptance or deployment.
"""
    },

    {
        "title": "Black Box Testing",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Black Box Testing",
        "category": "Testing",
        "difficulty": "Medium",
        "keywords": "black box testing input output functionality",
        "content": """
Black-box testing tests software functionality without requiring knowledge
of the internal implementation or source code.

The tester focuses on inputs, outputs, and externally observable behavior.
"""
    },

    {
        "title": "White Box Testing",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "White Box Testing",
        "category": "Testing",
        "difficulty": "Medium",
        "keywords": "white box testing source code paths logic coverage",
        "content": """
White-box testing uses knowledge of the internal structure and source code.

It can test:
- Statements
- Branches
- Conditions
- Paths
- Internal logic

The goal is to increase structural coverage and find implementation defects.
"""
    },

    # ============================================================
    # SOFTWARE MAINTENANCE
    # ============================================================

    {
        "title": "Software Maintenance",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Software Maintenance",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software maintenance modification post deployment",
        "content": """
Software maintenance is the modification of software after delivery to correct
faults, adapt to environmental changes, improve functionality, or prevent
future problems.
"""
    },

    {
        "title": "Corrective Maintenance",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Corrective Maintenance",
        "category": "Maintenance",
        "difficulty": "Easy",
        "keywords": "corrective maintenance bugs faults errors",
        "content": """
Corrective maintenance fixes defects, bugs, errors, or failures discovered
after software has been delivered.

Example:
Fixing a login error that prevents valid users from signing in.
"""
    },

    {
        "title": "Adaptive Maintenance",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Adaptive Maintenance",
        "category": "Maintenance",
        "difficulty": "Easy",
        "keywords": "adaptive maintenance operating system environment hardware",
        "content": """
Adaptive maintenance modifies software so that it continues to operate in
a changed environment.

Examples:
- Supporting a new operating system
- Adapting to new hardware
- Supporting a changed database platform
- Adapting to new external regulations
"""
    },

    {
        "title": "Perfective Maintenance",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Perfective Maintenance",
        "category": "Maintenance",
        "difficulty": "Easy",
        "keywords": "perfective maintenance enhancement performance usability features",
        "content": """
Perfective maintenance improves or enhances software after delivery.

Examples include:
- Improving performance
- Improving usability
- Adding useful features
- Improving maintainability
"""
    },

    {
        "title": "Preventive Maintenance",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Preventive Maintenance",
        "category": "Maintenance",
        "difficulty": "Easy",
        "keywords": "preventive maintenance future problems refactoring reliability",
        "content": """
Preventive maintenance modifies software to reduce the possibility of future
failures and make future maintenance easier.

Examples include code refactoring, improving documentation, and restructuring
poorly designed components.
"""
    },

    # ============================================================
    # EXAM / REVISION KNOWLEDGE
    # ============================================================

    {
        "title": "Cohesion vs Coupling",
        "subject": "Software Engineering",
        "unit": "Unit III",
        "topic": "Cohesion and Coupling",
        "category": "Exam Important",
        "difficulty": "Medium",
        "keywords": "cohesion coupling difference high low design",
        "content": """
Cohesion measures how closely related the responsibilities inside one module are.

Coupling measures how strongly one module depends on another.

Good software design generally aims for:
- High cohesion
- Low coupling

High cohesion makes modules focused and easier to understand.
Low coupling reduces dependencies and makes changes safer.
"""
    },

    {
        "title": "Software Testing Levels",
        "subject": "Software Engineering",
        "unit": "Unit IV",
        "topic": "Testing Levels",
        "category": "Exam Important",
        "difficulty": "Medium",
        "keywords": "unit integration system acceptance testing levels",
        "content": """
The common levels of software testing are:

1. Unit Testing — tests individual components.
2. Integration Testing — tests interactions between components.
3. System Testing — tests the complete integrated system.
4. Acceptance Testing — checks whether the system satisfies customer needs.

Testing usually progresses from smaller components toward the complete system.
"""
    },

    {
        "title": "Software Process Model Comparison",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Process Model Comparison",
        "category": "Exam Important",
        "difficulty": "Medium",
        "keywords": "waterfall incremental spiral prototype agile comparison",
        "content": """
Waterfall is sequential and works better when requirements are stable.

Incremental development delivers the system in multiple increments.

Prototyping is useful when requirements are unclear.

Spiral emphasizes risk analysis and is suitable for large high-risk projects.

Agile emphasizes short iterations, customer collaboration, frequent delivery,
and adaptation to changing requirements.
"""
    },

    {
        "title": "Software Engineering Exam Strategy",
        "subject": "Software Engineering",
        "unit": "Unit I",
        "topic": "Exam Strategy",
        "category": "Exam Strategy",
        "difficulty": "Easy",
        "keywords": "software engineering exam important questions revision",
        "content": """
Important Software Engineering topics for revision include:

1. Software engineering definition
2. Software crisis
3. Software engineering layers
4. Waterfall model
5. Incremental model
6. Prototyping model
7. Spiral model
8. Agile model
9. Functional and non-functional requirements
10. SRS
11. Requirements validation
12. Cohesion and coupling
13. UML
14. Use case diagrams
15. Verification and validation
16. Testing levels
17. Black-box and white-box testing
18. Software maintenance
19. Corrective, adaptive, perfective, and preventive maintenance
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

    for item in SE_KNOWLEDGE:

        if add_knowledge(item):
            added += 1
        else:
            skipped += 1

    print("=" * 60)
    print("EchoMind Software Engineering Knowledge Seed")
    print("=" * 60)
    print(f"Added:   {added}")
    print(f"Skipped: {skipped}")
    print(f"Total entries in seed: {len(SE_KNOWLEDGE)}")
    print("=" * 60)


if __name__ == "__main__":
    main()