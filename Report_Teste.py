from reportlab.pdfgen import canvas

headerText = input()
subHeaderText = input()
def main(args):
    cnv = canvas.Canvas('Alo_Mundo.pdf')
    cnv.drawString(1,500,headerText)
    cnv.drawString(20,12,subHeaderText)

    cnv.save()
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

