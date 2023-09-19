def escrever_carta(destinatario, data, carta):
    data_nova = data.replace("/", ".")
    print(data_nova)
    nome_arquivo = destinatario + data_nova + ".txt"
    arquivo = open(nome_arquivo, "w")
    arquivo.write(carta)

