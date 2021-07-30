#!/bin/bash

# list databases
show dbs

# create database
use db_validator

# popular o database com as regras básicas
db.rules.insertOne({name: "*", category: "code", status: "active", type: "wildcard"})