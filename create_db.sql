CREATE TABLE "Assigments" ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_MENTOR` INTEGER NOT NULL, `TITLE` TEXT NOT NULL, `DATA` TEXT NOT NULL, `LINK` TEXT NOT NULL, `GROUP` TEXT )
CREATE TABLE "Attendence" ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_STUDENT` INTEGER NOT NULL, `DATE` TEXT NOT NULL, `STATUS` TEXT NOT NULL );
CREATE TABLE "Chekpoints" ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_STUDENTA` INTEGER NOT NULL, `TITLE` TEXT NOT NULL );
CREATE TABLE "Sumbissions" ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_ASSIGMENT` TEXT NOT NULL, `ID_STUDENT` TEXT NOT NULL, `ID_MENTOR` INTEGER, `GRADE` INTEGER, `DATE` TEXT NOT NULL, `LINK` TEXT NOT NULL )
CREATE TABLE `TEAM` ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `NAME` INTEGER NOT NULL );
CREATE TABLE `USERS_CHECKPOINT` ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_CHECKPOINT` INTEGER NOT NULL, `DATE` INTEGER NOT NULL, `GRADE` NUMERIC NOT NULL, `ID_STUDENT` INTEGER NOT NULL, `ID_MENTOR_1` INTEGER NOT NULL, `ID_MENTOR_2` INTEGER NOT NULL );
CREATE TABLE "Users" ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `Name` TEXT NOT NULL, `Surname` TEXT NOT NULL, `E-mail` TEXT NOT NULL UNIQUE, `Password` TEXT NOT NULL, `Type` TEXT NOT NULL );
CREATE TABLE `Users_team` ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_TEAM` INTEGER NOT NULL, `ID_USER` INTEGER NOT NULL );
INSERT INTO Users (ID, Name, Surname, "E-mail", Password, Type) VALUES (1, 'Student', 'Codecool', 'ja', 'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''', 'Student');
INSERT INTO Users (ID, Name, Surname, "E-mail", Password, Type) VALUES (2, 'Mentor', 'Codecool', 'prosty', 'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''', 'Mentor');
INSERT INTO Users (ID, Name, Surname, "E-mail", Password, Type) VALUES (3, 'Employee', 'Codecool', 'nw', 'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''', 'Employee');
INSERT INTO Users (ID, Name, Surname, "E-mail", Password, Type) VALUES (4, 'Manager', 'Codecool', 'jurek', 'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''', 'Manager');
