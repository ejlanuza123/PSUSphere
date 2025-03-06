from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE('Starting data population...'))
        self.create_colleges(5)
        self.create_programs(10)
        self.create_organizations(10)
        self.create_students(50)
        self.create_memberships(20)
        self.stdout.write(self.style.SUCCESS('Data population completed successfully.'))

    def create_colleges(self, count):
        fake = Faker()
        for _ in range(count):
            college_name = fake.unique.company()
            College.objects.get_or_create(college_name=college_name)
        self.stdout.write(self.style.SUCCESS(f'{count} colleges created successfully.'))
    
    def create_programs(self, count):
        fake = Faker()
        colleges = list(College.objects.all())
        if not colleges:
            self.stdout.write(self.style.ERROR('No colleges found. Programs cannot be created.'))
            return
        
        for _ in range(count):
            Program.objects.create(
                prog_name=fake.unique.job(),
                college=fake.random_element(colleges)
            )
        self.stdout.write(self.style.SUCCESS(f'{count} programs created successfully.'))
    
    def create_organizations(self, count):
        fake = Faker()
        colleges = list(College.objects.all())
        if not colleges:
            self.stdout.write(self.style.ERROR('No colleges found. Organizations cannot be created.'))
            return
        
        for _ in range(count):
            Organization.objects.create(
                name=fake.unique.company(),
                college=fake.random_element(colleges),
                description=fake.sentence()
            )
        self.stdout.write(self.style.SUCCESS(f'{count} organizations created successfully.'))

    def create_students(self, count):
        fake = Faker('en_PH')
        programs = list(Program.objects.all())
        if not programs:
            self.stdout.write(self.style.ERROR('No programs found. Students cannot be created.'))
            return
        
        for _ in range(count):
            Student.objects.create(
                student_id=f'{fake.random_int(2020, 2024)}-{fake.random_int(1000, 9999)}',
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=fake.random_element(programs)
            )
        self.stdout.write(self.style.SUCCESS(f'{count} students created successfully.'))

    def create_memberships(self, count):
        fake = Faker()
        students = list(Student.objects.all())
        organizations = list(Organization.objects.all())
        if not students or not organizations:
            self.stdout.write(self.style.ERROR('Students or organizations missing. Memberships cannot be created.'))
            return

        for _ in range(count):
            OrgMember.objects.create(
                student=fake.random_element(students),
                organization=fake.random_element(organizations),
                date_joined=fake.date_between(start_date='-2y', end_date='today')
            )
        self.stdout.write(self.style.SUCCESS(f'{count} student memberships created successfully.'))
