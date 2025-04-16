import psycopg2
from weasyprint import HTML

# Conecta ao banco PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    dbname="nomebancodedados",
    user="usuariobanco",
    password="senhabanco"
)
cursor = conn.cursor()

# Chama a função que gera o HTML no banco
cursor.execute("SELECT gerar_relatorio_html();")
html_conteudo = cursor.fetchone()[0]

# Salva o HTML como arquivo
with open("relatorio_clima.html", "w", encoding="utf-8") as arquivo_html:
    arquivo_html.write(html_conteudo)

# Gera o PDF com o WeasyPrint
HTML(string=html_conteudo).write_pdf("relatorio_clima.pdf")

print("✅ Relatório gerado com sucesso em HTML e PDF!")

# Fecha a conexão
cursor.close()
conn.close()
