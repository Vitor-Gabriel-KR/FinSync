import psycopg2
from psycopg2 import sql
from config import DB_CONFIG
from schema import TABLES
from seed import SEEDS


def connect(dbname=None):
    cfg = DB_CONFIG.copy()
    if dbname:
        cfg["dbname"] = dbname
    return psycopg2.connect(**cfg)


def database_exists():
    conn = connect("postgres")
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_CONFIG["dbname"],))
    exists = cur.fetchone() is not None
    conn.close()
    return exists


def create_database():
    conn = connect("postgres")
    cur = conn.cursor()
    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_CONFIG["dbname"])))
    conn.commit()
    conn.close()


def get_existing_tables(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT table_schema, table_name 
        FROM information_schema.tables 
        WHERE table_name IN %s
    """, (tuple(TABLES.keys()),))
    return {(row[0], row[1]) for row in cur.fetchall()}


def drop_table_any_schema(conn, table_name):
    cur = conn.cursor()
    cur.execute("""
        SELECT table_schema 
        FROM information_schema.tables 
        WHERE table_name = %s
    """, (table_name,))

    schemas = [row[0] for row in cur.fetchall()]

    for s in schemas:
        cur.execute(
            sql.SQL("DROP TABLE IF EXISTS {}.{} CASCADE")
            .format(sql.Identifier(s), sql.Identifier(table_name))
        )


def run_setup():
    print("\n=== SETUP DO BANCO ===")

    if not database_exists():
        print(f"Criando banco {DB_CONFIG['dbname']}...")
        create_database()
    else:
        print(f"Banco {DB_CONFIG['dbname']} já existe.")

    conn = connect()
    cur = conn.cursor()

    existing = get_existing_tables(conn)

    for table_name, create_sql in TABLES.items():
        print(f"Verificando {table_name}...")

        exists_anywhere = any(t[1] == table_name for t in existing)

        if exists_anywhere:
            print(f"{table_name} encontrado. Verificando schema correto...")

            if ("public", table_name) not in existing:
                print(f"{table_name} está no schema errado. Removendo...")
                drop_table_any_schema(conn, table_name)
                cur.execute(create_sql)
                print(f"{table_name} criado no schema public.")

        else:
            print(f"{table_name} não existe. Criando...")
            cur.execute(create_sql)
            print(f"{table_name} criada.")

    conn.commit()

    for table, seed_list in SEEDS.items():
        cur.execute(sql.SQL("SELECT COUNT(*) FROM {}").format(sql.Identifier(table)))
        count = cur.fetchone()[0]

        if count == 0:
            print(f"Inserindo seeds em {table}...")
            for seed in seed_list:
                cur.execute(seed)
        else:
            print(f"{table} já possui dados.")

    conn.commit()
    conn.close()
    print("\n=== SETUP COMPLETO ===")


if __name__ == "__main__":
    run_setup()
