from reportlab.pdfgen import canvas

texto1 = input()
def main(args):
    cnv = canvas.Canvas('Alo_Mundo.pdf')
    cnv.drawString(150,450,texto1)
    cnv.save()
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

