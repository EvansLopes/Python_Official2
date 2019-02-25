from reportlab.pdfgen import canvas

headerText = input().center(164)
subHeaderText = input().center(164)

def main(args):
    cnv = canvas.Canvas('Relatorio de texto.pdf')
    cnv.drawString(1,820,'Título: ' + headerText)
    cnv.drawString(1,818,'Nome: ' + subHeaderText)

    cnv.save()
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

