from fpdf import FPDF
# FPDF is an object or say its a class.
# Firstly adding basic code and trying

# an object for pdf
pdf = FPDF(orientation="L", format="a4", unit="mm")

# adding new page to this pdf
pdf.add_page()

# setting a new font it will be set for all cell down from this line
pdf.set_font(family="Times", style="BU", size=12)

# it's advised to set height of cell equals to font size.
# adding any data is done by cell the flow of code matters..
pdf.cell(w=0, ln=1, h=12, border=1, txt="Hello there", align="L")
pdf.cell(w=0, ln=1, h=12, border=1, txt="Namaste!", align="L")

# to shown output name of file is parameter
pdf.output("output.pdf")