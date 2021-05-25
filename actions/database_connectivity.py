import mysql.connector
def DataUpdate(exercise,stress,sleep):
              mydb = mysql.connector.connect( host="localhost", user="root",
               passwd="", database="rasa_health")
              mycursor = mydb.cursor()
              #sql = "CREATE TABLE health (exercise VARCHAR(255),stress  VARCHAR(30),sleep  VARCHAR(30))"
              sql='INSERT INTO health (Exercise, Stress, Sleep) VALUES ("{0}","{1}", "{2}");'.format(exercise,stress,sleep)
              mycursor.execute(sql)
              mydb.commit()
              print(mycursor.rowcount, "record inserted.")


#if __name__=="__main__":
              #  DataUpdate("hike","heigh","2 hours")