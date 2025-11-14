CREATE DATABASE peliculas;
USE peliculas;

CREATE TABLE peliculas(
    nombre VARCHAR(255),
    anio_estreno INT
);

INSERT INTO peliculas VALUES("Interestellar",2014);
INSERT INTO peliculas VALUES ("Inception", 2010);
INSERT INTO peliculas VALUES ("The Matrix", 1999);
INSERT INTO peliculas VALUES ("Avatar", 2009);
INSERT INTO peliculas VALUES ("The Godfather", 1972);
INSERT INTO peliculas VALUES ("Pulp Fiction", 1994);
INSERT INTO peliculas VALUES ("The Dark Knight", 2008);
INSERT INTO peliculas VALUES ("Forrest Gump", 1994);
INSERT INTO peliculas VALUES ("Gladiator", 2000);
INSERT INTO peliculas VALUES ("The Shawshank Redemption", 1994);
INSERT INTO peliculas VALUES ("Fight Club", 1999);
INSERT INTO peliculas VALUES ("The Prestige", 2006);
INSERT INTO peliculas VALUES ("Titanic", 1997);
INSERT INTO peliculas VALUES ("Jurassic Park", 1993);
INSERT INTO peliculas VALUES ("The Lion King", 1994);
INSERT INTO peliculas VALUES ("Back to the Future", 1985);
INSERT INTO peliculas VALUES ("Star Wars: A New Hope", 1977);
INSERT INTO peliculas VALUES ("Blade Runner", 1982);
INSERT INTO peliculas VALUES ("Toy Story", 1995);
INSERT INTO peliculas VALUES ("The Lord of the Rings: The Fellowship of the Ring", 2001);
INSERT INTO peliculas VALUES ("The Lord of the Rings: The Two Towers", 2002);
INSERT INTO peliculas VALUES ("The Lord of the Rings: The Return of the King", 2003);
INSERT INTO peliculas VALUES ("Alien", 1979);
INSERT INTO peliculas VALUES ("Terminator 2: Judgment Day", 1991);
INSERT INTO peliculas VALUES ("Whiplash", 2014);
INSERT INTO peliculas VALUES ("La La Land", 2016);
INSERT INTO peliculas VALUES ("Mad Max: Fury Road", 2015);
INSERT INTO peliculas VALUES ("The Social Network", 2010);
INSERT INTO peliculas VALUES ("Parasite", 2019);
INSERT INTO peliculas VALUES ("Joker", 2019);
INSERT INTO peliculas VALUES ("Coco", 2017);



SELECT

nombre AS 'Nombre de la Película',
anio_estreno AS 'Año de estreno'


FROM 

peliculas

ORDER BY
anio_estreno DESC;

+---------------------------------------------------+-----------------+
| Nombre de la Película                             | Año de estreno  |
+---------------------------------------------------+-----------------+
| Joker                                             |            2019 |
| Parasite                                          |            2019 |
| Coco                                              |            2017 |
| La La Land                                        |            2016 |
| Mad Max: Fury Road                                |            2015 |
| Interestellar                                     |            2014 |
| Whiplash                                          |            2014 |
| Inception                                         |            2010 |
| The Social Network                                |            2010 |
| Avatar                                            |            2009 |
| The Dark Knight                                   |            2008 |
| The Prestige                                      |            2006 |
| The Lord of the Rings: The Return of the King     |            2003 |
| The Lord of the Rings: The Two Towers             |            2002 |
| The Lord of the Rings: The Fellowship of the Ring |            2001 |
| Gladiator                                         |            2000 |
| The Matrix                                        |            1999 |
| Fight Club                                        |            1999 |
| Titanic                                           |            1997 |
| Toy Story                                         |            1995 |
| The Lion King                                     |            1994 |
| Forrest Gump                                      |            1994 |
| Pulp Fiction                                      |            1994 |
| The Shawshank Redemption                          |            1994 |
| Jurassic Park                                     |            1993 |
| Terminator 2: Judgment Day                        |            1991 |
| Back to the Future                                |            1985 |
| Blade Runner                                      |            1982 |
| Alien                                             |            1979 |
| Star Wars: A New Hope                             |            1977 |
| The Godfather                                     |            1972 |
+---------------------------------------------------+-----------------+