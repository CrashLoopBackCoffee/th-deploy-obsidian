#!/usr/bin/env bash

set -x
set -eu

black .
flake8ruff check --fix
