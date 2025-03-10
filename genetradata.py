import sqlite3
import random
from faker import Faker # type: ignore

fake = Faker()
conn = sqlite3.connect("personal_finance.db")
cursor = conn.cursor()

# Enable foreign keys in SQLite
cursor.execute("PRAGMA foreign_keys = ON;") 
cursor.execute("DROP TABLE IF EXISTS Savings")
cursor.execute("DROP TABLE IF EXISTS Expense")
cursor.execute("DROP TABLE IF EXISTS Income")
cursor.execute("DROP TABLE IF EXISTS Clients")

cursor.execute('''CREATE TABLE IF NOT EXISTS Clients (
        Client_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Client_Name TEXT NOT NULL
    )
''')

# Income Table (Allows multiple income entries per client)
cursor.execute('''
               
    CREATE TABLE IF NOT EXISTS Income (
        Income_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Client_ID INTEGER NOT NULL,
        Source TEXT NOT NULL,
        Amount REAL NOT NULL,
        Income_Date DATE NOT NULL,
        Category TEXT NOT NULL,
        Payment_Method TEXT NULL,
    FOREIGN KEY (Client_ID) REFERENCES Clients(Client_ID) ON DELETE CASCADE    )
''')






cursor.execute('''CREATE TABLE IF NOT EXISTS Expense (
    Expense_ID INTEGER PRIMARY KEY AUTOINCREMENT,  
    Client_ID INTEGER NOT NULL,  
    Category TEXT NOT NULL,  
    Expense_Date DATE NOT NULL,  
    Amount REAL NOT NULL, 
    Payment_Method TEXT  NULL,  
    Priority_Level TEXT CHECK (Priority_Level IN ('Essential', 'Non-Essential', 'Other')) NOT NULL, 
FOREIGN KEY (Client_ID) REFERENCES Clients(Client_ID) ON DELETE CASCADE);''')

# -- 3. Savings Table (Tracks money saved by the client)
cursor.execute('''CREATE TABLE IF NOT EXISTS Savings (
    Saving_ID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each saving entry
    Client_ID INTEGER NOT NULL,  -- Foreign Key linking to clent Table
    Expense_ID INTEGER NOT NULL,  -- Foreign Key linking to Expense Table
    Saving_Type TEXT NOT NULL,  -- Emergency Fund, Retirement, Vacation, etc.
    Payment_Method TEXT  NULL,  -- Bank Transfer, Cash, Investment Account
    Saving_Date DATE NOT NULL,  -- Date of saving
    Amount_Saved REAL NOT NULL,  -- Total money saved
    Interest_Rate REAL  NULL,  -- Interest earned on savings
    FOREIGN KEY (Client_ID) REFERENCES Clients(Client_ID) ON DELETE CASCADE
    FOREIGN KEY (Expense_ID) REFERENCES Expense(Expense_ID) ON DELETE CASCADE
);''')
print("tablecreated")


conn.commit()
conn.close()