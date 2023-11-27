import databases
import sqlalchemy
import os

#os: para acessar os valores internos do sistema operacional utilizamos, OS para executar o terminal
#sqlachemy: 
#getenv: 
#env: ambiente virtual
#export DATABASE_URL=sqlite://db.sqlite
#
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
TEST_DATABASE =  os.getenv('TEST_DATABSE', 'false') in ('true', 'yes')
database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABASE)
metadata = sqlalchemy.MetaData()
