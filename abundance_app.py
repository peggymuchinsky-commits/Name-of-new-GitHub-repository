
import streamlit as st

st.set_page_config(page_title="Financial Abundance Tracker", layout="centered")

st.title("💸 Financial Abundance Tracker")

st.markdown("Track your income, expenses, and projected savings over time.")

# User input
income = st.number_input("Enter your monthly income ($)", min_value=0, step=100)

st.subheader("Expenses")
expense_categories = ["Rent", "Groceries", "Transportation", "Subscriptions", "Misc"]
expenses = {}
for category in expense_categories:
    expenses[category] = st.number_input(f"{category} ($)", min_value=0, step=50)

goal = st.number_input("Set your total savings goal ($)", min_value=0, step=500)

months = st.slider("Projection Period (months)", 1, 24, 6)

# Calculate balance and savings
total_expenses = sum(expenses.values())
balance = income - total_expenses
projected_savings = balance * months

# Display summary
st.markdown("---")
st.subheader("📊 Summary")
st.write(f"**Total Monthly Expenses:** ${total_expenses}")
st.write(f"**Remaining Monthly Balance:** ${balance}")
st.write(f"**Projected Savings in {months} months:** ${projected_savings}")

# Goal feedback
st.markdown("---")
if projected_savings >= goal:
    st.success(f"✅ You will hit your goal of ${goal} in {months} months!")
else:
    st.warning(f"⚠️ You need to either increase income or reduce expenses to reach your goal.")

st.markdown("💡 Tip: Abundance isn't just about how much you earn, it's about how you manage and multiply what you keep.")
