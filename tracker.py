#Expense Tracker - Installment 3: tracker does math
#Author: King Arthur R. Ambo
#Description: tracker does logical and mathematical operations for tax, subtotal, grand total, over budget(True or False), and budget left.

print("="* 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("="* 40)

#print("\nWelcome! This is your personal expense tracker.")
#as instructed, the welcome header is removed.

print("\nMAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)\n")

# --- user input ---

name = input("\nWhat is your name? ")
print(f"\nHello {name}! Let's log two expenses.")
print ()

subtotal = 0 

item1 = input("First expense? ")
amount1 =float(input("Amount? "))

item2 = input("Second expense? ")
amount2 =float(input("Amount? "))

tax_percent = int(input("Tax rate? "))

budget = float(input("Your budget? "))

# --- Data processing ---
subtotal += amount1
subtotal += amount2

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

over_budget = total > budget
left = budget - total

# --- summary ---

print()
print("-" * 40)
print("SUMMARY")
print(f"    - {item1}:\t\t${amount1:.2f}")
print(f"    - {item2}:\t\t${amount2:.2f}")
print(f"Subtotal:\t\t${subtotal:.2f}")
print(f"Average:\t\t${average:.2f}") 
print(f"Tax({tax_percent}%):\t\t${tax:.2f}")
print(f"Grand Total:\t\t${total:.2f}")
print(f"Over Budget?\t\t{over_budget}")
print(f"Left in budget:\t\t${left:.2f}")
print("-" * 40)
print("Made by: King Arthur R. Ambo | Installment 3")
