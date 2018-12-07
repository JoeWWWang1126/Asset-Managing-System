import pdfkit
class getpdf:
    def gpdf(self, HRID, HRName, AssetID, AssetName, TimeLimit,filename):
        body = """  <html>
            <head>
                <title>物料借用申请表</title>
            </head>
            <style type="text/css">
                body {background-color: rgb(84, 209, 178)}
                p {margin-left: 20px;text-align: center;font-size: 70px;color: rgb(14, 13, 13);font-family: verdana;}
                h2{text-align: right;font-family: Verdana;}
                h3{font-size: 35px}
                a{font-size: 25px;font-style: italic;}
                h4{text-align: center; font-size: 30px;color: tomato;font-family:sans-serif;}
                </style>
            <body>
                <p>Application Sheet</p>
                <h3>Employee ID:</h3><h4> """ + HRID + """</h4>
                <h3>Employee Name:</h3><h4>""" + HRName + """</h4>
                <h3>Asset ID:</h3><h4>""" + AssetID + """</h4>
                <h3>Asset Name:</h3><h4>""" + AssetName + """</h4>
                <h3>Period:</h3><h4>""" + TimeLimit + """ Days</h4>
                
                <br><br><br><br><br><br><br><br><br><br>
                <h2>Signature:______________</h2>
                <a href="mailto:joe_wwang@outlook.com">Mail to The Admin</a>

            </body>
        </html>
            """
        pdfkit.from_string(body, filename)


# pdfkit.from_string(body, 'out.pdf')
# pdfkit.from_file('test3.html',r'C:\Users\HP\Desktop\file_pdf.pdf')