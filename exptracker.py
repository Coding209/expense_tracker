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
st.title("Simple Expense Tracker")

# Store expenses and budget in session state
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# --- Budget Input (Challenge 1) ---
st.subheader("Set Your Budget")
budget = st.number_input("Enter your budget amount", min_value=0.0)

# --- Expense Form ---
st.subheader("Add a New Expense")
with st.form("expense_form"):
    amount = st.number_input("Amount", min_value=0.0, key="expense_amount")
    category = st.text_input("Category")
    submitted = st.form_submit_button("Add Expense")
    if submitted:
        if category.strip():
            add_expense(st.session_state.expenses, amount, category)
            st.success("Expense added!")
        else:
            st.warning("Please enter a valid category.")

# --- Show Expenses ---
st.subheader("All Expenses")
if st.session_state.expenses:
    print_expenses(st.session_state.expenses)
else:
    st.write("No expenses yet.")

# --- Show Total ---
st.subheader("Total Spent")
total = total_expenses(st.session_state.expenses)
st.write(f"${total}")

# --- Budget Comparison (Challenge 2) ---
st.subheader("Budget Overview")
if budget > 0:
    remaining = budget - total
    if remaining >= 0:
        st.success(f"You are within budget. Remaining: ${remaining:.2f}")
    else:
        st.error(f"You exceeded the budget by ${abs(remaining):.2f}")
else:
    st.info("No budget entered yet.")

# --- Filter by Category ---
st.subheader("Filter by Category")
categories = list(set([e['category'] for e in st.session_state.expenses]))
if categories:
    selected = st.selectbox("Select a category", categories)
    filtered = filter_expenses_by_category(st.session_state.expenses, selected)
    st.write(f"Expenses for {selected}:")
    print_expenses(filtered)


