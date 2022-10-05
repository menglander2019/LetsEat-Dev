DROP TABLE IF EXISTS userPreferences;
DROP TABLE IF EXISTS userProfile;

CREATE TABLE userProfile
(
    userID int(8) not null,
    email varchar(15) not null,
    password char(15) not null,
    dob date not null,
    gender varchar(15) not null,
    name varchar(15) not null,
    primary key (userID)
);

CREATE TABLE userPreferences
(
    userID int(8) not null,
    positivePreferences varchar(250) not null,
    negativePreferences varchar(250) not null,
    foreign key (userID) references userProfile(userID),
    primary key (userID)
);
