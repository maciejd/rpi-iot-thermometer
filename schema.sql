drop table if exists temps;
create table temps (
  id integer primary key autoincrement,
  temp double not null,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
