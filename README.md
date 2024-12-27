# Christmas Toy Optimization

This project solves the problem of maximizing the daily profit from toy production and packaging during the Christmas season. It was developed as part of course **Análise e Síntese de Algoritmos** at **Instituto Superior Técnico (IST)*** using **Python** and the **PuLP** library for linear programming (LP). The program determines the optimal number of individual toys and special packages to produce, respecting production capacity constraints.

## Features
- **Linear Programming Model**:
  - Formulated a profit-maximizing LP problem with constraints on production capacity and packaging rules.
- **Special Package Optimization**:
  - Incorporates special packages containing three distinct toys, yielding higher profits than individual sales.
- **Dynamic Constraints**:
  - Ensures compliance with individual toy production limits and overall capacity.

## Problem Description
The program receives:
1. The number of toys (`t`), the number of special packages (`p`), and the maximum daily production capacity (`max`).
2. A list of toys, each with:
   - `li`: Profit per toy.
   - `ci`: Maximum daily production capacity for the toy.
3. A list of packages, each with:
   - Three toy indices (`i, j, k`).
   - `lijk`: Profit for the package.

### Example

![image](https://github.com/user-attachments/assets/b843c549-a31e-4a78-be72-1186f38af846)


In this example, the program computes the optimal combination of individual toys and packages to maximize profit while adhering to production constraints.

## My Contributions
1. **Algorithm Implementation**:
   - Designed and implemented the linear programming model using the PuLP library.
   - Developed functions for parsing input and setting up LP variables and constraints.
2. **Testing and Debugging**:
   - Validated the solution using test cases provided by the course.

## Provided Materials
- Test cases for validation were provided as part of the project.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `PuLP`: For formulating and solving the linear programming model.
  - `GLPK`: As the solver backend.

## How It Works
1. **Input Parsing**:
   - Reads toy and package details from standard input.
2. **LP Model Setup**:
   - Defines decision variables for toy and package production.
   - Adds constraints:
     - Individual toy limits.
     - Total production capacity.
   - Formulates the objective function to maximize profit.
3. **Output**:
   - Prints the maximum achievable profit.

## Installation
1. Install required libraries:
   ```bash
   python3 -m pip install pulp
   sudo apt-get install glpk-utils  # For GLPK solver

## Acknowledgments
This project was developed as part of an academic exercise at Instituto Superior Técnico (IST). Test cases were provided by the course instructors.


