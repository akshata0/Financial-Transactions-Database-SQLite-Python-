# Financial-Transactions-Database-SQLite-Python-

Project Overview
This project involves creating a financial transactions database using SQLite and Python. The database is designed to store and manage clients' income, expenses, and savings efficiently. The tables are created using SQL DDL statements executed via Python’s sqlite3 module.

Database Schema
The database consists of four main tables:

Clients – Stores client details (Client_ID, Client_Name).
Income – Tracks income sources, amounts, and payment methods.
Expense – Records expenses with categories, priority levels, and payment methods.
Savings – Links savings to expenses and stores saving types and interest rates.
The schema is designed using foreign keys to ensure referential integrity.

Key Features
✔ SQLite for lightweight, local database storage
✔ Python’s sqlite3 library to execute SQL queries
✔ Structured ER Diagram for relational mapping
✔ Secure and efficient data management with constraints

Project Files
database_creation.py – Python script to generate the SQLite database and tables.
er_diagram.png – ER Diagram representing the database schema.
sample_data.py – Script to insert sample financial records.
README.md – This file with project details.
