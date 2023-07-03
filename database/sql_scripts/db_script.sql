create database scheduleapp;
\c scheduleapp;

CREATE TABLE all_User (
  Id_user  serial NOT NULL UNIQUE,
  Surname  varchar(40) NOT NULL, 
  Name     varchar(40) NOT NULL,
  Ochestvo varchar(40) NOT NULL, 
  password bytea NOT NULL, 
  email    varchar(100) NOT NULL UNIQUE, 
  login    varchar(50) NOT NULL UNIQUE,  
  admin    bool, 
  PRIMARY KEY (Id_user));

CREATE TABLE Building (
  id_build      serial NOT NULL UNIQUE, 
  name_building varchar(10), 
  PRIMARY KEY (id_build));

CREATE TABLE Classrooms (
  number_class int4 NOT NULL, 
  id_build     int4 NOT NULL, 
  PRIMARY KEY (number_class, 
  id_build));

CREATE TABLE Department (
  id_dept   serial NOT NULL UNIQUE, 
  Dept_name varchar(40) NOT NULL UNIQUE, 
  PRIMARY KEY (id_dept));

CREATE TABLE Lessons (
  id_lesson    serial NOT NULL UNIQUE, 
  id_group     int4 NOT NULL, 
  id_teacher   int4 NOT NULL, 
  para         int2 NOT NULL, 
  id_subject   int4 NOT NULL,  
  type_lesson  varchar(20), 
  number_class int4 NOT NULL, 
  id_build     int4 NOT NULL, 
  start_date   date NOT NULL, 
  end_date     date NOT NULL, 
  frequency    int4 NOT NULL,  
  CONSTRAINT id_lesson 
    PRIMARY KEY (id_lesson));

CREATE TABLE st_Groups (
  id_group    serial NOT NULL UNIQUE, 
  title_group varchar(20) NOT NULL UNIQUE, 
  id_dept     int4, 
  PRIMARY KEY (id_group));

CREATE TABLE Students (
  Id_student  serial NOT NULL UNIQUE, 
  id_group    int4 NOT NULL, 
  Name        varchar(50) NOT NULL, 
  Surname     varchar(50) NOT NULL, 
  Ochestvo    varchar(50) NOT NULL, 
  PRIMARY KEY (Id_student));

CREATE TABLE Subjects (
  id_subject   serial NOT NULL UNIQUE, 
  name_subject varchar(40) NOT NULL UNIQUE, 
  PRIMARY KEY (id_subject));

CREATE TABLE Teachers (
  Id_teacher serial NOT NULL UNIQUE, 
  Name       varchar(40) NOT NULL, 
  Surname    varchar(50) NOT NULL, 
  Ochestvo   varchar(50) NOT NULL, 
  PRIMARY KEY (Id_teacher));

ALTER TABLE Students ADD CONSTRAINT r_1 FOREIGN KEY (id_group) REFERENCES st_Groups (id_group);
ALTER TABLE Lessons ADD CONSTRAINT r_2 FOREIGN KEY (id_group) REFERENCES st_Groups (id_group);
ALTER TABLE Lessons ADD CONSTRAINT r_3 FOREIGN KEY (id_subject) REFERENCES Subjects (id_subject);
ALTER TABLE Lessons ADD CONSTRAINT r_4 FOREIGN KEY (id_teacher) REFERENCES Teachers (Id_teacher);
ALTER TABLE st_Groups ADD CONSTRAINT r_5 FOREIGN KEY (id_dept) REFERENCES Department (id_dept);
ALTER TABLE Lessons ADD CONSTRAINT r_6 FOREIGN KEY (number_class, id_build) REFERENCES Classrooms (number_class, id_build);
ALTER TABLE Classrooms ADD CONSTRAINT r_7 FOREIGN KEY (id_build) REFERENCES Building (id_build);

CREATE OR REPLACE FUNCTION fmod (
   dividend double precision,
   divisor double precision
) RETURNS double precision
    LANGUAGE sql IMMUTABLE AS
'SELECT dividend - floor(dividend / divisor) * divisor';

CREATE OR REPLACE FUNCTION GET_CUR_LESSON( start_date in date, curdate in date, end_date in date ,frequency in int4 ) 
RETURNS int4 as 
$$
DECLARE
	v_r int4;
BEGIN 
  IF  fmod((curdate - start_date)::float /7, frequency) = 0 and curdate <= end_date
  then 
    V_R := 1;
  ELSE
    V_R := 0;
  END IF;
  return v_r;
END;
$$
LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION chack_lasson() returns trigger as 
$$
declare
c integer;
begin

if NEW.start_date > NEW.end_date then
  RAISE EXCEPTION 'Дата начала должна быть меньше даты окончания!';
end if;

select count(*) into c from Lessons l 
	where GET_CUR_LESSON(l.start_date, NEW.start_date, l.end_date, l.frequency) = 1 
	and l.para = NEW.para
	and l.id_group = NEW.id_group;

if c > 0 then
	RAISE EXCEPTION 'Пара в то время уже назначена!';
  
end if;
return NEW;
end
$$ LANGUAGE plpgsql;

create trigger chak_l before 
insert or update on lessons 
for each row execute procedure chack_lasson();
---

insert into all_user(surname,name,ochestvo,login, password, admin, email) 
       values ('admin', 'admin', 'admin','admin' , sha256('12345'), true, 'admin@admin.com');

