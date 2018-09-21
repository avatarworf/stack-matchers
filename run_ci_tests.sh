#!/usr/bin/env bash

# this is used by the aws-composer-tools pipeline to test / check coverage

set -e

if [ -d venv ]; then
    rm -rf venv
fi

virtualenv -p python3.6 venv >/dev/null 2>&1

source venv/bin/activate

pip install --upgrade pip==10.0.1
pip install \
        -U \
        -e \
        "git+ssh://git@github.com/Financial-Times/aws-composer-pipeline-scripts-general.git@${composer_commit}#egg=aws_composer_general" \
        "git+ssh://git@github.com/Financial-Times/aws-composer-pipeline-scripts-general.git@${composer_commit}#egg=aws_composer_general[testing]" \
        --process-dependency-links

composer run-tests tests --coverage --cov_dir stack-matchers

coverage run \
    --source stack_matchers \
    -m pytest \
    --junitxml=tools-ci-pytest.xml \
    tests

coverage html \
    --omit '*cli.py','*__init__.py' \
    --fail-under 60
