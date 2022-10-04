DROP TABLE IF EXISTS userProfile;

CREATE TABLE userProfile
(
    username varchar(15) not null,
    password char(15) not null,
    primary key (username)
);
