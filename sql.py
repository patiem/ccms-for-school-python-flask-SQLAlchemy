import sqlite3


def connect_db(DATABASE_NAME='CCMS.db'):
    return sqlite3.connect(DATABASE_NAME)


def query(query):

    query_result = list()
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    for row in c.execute(query):
        query_result.append(row)

    conn.commit()

    close_db(conn)

    if query_result != []:
        return query_result


def close_db(conn):
    conn.close()

