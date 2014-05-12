import unittest
import logging

class DBConfig:
    def __init__(self, configStr):
        self.__data = {}
        for line in configStr.split('\n'):
            line = line.strip()
            if line[0:3] == '--!':
                data = line[3:].strip().split(':')
                key = data[0].strip().lower()
                value = data[1].strip()
                self.__data[key] = value
        print str(self.__data)
        pass

    def getParameter(self,parameter):
        print parameter
        print str(self.__data)
        return self.__data.get(parameter,'')
        



class TestDBConfig(unittest.TestCase):
    def setUp(self):
        self.data_mysql = '''
--! product: mysql
--! hostname: 127.0.0.1
--! user: root
--! password: root


CREATE TABLE [dbo].[TableName] 
    (
	Id		INT IDENTITY(1,1)		NOT NULL

	CONSTRAINT [PK_] PRIMARY KEY CLUSTERED ([Id]) 
	)
    GO

        '''
    def test_mysql(self):
        dbcfg = DBConfig(self.data_mysql)
        self.assertEqual(
            'mysql',
            dbcfg.getParameter('product')
        )
        self.assertEqual(
            '127.0.0.1',
            dbcfg.getParameter('hostname')
        )
        self.assertEqual(
            'root',
            dbcfg.getParameter('user')
        )
        self.assertEqual(
            'root',
            dbcfg.getParameter('password')
        )


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDBConfig)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
