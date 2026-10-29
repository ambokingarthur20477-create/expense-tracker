#Expense Tracker - Installment 4: the tracker makes decisions
#Author: King Arthur R. Ambo
#Description: The expense tracker that calculate tax, subtotal, and grand total, while evaluating budget status (Over Budget, Careful 90% threshold, or Within Budget) and displaying exact remaining or excess amounts.

# --- header ---

print("="* 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("="* 40)

# --- main menu ---

print("\nMAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)\n")

# --- user input ---

name = input("\nWhat is your name? ")
print(f"\nHello {name}! Let's log two expenses.")
print ()

# --- user input module 1: for expenses and amounts ---

item1 = input("First expense? ")
amount1 =float(input("Amount? "))

# --- Decision making Module 1:  for expense amount ---

if amount1 > 200: 
    print("Huge expense - are you sure?")
elif amount1 >= 100:
    print("Big expense.")
elif amount1 >= 50:
    print("Moderate expense.")
else:
    print("Small expense.")

# --- user input module 2: for expenses and amounts ---

item2 = input("Second expense? ")
amount2 =float(input("Amount? "))

# --- Decision making Module 2: for expense amount ---

if amount2 > 200: 
    print("Huge expense - are you sure?")
elif amount2 >= 100:
    print("Big expense.")
elif amount2 >= 50:
    print("Moderate expense.")
else:
    print("Small expense.")

# --- Early data processing for subtotal ---

subtotal = 0 
subtotal += amount1
subtotal += amount2

# --- Decision making Module 3: for subtotal ---
if subtotal > 100: 
    print("Two big expenses in a row - slow down!")


# --- user input module 3: for tax  ---

tax_percent = int(input("Tax rate? "))

# --- user input module 4: for budget ---

budget = float(input("Your budget? "))

# --- Data processing ---

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
left = budget - total

# --- summary ---

print()
print("-" * 40)
print("SUMMARY")
print(f"    - {item1}: \t\t\t\t${amount1:.2f}")
print(f"    - {item2}: \t\t\t\t${amount2:.2f}")
print(f"Subtotal: \t\t\t\t${subtotal:.2f}")
print(f"Average: \t\t\t\t${average:.2f}") 
print(f"Tax({tax_percent}%): \t\t\t\t${tax:.2f}")
print(f"Grand Total: \t\t\t\t${total:.2f}")

# --- Decision making Module 4: for budget ---

if total > budget:
    print(f"Over Budget: by \t\t\t${total - budget:.2f}")
elif total >= (0.9 * budget):
    print(f"Careful: only \t\t\t\t${left:.2f}")
else: 
    print(f"Within Budget \t\t\t\t${left:.2f}")

print("-" * 40)
print("Made by: King Arthur R. Ambo | Installment 4")