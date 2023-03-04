DROP TABLE IF EXISTS userPreferences;
DROP TABLE IF EXISTS userProfiles;

CREATE TABLE userProfiles
(
    userID int(8) not null,
    email varchar(30) not null,
    password char(60) not null,
    dob date not null,
    gender varchar(15) not null,
    name varchar(30) not null,
    primary key (userID)
);

CREATE TABLE userPreferences
(
    userID int(8) not null,
    positivePreferences varchar(250) not null,
    negativePreferences varchar(250) not null,
    restrictions varchar(250) not null,
    foreign key (userID) references userProfiles(userID),
    primary key (userID)
);
