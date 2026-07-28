basic = float(input("Enter Basic Salary: "))

da = basic * 10 / 100
hra = basic * 20 / 100
gross_salary = basic + da + hra

pf = basic * 12 / 100
professional_tax = 200
income_tax = gross_salary * 5 / 100

total_deductions = pf + professional_tax + income_tax
net_salary = gross_salary - total_deductions
annual_salary = net_salary * 12

print("\n===== SALARY SLIP =====")
print("Basic Salary:", basic)
print("DA:", da)
print("HRA:", hra)
print("Gross Salary:", gross_salary)
print("PF:", pf)
print("Professional Tax:", professional_tax)
print("Income Tax:", income_tax)
print("Total Deductions:", total_deductions)
print("Net Salary:", net_salary)
print("Annual Salary:", annual_salary)