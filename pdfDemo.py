from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
class MakingPdf:
    def pdfMaker(self,c, HRID, HRName, AssetID, AssetName, TimeLimit):
        from reportlab.lib.units import inch
        c.translate(inch, inch)
        c.setFont("Helvetica", 20)
        c.drawString(1.6 * inch, 9 * inch, 'Material Application Form')
        c.setFont("Helvetica", 15)
        c.drawString(0.5 * inch, 8 * inch, "Employee ID: " + HRID)
        c.drawString(0.5 * inch, 7.5 * inch, "Employee Name: " + HRName)
        c.drawString(-2 * inch, 6.5 * inch,
                     "-------------------------------Items----------------------------------------------------------------------------------------------------")
        c.drawString(0.5 * inch, 6 * inch, 'Fixed Asset ID: ' + AssetID)
        c.drawString(0.5 * inch, 5 * inch, 'Fixed Asset Name: ' + AssetName)
        c.drawString(0.5 * inch, 4 * inch, 'Time Limit: ' + TimeLimit)
        c.drawString(3 * inch, 0, "Signature For Apply _______________")
        c.drawString(3 * inch, -0.5 * inch, "Signature For Confirm _______________")



