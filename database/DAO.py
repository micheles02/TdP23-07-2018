from database.DB_connect import DBConnect
from model.stato import Stato


class DAO:

    def __init__(self):
        pass

    @staticmethod
    def getYear():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """select distinct year(s.datetime) as year
                   from sighting s
                   order by year"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])




        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary = True)

        query = """select s.*
                   from state s"""

        cursor.execute(query)

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        conn.close()
        return result



    @staticmethod
    def getArchi(year, giorni):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """select n.state1 as s1, n.state2 as s2, count(*) as peso
                   from neighbor n, sighting st1, sighting st2
                   where st1.state < st2.state
                   and (st1.state = n.state1) and (st2.state = n.state2)
                   and year(st1.datetime) = %s
                   and year(st2.datetime) = %s
                   and datediff(st1.datetime,st2.datetime) <= %s
                   group by n.state1, n.state2"""

        cursor.execute(query, (year, year, giorni,))

        for row in cursor:
            result.append((row["s1"], row["s2"], row["peso"]))

        cursor.close()
        conn.close()
        return result


