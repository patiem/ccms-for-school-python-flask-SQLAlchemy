BEGIN TRANSACTION;
CREATE TABLE `comments` (
    `id`    INTEGER,
    `sub_id`    INTEGER,
    `comment`    TEXT,
    PRIMARY KEY(`id`)
);
INSERT INTO `comments` VALUES (27,51,'eJTZryxk,c');
INSERT INTO `comments` VALUES (28,52,'eJTZryxk,c');
INSERT INTO `comments` VALUES (29,53,'eJTZryxk,c');
INSERT INTO `comments` VALUES (30,54,'eJTZryxk,c');
INSERT INTO `comments` VALUES (31,23,'asdasd');
INSERT INTO `comments` VALUES (32,24,'google');
INSERT INTO `comments` VALUES (33,25,'testowy');
INSERT INTO `comments` VALUES (34,26,'testowy');
INSERT INTO `comments` VALUES (35,27,'testowy');
INSERT INTO `comments` VALUES (36,28,'testowy');
INSERT INTO `comments` VALUES (37,29,'testowy');
INSERT INTO `comments` VALUES (38,30,'testowy');
INSERT INTO `comments` VALUES (39,31,'testowy');
INSERT INTO `comments` VALUES (40,32,'testowy');
CREATE TABLE "Users_team"
(
    ID INTEGER PRIMARY KEY,
    ID_TEAM INTEGER NOT NULL,
    ID_USER INTEGER NOT NULL
);
INSERT INTO `Users_team` VALUES (1,26,11);
CREATE TABLE `Users_checkpoints` ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_CHECKPOINT` INTEGER NOT NULL, `DATE` TEXT NOT NULL, `GRADE` NUMERIC NOT NULL, `ID_STUDENT` INTEGER NOT NULL, `ID_MENTOR_1` INTEGER NOT NULL, `ID_MENTOR_2` INTEGER NOT NULL );
INSERT INTO `Users_checkpoints` VALUES (135,44,'2017-03-24','red',11,2,21);
INSERT INTO `Users_checkpoints` VALUES (136,44,'2017-03-24','red',45,2,21);
CREATE TABLE "Users" (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT NOT NULL,
	`Surname`	TEXT NOT NULL,
	`Email`	TEXT NOT NULL UNIQUE,
	`Telephone`	TEXT,
	`Password`	TEXT NOT NULL,
	`Type`	TEXT NOT NULL
);
INSERT INTO `Users` VALUES (2,'Przemysław','Ciąćka','prosty',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Mentor');
INSERT INTO `Users` VALUES (11,'Kamil','Mika','kam@kam.com','1223342142','b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Student');
INSERT INTO `Users` VALUES (21,'Mateusz','Ostafil','prosty2',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Mentor');
INSERT INTO `Users` VALUES (22,'Rafał','Stępień','prosty3',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Mentor');
INSERT INTO `Users` VALUES (34,'Employee','Codecool','nw',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Employee');
INSERT INTO `Users` VALUES (44,'Manager','Codecool','jurek',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Manager');
INSERT INTO `Users` VALUES (45,'Student','Codecool','ty',NULL,'b''\xb2\xf7=\xf0\xc9\xdat\xe1\xa3\xcf\xb7\xe6\x80ee\xff@\r\xf6\x13f\x10|\x18N\xa3\xcbb\x83\xa7r\x85''','Student');
CREATE TABLE `TEAMS` ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `NAME` TEXT NOT NULL );
INSERT INTO `TEAMS` VALUES (26,'Nowy Team');
CREATE TABLE "Sumbissions"
(
    ID INTEGER PRIMARY KEY,
    ID_ASSIGMENT INTEGER NOT NULL,
    ID_STUDENT INTEGER NOT NULL,
    GRADE INTEGER,
    DATE TEXT NOT NULL,
    LINK TEXT NOT NULL,
    ID_MENTOR INTEGER
);
INSERT INTO `Sumbissions` VALUES (3,3,1,37,'2017-02-09','https://github.com/patiem',2);
INSERT INTO `Sumbissions` VALUES (4,4,1,37,'2017-02-09','https://github.com/patiem',2);
INSERT INTO `Sumbissions` VALUES (23,2,1,69,'2017-03-20','asda',2);
INSERT INTO `Sumbissions` VALUES (24,1,45,38,'2017-03-20','www.google.pl',2);
INSERT INTO `Sumbissions` VALUES (25,13,5,61,'2017-03-21','www.facebook.com',2);
INSERT INTO `Sumbissions` VALUES (26,13,6,61,'2017-03-21','www.facebook.com',2);
INSERT INTO `Sumbissions` VALUES (27,13,13,61,'2017-03-21','www.facebook.com',2);
INSERT INTO `Sumbissions` VALUES (28,13,11,61,'2017-03-21','www.facebook.com',2);
INSERT INTO `Sumbissions` VALUES (29,13,11,61,'2017-03-21','www.facebook.com',2);
INSERT INTO `Sumbissions` VALUES (30,13,12,61,'2017-03-21','www.facebook.com',2);
INSERT INTO `Sumbissions` VALUES (31,13,45,61,'2017-03-21','www.facebook.com',2);
INSERT INTO `Sumbissions` VALUES (32,13,46,61,'2017-03-21','www.facebook.com',2);
CREATE TABLE `Checkpoints`( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_USER` INTEGER NOT NULL, `TITLE` TEXT NOT NULL, `START_DATE` TEXT NOT NULL);
INSERT INTO `Checkpoints` VALUES (44,2,'SQL','2017-03-10');
INSERT INTO `Checkpoints` VALUES (45,2,'Test','2017-03-10');
INSERT INTO `Checkpoints` VALUES (46,2,'asdf','2017-03-10');
INSERT INTO `Checkpoints` VALUES (47,2,'asdf','2017-03-10');
INSERT INTO `Checkpoints` VALUES (48,2,'test2','2017-03-20');
CREATE TABLE `Attendance`( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_STUDENT` INTEGER NOT NULL, `DATE` TEXT NOT NULL, `STATUS` TEXT NOT NULL );
INSERT INTO `Attendance` VALUES (7,11,'2017-03-10','Present');
INSERT INTO `Attendance` VALUES (10,45,'2017-03-10','Absent');
INSERT INTO `Attendance` VALUES (12,11,'2017-03-20','Present');
INSERT INTO `Attendance` VALUES (14,45,'2017-03-20','Present');
INSERT INTO `Attendance` VALUES (15,11,'2017-03-21','Present');
INSERT INTO `Attendance` VALUES (16,45,'2017-03-21','Present');
INSERT INTO `Attendance` VALUES (29,11,'2017-03-23','Present');
INSERT INTO `Attendance` VALUES (30,45,'2017-03-23','Late');
INSERT INTO `Attendance` VALUES (33,11,'2017-03-24','None');
INSERT INTO `Attendance` VALUES (34,45,'2017-03-24','None');
CREATE TABLE `Assigments`( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `ID_MENTOR` INTEGER NOT NULL, `TITLE` TEXT NOT NULL, `START_DATA` TEXT NOT NULL, `END_DATA` TEXT NOT NULL, `LINK` TEXT NOT NULL, `GROUP` TEXT);
INSERT INTO `Assigments` VALUES (1,2,'Test_123','2017-02-05','2017-02-15','<section>
        <div class="description">
        <article>
            <h3>Story</h3>
            <div>A client came and asked about a software for displaying information about cities, towns and villages in Małopolska.
                Good news is that he is providing data file (Link (Łącza do strony zewnętrznej.)).
                Bad news, he''s totally newbie when it comes to IT and is interesting only in results.
                ASAP results, to be more precised. </div>
        </article>
        <article>
            <h3>Descripion</h3>
            <div>Please:
                I. Define what classes you''ll implement in the system.
                II. Draw UML Class diagram.
                III. Create a python program that suits client''s needs. </div>
        </article>
        <article>
            <h3>Illustration</h3>
            <figure>
                <img src="https://scontent-waw1-1.xx.fbcdn.net/v/t1.0-9/1524687_10202387511361199_1643696660_n.jpg?oh=78f4151af1f0c67ea5c5fae54e2360a3&oe=593E63FD" />
            </figure>
        </article>
        </div>
    </section>','0');
INSERT INTO `Assigments` VALUES (2,2,'Test_2','2017-02-20','2017-02-28','<section>
        <div class="description">
        <article>
            <h3>Story</h3>Dupa dupa dupa dupa </div>
        </article>
        <article>
            <h3>Descripion</h3>
            <div>Please:
                I. Define what classes you''ll implement in the system.
                II. Draw UML Class diagram.
                III. Create a python program that suits client''s needs. </div>
        </article>
        <article>
            <h3>Illustration</h3>
            <figure>
                <img src="https://scontent-waw1-1.xx.fbcdn.net/v/t1.0-9/1524687_10202387511361199_1643696660_n.jpg?oh=78f4151af1f0c67ea5c5fae54e2360a3&oe=593E63FD" />
            </figure>
        </article>
        </div>
    </section>','0');
INSERT INTO `Assigments` VALUES (3,2,'Test_3','2017-01-05','2017-01-15','<section>
        <div class="description">
        <article>
            <h3>Story</h3>Dupa dupa dupa dupa </div>
        </article>
        <article>
            <h3>Descripion</h3>
            <div>Please:
                I. Define what classes you''ll implement in the system.
                II. Draw UML Class diagram.
                III. Create a python program that suits client''s needs. </div>
        </article>
        <article>
            <h3>Illustration</h3>
            <figure>
                <img src="https://scontent-waw1-1.xx.fbcdn.net/v/t1.0-9/1524687_10202387511361199_1643696660_n.jpg?oh=78f4151af1f0c67ea5c5fae54e2360a3&oe=593E63FD" />
            </figure>
        </article>
        </div>
    </section>','1');
INSERT INTO `Assigments` VALUES (4,2,'Test_4','2017-02-05','2017-02-15','ass_3.txt','1');
INSERT INTO `Assigments` VALUES (13,2,'Testowy','2017-02-23','2017-02-25','Testowy','1');
COMMIT;
