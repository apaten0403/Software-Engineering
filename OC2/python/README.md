# Theatrical Players Refactoring Kata
## 1. Build and Test Instructions

### Requirements

- Python 3.12 or a compatible Python version
- `pytest` for running automated tests

### Running the Tests

Run from the project root directory:

```powershell
python -m pytest -v
```

The `-v` shows each individual test and it's result.

To install pytest:

```powershell
python -m pip install pytest
```

## 2. Initial and Final Test Results

### Initial Test Results
**Result:** 2 tests passed, 0 failed.

- `test_example_statement` — PASSED
- `test_statement_with_new_play_types` — PASSED


### Final Test Results
**Final result:** 6 tests passed, 0 failed. 

- `test_example_statement` — PASSED       
- `test_statement_with_new_play_types` — PASSED      
- `test_statement_with_small_audience` — PASSED       
- `test_tragedy_at_30_audience_member_boundary` — PASSED      
- `test_historical_case` — PASSED             
- `test_historical_case_with_volume_credit_rounded_down` — PASSED   


### Test Explanations
1. **`test_statement_with_small_audience`**  
   This test verifies that a statement containing a single tragedy performance with 13 audience members has the correct title, amount, and volume credits displayed. The title displayed is Othello, the charge is $400.00, and volume credits gained are 0. This checks that audiences below the the given amount don't get any credits.
 
2. **`test_tragedy_at_30_audience_member_boundary`**  
   This test verifies that a tragedy performance with exactly 30 audience members is charged $400.00. This ensures that the rule of adding extra fees to larger audiences starts after 30 people, not including 30 people.

3. **`test_historical_case`**
    This test verifies that a historical performance has the correct title, amount, and volume credits. The title displayed is Henry V, the charge is $725.00, and volume credits gained are 7. This checks that the new performance type is correctly implemented.

4. **`test_historical_case_with_volume_credit_rounded_down`**
    This test verifies that a historical performance will correctly round down the audience to give the correct volume credit. An audience of 14 should give 2 credits.

## 3. Refactoring Log
### Refactoring 1: Extracting the Amount Calculation

**(a) What changed**

I extracted the pricing logic from `statement()` into a separate `amount_for()` helper function. The function calculates the charge for an individual performance, while `statement()` continues to generate the statement, calculate credits, format the output, and maintain the total amount.

**(b) Why the change improved the design**

This separates pricing from statement generation. The code is easier to read and maintain because changes to pricing rules can be made in one place without navigating the rest of the statement-generation logic.

**(c) How behavior was verified**

Check Git commit history (Refactor 1).

### Refactoring 2: Renaming `this_amount` to `result`

**(a) What changed**

I renamed the local variable `this_amount` to `result` inside `amount_for()`. The variable still stores the calculated performance charge and is returned by the function.

**(b) Why the change improved the design**

The name `result` makes the function's return value clearer and follows the naming convention used in the reference material. This improves consistency and readability without changing the calculation.

**(c) How behavior was verified**

Check Git commit history (Refactor 2).

### Refactoring 3: Adding helper functions

**(a) What changed**

I moved `play_for()` and `amount_for()` inside `statement()`. I then removed the `plays` parameter from `play_for()` and the `play` parameter from `amount_for()`, updating their calls accordingly.

**(b) Why the change improved the design**

The helper functions can access variables from the enclosing `statement()` function. This eliminates unnecessary parameters, simplifies function calls, and keeps the helpers close to the code that uses them.

**(c) How behavior was verified**

Check Git commit history (Refactor 4).

### Refactoring 4: Extracting Volume Credit Calculation

**(a) What changed**

I moved the volume-credit calculation into a separate `volume_credits_for(perf)` helper function. The main loop calls the helper and adds its returned value to the running total, `volume_credits`.

**(b) Why the change improved the design**

The function does one job, which is calculating credits for an individual performance. Keeping the running total in the main loop also avoids modifying an enclosing variable inside a nested Python function.

**(c) How behavior was verified**

Check Git commit history (Refactor 5).

## 4. Reflection

The refactoring that most improved the design was extracting the amount calculation into its own function. The original statement function did all responsibilities of the program, like figuring out the prices, calculating credits, and formatting the output. Separating the pricing logic made the code easier to understand because it was easier to see the purpose of each part. It also made the program easier to maintain, since you knew exactly where to go when updating pricing or adding a new performance. 

Refactoring is different from adding functionality because refactoring changes the code itself without changing how it is used. Adding functionality introduces new behavior or capabilities, while refactoring only makes the current code more efficient or easier to read. During the refactoring process, the original tests helped verify that the original pricing rules and statement output continued to work. The new historical play requirement, on the other hand, required introducing additional pricing and volume-credit rules.

The new design helped me add historical plays by making the pricing and credit calculations easier to locate and modify. Separating calculations into helper functions reduced the amount of logic handled directly by the main function. But, this does not mean that only doing extracting of functions completely eliminates the need to modify the current logic when adding new play types. A better object-oriented design could use polymorphism to allow each play type to implement its own pricing and credit calculations.

Several of the original maintainability issues were addressed, including extracting code into smaller functions, renaming variables for clarity, and extracting the volume credit calculations. Extracting all parts of the function into separate functions reduced the number of responsibilities handled by the original main function. Renaming `this_amount` to `result` made the code more consistent and easier to follow. Adding helper functions and removing unnecessary parameters simplified function calls and kept related code together. Extracting the volume-credit calculation made that logic easier to understand and modify independently.

Overall, these changes improved the organization and readability of the implementation while preserving its existing behavior. Adding the historical play also showed that a good design matters because new requirements are easier to implement when responsibilities are separated. Automated tests remain important because they provide evidence that improvements to the internal design have not unintentionally changed existing functionality.

## 5. Attribution and Modifications

**Original project:** [Theatrical Players Refactoring Kata](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata)

**Author:** Alexis Paten 
**Date:** October 25, 2026

**GitHub Repository:** [View the project on GitHub] (https://github.com/apaten0403/Software-Engineering.git)

**Modifications made:**

- Refactored the Python implementation to improve readability and separation of responsibilities.
- Extracted pricing and volume-credit calculations into helper functions.
- Renamed a local variable to improve clarity and consistency.
- Added 4 more tests for existing pricing, volume-credit behavior, and the addition of a new type.
- Documented the refactoring process, testing approach, and design reflection.

## 6. Generative AI Disclosure

Generative AI was used to clarify code