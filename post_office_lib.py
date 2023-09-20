from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def remover_barra(data):
    data_nova = data.replace("/", ".")
    return data_nova

def escrever_carta(destinatario, data, carta):
    data_nova = remover_barra(data)
    print(data_nova)
    nome_arquivo = destinatario + data_nova + ".txt"
    arquivo = open(nome_arquivo, "w")
    arquivo.write(carta)

def gerar_pdf(carta, destinatario, data):  
    data_nova = remover_barra(data)  
    # Abra o arquivo PDF para escrita
    pdf_filename = destinatario + data_nova + '.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Escreva conteúdo no arquivo PDF
    c.drawString(100, 750, carta)

    # Salve o arquivo PDF e feche o objeto canvas
    c.save()

    print(f"Arquivo PDF '{pdf_filename}' criado com sucesso.")