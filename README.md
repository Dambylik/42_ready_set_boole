# Ready Set Boole

> [!IMPORTANT]
> All formulas are written in **Reverse Polish Notation (RPN)**.  
> Evaluation is stack-based unless otherwise specified.

---

# Exercise 00 – Boolean Evaluation

## Goal
Evaluate a propositional formula written in RPN.

## Supported Operators

| Symbol | Meaning |
|--------|---------|
| `&` | AND |
| `|` | OR |
| `!` | NOT |
| `>` | Implication |
| `=` | Equivalence |

> [!NOTE]
> Evaluation uses a stack.  
> Time complexity: **O(n)**

### Core Idea
1. Read left → right.
2. Push operands.
3. When operator appears:
   - Pop operands.
   - Apply operation.
   - Push result.

---

# Exercise 01 – Truth Table

## Goal
Generate the full truth table of a formula.

> [!IMPORTANT]
> If the formula has `n` variables → there are **2ⁿ rows**.

### Key Concepts
- Variable extraction
- Binary enumeration
- Repeated evaluation

Time complexity: **O(n · 2ⁿ)**

---

# Exercise 02 – AST Construction

## Goal
Build an Abstract Syntax Tree (AST) from RPN.

### Node Structure
- `value`
- `left`
- `right`

> [!TIP]
> Leaves = variables  
> Internal nodes = operators

The AST becomes the base structure for normalization and transformations.

---

# Exercise 03 – Boolean Evaluation from AST

## Goal
Evaluate a formula using recursive tree traversal.

### Why?
- Cleaner architecture
- Enables rewriting (NNF, CNF)
- Separation of parsing and evaluation

---

# Exercise 04 – Logical Equivalences

## Goal
Understand and apply rewriting rules.

### Key Equivalences

Implication: A > B ≡ ¬A ∨ B
Equivalence: A = B ≡ (A ∧ B) ∨ (¬A ∧ ¬B)


> [!IMPORTANT]
> These rules are required before converting to normal forms.

---

# Exercise 05 – Negation Normal Form (NNF)

## Goal
Transform formula into **NNF**.

## Definition
A formula is in NNF if:
- Only `&` and `|`
- Negations apply only to variables
- No `>` or `=`

### Rewrite Rules

De Morgan: 
!(A | B) → !A & !B
!(A & B) → !A | !B

Double negation: !!A → A

> [!NOTE]
> NNF simplifies CNF conversion.

---

# Exercise 06 – Conjunctive Normal Form (CNF)

## Goal
Convert NNF into CNF.

## Definition
CNF is: (Clause1) & (Clause2) & ...
Each clause: Literal | Literal | ...


### Core Rule
Distribute OR over AND: A | (B & C) → (A | B) & (A | C)


> [!WARNING]
> CNF conversion can cause exponential growth.

---

# Exercise 07 – SAT Solver

## Goal
Determine if a formula is satisfiable.

## Definition
SAT asks:

> Does there exist an assignment making the formula true?

### Method
- Extract variables
- Try all 2ⁿ assignments
- Evaluate formula

> [!IMPORTANT]
> SAT is NP-complete.  
> Brute force complexity: **O(2ⁿ)**

---

# Interlude 01 – Rules of Inference

Logical reasoning principles:

- Modus Ponens
- Modus Tollens
- Resolution
- Hypothetical Syllogism

Example:
A
A → B
∴ B

Used in automated reasoning systems.

---

# Interlude 02 – Set Theory

Logical operators correspond to set operations:

| Logic | Set |
|--------|------|
| A ∧ B | A ∩ B |
| A ∨ B | A ∪ B |
| ¬A | U \ A |

> [!NOTE]
> Universe = union of all sets.

---

# Exercise 08 – Powerset

## Goal
Generate all subsets of a set.

If a set has `n` elements: |P(S)| = 2ⁿ

### Method
Use bitmask enumeration.

Time complexity: **O(n · 2ⁿ)**

> [!TIP]
> First subset is always `[]` (empty set).

---

# Exercise 09 – Set Evaluation

## Goal
Evaluate logical formulas on sets.

Variables represent sets.

### Operator Mapping

| Logic | Set Operation |
|--------|---------------|
| `&` | Intersection |
| `|` | Union |
| `!` | Complement |
| `>` | (¬A ∪ B) |
| `=` | Equivalence |

> [!IMPORTANT]
> Complement is relative to the universe.

---

# Exercise 10 – Space-Filling Curve (Morton Code)

## Goal
Map (x, y) ∈ [0..65535]² → float ∈ [0,1].

### Method
1. Interleave bits of x and y.
2. Build 32-bit Morton code.
3. Normalize: value = morton_code / (2³² − 1)

> [!NOTE]
> Also known as **Z-order curve**.

Properties:
- Preserves spatial locality
- Used in spatial indexing

---

# Exercise 11 – Reverse Mapping

## Goal
Implement inverse mapping: f⁻¹(f(x, y)) = (x, y)

### Method
- Convert float → 32-bit integer
- De-interleave bits
- Reconstruct x and y

> [!IMPORTANT]
> The mapping is bijective on:
>
> `[0..65535] × [0..65535]`

---

# Global Pipeline
RPN → AST → NNF → CNF → SAT


Set algebra extends logical semantics.  
Morton encoding applies bit logic to geometry.

---

# Complexity Summary

| Exercise | Complexity |
|-----------|------------|
| Eval | O(n) |
| Truth Table | O(n · 2ⁿ) |
| SAT | O(2ⁿ) |
| Powerset | O(n · 2ⁿ) |
| CNF | Worst-case exponential |
| Morton Map | O(1) |

---

# Concepts Covered

- Boolean algebra
- Logical equivalence
- Normal forms (NNF, CNF)
- SAT problem
- Set theory
- Bit manipulation
- Space-filling curves
- Algorithmic complexity