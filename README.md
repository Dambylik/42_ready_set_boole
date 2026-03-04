## Ready Set Boole

This project is a collection of small exercises around **bitwise operations**, **boolean logic in Reverse Polish Notation (RPN)**, **normal forms**, **satisfiability**, **sets**, and **space-filling curves**.  
Each file `exNN_*.py` is a self‑contained program with a `main()` you can run from the command line.

---

Expressions are always given in **RPN** (Reverse Polish Notation), e.g. `AB&` means \(A \land B\).

---

## Exercises Overview

### ex00_adder.py — Bitwise Adder (u32)

**Goal**: Implement addition without using `+`, only bitwise operations.

- `adder(a, b)`:
  - Uses `^` for sum without carry.
  - Uses `(a & b) << 1` for the carry.
  - Repeats until carry is zero, then masks the result with `U32_MAX` so it stays in the 32‑bit unsigned range.
- `main()`:
  - Parses two integers from CLI.
  - Checks they are in \([0, 2^{32}-1]\).
  - Prints the result.

---

### ex01_multiplier.py — Bitwise Multiplier (u32)

**Goal**: Multiply two unsigned 32‑bit integers using only shifting and the `adder` from ex00.

- `multiplier(a, b)`:
  - Interprets `b` in binary.
  - If the current least significant bit of `b` is `1`, adds `a` to `result`.
  - Shifts `a` left (×2) and `b` right (÷2) each iteration.
  - Masks intermediate results to stay in u32 range.
- `main()`:
  - Same argument parsing and u32 checks as `ex00_adder.py`.

---

### ex02_gray_code.py — Gray Code

**Goal**: Compute the Gray code of a number.

- `gray_code(n)`:
  - Returns `n ^ (n >> 1)`.
- `main()`:
  - Parses one u32 integer.
  - Prints its Gray code.

---

### ex03_boolean_evaluation.py — Boolean RPN Evaluator + AST

**Goal**: Evaluate boolean formulas written in RPN and build an AST.

- `Node`:
  - Simple binary tree node with `value`, `left`, `right`.
- `build_ast(expr)`:
  - Reads expression left‑to‑right.
  - Pushes operands (`0`, `1`, or variables `A`–`Z`) onto a stack.
  - Unary `!` pops one child, binary operators `&|^>=` pop two children.
  - The final stack element is the AST root.
- `boolean_eval(expr)`:
  - Similar stack machine, but values are booleans (`False` for `0`, `True` for `1`).
  - Implements:
    - `!` = NOT
    - `&` = AND
    - `|` = OR
    - `^` = XOR
    - `>` = implication (\(\neg a \lor b\))
    - `=` = equivalence (\(a == b\))
- `main()`:
  - Validates characters.
  - Prints the boolean result and a textual representation of the AST.

---

### ex04_truth_table.py — Truth Table Generator

**Goal**: Print the full truth table of a boolean formula in RPN.

- `print_truth_table(formula)`:
  - Extracts all uppercase letters (variables) and sorts them.
  - For each integer `i` from `0` to `2^n - 1`:
    - Interprets bits of `i` as a truth assignment to the variables.
    - Builds a new RPN string where each variable becomes `'0'` or `'1'`.
    - Calls `boolean_eval()` to get the result.
    - Prints the row as `0/1` values with the final result.
- `main()`:
  - Validates formula characters.
  - Calls `print_truth_table`.


---

### ex05_neg_normal_form.py — Negation Normal Form (NNF)

**Goal**: Convert a boolean formula to **Negation Normal Form**, where:
- Only `!`, `&`, and `|` remain.
- Negation appears only directly in front of variables.

Key functions:

- `to_nnf(node)`:
  - Works over the AST from `build_ast`.
  - Pushes negations inward using logical equivalences:
    - `!!A → A`
    - `!(A & B) → !A | !B`
    - `!(A | B) → !A & !B`
    - `A > B → !A | B`
    - `A = B → (A & B) | (!A & !B)`
    - `A ^ B → (A & !B) | (!A & B)`
  - Recursively normalizes children.
- `ast_to_rpn(node)`:
  - Converts the normalized AST back into an RPN string.
- `negation_normal_form(formula)`:
  - Composes `build_ast` → `to_nnf` → `ast_to_rpn`.
- `main()`:
  - Reads a formula and prints its NNF in RPN.

Logic: symbolic AST rewriting using standard logical equivalences.

---

### ex06_conj_normal_form.py — Conjunctive Normal Form (CNF)

**Goal**: Convert a boolean formula to **Conjunctive Normal Form** (AND of ORs).

- `to_cnf(node)`:
  - Assumes input is already NNF.
  - Recursively distributes `|` over `&`:
    - `(A & B) | C → (A | C) & (B | C)`
    - `A | (B & C) → (A | B) & (A | C)`
- `conjunctive_normal_form(expr)`:
  - Builds AST, applies `to_nnf` from ex05, then `to_cnf`, then `ast_to_rpn`.
- `main()`:
  - Reads formula and prints its CNF in RPN.

Logic: CNF is obtained by first pushing negations down (NNF) and then distributing OR over AND.

---

### ex07_sat.py — SAT Solver on CNF

**Goal**: Decide if a boolean formula is **satisfiable** (there exists an assignment that makes it true).

- Reuses:
  - `build_ast` from ex03
  - `to_nnf` from ex05
  - `to_cnf` from ex06
- Steps:
  1. Build AST, convert to NNF, then CNF.
  2. `extract_clauses(node)`:
     - Interprets the CNF AST as a conjunction of disjunctions.
     - Returns a list of clauses; each clause is a list of literals.
  3. `extract_literals(node)`:
     - Breaks a clause into literals like `('!', 'A')` or `(None, 'B')`.
  4. `evaluate_clause(clause, assignment)`:
     - Clause is satisfied if at least one literal is true under the assignment.
  5. `is_satisfiable(expr)`:
     - Enumerates all boolean assignments (bitmask over variables).
     - Checks if all clauses are satisfied for some assignment.
- `main()`:
  - Reads a formula string and prints `True` or `False`.

Logic: brute‑force SAT solver working on CNF with bitmask enumeration.

---

### ex08_powerset.py — Powerset via Bitmasks

**Goal**: Compute the powerset of a list of integers.

- `powerset(set_)`:
  - Deduplicates and sorts the elements.
  - For each mask from `0` to `2^n - 1`, builds one subset by including the `i`‑th element when bit `i` of the mask is `1`.
- `main()`:
  - Parses a space‑separated list of integers from the CLI argument.
  - Prints each subset.

Logic: same bitmask enumeration idea used in truth tables and SAT.

---

### ex09_set_evaluation.py — Set Expression Evaluation in RPN

**Goal**: Evaluate RPN formulas over **sets of integers**, using set operations analogous to boolean operators.

- `eval_set(formula, sets)`:
  - Converts input lists into Python `set`s.
  - Builds the **universe** as the union of all sets.
  - Uses a stack:
    - Variables `A`, `B`, `C`, … refer to sets by index.
    - `!A` → complement wrt universe: `universe - A`.
    - `&` → intersection.
    - `|` → union.
    - `>` → implication: `(universe - A) | B`.
    - `=` → equivalence: `(A & B) | (!A & !B)` using set operations.
  - Returns the resulting set as a **sorted list** of integers.
- `main()`:
  - Example usage:

