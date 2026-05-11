create extension if not exists pgcrypto;
create table if not exists users (
  id serial primary key,
   email varchar(255) not null,
   password varchar(255) not null,
   role varchar(7) not null
  );
create unique index if not exists ux_users_email_ci on users (email);

create table if not exists  questions (
    id serial primary key,
    question_text text not null
);

create table if not exists answers (
    id serial primary key,
    question_id int not null references questions(id) on delete cascade,
    variant text not null,
    score int default 0,
    position int not null
);

CREATE TABLE if not exists user_answers (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL references users(id) on delete cascade,
    question_id INT NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    answer_id INT NOT NULL REFERENCES answers(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (user_id, question_id)
);

create table if not exists refresh_token (
    id int primary key,
    user_id int NOT NULL references users(id) on delete cascade,
    token text not null unique,
    created_at TIMESTAMP DEFAULT NOW()
    );

ALTER TABLE answers
ADD CONSTRAINT answers_question_id_id_unique
UNIQUE (id, question_id);

ALTER TABLE user_answers
ADD CONSTRAINT fk_answer_question
FOREIGN KEY (answer_id, question_id)
REFERENCES answers(id, question_id);

CREATE TABLE if not exists attempts (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL references users(id) on delete cascade,
    started_at TIMESTAMP DEFAULT NOW()
);

ALTER TABLE user_answers
ADD COLUMN attempt_id INT REFERENCES attempts(id);

insert into users (email, password, role)
  values ('example@domain.com', '$2b$12$mCi.qNW5aGspCdyDPfOpzerV.xcDDx551oxgL4Ug7ULFU2d4MxGrq', 'admin') on conflict (email) do nothing;