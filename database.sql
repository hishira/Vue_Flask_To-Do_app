drop table if exists zadania;
create table if not exists zadania(
	zadanie_id serial primary key ,
	tresc_zadania text not null
);
INSERT INTO zadania ( tresc_zadania) VALUES ('Pierwszy rekord w tabeli, przykladowy tekst');
INSERT INTO zadania ( tresc_zadania) VALUES ('Kolejny rekord do dodania do bazy danych');
INSERT INTO zadania ( tresc_zadania) VALUES ('I jeszcze jeden dla pewnosci jak to bedzie wygladac');
