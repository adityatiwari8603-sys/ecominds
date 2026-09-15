from database import get_connection


KNOWLEDGE = [

    # ============================================================
    # UNIT I - MULTIVARIABLE DIFFERENTIAL CALCULUS
    # ============================================================

    {
        "title": "Mathematics-III",
        "content": """
Mathematics-III is a Semester 3 mathematics course covering
Multivariable Calculus and Differential Equations.

The MDU syllabus contains four units:
1. Multivariable Differential Calculus
2. Multivariable Integral Calculus
3. Ordinary Differential Equations of First Order
4. Ordinary Differential Equations of Second and Higher Order.
""",
        "unit": "Unit I-IV",
        "topic": "Mathematics-III",
        "category": "Subject Overview",
        "difficulty": "Basic",
        "keywords": "mathematics 3 multivariable calculus differential equations mdu"
    },

    {
        "title": "Limit of a Function of Several Variables",
        "content": """
A limit of a function of several variables describes the value approached
by the function as its variables approach specified values.

For a function f(x,y), the limit as (x,y) approaches (a,b) is written as:

lim f(x,y) = L
as (x,y) -> (a,b).

The limit exists only when the function approaches the same value along
all possible paths approaching the point.
""",
        "unit": "Unit I",
        "topic": "Limits",
        "category": "Concept Explanation",
        "difficulty": "Basic",
        "keywords": "limit multivariable function x y"
    },

    {
        "title": "Continuity of a Function of Several Variables",
        "content": """
A function f(x,y) is continuous at (a,b) if:

1. f(a,b) exists.
2. lim f(x,y) as (x,y) approaches (a,b) exists.
3. The limit equals f(a,b).

Therefore:

lim f(x,y) = f(a,b).

Continuity means that there is no break, jump or discontinuity at the
specified point.
""",
        "unit": "Unit I",
        "topic": "Continuity",
        "category": "Concept Explanation",
        "difficulty": "Basic",
        "keywords": "continuity multivariable function"
    },

    {
        "title": "Partial Derivatives",
        "content": """
Partial differentiation is differentiation of a function of several
variables with respect to one variable while keeping the other variables
constant.

For z = f(x,y):

Partial derivative with respect to x is denoted by ∂z/∂x.

Partial derivative with respect to y is denoted by ∂z/∂y.

Example:

z = x^2 y + y^3

∂z/∂x = 2xy

∂z/∂y = x^2 + 3y^2.
""",
        "unit": "Unit I",
        "topic": "Partial Derivatives",
        "category": "Concept Explanation",
        "difficulty": "Basic",
        "keywords": "partial derivative partial differentiation x y z"
    },

    {
        "title": "Higher Order Partial Derivatives",
        "content": """
Higher order partial derivatives are obtained by differentiating partial
derivatives again.

For z = f(x,y), common second-order derivatives are:

∂²z/∂x²
∂²z/∂y²
∂²z/∂x∂y
∂²z/∂y∂x

Under suitable continuity conditions, mixed partial derivatives are equal:

∂²z/∂x∂y = ∂²z/∂y∂x.
""",
        "unit": "Unit I",
        "topic": "Partial Derivatives",
        "category": "Concept Explanation",
        "difficulty": "Intermediate",
        "keywords": "higher order partial derivative mixed derivative"
    },

    {
        "title": "Homogeneous Function",
        "content": """
A function f(x,y) is homogeneous of degree n if:

f(tx,ty) = t^n f(x,y).

The number n is called the degree of the homogeneous function.

Example:

f(x,y) = x^2 + xy + y^2

is homogeneous of degree 2 because every term has total degree 2.
""",
        "unit": "Unit I",
        "topic": "Homogeneous Functions",
        "category": "Concept Explanation",
        "difficulty": "Intermediate",
        "keywords": "homogeneous function degree"
    },

    {
        "title": "Euler's Theorem for Homogeneous Functions",
        "content": """
If z = f(x,y) is a homogeneous function of degree n, then Euler's theorem
states:

x(∂z/∂x) + y(∂z/∂y) = nz.

For three variables:

x(∂u/∂x) + y(∂u/∂y) + z(∂u/∂z) = nu.

Euler's theorem is useful for verifying and simplifying homogeneous
function problems.
""",
        "unit": "Unit I",
        "topic": "Euler's Theorem",
        "category": "Important Formula",
        "difficulty": "Intermediate",
        "keywords": "Euler theorem homogeneous function"
    },

    {
        "title": "Total Derivative",
        "content": """
A total derivative considers the dependence of a dependent variable on
multiple independent variables.

If z = f(x,y), where x and y depend on another variable t, then:

dz/dt = (∂z/∂x)(dx/dt) + (∂z/∂y)(dy/dt).

Total differentiation is different from partial differentiation because
all variable dependencies are considered.
""",
        "unit": "Unit I",
        "topic": "Total Derivative",
        "category": "Concept Explanation",
        "difficulty": "Intermediate",
        "keywords": "total derivative chain rule multivariable"
    },

    {
        "title": "Maxima and Minima of Functions of Two Variables",
        "content": """
For z = f(x,y), stationary points are generally found by solving:

∂f/∂x = 0
∂f/∂y = 0.

After finding stationary points, use second partial derivatives to classify
them.

Let:

A = ∂²f/∂x²
B = ∂²f/∂x∂y
C = ∂²f/∂y²

and

D = AC - B².

If D > 0 and A > 0, the point is a local minimum.

If D > 0 and A < 0, the point is a local maximum.

If D < 0, the point is a saddle point.

If D = 0, the test is inconclusive.
""",
        "unit": "Unit I",
        "topic": "Maxima and Minima",
        "category": "Important Formula",
        "difficulty": "Advanced",
        "keywords": "maximum minimum stationary point second derivative test"
    },

    {
        "title": "Saddle Point",
        "content": """
A saddle point is a stationary point that is neither a local maximum nor
a local minimum.

For a function of two variables, the second derivative test commonly
identifies a saddle point when:

D = AC - B² < 0.

At a saddle point, the function increases in some directions and decreases
in other directions.
""",
        "unit": "Unit I",
        "topic": "Saddle Points",
        "category": "Concept Explanation",
        "difficulty": "Intermediate",
        "keywords": "saddle point maxima minima"
    },

    {
        "title": "Lagrange's Method of Undetermined Multipliers",
        "content": """
Lagrange's method is used to find maxima or minima of a function subject
to a constraint.

For maximizing or minimizing:

f(x,y,z)

subject to:

g(x,y,z) = 0,

introduce a multiplier λ and solve:

∇f = λ∇g.

Equivalently:

fx = λgx
fy = λgy
fz = λgz
g(x,y,z) = 0.

The method is called the method of Lagrange multipliers.
""",
        "unit": "Unit I",
        "topic": "Lagrange Multipliers",
        "category": "Problem Solving",
        "difficulty": "Advanced",
        "keywords": "Lagrange multiplier maxima minima constraint"
    },


    # ============================================================
    # UNIT II - MULTIVARIABLE INTEGRAL CALCULUS
    # ============================================================

    {
        "title": "Double Integral",
        "content": """
A double integral integrates a function of two variables over a region.

It is written as:

∫∫ f(x,y) dA.

A double integral can be evaluated as an iterated integral, for example:

∫[a to b] ∫[g1(x) to g2(x)] f(x,y) dy dx.

Double integrals are used to calculate areas and other quantities over
two-dimensional regions.
""",
        "unit": "Unit II",
        "topic": "Double Integral",
        "category": "Concept Explanation",
        "difficulty": "Intermediate",
        "keywords": "double integral multiple integral"
    },

    {
        "title": "Change of Order of Integration",
        "content": """
Change of order of integration means converting an iterated double
integral from one order to the other.

For example:

∫ dx ∫ dy

can be changed to:

∫ dy ∫ dx

after correctly describing the same region in the coordinate plane.

The important step is to identify and redraw the region before changing
the limits.
""",
        "unit": "Unit II",
        "topic": "Change of Order of Integration",
        "category": "Problem Solving",
        "difficulty": "Advanced",
        "keywords": "change order integration double integral limits"
    },

    {
        "title": "Change of Variables in Double Integrals",
        "content": """
Change of variables is used to simplify a double integral by replacing
the original variables with new variables.

If:

x = x(u,v)
y = y(u,v),

then:

dx dy = |∂(x,y)/∂(u,v)| du dv.

The determinant is called the Jacobian.

Therefore, the Jacobian must be included when changing variables.
""",
        "unit": "Unit II",
        "topic": "Change of Variables",
        "category": "Important Formula",
        "difficulty": "Advanced",
        "keywords": "change variables Jacobian double integral"
    },

    {
        "title": "Jacobian",
        "content": """
The Jacobian is the determinant used during transformation of variables.

For:

x = x(u,v)
y = y(u,v),

the Jacobian is:

∂(x,y)/∂(u,v)

= | x_u  x_v |
  | y_u  y_v |.

Thus:

dx dy = |J| du dv.

Jacobians are especially useful in changing variables in double integrals.
""",
        "unit": "Unit II",
        "topic": "Jacobian",
        "category": "Important Formula",
        "difficulty": "Advanced",
        "keywords": "Jacobian determinant transformation variables"
    },

    {
        "title": "Area Using Double Integral",
        "content": """
The area of a plane region R can be calculated using a double integral:

Area = ∫∫R 1 dA.

The main steps are:

1. Draw or identify the region.
2. Determine the limits of integration.
3. Set up the double integral.
4. Evaluate the integral.

Double integration is therefore useful for finding areas enclosed by plane
curves.
""",
        "unit": "Unit II",
        "topic": "Applications of Double Integral",
        "category": "Application",
        "difficulty": "Intermediate",
        "keywords": "area plane curves double integral"
    },

    {
        "title": "Triple Integral",
        "content": """
A triple integral integrates a function of three variables over a
three-dimensional region.

It is written as:

∫∫∫ f(x,y,z) dV.

For volume, the integrand is 1:

Volume = ∫∫∫R 1 dV.

Triple integrals extend the idea of double integration from two dimensions
to three dimensions.
""",
        "unit": "Unit II",
        "topic": "Triple Integral",
        "category": "Concept Explanation",
        "difficulty": "Advanced",
        "keywords": "triple integral volume three dimensional"
    },


    # ============================================================
    # UNIT III - FIRST ORDER DIFFERENTIAL EQUATIONS
    # ============================================================

    {
        "title": "Differential Equation",
        "content": """
A differential equation is an equation involving an unknown function and
its derivatives.

An ordinary differential equation contains derivatives with respect to
one independent variable.

Examples include:

dy/dx = x

and:

d²y/dx² + y = 0.

Differential equations are used to model physical and engineering systems.
""",
        "unit": "Unit III",
        "topic": "Differential Equations",
        "category": "Concept Explanation",
        "difficulty": "Basic",
        "keywords": "differential equation ODE definition"
    },

    {
        "title": "Linear Differential Equation of First Order",
        "content": """
A first-order linear differential equation has the standard form:

dy/dx + P(x)y = Q(x).

Its integrating factor is:

IF = e^(∫P(x)dx).

Multiplying the equation by the integrating factor allows the left side
to be written as the derivative of a product.

The solution is obtained by integrating both sides.
""",
        "unit": "Unit III",
        "topic": "Linear Differential Equation",
        "category": "Important Formula",
        "difficulty": "Intermediate",
        "keywords": "first order linear differential equation integrating factor"
    },

    {
        "title": "Bernoulli's Differential Equation",
        "content": """
Bernoulli's differential equation has the form:

dy/dx + P(x)y = Q(x)y^n,

where n is not equal to 0 or 1.

Use the substitution:

v = y^(1-n).

This converts the Bernoulli equation into a first-order linear differential
equation in v.
""",
        "unit": "Unit III",
        "topic": "Bernoulli Equation",
        "category": "Problem Solving",
        "difficulty": "Advanced",
        "keywords": "Bernoulli differential equation substitution"
    },

    {
        "title": "Exact Differential Equation",
        "content": """
A differential equation:

M(x,y)dx + N(x,y)dy = 0

is exact if:

∂M/∂y = ∂N/∂x.

When the equation is exact, there exists a function F(x,y) such that:

dF = M dx + N dy.

The solution is:

F(x,y) = C.
""",
        "unit": "Unit III",
        "topic": "Exact Differential Equation",
        "category": "Important Formula",
        "difficulty": "Intermediate",
        "keywords": "exact differential equation M N condition"
    },

    {
        "title": "Equations Reducible to Exact Differential Equations",
        "content": """
Some differential equations are not initially exact but can be converted
into exact equations by multiplying them by a suitable integrating factor.

An integrating factor is selected so that the modified equation satisfies:

∂M/∂y = ∂N/∂x.

After making the equation exact, integrate to obtain the solution.
""",
        "unit": "Unit III",
        "topic": "Reducible to Exact Equations",
        "category": "Problem Solving",
        "difficulty": "Advanced",
        "keywords": "integrating factor reducible exact differential equation"
    },

    {
        "title": "Simple Electric Circuit Differential Equation",
        "content": """
Differential equations can be used to model simple electric circuits.

For an RL circuit, Kirchhoff's voltage law can lead to a first-order
differential equation involving current and its derivative.

A typical model has the form:

L(di/dt) + Ri = E(t),

where:

L = inductance,
R = resistance,
i = current,
E(t) = applied voltage.

The differential equation is solved to determine current as a function
of time.
""",
        "unit": "Unit III",
        "topic": "Applications to Electric Circuits",
        "category": "Application",
        "difficulty": "Advanced",
        "keywords": "electric circuit differential equation RL circuit current"
    },

    {
        "title": "Newton's Law of Cooling",
        "content": """
Newton's law of cooling states that the rate of change of temperature of
an object is proportional to the difference between the object's
temperature and the surrounding temperature.

The differential equation can be written as:

dT/dt = -k(T - Ts),

where:

T = object's temperature,
Ts = surrounding temperature,
k = positive constant.

The model is used to determine the temperature of an object over time.
""",
        "unit": "Unit III",
        "topic": "Newton's Law of Cooling",
        "category": "Application",
        "difficulty": "Intermediate",
        "keywords": "Newton law cooling temperature differential equation"
    },

    {
        "title": "Heat Flow Differential Equation",
        "content": """
Heat-flow problems can be modeled using differential equations.

The temperature or heat quantity changes with time according to physical
conditions and heat-transfer relationships.

Differential equations are used to determine temperature variation and
heat-flow behavior.
""",
        "unit": "Unit III",
        "topic": "Heat Flow",
        "category": "Application",
        "difficulty": "Advanced",
        "keywords": "heat flow differential equation temperature"
    },

    {
        "title": "Orthogonal Trajectories",
        "content": """
Orthogonal trajectories are curves that intersect a given family of
curves at right angles.

The general method is:

1. Start with the family of curves.
2. Differentiate to obtain a differential equation.
3. Replace the slope dy/dx by its negative reciprocal.
4. Solve the resulting differential equation.

If the original slope is m, the perpendicular slope is:

-1/m.
""",
        "unit": "Unit III",
        "topic": "Orthogonal Trajectories",
        "category": "Problem Solving",
        "difficulty": "Advanced",
        "keywords": "orthogonal trajectories perpendicular curves slope"
    },


    # ============================================================
    # UNIT IV - SECOND AND HIGHER ORDER DIFFERENTIAL EQUATIONS
    # ============================================================

    {
        "title": "Second Order Linear Differential Equation",
        "content": """
A second-order linear differential equation has the general form:

a d²y/dx² + b dy/dx + cy = f(x).

If f(x) = 0, the equation is homogeneous.

If f(x) is not zero, the equation is non-homogeneous.

Solutions are generally expressed using a complementary function and a
particular integral.
""",
        "unit": "Unit IV",
        "topic": "Second Order Differential Equations",
        "category": "Concept Explanation",
        "difficulty": "Intermediate",
        "keywords": "second order linear differential equation"
    },

    {
        "title": "Higher Order Linear Differential Equation",
        "content": """
A higher-order linear differential equation contains derivatives higher
than the first derivative.

A general nth-order equation can be written as:

a_n y^(n) + a_(n-1)y^(n-1) + ... + a_1 y' + a_0 y = f(x).

The solution depends on the complementary function and particular
integral.
""",
        "unit": "Unit IV",
        "topic": "Higher Order Differential Equations",
        "category": "Concept Explanation",
        "difficulty": "Advanced",
        "keywords": "higher order linear differential equation"
    },

    {
        "title": "Complete Solution of Linear Differential Equation",
        "content": """
For a non-homogeneous linear differential equation, the complete solution
is:

Complete Solution = Complementary Function + Particular Integral.

Therefore:

y = CF + PI.

The complementary function solves the associated homogeneous equation,
while the particular integral provides a solution corresponding to the
non-homogeneous term.
""",
        "unit": "Unit IV",
        "topic": "Complete Solution",
        "category": "Important Formula",
        "difficulty": "Intermediate",
        "keywords": "complete solution CF PI complementary function particular integral"
    },

    {
        "title": "Complementary Function",
        "content": """
The complementary function is the general solution of the associated
homogeneous differential equation.

For a linear differential equation with constant coefficients, assume:

y = e^(mx).

Substitution produces the auxiliary or characteristic equation.

The roots of this equation determine the form of the complementary
function.
""",
        "unit": "Unit IV",
        "topic": "Complementary Function",
        "category": "Concept Explanation",
        "difficulty": "Intermediate",
        "keywords": "complementary function auxiliary equation characteristic roots"
    },

    {
        "title": "Particular Integral",
        "content": """
The particular integral is a particular solution of a non-homogeneous
linear differential equation.

For an equation:

F(D)y = X,

the particular integral is commonly written as:

PI = 1/F(D) X.

Different methods are used depending on the form of X.
""",
        "unit": "Unit IV",
        "topic": "Particular Integral",
        "category": "Concept Explanation",
        "difficulty": "Advanced",
        "keywords": "particular integral differential equation PI operator method"
    },

    {
        "title": "Variation of Parameters",
        "content": """
Variation of parameters is a method for finding the particular integral
of a non-homogeneous linear differential equation.

The method assumes that the constants appearing in the complementary
function are variable functions.

For a second-order equation, the complementary solutions are used to
construct suitable parameter functions, which are then integrated to
obtain the particular solution.
""",
        "unit": "Unit IV",
        "topic": "Variation of Parameters",
        "category": "Problem Solving",
        "difficulty": "Advanced",
        "keywords": "variation parameters particular integral differential equation"
    },

    {
        "title": "Cauchy's Linear Differential Equation",
        "content": """
Cauchy's linear differential equation, also called an Euler-Cauchy
equation, has variable coefficients related to powers of x.

A typical second-order form is:

x² y'' + axy' + by = f(x).

A common substitution is:

x = e^t

or equivalently:

t = ln x,

which can convert the equation into one with constant coefficients.
""",
        "unit": "Unit IV",
        "topic": "Cauchy Linear Equation",
        "category": "Problem Solving",
        "difficulty": "Advanced",
        "keywords": "Cauchy Euler equation differential equation"
    },

    {
        "title": "Legendre's Linear Differential Equation",
        "content": """
Legendre's linear differential equations are higher-order linear
differential equations with variable coefficients.

They can often be transformed using an appropriate change of variables
into a form that can be solved using methods for linear differential
equations with constant coefficients.

The exact transformation depends on the given equation.
""",
        "unit": "Unit IV",
        "topic": "Legendre Linear Equation",
        "category": "Concept Explanation",
        "difficulty": "Advanced",
        "keywords": "Legendre linear differential equation"
    },

    {
        "title": "Simultaneous Linear Differential Equations",
        "content": """
Simultaneous linear differential equations involve two or more dependent
variables connected through differential equations.

For equations with constant coefficients, operator methods can be used to
eliminate one variable and obtain a higher-order differential equation
in the remaining variable.

After solving, substitute back to obtain the other dependent variable.
""",
        "unit": "Unit IV",
        "topic": "Simultaneous Differential Equations",
        "category": "Problem Solving",
        "difficulty": "Advanced",
        "keywords": "simultaneous linear differential equations constant coefficients"
    },

    {
        "title": "Oscillatory Electric Circuit",
        "content": """
Linear differential equations can model oscillatory electric circuits.

For an RLC circuit, Kirchhoff's laws can produce a second-order
differential equation involving charge or current.

A typical form is:

Lq'' + Rq' + (1/C)q = E(t),

where:

L = inductance,
R = resistance,
C = capacitance,
q = charge,
E(t) = applied voltage.

The resulting differential equation is used to study the electrical
oscillation of the circuit.
""",
        "unit": "Unit IV",
        "topic": "Oscillatory Electric Circuits",
        "category": "Application",
        "difficulty": "Advanced",
        "keywords": "RLC circuit oscillatory electric circuit differential equation"
    },


    # ============================================================
    # EXAM / REVISION
    # ============================================================

    {
        "title": "Mathematics-III Important Topics",
        "content": """
Important MDU Mathematics-III topics include:

Unit I:
- Limits and continuity
- Partial derivatives
- Homogeneous functions
- Euler's theorem
- Total derivatives
- Maxima and minima
- Saddle points
- Lagrange multipliers

Unit II:
- Double integrals
- Change of order
- Change of variables
- Jacobian
- Area using double integrals
- Triple integrals

Unit III:
- Linear differential equations
- Bernoulli equation
- Exact differential equations
- Equations reducible to exact form
- Electric circuit applications
- Newton's law of cooling
- Heat flow
- Orthogonal trajectories

Unit IV:
- Higher-order linear differential equations
- Complementary function
- Particular integral
- Variation of parameters
- Cauchy's equation
- Legendre's equation
- Simultaneous linear differential equations
- Oscillatory electric circuits
""",
        "unit": "Unit I-IV",
        "topic": "Exam Revision",
        "category": "Exam Important",
        "difficulty": "Advanced",
        "keywords": "mathematics 3 important topics exam revision MDU"
    },

    {
        "title": "Mathematics-III Exam Strategy",
        "content": """
For Mathematics-III numerical problems, students should:

1. Identify the type of problem.
2. Write the appropriate formula or standard equation.
3. Show the substitution clearly.
4. Perform differentiation or integration step by step.
5. Keep constants of integration where required.
6. State the final answer clearly.

For differential equations, first identify whether the equation is linear,
Bernoulli, exact, second-order linear, Cauchy, Legendre, or simultaneous.

For multivariable calculus, carefully identify the required partial
derivatives, region, limits, Jacobian, or stationary points.
""",
        "unit": "Unit I-IV",
        "topic": "Exam Strategy",
        "category": "Exam Important",
        "difficulty": "Intermediate",
        "keywords": "math 3 exam strategy numerical problems MDU"
    }
]


def seed_database():
    connection = get_connection()

    added = 0
    skipped = 0

    for item in KNOWLEDGE:
        existing = connection.execute(
            "SELECT id FROM knowledge WHERE title = ?",
            (item["title"],)
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
                item["content"].strip(),
                "Mathematics-III",
                item["unit"],
                item["topic"],
                item["category"],
                item["difficulty"],
                item["keywords"],
                "EchoMind MDU Knowledge Seed"
            )
        )

        added += 1

    connection.commit()
    connection.close()

    print("=" * 60)
    print("EchoMind Mathematics-III Knowledge Seed")
    print("=" * 60)
    print(f"Added:   {added}")
    print(f"Skipped: {skipped}")
    print(f"Total entries in seed: {len(KNOWLEDGE)}")
    print("=" * 60)


if __name__ == "__main__":
    seed_database()