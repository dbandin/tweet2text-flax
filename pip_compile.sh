#!/bin/bash
pip-compile --no-emit-index-url --output-file requirements/dev.txt requirements/dev.in
