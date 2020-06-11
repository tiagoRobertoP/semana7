import random
from collections import Counter
import matplotlib.pyplot as plt
import math



def gera_sexo(quantidade_de_usuarios_na_rede):
    sexo =[]
    for i in range(quantidade_de_usuarios_na_rede):
        if (((random.randint(0,10))%2) == 0):
            sexo.append((i,"M"))
        else:
            sexo.append((i,"F"))
    return sexo                




def quantidade_de_amigos_por_sexo(gera_sexo):
    cont_sexo = []
    m = 0
    f = 0
    for j , i in gera_sexo:
        if (i == "M"):
            m += 1
        else:
            f += 1
    cont_sexo.append(m)  
    cont_sexo.append(f)      
    return (cont_sexo)        
    



def gera_idade(quantidade_de_usuarios_na_rede):
    idades = []
    for i in range(quantidade_de_usuarios_na_rede):
        idades.append((i,random.randint(18,60)))
    return idades


def gera_histograma_amigo_por_sexo(quantidade_de_amigos_por_sexo, qtde_usuarios_na_rede):
    x= ["M", "F"]
    xs = x
    ys = quantidade_de_amigos_por_sexo
    plt.bar(xs, ys)
    plt.axis([-1, 2, 0, qtde_usuarios_na_rede ])
    plt.title("Histograma da Contagem de Amigos por sexo")
    plt.xlabel("sexo")
    plt.ylabel("# de amigos")
    plt.show()


def idade(gera_idade):
    a = Counter(i for i, _ in gera_idade)
    b = Counter(i for _, i in gera_idade)
    tudo = a + b
    return Counter(x for x in b.values())



def gera_histograma_amigo_por_idade(idade, qtde_usuarios_na_rede):
    xs = range(qtde_usuarios_na_rede)
    ys = [idade[x] for x in xs]
    plt.bar(xs, ys)
    plt.axis([-0, qtde_usuarios_na_rede, 0, qtde_usuarios_na_rede])
    plt.title("Histograma da Contagem de Amigos")
    plt.xlabel("# de amigos")
    plt.ylabel("# de pessoas")
    plt.show()


def quantidade_de_usuarios_na_rede():
    return 100


def gera_amizades(numero_conexoes_desejado, qtde_usuarios_na_rede):
    conexoes = []
    for i in range(numero_conexoes_desejado):
        while True:
            u1 = random.randint(0, qtde_usuarios_na_rede - 1)
            u2 = random.randint(0, qtde_usuarios_na_rede - 1)
            if u1 != u2:
                conexoes.append((u1, u2))
                break
    return [aux for aux in set(conexoes)]


def quantidade_de_amigos(amizades):
    a = Counter(i for i, _ in amizades)
    b = Counter(i for _, i in amizades)
    tudo = a + b
    return Counter(x for x in tudo.values())


def gera_histograma_contagem_amigos(quantidade_de_amigos, qtde_usuarios_na_rede):
    xs = range(qtde_usuarios_na_rede)
    ys = [quantidade_de_amigos[x] for x in xs]
    plt.bar(xs, ys)
    plt.axis([0, qtde_usuarios_na_rede, 0, qtde_usuarios_na_rede / 4])
    plt.title("Histograma da Contagem de Amigos")
    plt.xlabel("# de amigos")
    plt.ylabel("# de pessoas")
    plt.show()


def media_qtde_amigos(qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    return sum(so_qtdes) / sum(x for x in qtde_amigos.values())


def teste_gera_histograma_contagem_amigos():
    qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades(5000, qtde_usuarios_na_rede)
    qtde_amigos = quantidade_de_amigos(amizades)
    gera_histograma_contagem_amigos(qtde_amigos, qtde_usuarios_na_rede)


def teste_media_qtde_amigos():
    print(
        f"Média: {media_qtde_amigos(quantidade_de_amigos(gera_amizades(5000, quantidade_de_usuarios_na_rede())))}"
    )


def mediana_qtde_amigos(qtde_amigos):
    so_qtde = [x * y for x, y in qtde_amigos.items()]
    ordenada = sorted(so_qtde)
    meio = len(ordenada) // 2
    return (
        ordenada[meio] if meio % 2 == 1 else (ordenada[meio - 1] + ordenada[meio]) / 2
    )


def teste_mediana_qtde_amigos():
    print(
        f"Mediana: {mediana_qtde_amigos(quantidade_de_amigos(gera_amizades(50, quantidade_de_usuarios_na_rede())))}"
    )


def quantil(qtde_amigos, percentual):
    so_qtde = [x * y for x, y in qtde_amigos.items()]
    indice = int(percentual * len(so_qtde))
    return sorted(so_qtde)[indice]


def teste_quantil():
    print(
        f"Quantil(50%): {quantil(quantidade_de_amigos(gera_amizades(50, quantidade_de_usuarios_na_rede())), 0.5)}"
    )


def moda_qtde_amigos(qtde_amigos):
    moda = max(qtde_amigos.values())
    return [x for x, count in qtde_amigos.items() if count == moda]


def teste_moda_qtde_amigos():
    print(
        f"Moda: {moda_qtde_amigos(quantidade_de_amigos(gera_amizades(100 * 99, quantidade_de_usuarios_na_rede())))}"
    )


def diferencas_em_relacao_a_media(qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    media = media_qtde_amigos(qtde_amigos)
    return [x - media for x in so_qtdes]


def soma_dos_quadrados(diferencas):
    return sum(x ** 2 for x in diferencas)


def variancia(qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    return soma_dos_quadrados(diferencas_em_relacao_a_media(qtde_amigos)) / (
        len(so_qtdes) - 1
    )


def desvio_padrao(qtde_amigos):
    return math.sqrt(variancia(qtde_amigos))


def main():
    #teste_moda_qtde_amigos()
    # teste_gera_histograma_contagem_amigos()
    # teste_media_qtde_amigos()
    # teste_mediana_qtde_amigos()
    # teste_quantil()
    
    gera_histograma_amigo_por_idade(idade(gera_idade(quantidade_de_usuarios_na_rede())), quantidade_de_usuarios_na_rede())
    
    #print (gera_sexo(quantidade_de_usuarios_na_rede()))
    #print (gera_idade(quantidade_de_usuarios_na_rede()))
    #print (quantidade_de_amigos_por_sexo(gera_sexo(quantidade_de_usuarios_na_rede())))

main()