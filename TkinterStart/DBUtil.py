import cx_Oracle as Oracle


def create_connection_map():
    conn_map = {'local': Oracle.connect('system/admin@localhost/xe')}
    return conn_map


class DBUtil:
    def __init__(self) -> None:
        self.__connections = create_connection_map()

    def get_all_results(self, environment):
        cursor = self.__connections[environment].cursor()
        cursor.execute('SELECT * FROM PHONE_DETAILS')
        result = cursor.fetchall()
        cursor.close()
        return result

    def get_all_users(self, environment: "Environment name as String"):
        result = []
        cursor = self.__connections[environment].cursor()
        cursor.execute('SELECT * FROM PHONE_DETAILS')
        for res in cursor.fetchall():
            result.append(res[1])
        cursor.close()
        return result

    def get_user_details(self, environment, user):
        cursor = self.__connections[environment].cursor()
        cursor.execute("SELECT * FROM PHONE_DETAILS WHERE OWNER_NAME='{}'".format(user))
        result = cursor.fetchone()
        cursor.close()
        if result is not None:
            return list(result)
        return []

    def __del__(self):
        for connection in self.__connections.values():
            connection.close()
