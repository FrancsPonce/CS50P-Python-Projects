from fpdf import FPDF

name = input("Name: ")

class PDF():
    def __init__(self,name):
        self._pdf = FPDF()

        self._pdf.add_page()

        self._pdf.set_font("helvetica", "B", 50)


        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT",align="C")

        self._pdf.image("shirtificate.png", w=self._pdf.epw)

        self._pdf.set_font_size(34)

        self._pdf.set_text_color(255,255,255)

        self._pdf.text(x= 48 , y= 140, txt= f" {name} took CS50")


    def save(self,name):
        self._pdf.output(name)


convert_pdf= PDF(name)
convert_pdf.save("shirtificate.pdf")
