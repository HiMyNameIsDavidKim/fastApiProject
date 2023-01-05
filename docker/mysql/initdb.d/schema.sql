create table users(
    id int(11) primary key,
    username varchar(100),
    pwd varchar(255),
    created_at date,
    ranks integer,
    points integer
)charset = utf8;