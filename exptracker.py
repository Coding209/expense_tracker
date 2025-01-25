import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state for expenses
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Function to add a new expense
def add_expense(amount, category):
    st.session_state.expenses.append({'amount': amount, 'category': category})

# Function to display all expenses
def display_expenses(expenses):
    if not expenses:
        st.write("No expenses to show.")
    else:
        # Create a pandas DataFrame for better presentation
        df = pd.DataFrame(expenses)
        st.write(df)

# Function to calculate total expenses
def total_expenses(expenses):
    return sum([expense['amount'] for expense in expenses])

# Function to filter expenses by category
def filter_expenses_by_category(expenses, category):
    return [expense for expense in expenses if expense['category'].lower() == category.lower()]

# Function to visualize expenses by category
def plot_expenses_by_category(expenses):
    if expenses:
        df = pd.DataFrame(expenses)
        category_totals = df.groupby('category')['amount'].sum()
        
        # Plot a pie chart
        fig, ax = plt.subplots()
        category_totals.plot(kind='pie', autopct='%1.1f%%', ax=ax, startangle=90)
        ax.set_ylabel('')
        st.pyplot(fig)
    else:
        st.write("No data available for chart.")

# Streamlit app interface
st.title("Expense Tracker App")

# Sidebar for navigation
st.sidebar.header("Options")
option = st.sidebar.selectbox(
    "Select an option",
    ["Add an expense", "List all expenses", "Show total expenses", "Filter expenses by category", "View expenses by category chart"]
)

# Add an expense
if option == "Add an expense":
    st.header("Add a New Expense")
    amount = st.number_input("Enter amount", min_value=0.01, step=0.01)
    category = st.text_input("Enter category")
    
    if st.button("Add Expense"):
        if amount > 0 and category:
            add_expense(amount, category)
            st.success(f"Expense of ${amount} for {category} added!")
        else:
            st.warning("Please provide valid inputs for both amount and category.")

# List all expenses
elif option == "List all expenses":
    st.header("All Expenses")
    display_expenses(st.session_state.expenses)

# Show total expenses
elif option == "Show total expenses":
    st.header("Total Expenses")
    total = total_expenses(st.session_state.expenses)
    st.write(f"Total Expenses: ${total:.2f}")

# Filter expenses by category
elif option == "Filter expenses by category":
    st.header("Filter Expenses by Category")
    category = st.text_input("Enter category to filter")
    
    if st.button("Filter"):
        if category:
            filtered_expenses = filter_expenses_by_category(st.session_state.expenses, category)
            st.write(f"Expenses for {category}:")
            display_expenses(filtered_expenses)
        else:
            st.warning("Please enter a category to filter.")

# View expenses by category chart
elif option == "View expenses by category chart":
    st.header("Expenses by Category Chart")
    plot_expenses_by_category(st.session_state.expenses)
