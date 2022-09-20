create database stars;
use stars;
create table transaction(
    transaction_id varchar(40) primary key,
    transaction_type_code int references transaction_type(transaction_type_code),
    stars int,
    transaction_date TIMESTAMP,
    account_id varchar(40) references  account(account_id)
);
create table account(
    account_id varchar(40) primary key,
    first_name varchar(40),
    last_name varchar(40),
    stars int
);


create table transaction_type (
    transaction_type varchar(40),
    transaction_type_code int primary key
);


INSERT INTO transaction_type(transaction_type, transaction_type_code) values ('DEBIT', 0);
INSERT INTO transaction_type(transaction_type, transaction_type_code) values ('CREDIT', 1);

insert into account(stars.account.account_id, stars.account.first_name, stars.account.last_name, stars.account.stars)
values(UUID(), 'Agalya', 'Gunasekaran', 91),
       (uuid(), 'Ani', 'Gunasekaran', 89),
       (uuid(), 'Nithya', 'Natarajan', 60),
       (uuid(), 'Gunasekaran', 'Pasupathi', 60);

