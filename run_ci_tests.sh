#!/usr/bin/env bash

# this is used by the aws-composer-tools pipeline to test / check coverage

set -xe

if [ -d venv ]; then
    rm -rf venv
fi

virtualenv venv
source venv/bin/activate
set -xe

curl -s https://bootstrap.pypa.io/get-pip.py > get-pip.py
python get-pip.py

pip install -r requirements.txt

coverage run \
    --source stack_matchers \
    -m pytest \
    --junitxml=tools-ci-pytest.xml \
    tests
coverage html \
    --omit '*cli.py','*__init__.py' \
    --fail-under 90
