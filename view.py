import sqlite3 as lite
import pandas as pd

con= lite.connect('dados.db')

def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query,i)


def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em,valor) VALUES (?,?,?)"
        cur.execute(query,i)

def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em,valor) VALUES (?,?,?)"
        cur.execute(query,i)

def deletar_categorias(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Categoria WHERE id=?"
        cur.execute(query, i)

def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)

def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)

def ver_categoria():
    lista_itens = []

    with con :
            cur = con.cursor()
            cur.execute("SELECT * FROM Categoria")
            linha = cur.fetchall()
            for l in linha:
                lista_itens.append(l)

    return lista_itens

def ver_gastos():
    lista_itens = []

    with con :
            cur = con.cursor()
            cur.execute("SELECT * FROM Gastos")
            linha = cur.fetchall()
            for l in linha:
                lista_itens.append(l)

    return lista_itens

def ver_receitas():
    lista_itens = []

    with con :
            cur = con.cursor()
            cur.execute("SELECT * FROM Receitas")
            linha = cur.fetchall()
            for l in linha:
                lista_itens.append(l)

    return lista_itens

def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

def bar_valores():
    # Receita Total ------------------------
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesas Total ------------------------
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    despesas_total = sum(gastos_lista)

    # Despesas Total ------------------------
    saldo_total = receita_total - despesas_total

    return[receita_total,despesas_total,saldo_total]
def porcentagem_valor():
   
        # Receita Total ------------------------
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

        # Despesas Total ------------------------
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    despesas_total = sum(gastos_lista)

        # Despesas Total ------------------------
    porcentagem = (1-((receita_total-despesas_total)/receita_total))*100
    return[porcentagem]

def pie_valores():
    gastos = ver_gastos()
    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista,columns = ['id', 'categoria', 'Data', 'valor'])

    # Get the sum of the durations per month
    dataframe = dataframe.groupby('categoria')['valor'].sum()
   
    lista_quantias = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return([lista_categorias,lista_quantias])