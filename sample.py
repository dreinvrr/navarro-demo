def check_loan_eligibility(monthly_salary, loan_amount):
    if monthly_salary < 30000.00:
        return False, "Your monthly salary is below the minimum requirement of 30,000.00"
    elif loan_amount > 10 * monthly_salary:
        return False, "The requested loan amount exceeds 10 times your monthly salary"
    else:
        return True, "You are eligible for the loan"

def calculate_loan_with_interest(loan_amount, months):
    interest_rate = 0.10  # 10% interest
    total_amount = loan_amount * (1 + interest_rate)
    monthly_payment = total_amount / months
    return total_amount, monthly_payment

def main():
    monthly_salary = float(input("Enter your monthly salary: "))
    loan_amount = float(input("Enter the loan amount requested: "))

    eligible, message = check_loan_eligibility(monthly_salary, loan_amount)

    if eligible:
        print(message)
        months = int(input("Enter the number of months for repayment: "))
        total_amount, monthly_payment = calculate_loan_with_interest(loan_amount, months)
        print(f"Total amount to be repaid: {total_amount:.2f}")
        print(f"Monthly payment: {monthly_payment:.2f}")
    else:
        print(f"Loan not approved. Reason: {message}")

if __name__ == "__main__":
    main()