import sqlalchemy
import psycopg2



engine = sqlalchemy.create_engine('postgresql://ssvt:qqq@localhost:5432/hw')


connection = engine.connect()

add_new = connection.execute("INSERT INTO album(id,album_name,album_date) VALUES(1,'Curtis', 2007 )")
 # delete = connection.execute("DELETE FROM album(album_date)")


# select = connection.execute("SELECT * FROM genre").fetchall()
# print(select)



INSERT INTO ALBUM            # Забиваем альбом
VALUES(2,'Madame',2005)
VALUES(2,'Along Came a Spider',2009)
VALUES(2,'Hot Jazz Classics',1943)
VALUES(2,'Celestica',2018)
VALUES(2,'Tha Blue Carpet Treatment',2019)
VALUES(2,'Nite Traxx',2005)
;

INSERT INTO SINGER_GENRE # Забиваем сингер жанр
VALUES(8,8,3);

insert into track # Забиваем трэки
values(8,'Nite ',357,8)