from sqlalchemy import create_engine

# Atualize com seus dados reais de acesso:
DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/projeto_utcs_vital"

engine = create_engine(DATABASE_URL)
