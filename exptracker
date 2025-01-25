import streamlit as st

# Sample expense list
expenses = []

# Function to add a new expense
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Function to print expenses
def print_expenses(expenses):
    if not expenses:
        st.write("No expenses to show.")
    else:
        for expense in expenses:
            st.write(f"Amount: {expense['amount']}, Category: {expense['category']}")

# Function to calculate total expenses
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# Function to filter expenses by category
def filter_expenses_by_category(expenses, category):
    return list(filter(lambda expense: expense['category'] == category, expenses))

# Streamlit app interface
st.title("Expense Tracker App")

# Sidebar for navigation
st.sidebar.header("Options")
option = st.sidebar.selectbox(
    "Select an option",
    ["Add an expense", "List all expenses", "Show total expenses", "Filter expenses by category"]
)

if option == "Add an expense":
    st.header("Add a New Expense")
    amount = st.number_input("Enter amount", min_value=0.01, step=0.01)
    category = st.text_input("Enter category")
    
    if st.button("Add Expense"):
        if amount > 0 and category:
            add_expense(expenses, amount, category)
            st.success(f"Expense of ${amount} for {category} added!")
        else:
            st.warning("Please provide valid inputs for both amount and category.")

elif option == "List all expenses":
    st.header("All Expenses")
    print_expenses(expenses)

elif option == "Show total expenses":
    st.header("Total Expenses")
    total = total_expenses(expenses)
    st.write(f"Total Expenses: ${total:.2f}")

elif option == "Filter expenses by category":
    st.header("Filter Expenses by Category")
    category = st.text_input("Enter category to filter")
    
    if st.button("Filter"):
        if category:
            filtered_expenses = filter_expenses_by_category(expenses, category)
            st.write(f"Expenses for {category}:")
            print_expenses(filtered_expenses)
        else:
            st.warning("Please enter a category to filter.")

