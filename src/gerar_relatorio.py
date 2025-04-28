import psycopg2
from xhtml2pdf import pisa

# Função para gerar o PDF a partir de HTML
def converter_html_para_pdf(source_html, output_filename):
    with open(output_filename, "wb") as output_file:
        pisa_status = pisa.CreatePDF(source_html, dest=output_file)
    return not pisa_status.err

# Conectar ao banco de dados PostgreSQL
def conectar_banco():
    try:
        conn = psycopg2.connect(
            host="localhost",       # Endereço do banco
            dbname="nomedobanco",     # Nome do banco de dados
            user="nomedousuario",     # Usuário do banco de dados
            password="senhabanco"    # Senha do banco de dados
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Obter o conteúdo HTML do banco de dados
def obter_html_do_banco(cursor):
    try:
        cursor.execute("SELECT gerar_relatorio_html();")  # Chame sua função SQL ou query
        html_conteudo = cursor.fetchone()[0]
        return html_conteudo
    except Exception as e:
        print(f"Erro ao executar consulta SQL: {e}")
        return None

# Função principal
def gerar_relatorio_pdf():
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        # Obter o conteúdo HTML gerado no banco
        html_conteudo = obter_html_do_banco(cursor)
        
        if html_conteudo:
            # Gerar PDF a partir do HTML
            sucesso = converter_html_para_pdf(html_conteudo, "relatorio_clima.pdf")
            if sucesso:
                print("✅ Relatório gerado com sucesso em PDF!")
            else:
                print("❌ Erro ao gerar o PDF.")
        else:
            print("❌ Erro ao obter conteúdo HTML do banco de dados.")
        
        # Fechar a conexão
        cursor.close()
        conn.close()
    else:
        print("❌ Não foi possível conectar ao banco de dados.")

# Rodar a função principal
if __name__ == "__main__":
    gerar_relatorio_pdf()
