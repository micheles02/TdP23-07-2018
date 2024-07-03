from database.DB_connect import DBConnect
from model.stato import Stato


class DAO:

    def __init__(self):
        pass
    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(year(s.`datetime`)) as year
                from new_ufo_sightings.sighting s """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from new_ufo_sightings.state s  """

        cursor.execute(query, )

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getVicini():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from new_ufo_sightings.neighbor n """

        cursor.execute(query, )

        for row in cursor:
            result.append((row["state1"], row["state2"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(u, v, anno, giorni):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor(dictionary=True)
        query = """select s.state as s1, s2.state as s2, count(distinct(s.id)) as peso
                from sighting s, sighting s2 
                where ((s.state = %s and s2.state = %s) or (s.state = %s and s2.state = %s))
                and abs(datediff(s.`datetime`, s2.`datetime`)) < %s and year(s.`datetime`) = %s"""

        cursor.execute(query, (u, v, v, u, giorni, anno))

        for row in cursor:
            if row["peso"]:
                result = row["peso"]

        cursor.close()
        conn.close()
        return result