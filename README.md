# 🇮🇳 Indian Tax Predictor 

##  Overview of the Project

The Indian Tax Predictor is a simple, command-line utility built in Python designed to provide quick, rough estimations of Indian income tax liability and potential tax deductions for common financial instruments like home and education loans.

This tool is intended for informational and educational purposes, allowing users to understand the impact of various income levels and deductions based on a simplified tax structure and current (or near-current) deduction limits.

##  Features

The application offers a menu-driven interface to calculate the following:

* **Income Tax Calculation:** Estimates the tax liability based on a tiered tax slab system, applied to the annual gross income after a standard deduction. It also incorporates the mandatory **4% Health and Education Cess**.
* **Home Loan Interest Deduction (Sec 24(b)):** Calculates the potential annual tax deduction for interest paid on a home loan, limited to **₹2,00,000** for self-occupied property (based on a simplified interest calculation).
* **Education Loan Interest Deduction (Sec 80E):** Calculates the potential annual tax deduction for the entire interest paid on an education loan.
* **Property Deduction/Tax (Simplified Sec 80C):** Provides a rough estimate of potential deductions for property purchases (e.g., principal repayment component) capped at **₹1,50,000**.
* **House Tax (Municipal Property Tax) Estimate:** Gives a basic estimation of local property tax based on a simple percentage of the property value.

##  Technologies/Tools Used

* **Language:** Python 3 (specifically, CPython)
* **Environment:** Command Line Interface (CLI)

##  Steps to Install & Run the Project

Since this is a single Python script with no external dependencies, running the project is straightforward:

1.  **Save the Code:** Save the provided Python code into a file named `tax_predictor.py`.
2.  **Open Terminal/Command Prompt:** Navigate to the directory where you saved the file.
3.  **Execute the Script:** Run the script using the Python interpreter:

    ```bash
    python tax_predictor.py
    ```
4.  **Follow the Prompts:** The program will present a menu. Enter the corresponding number (1-5) for the calculation you wish to perform and follow the input prompts.

##  Instructions for Testing

To verify the functionality, use the following test cases:

| Test Case | Feature | Input (Income/Details) | Expected Output (Logic Check) |
| :--- | :--- | :--- | :--- |
| **Tax Slab 1** | Income Tax (1) | Gross Income: ₹3,00,000 | Taxable Income: ₹2,50,000. **Tax: ₹0.00** (Taxable income is below the ₹3,00,000 threshold). |
| **Tax Slab 2** | Income Tax (1) | Gross Income: ₹5,00,000 | Taxable Income: ₹4,50,000. Tax on (450k-300k=150k) @ 5%. Tax = ₹7,500. **Total Tax: ₹7,800.00** (₹7,500 \* 1.04) |
| **Tax Slab 5+** | Income Tax (1) | Gross Income: ₹20,00,000 | Taxable Income: ₹19,50,000. Tax should be substantial, calculated across multiple slabs up to 30%. |
| **Sec 24(b) Cap** | Home Loan (2) | Loan: 50,00,000, Rate: 8.0, Period: 10 years | Annual Interest (Simple): ₹4,00,000. **Deduction: ₹2,00,000.00** (Capped by Section 24(b)) |
| **Sec 80E** | Education Loan (3) | Loan: 10,00,000, Rate: 10.0, Period: 5 years | Annual Interest (Simple): ₹2,00,000. **Deduction: ₹2,00,000.00** (No cap applied in 80E) |
