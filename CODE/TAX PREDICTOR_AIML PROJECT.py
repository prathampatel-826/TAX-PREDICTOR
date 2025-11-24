def calculate_income_tax(taxable_income):
    if taxable_income <= 0:
        tax = 0
    elif taxable_income <= 300000:
        tax = 0
    elif taxable_income <= 700000:
        tax = (taxable_income - 300000) * 0.05
    elif taxable_income <= 1000000:
        tax = (700000 - 300000) * 0.05 + (taxable_income - 700000) * 0.10
    elif taxable_income <= 1200000:
        tax = (700000 - 300000) * 0.05 + (1000000 - 700000) * 0.10 + (taxable_income - 1000000) * 0.15
    elif taxable_income <= 1500000:
        tax = (700000 - 300000) * 0.05 + (1000000 - 700000) * 0.10 + (1200000 - 1000000) * 0.15 + (taxable_income - 1200000) * 0.20
    else:
        tax = (700000 - 300000) * 0.05 + (1000000 - 700000) * 0.10 + (1200000 - 1000000) * 0.15 + (1500000 - 1200000) * 0.20 + (taxable_income - 1500000) * 0.30
    
    total_tax = tax * 1.04
    return total_tax

def calculate_home_loan_deduction(loan_amount, interest_rate, time_period_years):
    total_interest = loan_amount * (interest_rate / 100) * time_period_years
    annual_deduction = min(total_interest / time_period_years, 200000)
    return annual_deduction

def calculate_education_loan_deduction(loan_amount, interest_rate, time_period_years):
    total_interest = loan_amount * (interest_rate / 100) * time_period_years
    annual_deduction = total_interest / time_period_years
    return annual_deduction

def calculate_property_tax_or_deduction(property_value, type_of_property):
    if type_of_property.lower() == 'purchase':
        deduction = min(property_value * 0.1, 150000)  
    else:
        deduction = 0
    return deduction

def main():
    print("Indian Tax Predictor")
    print("Choose the type of tax/deduction to calculate:")
    print("1. Income Tax")
    print("2. Home Loan Interest Deduction")
    print("3. Education Loan Interest Deduction")
    print("4. Property Tax/Deduction")
    print("5. House Tax (Municipal Property Tax - Basic Estimate)")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == '1':
        try:
            income = float(input("Enter your annual gross income in rupees: "))
            taxable_income = income - 50000 
            tax = calculate_income_tax(taxable_income)
            print(f"Taxable Income (after ₹50,000 deduction): ₹{taxable_income:.2f}")
            print(f"Estimated Income Tax: ₹{tax:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    elif choice == '2':
        try:
            loan_amount = float(input("Enter loan amount in rupees: "))
            interest_rate = float(input("Enter annual interest rate (e.g., 8.5): "))
            time_period = float(input("Enter time period in years: "))
            deduction = calculate_home_loan_deduction(loan_amount, interest_rate, time_period)
            print(f"Annual Home Loan Interest Deduction: ₹{deduction:.2f}")
            print("Note: This can reduce your taxable income under Section 24(b).")
        except ValueError:
            print("Invalid input. Please enter numbers.")
    
    elif choice == '3':
        try:
            loan_amount = float(input("Enter loan amount in rupees: "))
            interest_rate = float(input("Enter annual interest rate (e.g., 8.5): "))
            time_period = float(input("Enter time period in years: "))
            deduction = calculate_education_loan_deduction(loan_amount, interest_rate, time_period)
            print(f"Annual Education Loan Interest Deduction: ₹{deduction:.2f}")
            print("Note: This can reduce your taxable income under Section 80E.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
    
    elif choice == '4':
        try:
            property_value = float(input("Enter property value in rupees: "))
            type_of_property = input("Type of property (e.g., purchase, sale): ").strip()
            deduction = calculate_property_tax_or_deduction(property_value, type_of_property)
            print(f"Estimated Property Deduction: ₹{deduction:.2f}")
            print("Note: This is a rough estimate for deductions under Section 80C or capital gains.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
    
    elif choice == '5':
        try:
            property_value = float(input("Enter property value in rupees (for tax base): "))
            tax_rate = 0.002  
            house_tax = property_value * tax_rate
            print(f"Estimated House Tax (Municipal): ₹{house_tax:.2f}")
            print("Note: Actual rates vary by location; consult local authorities.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    else:
        print("Invalid choice. Please select 1-5.")
    
    again = input("Calculate another? (y/n): ").lower()
    if again == 'y':
        main()
    else:
        print("Goodbye!")
        
if __name__ == "__main__":
    main()
