import sqlite3

def unsafe_query(user_input):
    conn = sqlite3.connect(':memory:') 
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def safe_query(user_input):
    conn = sqlite3.connect(':memory:')  
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = ?"
    cursor.execute(query, (user_input,))
    result = cursor.fetchall()
    conn.close()
    return result
  
def safe_query_with_orm(user_input):
    engine = create_engine('sqlite:///:memory:')
    metadata = MetaData()
    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String))
    metadata.create_all(engine)

  
    with engine.connect() as conn:
        conn.execute(users.insert(), [{"name": "Alice"}, {"name": "Bob"}])


    Session = sessionmaker(bind=engine)
    session = Session()


    result = session.query(users).filter(users.c.name == user_input).all()
    session.close()
    return result


user_input = "Bob"

print("Unsafe Query Result:", unsafe_query(user_input))

print("Safe Query Result:", safe_query(user_input))


print("Safe Query with ORM Result:", safe_query_with_orm(user_input))

