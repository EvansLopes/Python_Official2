teste = open('testeTxt.html', 'w')
teste2 = open('testeExcel.xls','w')
teste3 = open('testeWord.docx','w')
teste4 = open('testeCSV.csv','w')
teste5 = open('testePython.py','w')

docx = input()
csv = input()


teste.write(docx)
teste.close()

teste2.write(csv)
teste3.write(input())
teste4.write(input())
teste5.write(input())


teste2.close()
teste3.close()
teste4.close()
teste5.close()