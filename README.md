# DJCODEBOT

The project for self-study of the Django framework.

## Setup

This project uses uv for dependency management.  
The bash script django_start_uvv2.sh from the repository [MyBashScripts](https://github.com/vikornienko/myBashScripts) was used to launch this project.  

## Description

This is a web service project build using the Django framework. The project incorporates:  

- uv package manager;  
- mypy type checking;  
- ruff linter and formatter;  
- pre-commit hooks;  
- makefile for command automation;  
- bootstrap 5 and prism.js for frontend;  
- compatible with OpenAI API.  

This service helps users fix buggy code.  
The user enters code into a field on the page; this code is then sent to a LLM API, wich returns the correct code.

## Configure the Git repository

I using self-hosted gitlab ce and github.com for storing my repositories.  

For self-hosted gitlab ce:

git init --initial-branch=main --object-format=sha1
uv run pre-commit install
git add .  
make rpc
git commit -m "Initial commit"

For github.com:  

git remote add github <git@github.com>:vikornienko/djcodebot.git  
git push -u github main  
git push -u github dev

## Commands from Makefile

- \`make rs\` - Run development server
- \`make mm\` - Make migrations
- \`make mig\` - Apply migrations
- \`make csu\` - Create superuser
- \`make sa\` - Start new app
