from django.db.models import Model
from django.db import models


class SiteSetting(models.Model):
    """Handles global elements like the logo, profile picture, and footer contact info."""
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='site/', blank=True, null=True, help_text="Your long profile picture for the homepage")
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    linkedin_url = models.URLField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Site Setting"

    def __str__(self):
        return "Global Site Settings"


class Experience(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., Software Developer")
    company_name = models.CharField(max_length=255, null=True, blank=True, help_text="Name of the company or organization")
    start_date = models.DateField(null=True, blank=True, help_text="Start date of employment")
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if currently working here")
    is_current = models.BooleanField(default=False, help_text="Check if you currently work here")
    about = models.TextField(help_text="Description of the experience")
    image = models.ImageField(upload_to='experiences/', blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Order to display on the page")

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        if self.company_name:
            return f"{self.title} at {self.company_name}"
        return self.title


class Education(models.Model):
    institution = models.CharField(max_length=255, help_text="Name of School, College, or University")
    degree_or_title = models.CharField(max_length=200, help_text="e.g., Bachelor of Science in Computer Science")
    start_date = models.DateField(null=True, blank=True, help_text="Start date of study")
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if currently pursuing")
    is_current = models.BooleanField(default=False, help_text="Check if you are currently studying here")
    about = models.TextField(blank=True, help_text="Brief summary or description")
    accomplishments = models.TextField(
        blank=True,
        help_text="Key achievements, honors, GPA, relevant coursework, etc."
    )
    image = models.ImageField(upload_to='education/', blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Display order")

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.degree_or_title} - {self.institution}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=255, blank=True, help_text="Link to GitHub or live project")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    # New fields for stack and tools
    tech_stack = models.CharField(max_length=255, blank=True, help_text="e.g., Django, PostgreSQL, Tailwind CSS")
    tools_used = models.CharField(max_length=255, blank=True, help_text="e.g., Git, PyCharm, LangChain")

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Certification(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=255, blank=True, help_text="Link to verify certification")
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Skill(models.Model):
    SKILL_TYPES = (
        ('HARD', 'Hard Skill'),
        ('SOFT', 'Soft Skill'),
    )
    heading = models.CharField(max_length=100, help_text="Name of the skill, e.g., Python")
    icon = models.ImageField(upload_to='skills/')
    skill_type = models.CharField(max_length=4, choices=SKILL_TYPES, default='HARD')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['skill_type', 'order']

    def __str__(self):
        return f"{self.heading} ({self.get_skill_type_display()})"



class ExtraCurricular(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., Hackathon Organizer")
    organization = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    date = models.CharField(max_length=100, blank=True, help_text="e.g., 2024 - 2025")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Reference(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=255, help_text="e.g., Senior Developer at TechCorp")
    contact_info = models.CharField(max_length=255, blank=True, help_text="Email or LinkedIn profile")
    quote = models.TextField(blank=True, help_text="What they said about you")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200, help_text="Company Name")
    logo = models.ImageField(upload_to='companies/')
    link = models.URLField(max_length=255, blank=True, help_text="Optional link to the company website")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name