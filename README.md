# 🌎 Relatório Diário de UTCs com Base no Clima Local

Este projeto foi desenvolvido como parte da Unidade I da disciplina **Laboratório de Banco de Dados**, ministrada pelo professor **Francisco Vital**, no curso de **Ciência da Computação** da **UNIMA/Afya**.

## 📌 Objetivo

O objetivo principal do projeto é criar um sistema que:

- Armazena dados meteorológicos de diferentes localidades com seus respectivos fusos horários (UTCs);
- Gera relatórios automáticos em formato PDF com as condições climáticas do dia;
- Possui funcionalidades de log e auditoria das atualizações dos dados;
- Integra banco de dados relacional (PostgreSQL) com Python para geração de relatórios dinâmicos e automatizados.

## 🧑‍💻 Tecnologias Utilizadas

- **PostgreSQL**: Sistema gerenciador de banco de dados relacional;
- **Python 3**: Linguagem utilizada para consumir e manipular os dados;
- **xhtml2pdf**: Biblioteca para geração de arquivos PDF a partir de conteúdo HTML;
- **psycopg2**: Biblioteca de conexão entre Python e PostgreSQL.

## 🗃️ Estrutura do Banco de Dados

### Tabelas criadas:

- `utcs`: Armazena os nomes e códigos dos fusos horários;
- `clima`: Guarda dados climáticos como temperatura, condição e previsão;
- `relatorios`: Guarda os relatórios gerados em HTML;
- `logs_eventos`: Registra eventos de atualização no sistema.

### Triggers e Funções:

- Trigger para logar atualizações na tabela `clima`;
- Trigger que gera relatórios automaticamente após atualização de clima;
- Função `gerar_relatorio_html()` para gerar o conteúdo do relatório.

## 📄 Geração de Relatórios

O sistema gera automaticamente um relatório em PDF com os dados climáticos do dia. O conteúdo é salvo na raiz do projeto e aberto automaticamente ao ser criado, contendo informações como:

- Nome da cidade;
- Data da previsão;
- Condição do clima;
- Temperatura mínima e máxima.

### ⚙️ Funcionalidades
O sistema conta com as seguintes funcionalidades principais:

🕒 Gerenciamento de fusos horários (UTCs): Armazena e organiza os códigos e nomes dos fusos utilizados para geração dos relatórios;

📝 Geração automática de relatórios climáticos: A cada atualização de dados na tabela clima, um relatório em PDF é gerado automaticamente contendo informações detalhadas da previsão do tempo;

🧾 Armazenamento de relatórios em HTML: Antes da conversão para PDF, o relatório é salvo em HTML para registro e possível reutilização;

📊 Sistema de logs e auditoria: Cada modificação relevante na base de dados gera um evento registrado na tabela logs_eventos, facilitando o acompanhamento das alterações;

🔄 Integração entre Python e PostgreSQL: A aplicação utiliza scripts Python para manipular os dados do banco e gerar os relatórios de forma dinâmica;

📂 Salvamento e visualização automática do PDF: O arquivo é salvo na raiz do projeto e aberto automaticamente após sua criação.

## ✅ Requisitos

Crie um ambiente virtual e instale as dependências com:

```pip install -r requirements.txt```

📁 requirements.txt

- psycopg2
- xhtml2pdf

### 🧪 Como Executar
Crie as tabelas no PostgreSQL com os comandos SQL disponíveis no projeto;

- Insira os dados de UTCs e clima;
- Execute o script Python para gerar o relatório PDF automaticamente.

### 👥 Integrantes do Projeto

- Arthur Menezes Maciel
- Gabriel Clementino Camerino Ávila
- Ivanildo Marques de Souza Filho
- Maria de Fátima Nunes Alves