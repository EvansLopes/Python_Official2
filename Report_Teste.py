from reportlab.pdfgen import canvas

headerText = input().center(0)
subHeaderText = input().center(0)
print(164-(len(headerText)/2))

def main(args):
    cnv = canvas.Canvas('Relatorio de texto.pdf')
    cnv.drawString(164-(len(headerText)/2), 800, 'Título: ' + headerText)
    cnv.drawString(164-(len(subHeaderText)/2), 788, 'Nome: ' + subHeaderText)
#-(len(headerText)/2)
    cnv.drawString(30, 770, 'Nome do funcionário')
    cnv.drawString(230, 770, 'Idade do funcionário')
    cnv.drawString(400, 770, 'Cidade do Funcionário')
    cnv.save()
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))