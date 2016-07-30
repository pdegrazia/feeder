drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  pet_name text not null
);