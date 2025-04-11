import os
import psycopg2
from datetime import datetime
from xhtml2pdf import pisa

# Função para gerar o PDF usando xhtml2pdf
def gerar_pdf(conteudo_html, caminho_pdf):
    with open(caminho_pdf, "w+b") as arquivo_pdf:
        pisa_status = pisa.CreatePDF(conteudo_html, dest=arquivo_pdf)
        return not pisa_status.err  # Retorna True se não houver erro

# Conectar ao banco
conn = psycopg2.connect(
    dbname="nomedobanco",
    user="nomeusuario",
    password="senhabanco",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Buscar o último relatório
cursor.execute("""
    SELECT conteudo_html, data_geracao
    FROM relatorios
    ORDER BY data_geracao DESC
    LIMIT 1
""")
resultado = cursor.fetchone()

if resultado:
    conteudo_html, data_geracao = resultado

    # Nome e caminho do PDF na pasta do projeto
    nome_pdf = f"relatorio_{data_geracao.strftime('%Y%m%d_%H%M%S')}.pdf"
    caminho_pdf = os.path.join(os.getcwd(), nome_pdf)

    # Gerar o PDF
    sucesso = gerar_pdf(conteudo_html, caminho_pdf)

    if sucesso:
        print(f"✅ PDF gerado com sucesso: {caminho_pdf}")
        os.startfile(caminho_pdf)  # Só funciona no Windows
    else:
        print("❌ Falha ao gerar o PDF.")
else:
    print("❌ Nenhum relatório encontrado.")

cursor.close()
conn.close()