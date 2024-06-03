## 1. How can you identify when you can use dynamic programming to solve a problem?
- a. The problem can be divided into overlapping subproblems, and it exhibits optimal substructure.
- b. The problem can be solved using the locally optimal choice at each stage.
- c. The problem involves recursive solutions where subproblems are independent of each other.
- d. The problem can be divided into subproblems that are non-overlapping but share the same optimal solution approach.

## 2. What is the top-down approach in dynamic programming?
- a. A method where you start solving the smallest subproblems first and use their solutions to build up solutions to larger subproblems.
- b. A method where you break down a problem into subproblems, solve each subproblem just once, and store their solutions to avoid redundant work, starting from the base case.
- c. A method where you solve the problem by recursively breaking it down into smaller subproblems and using memoization to store intermediate results.
- d. A method where you solve subproblems iteratively, building the solution from the base case up to the original problem.

## 3. What is the bottom-up approach in dynamic programming?
- a. A method where you solve subproblems in parallel to optimize computation time.
- b. A method where you solve subproblems iteratively, building the solution from the base case up to the original problem.
- c. A method where you solve the problem by recursively breaking it down into smaller subproblems and using memoization to store intermediate results.
- d. A method where you select specific subproblems to solve and combine their solutions to form the final answer.

## 4. Without memoization, a recursive solution for Fibonacci Number would have the time complexity:
- a. O(n)
- b. O(log n)
- c. O(2^n)
- d. O(n^2)

## 5. Usually, top-down algorithms are faster than bottom-up ones.
- a. True
- b. False

## 6. A common characteristic of problems that can be solved with dynamic programming is that they ask for the maximum or minimum of something.
- a. True
- b. False

## 7. Which of the following must be done when converting a top-down dynamic programming solution into a bottom-up dynamic programming solution?
- a. Change plus to minus in the recurrence relation.
- b. Create new base cases.
- c. Find the correct order in which to iterate over the states.
- d. Implement caching to store intermediate results.

## 8. Which characteristic distinguishes dynamic programming (DP) problems from greedy problem-solving approaches?
- a. They involve making locally optimal decisions at each step.
- b. They require solving overlapping subproblems and storing their solutions to avoid redundant computation.
- c. They involve "future decisions" that depend on earlier decisions made in the solution process.
- d. They rely on heuristics to approximate the optimal solution efficiently.

## 9. Which of the following data structures is commonly used for memoization in dynamic programming?
- a. Stack
- b. Queue
- c. Hash Table
- d. Linked List

## 10. Which dynamic programming technique is generally preferred when space efficiency is a concern?
- a. Top-down approach with memoization.
- b. Bottom-up approach with iteration.
- c. Recursion without memoization.
- d. Depth-first search with pruning.