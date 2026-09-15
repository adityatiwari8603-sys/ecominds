import sqlite3

DATABASE_NAME = "ecomind.db"


SOFTWARE_ENGINEERING_KNOWLEDGE = [

    # ============================================================
    # UNIT I — SOFTWARE ENGINEERING BASICS
    # ============================================================

    {
        "title": "What is Software Engineering?",
        "content": "Software engineering is the systematic, disciplined and measurable approach to the development, operation, maintenance and evolution of software. It applies engineering principles to software development so that software is reliable, maintainable, efficient and meets user requirements.",
        "unit": "Unit I",
        "topic": "Software Engineering Basics",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software engineering, definition, systematic, disciplined, measurable, software development"
    },

    {
        "title": "Software",
        "content": "Software is a collection of programs, procedures, data and related documentation that instructs a computer system to perform specific tasks. Software can be broadly classified as system software, application software and embedded software.",
        "unit": "Unit I",
        "topic": "Software Engineering Basics",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software, program, application, system software, embedded software"
    },

    {
        "title": "Software Characteristics",
        "content": "Important characteristics of software include that it is developed rather than manufactured, it does not physically wear out like hardware, it can become difficult to maintain as changes accumulate, and it is highly dependent on requirements, design and development practices.",
        "unit": "Unit I",
        "topic": "Software Engineering Basics",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software characteristics, developed, manufactured, wear out, maintenance"
    },

    {
        "title": "Software Crisis",
        "content": "Software crisis refers to the difficulties experienced in software development when projects become large and complex. Common problems include late delivery, high cost, unreliable software, difficulty in maintenance and failure to satisfy user requirements. Software engineering practices were developed to address these problems.",
        "unit": "Unit I",
        "topic": "Software Crisis",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "software crisis, cost, delay, failure, maintenance, complexity"
    },

    {
        "title": "Need for Software Engineering",
        "content": "Software engineering is needed to manage increasing software complexity, control development cost and schedule, improve software quality, satisfy user requirements, make software maintainable and provide systematic development practices.",
        "unit": "Unit I",
        "topic": "Software Engineering Basics",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "need, software engineering, quality, cost, schedule, maintenance"
    },

    {
        "title": "Software Engineering Layers",
        "content": "Software engineering can be viewed as a layered technology consisting of quality focus, process, methods and tools. Quality focus provides the foundation, process provides the framework for development, methods provide technical procedures and tools provide automated or semi-automated support.",
        "unit": "Unit I",
        "topic": "Software Engineering Layers",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "layers, quality focus, process, methods, tools"
    },

    {
        "title": "Software Process",
        "content": "A software process is a structured set of activities used to develop, deliver and maintain software. Typical activities include communication, planning, modeling, construction and deployment.",
        "unit": "Unit I",
        "topic": "Software Process",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software process, activities, communication, planning, modeling, construction"
    },

    {
        "title": "Generic Software Process Framework",
        "content": "A generic software process framework commonly includes communication, planning, modeling, construction and deployment activities. Communication focuses on understanding requirements, planning establishes the project plan, modeling develops analysis and design, construction implements and tests the software, and deployment delivers the product and gathers feedback.",
        "unit": "Unit I",
        "topic": "Software Process",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "process framework, communication, planning, modeling, construction, deployment"
    },

    {
        "title": "Software Process Models",
        "content": "Software process models describe how software development activities are organized. Common models include Waterfall, Incremental, Prototyping, Spiral and Agile approaches. The appropriate model depends on project requirements, risk, customer involvement and development constraints.",
        "unit": "Unit I",
        "topic": "Software Process Models",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "process model, waterfall, incremental, prototype, spiral, agile"
    },

    {
        "title": "Waterfall Model",
        "content": "The Waterfall model is a sequential software development model in which development progresses through phases such as requirements, design, implementation, testing, deployment and maintenance. A phase generally completes before the next phase begins.",
        "unit": "Unit I",
        "topic": "Waterfall Model",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "waterfall, sequential model, requirements, design, implementation, testing"
    },

    {
        "title": "Waterfall Model Advantages",
        "content": "Advantages of the Waterfall model include simple structure, clearly defined phases, easy project planning and documentation, and clearly defined milestones. It can work well when requirements are stable and well understood.",
        "unit": "Unit I",
        "topic": "Waterfall Model",
        "category": "Exam Tip",
        "difficulty": "Easy",
        "keywords": "waterfall advantages, planning, documentation, stable requirements"
    },

    {
        "title": "Waterfall Model Limitations",
        "content": "Limitations of the Waterfall model include difficulty accommodating changing requirements, late discovery of problems and limited customer feedback during development. Working software is generally delivered relatively late in the process.",
        "unit": "Unit I",
        "topic": "Waterfall Model",
        "category": "Common Mistake",
        "difficulty": "Medium",
        "keywords": "waterfall limitations, changing requirements, feedback, late testing"
    },

    {
        "title": "Incremental Model",
        "content": "The Incremental model develops software through multiple increments. Each increment adds functionality to the previous release, allowing useful software to be delivered earlier and requirements to be refined over time.",
        "unit": "Unit I",
        "topic": "Incremental Model",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "incremental model, increments, releases, functionality"
    },

    {
        "title": "Prototyping Model",
        "content": "The Prototyping model creates an early working model of the proposed system to understand or validate requirements. Users can interact with the prototype and provide feedback before the final system is developed.",
        "unit": "Unit I",
        "topic": "Prototyping Model",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "prototype, prototyping, requirements, feedback, user"
    },

    {
        "title": "Spiral Model",
        "content": "The Spiral model is a risk-driven software process model that combines iterative development with systematic risk analysis. Each spiral cycle generally involves planning, risk analysis, engineering and evaluation.",
        "unit": "Unit I",
        "topic": "Spiral Model",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "spiral model, risk, iterative, planning, analysis"
    },

    {
        "title": "Agile Software Development",
        "content": "Agile software development is an iterative and incremental approach that emphasizes frequent delivery of working software, customer collaboration, responsiveness to change and continuous feedback.",
        "unit": "Unit I",
        "topic": "Agile Development",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "agile, iterative, incremental, customer collaboration, feedback"
    },

    {
        "title": "Agile Principles",
        "content": "Important Agile ideas include frequent delivery of working software, welcoming changing requirements, close collaboration between developers and stakeholders, continuous attention to technical excellence, simplicity and regular reflection for improvement.",
        "unit": "Unit I",
        "topic": "Agile Development",
        "category": "Exam Tip",
        "difficulty": "Medium",
        "keywords": "agile principles, working software, change, collaboration, simplicity"
    },

    # ============================================================
    # UNIT II — REQUIREMENTS ENGINEERING
    # ============================================================

    {
        "title": "Requirements Engineering",
        "content": "Requirements engineering is the systematic process of discovering, analyzing, documenting, validating and managing the services and constraints required from a software system.",
        "unit": "Unit II",
        "topic": "Requirements Engineering",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "requirements engineering, elicitation, analysis, specification, validation"
    },

    {
        "title": "Functional Requirements",
        "content": "Functional requirements describe what a software system should do. They specify services, system behavior, inputs, outputs and responses to particular situations.",
        "unit": "Unit II",
        "topic": "Functional Requirements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "functional requirement, services, behavior, input, output"
    },

    {
        "title": "Non-Functional Requirements",
        "content": "Non-functional requirements specify constraints and quality attributes of a software system. Examples include performance, security, reliability, usability, availability and maintainability.",
        "unit": "Unit II",
        "topic": "Non-Functional Requirements",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "non functional, performance, security, reliability, usability"
    },

    {
        "title": "Functional vs Non-Functional Requirements",
        "content": "Functional requirements describe what the system does, while non-functional requirements describe constraints or quality attributes under which the system operates. For example, processing a payment is functional, while processing it within a specified response time is non-functional.",
        "unit": "Unit II",
        "topic": "Requirements Engineering",
        "category": "Exam Tip",
        "difficulty": "Easy",
        "keywords": "functional, non-functional, comparison, requirements"
    },

    {
        "title": "Requirements Elicitation",
        "content": "Requirements elicitation is the process of collecting requirements from stakeholders and other sources. Techniques include interviews, questionnaires, observation, workshops, document analysis and prototyping.",
        "unit": "Unit II",
        "topic": "Requirements Elicitation",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "elicitation, interviews, questionnaires, observation, stakeholders"
    },

    {
        "title": "Requirements Analysis",
        "content": "Requirements analysis examines collected requirements to identify conflicts, ambiguity, incompleteness, feasibility issues and priorities. The goal is to produce a consistent and understandable set of requirements.",
        "unit": "Unit II",
        "topic": "Requirements Analysis",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "requirements analysis, ambiguity, conflict, feasibility, priority"
    },

    {
        "title": "Software Requirements Specification",
        "content": "Software Requirements Specification (SRS) is a formal document that describes the functional and non-functional requirements of a software system. It provides an agreement between stakeholders and the development team about what the system should provide.",
        "unit": "Unit II",
        "topic": "SRS",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "SRS, software requirements specification, requirements document"
    },

    {
        "title": "Characteristics of Good SRS",
        "content": "A good SRS should be correct, unambiguous, complete, consistent, verifiable, modifiable and traceable. Requirements should be clear enough that developers and testers can understand and verify them.",
        "unit": "Unit II",
        "topic": "SRS",
        "category": "Exam Tip",
        "difficulty": "Medium",
        "keywords": "SRS characteristics, correct, complete, consistent, verifiable, traceable"
    },

    {
        "title": "SRS Common Mistake",
        "content": "A common SRS mistake is using vague words such as fast, easy, user-friendly or efficient without measurable criteria. Requirements should be precise and testable so that their satisfaction can be verified.",
        "unit": "Unit II",
        "topic": "SRS",
        "category": "Common Mistake",
        "difficulty": "Easy",
        "keywords": "SRS mistake, vague requirements, testable, measurable"
    },

    {
        "title": "Requirements Validation",
        "content": "Requirements validation checks whether requirements correctly represent stakeholder needs and are suitable for development. Validation can identify validity, consistency, completeness, realism and verifiability problems.",
        "unit": "Unit II",
        "topic": "Requirements Validation",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "requirements validation, validity, consistency, completeness, verification"
    },

    {
        "title": "Requirements Management",
        "content": "Requirements management deals with identifying, documenting, tracking, prioritizing and controlling changes to requirements throughout the software project.",
        "unit": "Unit II",
        "topic": "Requirements Management",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "requirements management, change, tracking, prioritization"
    },

    # ============================================================
    # UNIT III — SOFTWARE DESIGN
    # ============================================================

    {
        "title": "Software Design",
        "content": "Software design is the process of transforming analyzed requirements into a blueprint for implementation. It defines the architecture, components, interfaces, data structures and interactions of the software.",
        "unit": "Unit III",
        "topic": "Software Design",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software design, architecture, components, interfaces, blueprint"
    },

    {
        "title": "Modularity",
        "content": "Modularity is the division of a software system into smaller, manageable modules. A modular design makes software easier to understand, develop, test, maintain and modify.",
        "unit": "Unit III",
        "topic": "Modularity",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "modularity, modules, design, maintenance"
    },

    {
        "title": "Cohesion",
        "content": "Cohesion measures how closely related the responsibilities within a module are. High cohesion is generally desirable because a highly cohesive module focuses on a well-defined responsibility.",
        "unit": "Unit III",
        "topic": "Cohesion and Coupling",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "cohesion, high cohesion, module, responsibility"
    },

    {
        "title": "Coupling",
        "content": "Coupling measures the degree of interdependence between software modules. Low coupling is generally desirable because modules with fewer dependencies are easier to change, test and maintain.",
        "unit": "Unit III",
        "topic": "Cohesion and Coupling",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "coupling, low coupling, dependency, modules"
    },

    {
        "title": "Cohesion and Coupling Design Principle",
        "content": "A good modular software design generally aims for high cohesion within modules and low coupling between modules. High cohesion keeps related responsibilities together, while low coupling reduces unnecessary dependencies.",
        "unit": "Unit III",
        "topic": "Cohesion and Coupling",
        "category": "Exam Tip",
        "difficulty": "Easy",
        "keywords": "high cohesion, low coupling, modular design"
    },

    {
        "title": "Software Architecture",
        "content": "Software architecture describes the high-level organization of a software system, including major components, their responsibilities and the relationships between them.",
        "unit": "Unit III",
        "topic": "Software Architecture",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "software architecture, components, relationships, structure"
    },

    {
        "title": "Data Design",
        "content": "Data design defines how data is organized, stored, accessed and managed within a software system. It includes designing data structures, databases and relationships required by the application.",
        "unit": "Unit III",
        "topic": "Data Design",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "data design, data structures, database, storage"
    },

    {
        "title": "Interface Design",
        "content": "Interface design defines how software components communicate with one another and how users interact with the software. A good interface should be understandable, consistent and appropriate for its intended users.",
        "unit": "Unit III",
        "topic": "Interface Design",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "interface design, user interface, components, communication"
    },

    {
        "title": "UML",
        "content": "Unified Modeling Language (UML) is a standardized modeling language used to visualize, specify and document software systems. UML provides diagrams for representing structure and behavior.",
        "unit": "Unit III",
        "topic": "UML",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "UML, Unified Modeling Language, modeling, diagrams"
    },

    {
        "title": "Use Case Diagram",
        "content": "A use case diagram represents interactions between external actors and the functions or services provided by a system. Actors represent external entities, while use cases represent system functionality from the user's perspective.",
        "unit": "Unit III",
        "topic": "UML",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "use case, actor, UML, system functionality"
    },

    # ============================================================
    # UNIT IV — TESTING AND MAINTENANCE
    # ============================================================

    {
        "title": "Software Testing",
        "content": "Software testing is the systematic process of evaluating software to find defects and determine whether it satisfies specified requirements. Testing helps improve confidence in software quality.",
        "unit": "Unit IV",
        "topic": "Software Testing",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software testing, defects, requirements, quality"
    },

    {
        "title": "Verification and Validation",
        "content": "Verification asks whether the software is being built correctly according to specifications, while validation asks whether the right software is being built to satisfy user needs.",
        "unit": "Unit IV",
        "topic": "Verification and Validation",
        "category": "Exam Tip",
        "difficulty": "Easy",
        "keywords": "verification, validation, V and V, specifications, user needs"
    },

    {
        "title": "Unit Testing",
        "content": "Unit testing tests individual software units or components in isolation. It is usually performed early in development to detect defects within small pieces of the software.",
        "unit": "Unit IV",
        "topic": "Unit Testing",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "unit testing, component, module, isolation"
    },

    {
        "title": "Integration Testing",
        "content": "Integration testing tests interactions and interfaces between combined software components. Its purpose is to identify defects caused by communication or interaction between modules.",
        "unit": "Unit IV",
        "topic": "Integration Testing",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "integration testing, modules, interfaces, interaction"
    },

    {
        "title": "System Testing",
        "content": "System testing evaluates the complete integrated software system to determine whether it satisfies its specified requirements.",
        "unit": "Unit IV",
        "topic": "System Testing",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "system testing, complete system, requirements"
    },

    {
        "title": "Acceptance Testing",
        "content": "Acceptance testing evaluates whether the software is acceptable to the customer or intended users and whether it meets their specified needs and requirements.",
        "unit": "Unit IV",
        "topic": "Acceptance Testing",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "acceptance testing, customer, user, requirements"
    },

    {
        "title": "Black Box Testing",
        "content": "Black box testing tests software behavior without requiring knowledge of its internal implementation. Test cases are designed from inputs, outputs and specified behavior.",
        "unit": "Unit IV",
        "topic": "Black Box Testing",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "black box, testing, inputs, outputs, behavior"
    },

    {
        "title": "White Box Testing",
        "content": "White box testing uses knowledge of the internal structure and implementation of software to design test cases. It can examine paths, conditions, statements and internal logic.",
        "unit": "Unit IV",
        "topic": "White Box Testing",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "white box, testing, internal logic, paths, conditions"
    },

    {
        "title": "Software Maintenance",
        "content": "Software maintenance is the modification of software after delivery to correct faults, adapt to environmental changes, improve performance or maintainability, or implement new requirements.",
        "unit": "Unit IV",
        "topic": "Software Maintenance",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "software maintenance, modification, faults, adaptation, improvement"
    },

    {
        "title": "Corrective Maintenance",
        "content": "Corrective maintenance modifies software to fix defects or errors discovered after deployment.",
        "unit": "Unit IV",
        "topic": "Software Maintenance",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "corrective maintenance, defects, errors, bugs"
    },

    {
        "title": "Adaptive Maintenance",
        "content": "Adaptive maintenance modifies software so that it continues to operate correctly when its environment changes, such as changes in operating systems, hardware or external interfaces.",
        "unit": "Unit IV",
        "topic": "Software Maintenance",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "adaptive maintenance, environment, operating system, hardware"
    },

    {
        "title": "Perfective Maintenance",
        "content": "Perfective maintenance modifies software to improve performance, usability, maintainability or other desirable characteristics, or to add enhancements based on changed user needs.",
        "unit": "Unit IV",
        "topic": "Software Maintenance",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "perfective maintenance, enhancement, performance, usability"
    },

    {
        "title": "Preventive Maintenance",
        "content": "Preventive maintenance modifies software to improve maintainability and reduce the probability of future failures or maintenance problems.",
        "unit": "Unit IV",
        "topic": "Software Maintenance",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "preventive maintenance, maintainability, future failures"
    },

    # ============================================================
    # EXAM STRATEGY
    # ============================================================

    {
        "title": "Software Engineering Exam Strategy",
        "content": "For Software Engineering theory answers, begin with a clear definition, then explain the concept using important points, and finish with advantages, limitations, comparison or examples only when supported by the question. For process models, draw a simple labeled diagram when appropriate.",
        "unit": "Unit I",
        "topic": "Exam Strategy",
        "category": "Exam Strategy",
        "difficulty": "Easy",
        "keywords": "exam strategy, software engineering, definition, diagram, theory"
    },

    {
        "title": "SRS Exam Strategy",
        "content": "For an SRS question, first define Software Requirements Specification, then explain its purpose and characteristics. Important characteristics include correctness, completeness, consistency, clarity, verifiability and traceability.",
        "unit": "Unit II",
        "topic": "SRS",
        "category": "Exam Strategy",
        "difficulty": "Easy",
        "keywords": "SRS exam, characteristics, answer strategy"
    },

    {
        "title": "Software Process Model Exam Strategy",
        "content": "For a software process model question, write the definition first, draw the model's major stages, explain each stage briefly, and then write suitable advantages and limitations when asked.",
        "unit": "Unit I",
        "topic": "Software Process Models",
        "category": "Exam Strategy",
        "difficulty": "Easy",
        "keywords": "process model exam, diagram, advantages, limitations"
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

    for item in SOFTWARE_ENGINEERING_KNOWLEDGE:

        existing = connection.execute(
            """
            SELECT id
            FROM knowledge
            WHERE title = ?
              AND subject = ?
            """,
            (item["title"], "Software Engineering")
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
                "Software Engineering",
                item["unit"],
                item["topic"],
                item["category"],
                item["difficulty"],
                item["keywords"],
                "EchoMind College Knowledge"
            )
        )

        added += 1

    connection.commit()
    connection.close()

    print(f"Added {added} Software Engineering knowledge entries.")
    print(f"Skipped {skipped} existing Software Engineering entries.")


if __name__ == "__main__":
    seed_database()