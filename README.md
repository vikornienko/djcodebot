# $PROJECT_NAME

$PROJECT_DESCRIPTION

## Setup

This project uses uv for dependency management.

## Configure the Git repository

git init --initial-branch=main --object-format=sha1
uv run pre-commit install
git add .
git commit -m "Initial commit"


## Commands from Makefile

- \`make rs\` - Run development server
- \`make mm\` - Make migrations
- \`make mig\` - Apply migrations
- \`make csu\` - Create superuser
- \`make sa\` - Start new app
