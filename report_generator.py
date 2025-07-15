
import pandas as pd
from fpdf import FPDF

# Read the CSV file
data = pd.read_csv("data.csv")

# Get summary statistics (only for numbers)
summary = data.describe()

# Create a PDF object
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add a title
pdf.cell(200, 10, txt="Summary Report", ln=True, align='C')
pdf.ln(10)  # Add some space

# Loop through each column and add mean and std to PDF
for column in summary.columns:
    mean = summary[column]["mean"]
    std = summary[column]["std"]
    text = f"{column} - Mean: {mean:.2f}, Std: {std:.2f}"
    pdf.cell(200, 10, txt=text, ln=True)

# Save the PDF file
pdf.output("report.pdf")

print("Report has been saved as report.pdf")
