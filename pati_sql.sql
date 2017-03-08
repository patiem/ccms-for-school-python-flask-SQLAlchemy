BEGIN TRANSACTION;
CREATE TABLE `Users_team` ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_TEAM` INTEGER NOT NULL, `ID_USER` INTEGER NOT NULL );
INSERT INTO `Users_team` VALUES (1,1,1);
INSERT INTO `Users_team` VALUES (2,1,5);
INSERT INTO `Users_team` VALUES (3,1,6);
CREATE TABLE `Users` ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `Name` TEXT NOT NULL, `Surname` TEXT NOT NULL, `E-mail` TEXT NOT NULL UNIQUE, `Telephone` TEXT, `Password` TEXT NOT NULL, `Type` TEXT NOT NULL );
INSERT INTO `Users` VALUES (1,'Student','Codecool','ja',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Student');
INSERT INTO `Users` VALUES (2,'Mentor','Codecool','prosty',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Mentor');
INSERT INTO `Users` VALUES (3,'Employee','Codecool','nw',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Employee');
INSERT INTO `Users` VALUES (4,'Manager','Codecool','jurek',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Manager');
INSERT INTO `Users` VALUES (5,'Student','Codecool','ty',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Student');
INSERT INTO `Users` VALUES (6,'Student','Codecool','my',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Student');
CREATE TABLE `TEAMS` ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `NAME` TEXT NOT NULL );
INSERT INTO `TEAMS` VALUES (1,'TeamTeam');
CREATE TABLE "Sumbissions" (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`ID_ASSIGMENT`	INTEGER NOT NULL,
	`ID_STUDENT`	INTEGER NOT NULL,
	`GRADE`	INTEGER,
	`DATE`	TEXT NOT NULL,
	`LINK`	TEXT NOT NULL,
	`ID_MENTOR`	INTEGER
);
INSERT INTO `Sumbissions` VALUES (3,3,1,4,'2017-02-09','Mniom/mniom',2);
INSERT INTO `Sumbissions` VALUES (4,4,1,3,'2017-02-09','ojojojo',2);
INSERT INTO `Sumbissions` VALUES (8,10,1,7,'2017-02-09','jolooo',2);
INSERT INTO `Sumbissions` VALUES (9,10,5,7,'2017-02-09','jolooo',2);
INSERT INTO `Sumbissions` VALUES (10,10,6,7,'2017-02-09','jolooo',2);
INSERT INTO `Sumbissions` VALUES (11,6,1,222,'2017-02-09','jkjkjkjl',2);
INSERT INTO `Sumbissions` VALUES (12,6,5,0,'2017-02-09','jkjkjkjl',0);
INSERT INTO `Sumbissions` VALUES (13,6,6,0,'2017-02-09','jkjkjkjl',2);
INSERT INTO `Sumbissions` VALUES (17,5,1,0,'2017-02-10','okokokok',0);
INSERT INTO `Sumbissions` VALUES (19,12,1,666,'2017-02-10','sxsxsxxsx',2);
INSERT INTO `Sumbissions` VALUES (20,12,5,666,'2017-02-10','sxsxsxxsx',2);
INSERT INTO `Sumbissions` VALUES (21,12,6,666,'2017-02-10','sxsxsxxsx',2);
INSERT INTO `Sumbissions` VALUES (22,1,1,0,'2017-02-10','ghghgjklkjhg',0);
CREATE TABLE `Assigments`( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_MENTOR` INTEGER NOT NULL, `TITLE` TEXT NOT NULL, `START_DATA` TEXT NOT NULL, `END_DATA` TEXT NOT NULL, `LINK` TEXT NOT NULL, `GROUP` TEXT);
INSERT INTO `Assigments` VALUES (1,2,'Test_123','2017-02-05','2017-02-15','ass_3.txt','0');
INSERT INTO `Assigments` VALUES (2,2,'Test_2','2017-02-20','2017-02-28','ass_3.txt','0');
INSERT INTO `Assigments` VALUES (3,2,'Test_3','2017-01-05','2017-01-15','ass_3.txt','0');
INSERT INTO `Assigments` VALUES (4,2,'Test_4','2017-02-05','2017-02-15','ass_3.txt','0');
INSERT INTO `Assigments` VALUES (5,2,'Dupa','2017-02-05','2017-02-15','Dupa.txt','0');
INSERT INTO `Assigments` VALUES (6,2,'Dupa_now','2017-02-05','2017-02-15','Dupa_now.txt','0');
INSERT INTO `Assigments` VALUES (7,2,'Test_456','2017-02-05','2017-02-15','ass_3.txt','0');
INSERT INTO `Assigments` VALUES (8,2,'Test_xxx','2017-02-05','2017-02-15','ass_3.txt','0');
INSERT INTO `Assigments` VALUES (9,2,'Future','2017-03-03','2017-04-04','Future.txt','0');
INSERT INTO `Assigments` VALUES (10,2,'Okropnie Ogromna Pupa','2017-01-12','2017-09-12','Okropnie_Ogromna_Pupa.txt','1');
INSERT INTO `Assigments` VALUES (11,2,'Hgghg','2017-12-02','2018-02-13','Hgghg.txt','1');
INSERT INTO `Assigments` VALUES (12,2,'Nowy Asss','2017-01-01','2017-03-01','Nowy_Asss.txt','1');
COMMIT;
