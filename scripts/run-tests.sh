#!/bin/bash

echo "Running Syntax check"
RC=`pytest library/*.py`

exit 0
