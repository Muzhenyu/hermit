import pymysql
from django.conf import settings
import os


class hermit_orm(object):
    def __init__(self):
        self.settings=settings.PYMYSQLLINK

    def __linktodatabase(self):
        conn = pymysql.connect(**self.settings)
        cursor = conn.cursor()
        return cursor


    def filter(self,sql):
        data={}
        cursor=self.__linktodatabase()
        cursor.execute(sql)
        data['data']=cursor.fetchall()
        return data

    def C_procedure(self,procedurename,param,sql,filename):
        cursor=self.__linktodatabase()
        procedure='create procedure '+procedurename+'('+param+')'+' begin '+sql+' end ;'
        try:
            cursor.execute(procedure)
        except Exception as e:
            print(e)
        else:
            if os.path.exists(filename):
                f=open(filename+'/'+procedurename+'.sql','w+')
                f.writelines(procedure)
                f.close()
            else:
                os.mkdir(filename)
                f=open(filename+'/'+procedurename+'.sql','w+')
                f.writelines(procedure)
                f.close()

    def R_procedure(self,procedurename,param,sql,filename):
        cursor=self.__linktodatabase()
        cursor.execute('drop procedure '+procedurename+' ;')
        procedure = 'create procedure ' + procedurename + '(' + param + ')' + ' begin ' + sql + ' end ;'
        try:
            cursor.execute(procedure)
        except Exception as e:
            print(e)
        else:
            f = open(filename + '/' + procedurename + '.sql', 'w+')
            f.writelines(procedure)
            f.close()

    def D_procedure(self,procedurename,filename):
        cursor=self.__linktodatabase()
        cursor.execute('drop procedure '+procedurename+' ;')
        os.remove(filename+'/'+procedurename+'.sql')
