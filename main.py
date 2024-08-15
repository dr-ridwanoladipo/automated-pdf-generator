from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    for i in range(row["Pages"] -1):
        pdf.add_page()

pdf.output("output.pdf")


# pdf.cell(w=0, h=12, txt="Hello there!", align="L", ln=1, border=1)
# pdf.set_font(family="Times", size=12)
# pdf.cell(w=0, h=12, txt="Hi Aminat!", align="L", ln=1)

