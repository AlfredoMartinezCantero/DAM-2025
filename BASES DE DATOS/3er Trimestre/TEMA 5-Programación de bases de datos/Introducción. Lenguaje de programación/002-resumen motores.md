InnoDB - Cell level locking
MyISAM = row level locking

MERGE_MYISAM = Distribuir una base de datos a lo largo de múltiples servidores, cada servidor tiene un cacho de la BBDD

**MEMORY - Memoria RAM**
Mucha más velocidad de acceso
Mucho menos espacio (en RAM que en disco duro)
Cuidado por que es volátil

**Archive - Comprimido**
Comprime la información de la tabla
Ocupa menos espacio en disco
El acceso a la información es más lento que con los otros motores

**Blackhole - agujero negro**
Hay ocasiones en las que necesitas tablas intermediarias para operaciones temporales, en ese caso, Blackhole no deja rastro

**CSV - Comma separated values**
