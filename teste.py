import post_office_lib

data = "17/06/1992"
quebra_linha = "\n"
destinatario = "oi"
mensagem = "tudo bem ?"
remetente = "sdasdasdasd"
maior = ">"
menor = "<"


carta =  "<" + data + ">" +  quebra_linha + "<" + destinatario + ">" + quebra_linha +  "<" + mensagem + ">" + quebra_linha + "<" + remetente + ">" 
print (carta)

post_office_lib.escrever_carta(destinatario, data, carta)   



