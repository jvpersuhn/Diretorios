import MySQLdb

class Connection():
    def __init__(self):
        self.host = 'mysql.topskills.study'
        self.database = 'topskills01'
        self.user = 'topskills01'
        self.passwd = 'ts2019'
        self.connection = MySQLdb.connect(host=self.host, database=self.database, user=self.user, passwd=self.passwd)
        self.cursor = self.connection.cursor()