import MySQLdb

database = MySQLdb.connect(host="localhost", user="root", passwd="Programer2021!")


def create_db(db):
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS music;")


def create_table(db):

    stmt = """CREATE TABLE IF NOT EXISTS instruments(
                isntrument_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                name VARCHAR(30) NOT NULL,
                family VARCHAR(30) NOT NULL,
                difficulty ENUM('easy', 'medium', 'hard') NOT NULL);"""

    cursor = db.cursor()
    cursor.execute('USE music;')
    cursor.execute(stmt)
    db.close()


def insert_into_instruments(db, list_of_instruments: list) -> None:

    stmt = """INSERT INTO instruments (name, family, difficulty) VALUES (%s, %s, %s)"""

    cursor = db.cursor()
    cursor.execute('USE music;')
    for instrument in list_of_instruments:
        cursor.execute(stmt, instrument)
    db.commit()


def insert_into_instruments_v2(db, list_of_instruments: list) -> None:

    stmt = """INSERT INTO instruments (name, family, difficulty) VALUES (%s, %s, %s)"""

    cursor = db.cursor()
    cursor.execute('USE music;')
    cursor.executemany(stmt, list_of_instruments)
    db.commit()


def get_instruments_count(db):

    query = """SELECT family, COUNT(isntrument_id) AS quantity FROM instruments GROUP BY family"""

    cursor = db.cursor()
    cursor.execute('USE music;')
    cursor.execute(query)
    query_result = cursor.fetchall()

    result = [{'family': family[0], 'count': family[1]} for family in query_result]
    result = tuple(result)

    return result


if __name__ == '__main__':

    instruments = [
        ('guitar', 'strings', 'medium'),
        ('piano', 'keyboard', 'hard'),
        ('harp', 'strings', 'hard'),
        ('triangle', 'percussion', 'easy'),
        ('flute', 'woodwind', 'medium'),
        ('violin', 'string', 'medium'),
        ('tambourine', 'percussion', 'easy'),
        ('organ', 'keyboard', 'hard'),
        ]
