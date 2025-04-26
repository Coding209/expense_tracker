import streamlit as st

# === Core Functions (Unchanged) ===
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        st.write(f'Amount: ${expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)

def filter_expenses_by_category(expenses, category):
    return [expense for expense in expenses if expense['category'] == category]

# === Streamlit App ===
st.title("Simple Expense Tracker with Budget")

# Store expenses and budget in session state
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

if 'budget' not in st.session_state:
    st.session_state.budget = 0

# Set budget
st.sidebar.header("Set Your Budget")
budget_input = st.sidebar.number_input("Monthly Budget", min_value=0.0)
if st.sidebar.button("Update Budget"):
    st.session_state.budget = budget_input
    st.success(f"Budget updated to ${st.session_state.budget:.2f}")

# Add expense form
st.subheader("Add a New Expense")
with st.form("expense_form"):
    amount = st.number_input("Amount", min_value=0.0)
    category = st.text_input("Category")
    submitted = st.form_submit_button("Add Expense")
    if submitted:
        if category.strip():
            add_expense(st.session_state.expenses, amount, category)
            st.success("Expense added!")
        else:
            st.warning("Please enter a valid category.")

# Show expenses
st.subheader("All Expenses")
if st.session_state.expenses:
    print_expenses(st.session_state.expenses)
else:
    st.write("No expenses yet.")

# Show total
st.subheader("Total Spent")
total = total_expenses(st.session_state.expenses)
st.write(f"${total}")

# Budget comparison
st.subheader("Budget Overview")
if st.session_state.budget > 0:
    remaining = st.session_state.budget - total
    st.write(f"Budget: ${st.session_state.budget}")
    if remaining >= 0:
        st.success(f"You are within budget. Remaining: ${remaining:.2f}")
    else:
        st.error(f"You exceeded the budget by ${abs(remaining):.2f}")
else:
    st.info("No budget set yet.")

# Filter by category
st.subheader("Filter by Category")
categories = list(set([e['category'] for e in st.session_state.expenses]))
if categories:
    selected = st.selectbox("Select a category", categories)
    filtered = filter_expenses_by_category(st.session_state.expenses, selected)
    st.write(f"Expenses for {selected}:")
    print_expenses(filtered)

