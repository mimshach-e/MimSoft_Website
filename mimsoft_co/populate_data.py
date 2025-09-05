#!/usr/bin/env python
"""
Script to populate the database with sample data for MimSoft Corporation website.
Run this after migrations: python manage.py shell < populate_data.py
"""

import os
import django
from datetime import date, timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mimsoft_co.settings')
django.setup()

from services.models import Service
from team.models import TeamMember
from projects.models import Project
from testimonials.models import Testimonial
from contact.models import ContactSubmission

def create_sample_data():
    print("Creating sample data...")
    
    # Create Services
    services_data = [
        {
            'name': 'Website Development',
            'category': 'SOFTWARE_DEV',
            'description': 'Custom website development using modern technologies like React, Django, and Node.js. We create responsive, SEO-optimized websites that drive business growth.',
            'order': 1
        },
        {
            'name': 'Mobile App Development',
            'category': 'SOFTWARE_DEV',
            'description': 'Native and cross-platform mobile applications for iOS and Android. We build user-friendly apps that engage customers and streamline business processes.',
            'order': 2
        },
        {
            'name': 'E-commerce Solutions',
            'category': 'SOFTWARE_DEV',
            'description': 'Complete e-commerce platforms with payment integration, inventory management, and customer analytics. We help businesses sell online effectively.',
            'order': 3
        },
        {
            'name': 'Social Media Management',
            'category': 'SOCIAL_MARKETING',
            'description': 'Comprehensive social media strategy and management. We create engaging content, manage campaigns, and build strong online communities.',
            'order': 4
        },
        {
            'name': 'Digital Marketing',
            'category': 'SOCIAL_MARKETING',
            'description': 'SEO, PPC, content marketing, and email campaigns. We use data-driven strategies to increase online visibility and drive conversions.',
            'order': 5
        },
        {
            'name': 'UI/UX Design',
            'category': 'CREATIVE',
            'description': 'User-centered design that creates intuitive, engaging user experiences. We design interfaces that users love and that drive business results.',
            'order': 6
        }
    ]
    
    services = []
    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            name=service_data['name'],
            defaults=service_data
        )
        services.append(service)
        if created:
            print(f"Created service: {service.name}")
    
    # Create Team Members
    team_data = [
        {
            'name': 'Sarah Johnson',
            'role': 'CEO & Founder',
            'bio': 'Sarah is a visionary leader with over 15 years of experience in software development and business strategy. She founded MimSoft with the mission to make technology accessible to businesses of all sizes.',
            'department': 'MANAGEMENT',
            'order': 1
        },
        {
            'name': 'Michael Chen',
            'role': 'Lead Software Engineer',
            'bio': 'Michael is a full-stack developer with expertise in Python, JavaScript, and cloud technologies. He leads our development team and ensures code quality across all projects.',
            'department': 'DEVELOPMENT',
            'order': 2
        },
        {
            'name': 'Emily Rodriguez',
            'role': 'Senior UI/UX Designer',
            'bio': 'Emily creates beautiful, intuitive user experiences that users love. She has a passion for human-centered design and stays current with the latest design trends.',
            'department': 'DESIGN',
            'order': 3
        },
        {
            'name': 'David Kim',
            'role': 'Digital Marketing Specialist',
            'bio': 'David specializes in SEO, PPC, and content marketing. He helps our clients increase their online visibility and drive measurable business results.',
            'department': 'MARKETING',
            'order': 4
        }
    ]
    
    team_members = []
    for member_data in team_data:
        member, created = TeamMember.objects.get_or_create(
            name=member_data['name'],
            defaults=member_data
        )
        team_members.append(member)
        if created:
            print(f"Created team member: {member.name}")
    
    # Create Projects
    projects_data = [
        {
            'title': 'E-commerce Platform for TechGear',
            'client_name': 'TechGear Inc.',
            'category': 'ECOMMERCE',
            'description': 'A comprehensive e-commerce platform with advanced inventory management, customer analytics, and seamless payment processing. The platform increased online sales by 300% in the first year.',
            'date_delivered': date.today() - timedelta(days=60),
            'project_url': 'https://techgear.com'
            # Note: client_logo field is optional and can be added via admin
        },
        {
            'title': 'Mobile Banking App for FinTech Solutions',
            'client_name': 'FinTech Solutions',
            'category': 'FINTECH',
            'description': 'A secure, user-friendly mobile banking application with biometric authentication, real-time notifications, and comprehensive financial management tools.',
            'date_delivered': date.today() - timedelta(days=120),
            'project_url': 'https://fintechsolutions.com'
            # Note: client_logo field is optional and can be added via admin
        },
        {
            'title': 'Corporate Website for GreenEnergy',
            'client_name': 'GreenEnergy Corp.',
            'category': 'WEB_APP',
            'description': 'A modern, responsive corporate website with integrated content management system, blog platform, and lead generation forms.',
            'date_delivered': date.today() - timedelta(days=90),
            'project_url': 'https://greenenergy.com'
            # Note: client_logo field is optional and can be added via admin
        }
    ]
    
    projects = []
    for project_data in projects_data:
        project, created = Project.objects.get_or_create(
            title=project_data['title'],
            defaults=project_data
        )
        # Add services to projects
        if created:
            project.service_provided.add(services[0])  # Website Development
            if 'Mobile' in project.title:
                project.service_provided.add(services[1])  # Mobile App Development
            if 'E-commerce' in project.title:
                project.service_provided.add(services[2])  # E-commerce Solutions
        projects.append(project)
        if created:
            print(f"Created project: {project.title}")
    
    # Create Testimonials
    testimonials_data = [
        {
            'client_name': 'Jennifer Smith',
            'company': 'TechGear Inc.',
            'role': 'Marketing Director',
            'content': 'MimSoft transformed our online presence completely. Their e-commerce platform exceeded our expectations and has significantly increased our sales. The team was professional, responsive, and delivered on time.',
            'is_featured': True
        },
        {
            'client_name': 'Robert Johnson',
            'company': 'FinTech Solutions',
            'role': 'CTO',
            'content': 'The mobile banking app developed by MimSoft is exceptional. It\'s secure, user-friendly, and has received excellent feedback from our customers. Highly recommended!',
            'is_featured': True
        },
        {
            'client_name': 'Lisa Wang',
            'company': 'GreenEnergy Corp.',
            'role': 'Communications Manager',
            'content': 'Working with MimSoft was a pleasure. They understood our vision perfectly and delivered a website that perfectly represents our brand and mission.',
            'is_featured': False
        }
    ]
    
    testimonials = []
    for testimonial_data in testimonials_data:
        testimonial, created = Testimonial.objects.get_or_create(
            client_name=testimonial_data['client_name'],
            company=testimonial_data['company'],
            defaults=testimonial_data
        )
        testimonials.append(testimonial)
        if created:
            print(f"Created testimonial from: {testimonial.client_name}")
    
    # Link testimonials to projects
    if len(testimonials) >= 3 and len(projects) >= 3:
        testimonials[0].project = projects[0]  # TechGear testimonial
        testimonials[0].save()
        testimonials[1].project = projects[1]  # FinTech testimonial
        testimonials[1].save()
        testimonials[2].project = projects[2]  # GreenEnergy testimonial
        testimonials[2].save()
        
        # Update projects with testimonials
        projects[0].testimonial = testimonials[0]
        projects[0].save()
        projects[1].testimonial = testimonials[1]
        projects[1].save()
        projects[2].testimonial = testimonials[2]
        projects[2].save()
    
    print("\nSample data creation completed successfully!")
    print(f"Created {len(services)} services")
    print(f"Created {len(team_members)} team members")
    print(f"Created {len(projects)} projects")
    print(f"Created {len(testimonials)} testimonials")

if __name__ == '__main__':
    create_sample_data()
