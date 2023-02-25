import pdfkit

html = "<h1>Test</h1>"

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
# pdfkit.from_url('pdfgen/templates/pdfgen/resume_light.html', 'resume_light.pdf', configuration=config)
pdf = pdfkit.from_string(html, "test.pdf", configuration=config)

print(type(pdf))
