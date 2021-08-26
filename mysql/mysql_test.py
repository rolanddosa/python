import unittest

import mysql.connector


class TestMySqlConnection(unittest.TestCase):

    @unittest.skip("requires a database")
    def test_mysql_connection(self):
        mydb = mysql.connector.connect(
            user="...",
            database="..."
        )
        print(mydb)
