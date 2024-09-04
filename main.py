from fpdf import FPDF
import pandas as pd

# Initialize the PDF object with A4 page size
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Disable auto page breaks for custom control
pdf.set_auto_page_break(auto=False, margin=0)

# Read the CSV file containing topics and number of pages
df = pd.read_csv("topics.csv")

# Iterate through each row of the DataFrame
for index, row in df.iterrows():
    # Add a new page for each topic
    pdf.add_page()

    # Set the font for the header and add the topic title
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Draw horizontal lines across the page for styling
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Add the footer for the first page
    pdf.ln(265)  # Move down to the footer area
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

    # Add additional pages for the topic if needed
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer for the additional page
        pdf.ln(277)  # Move down to the footer area
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

        # Draw horizontal lines across the page for styling
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

# Output the final PDF to a file
pdf.output("output.pdf")
