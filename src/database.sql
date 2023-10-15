CREATE TABLE payment_plan (
    contract_id INTEGER NOT NULL,
    planned_payment_id INTEGER NOT NULL,
    payment_amount NUMERIC(10, 2) NOT NULL,
    contract_date DATE NOT NULL,
    payment_date DATE NOT NULL,
    is_paid BOOLEAN NOT NULL,
    PRIMARY KEY (contract_id, planned_payment_id)
);

CREATE TABLE payments (
    actual_payment_id INTEGER primary key,
	contract_number varchar(20) not null,
    payment_amount NUMERIC(10, 2) NOT NULL,
    inn VARCHAR(20) NOT NULL,
    payment_date DATE NOT NULL,
    PRIMARY KEY (contract_id, payment_date)
);

CREATE TABLE overpayment (
    actual_payment_id INTEGER NOT NULL,
    contract_number VARCHAR(20) NOT NULL,
    additional_funds NUMERIC(10, 2) NOT NULL,
    inn VARCHAR(20) NOT NULL,
    payment_date DATE NOT NULL,
    PRIMARY KEY (actual_payment_id),
	unique(contract_number, inn, payment_date)
);

CREATE TABLE org_person (
    person_id INTEGER NOT NULL,
    org_id INTEGER NOT NULL,
    PRIMARY KEY (person_id, org_id)
);

CREATE TABLE debtors (
    organization VARCHAR(100) NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    number VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
);

CREATE TABLE organizations (
    id serial primary key,
    name VARCHAR(100) NOT NULL,
    contract_id INTEGER NOT NULL,
    inn VARCHAR(20) NOT NULL,
    unique(name, inn)
);

CREATE TABLE contact_person (
    id serial primary key,
    org_id INTEGER NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
);

CREATE TABLE contracts (
    id serial primary key,
    is_valid DATE NOT NULL,
    contract_number VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
);