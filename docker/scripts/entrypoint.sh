#!/bin/bash
echo "Running Django migrations..."
python manage.py migrate
exec "\$@"
