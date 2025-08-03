from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Set up production environment with superuser and initial data'

    def handle(self, *args, **options):
        self.stdout.write('Setting up production environment...')
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(
                self.style.SUCCESS('Superuser created successfully!')
            )
        else:
            self.stdout.write('Superuser already exists.')
        
        # Run migrations
        call_command('migrate')
        self.stdout.write(
            self.style.SUCCESS('Migrations completed successfully!')
        )
        
        # Collect static files
        call_command('collectstatic', '--noinput')
        self.stdout.write(
            self.style.SUCCESS('Static files collected successfully!')
        )
        
        self.stdout.write(
            self.style.SUCCESS('Production setup completed!')
        ) 