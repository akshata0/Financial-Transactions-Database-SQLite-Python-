import sqlite3
import random
from faker import Faker

# Initialize Faker for generating fake names & data
fake = Faker()

# Connect to SQLite database
conn = sqlite3.connect("personal_finance.db")
cursor = conn.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON;")


clients = [(fake.name(),) for _ in range(10)]  
cursor.executemany("INSERT INTO Clients (Client_Name) VALUES (?)", clients)

cursor.execute("SELECT Client_ID FROM Clients")
client_ids = [row[0] for row in cursor.fetchall()]

print(" Clients inserted")


income_sources = ["Salary", "Freelancing", "Investments", "Business", "Rental Income"]
categories = ["Active", "Passive", "Bonus"]
payment_methods = ["Bank Transfer", "Cash", "PayPal"]

for client_id in client_ids:
    num_sources = random.randint(3, 4)  
    for _ in range(num_sources):
        source = random.choice(income_sources)
        amount = round(random.uniform(5000, 50000), 2)
        income_date = fake.date_between(start_date="-5y", end_date="today")
        category = random.choice(categories)
        
        payment_method = random.choice(payment_methods) if random.random() > 0.2 else None

        cursor.execute("""
            INSERT INTO Income (Client_ID, Source, Amount, Income_Date, Category, Payment_Method)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (client_id, source, amount, income_date, category, payment_method))

        
        if random.random() < 0.1:
            cursor.execute("""
                INSERT INTO Income (Client_ID, Source, Amount, Income_Date, Category, Payment_Method)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (client_id, source, amount, income_date, category, payment_method))

print("Income data inserted")

expense_categories = {
    "Rent": "Essential", "EMI": "Essential", "Car Loan": "Essential", 
    "Savings": "Other", "Groceries": "Essential", "School Fee": "Essential", 
    "Gym": "Non-Essential", "Netflix Subscription": "Non-Essential", 
    "Electricity Bill": "Essential", "Income Tax": "Essential", "Water Bill": "Essential", "Other": "Other"
}
expense_payment_methods = ["Credit Card", "Cash", "Bank Transfer", "UPI"]

for _ in range(1000):
    client_id = random.choice(client_ids)  
    category = random.choice(list(expense_categories.keys()))
    expense_date = fake.date_between(start_date="-5y", end_date="today")  
    amount = round(random.uniform(500, 50000), 2) 
 
    payment_method = random.choice(expense_payment_methods) if random.random() > 0.2 else None
    
    priority_level = expense_categories[category]  

    cursor.execute("""
        INSERT INTO Expense (Client_ID, Category, Expense_Date, Amount, Payment_Method, Priority_Level)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (client_id, category, expense_date, amount, payment_method, priority_level))

    # 10% chance of inserting a duplicate expense
    if random.random() < 0.1:
        cursor.execute("""
            INSERT INTO Expense (Client_ID, Category, Expense_Date, Amount, Payment_Method, Priority_Level)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (client_id, category, expense_date, amount, payment_method, priority_level))

print("Expense data inserted")

cursor.execute("SELECT Expense_ID, Client_ID FROM Expense WHERE Category = 'Savings'")
expense_savings = cursor.fetchall()

if not expense_savings:
    print("No 'Savings' expenses found")
else:
    saving_categories = ["Stock", "Crypto", "Vacation", "Emergency Fund", "Medical Insurance", "Term Insurance", "SIP", "Gold Bonds"]
    saving_payment_methods = ["Bank Transfer", "UPI", "Credit Card", "Investment Account"]

    for _ in range(1000):
        expense_id, client_id = random.choice(expense_savings)  
        saving_type = random.choice(saving_categories)
        amount_saved = round(random.uniform(1000, 100000), 2)
        saving_date = fake.date_between(start_date="-5y", end_date="today")
        
        interest_rate = round(random.uniform(2, 12), 2) if random.random() > 0.2 else None
        
        payment_method = random.choice(saving_payment_methods)

        cursor.execute("""
            INSERT INTO Savings (Client_ID, Expense_ID, Saving_Type, Payment_Method, Saving_Date, Amount_Saved, Interest_Rate)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (client_id, expense_id, saving_type, payment_method, saving_date, amount_saved, interest_rate))

print("Savings data inserted")

conn.commit()
conn.close()

print("All data inserted")
