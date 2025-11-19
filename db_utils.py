from sqlalchemy import create_engine, text

def get_engine():
    return create_engine("postgresql+psycopg2://admin:admin123@localhost:5432/employees")

def test_connection():
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM employees LIMIT 3")).fetchall()
        print("DB connected successfully:")
        print(result[0] if result else "No data found.")

if __name__ == "__main__":
    test_connection()
