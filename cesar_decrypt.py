texto = input("texto: ")
n_casas = int(input("numero de casas: "))
n_text = ""

if(n_casas > 26):
    n_casas = n_casas % 26

for i in range(len(texto)):
    a_l_atual = ord(texto[i])
    if((65 <= a_l_atual and a_l_atual <= 90) or
        (97 <= a_l_atual and a_l_atual <= 122)):
        n_soma = a_l_atual - n_casas
        if(n_soma < 65 and a_l_atual <= 90):
            n_soma = 91-(65-n_soma)
        if(n_soma < 97 and (a_l_atual >= 97 and
            a_l_atual <= 122)):
            n_soma = 123-(97-n_soma)
        n_text += chr(n_soma)
    else:
        n_text += chr(a_l_atual)

print(n_text)
