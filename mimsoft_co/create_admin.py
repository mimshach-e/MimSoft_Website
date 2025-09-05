#!/usr/bin/env python
"""
Script to create a superuser with a known password.
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mimsoft_co.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    # Check if user already exists
    if User.objects.filter(username='mimsoft_admin').exists():
        user = User.objects.get(username='mimsoft_admin')
        user.set_password('MimSoft2024!')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("Updated existing superuser: mimsoft_admin")
        print("Password: MimSoft2024!")
    else:
        # Create new superuser
        user = User.objects.create_user(
            username='mimsoft_admin',
            email='admin@mimsoft.com',
            password='MimSoft2024!',
            is_staff=True,
            is_superuser=True
        )
        print("Created new superuser: mimsoft_admin")
        print("Password: MimSoft2024!")
    
    print("\nYou can now login to admin with:")
    print("Username: mimsoft_admin")
    print("Password: MimSoft2024!")

if __name__ == '__main__':
    create_superuser()






