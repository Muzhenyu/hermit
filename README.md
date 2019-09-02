# hermit
this code is source code of my django learning project, which I post in docker hub image lvbu89757/hermit:hermit_v1.1

areas_hangzhou.txt is the areas information for this project's database.

whole mysql example data is upload in the last push

this project is based on python3.6 and django 1.11.11

latest update: I have upload a interface for using pymysql and database procedure to get jsonfied data, I write this function
 in /webbacksoftware/webbacksoftware/utils/hermit_orm/self_define_orm.py you can use it to create, update, delete procedure 
you want. and it will generate a procedure sql file in a specified document so you can easily check and back_up your procedure
also it provide method to jsonfied data which have same name like orm filter (I mean it is called filter), hope this will help.