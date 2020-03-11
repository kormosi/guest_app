from weasyprint import HTML


class Weasy():

    def weasy():
        print("sucess!")
        HTML('http://weasyprint.org/').write_pdf('weasyprint-website.pdf')
