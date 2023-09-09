from fpdf import FPDF
import pandas as pd

# FPDF is an object or say its a class.
# Firstly adding basic code and trying

# an object for pdf
pdf = FPDF(orientation="L", format="a4", unit="mm")

df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    # adding new page to this pdf
    pdf.add_page()

    # setting a new font it will be set for all cell down from this line
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(250, 0, 0)

    # it's advised to set height of cell equals to font size.
    # adding any data is done by cell the flow of code matters.
    pdf.cell(w=0, ln=1, h=24, border=0, txt=row["Topic"], align="L")

    # we need a line and it will be decided by x and y axis so give coordinated of starting and ending points
    pdf.line(11, 27, 270, 27)

# to shown output name of file is parameter
pdf.output("output.pdf")
