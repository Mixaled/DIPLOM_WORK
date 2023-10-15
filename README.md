# Project README

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Scripts](#scripts)
  - [find_debtors.py](#find_debtorspy)
  - [clear_deb.py](#clear_debpy)
  - [clear.py](#clearpy)
  - [get.py](#getpy)
  - [json_format.py](#json_formatpy)
  - [send.py](#sendpy)
  - [test_BD.py](#test_bdpy)
- [Database Schema](#database-schema)
- [License](#license)

## Introduction

This repository contains a collection of Python scripts and SQL files related to debt management and data processing. These scripts are designed to work with a PostgreSQL database and SQLAlchemy as the database toolkit. The primary purpose of these scripts is to find and manage debtors, format data as JSON, and send it to a remote service.

## Project Structure

- **Scripts**: Contains Python scripts for various tasks.
- **data_base.sql**: SQL script defining the database schema.

## Scripts

### find_debtors.py

This script retrieves debtor information from the database and updates the debtors table based on certain criteria. It creates a view called `additional_info` and inserts relevant data into the `debtors` table.

### clear_deb.py

This script clears data from various tables related to organizations, contact persons, contracts, payments, overpayments, payment plans, and organization-person relationships, while keeping the `debtors` table intact.

### clear.py

This script clears data from various tables related to organizations, contact persons, contracts, payments, overpayments, payment plans, and organization-person relationships, including the `debtors` table.

### get.py

This script makes an HTTP GET request to a remote site, retrieves JSON data, and processes it by updating the database and removing debtors if their payments are marked as paid.

### json_format.py

This script queries the database to retrieve debtor information, formats it as JSON, and saves the JSON data to a file named `debtors.json` in the `send` directory.

### send.py

This script reads the `debtors.json` file from the `send` directory and sends it as a JSON payload to a remote service using an HTTP POST request.

### test_BD.py

This script populates the database with sample data for testing purposes. It inserts data into various tables, including organizations, contact persons, contracts, payments, overpayments, payment plans, and organization-person relationships.

## Database Schema

The `data_base.sql` file defines the database schema, including the following tables:

- `payment_plan`: Stores payment plan details.
- `payments`: Stores payment information.
- `overpayment`: Stores overpayment details.
- `org_person`: Represents the relationship between organizations and contact persons.
- `debtors`: Contains information about debtors.
- `organizations`: Stores information about organizations.
- `contact_person`: Contains data about contact persons.
- `contracts`: Stores contract information.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to your needs.
