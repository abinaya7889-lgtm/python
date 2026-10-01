import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [120, 150, 180, 160, 210, 250]

products = ["Laptop", "Mobile", "Tablet", "Watch"]

product_sales = [50, 80, 40, 30]

expenses = ["Food", "Travel", "Education", "Shopping"]

expense = [35, 20, 25, 20]

# Create dashboard
plt.figure(figsize=(12, 8))

# Line Chart
plt.subplot(2, 2, 1)

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid()

# Bar Chart
plt.subplot(2, 2, 2)

plt.bar(products, product_sales)

plt.title("Product Sales Comparison")
plt.xlabel("Product")
plt.ylabel("Sales")

# Pie Chart
plt.subplot(2, 2, 3)

plt.pie(
    expense,
    labels=expenses,
    autopct="%1.1f%%"
)

plt.title("Expense Distribution")

# Another Line Chart
plt.subplot(2, 2, 4)

students = ["A", "B", "C", "D", "E"]

marks = [80, 70, 90, 75, 85]

plt.plot(students, marks, marker="o")

plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.grid()

# Main title
plt.suptitle("DATA VISUALIZATION DASHBOARD")

plt.tight_layout()

# Save dashboard image
plt.savefig("data_visualization_dashboard.png")

# Display dashboard
plt.show()