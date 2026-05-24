create extension if not exists pgcrypto;
CREATE TABLE if not exists activation_codes (
    id SERIAL PRIMARY KEY,
    user_email VARCHAR NOT NULL,
    code VARCHAR NOT NULL UNIQUE,
    is_used BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL
);
CREATE INDEX if not exists ix_activation_codes_user_email
ON activation_codes (user_email);
create table if not exists users (
  id serial primary key,
   email varchar(255) not null,
   password varchar(255) not null,
   role varchar(7) not null,
    is_active boolean default false
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

ALTER TABLE answers
ADD CONSTRAINT answers_question_id_id_unique
UNIQUE (id, question_id);

CREATE TABLE attempts (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    started_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE user_answers (
    id SERIAL PRIMARY KEY,

    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    question_id INT NOT NULL REFERENCES questions(id) ON DELETE CASCADE,

    answer_id INT NOT NULL,

    attempt_id INT NOT NULL REFERENCES attempts(id) ON DELETE CASCADE,

    created_at TIMESTAMP DEFAULT NOW(),

    CONSTRAINT uix_attempt_question
        UNIQUE (attempt_id, question_id),

    CONSTRAINT fk_answer_question
        FOREIGN KEY (answer_id, question_id)
        REFERENCES answers(id, question_id)
);

create table if not exists refresh_tokens (
    id serial primary key,
    user_id int NOT NULL references users(id) on delete cascade,
    token text not null unique,
    created_at TIMESTAMP DEFAULT NOW()
    );

insert into users (email, password, role, is_active)
  values ('example@domain.com', '$2b$12$mCi.qNW5aGspCdyDPfOpzerV.xcDDx551oxgL4Ug7ULFU2d4MxGrq', 'admin', true) on conflict (email) do nothing;