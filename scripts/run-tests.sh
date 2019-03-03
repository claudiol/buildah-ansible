#!/bin/bash

echo "Running Syntax check"
RC=`pytest library/*.py`

echo "Results: $RC"

exit 0
