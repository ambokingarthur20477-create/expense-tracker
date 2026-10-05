#Expense Tracker - Installment 2: Talking to the User
#Author: King Arthur R. Ambo
#Description: ask for two expense and prints a summary.

print("="* 50)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("="* 50)

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

item1 = input("First expense? ")
amount1 =float(input("Amount? "))
item2 = input("Second expense? ")
amount2 =float(input("Amount? "))

# --- Data processing ---

total = amount1 + amount2
average = (amount1 + amount2) / 2

# --- summary ---

print()
print("-" * 50)
print("SUMMARY")
print(f"    - {item1}:\t\t${amount1:.2f}")
print(f"    - {item2}:\t\t${amount2:.2f}")
print(f"    - total:\t\t${total:.2f}")
print(f"    - average:\t\t${average:.2f}") 
print("-" * 50)

print("-" * 50)
print("Made by: King Arthur R. Ambo | Installment 2")
print("=" * 50)

