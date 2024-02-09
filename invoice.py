import pdfkit

# Path to wkhtmltopdf executable
config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")

# HTML file path
html_file = "invoice.html"

# PDF file path
pdf_file = "output.pdf"

# Convert HTML to PDF
pdfkit.from_file(html_file, pdf_file, configuration=config)
