from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now

# Gestor de usuarios personalizado
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

# Modelo de usuario personalizado
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Atributos básicos
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name_paternal = models.CharField(max_length=50, verbose_name="Apellido Paterno")
    last_name_maternal = models.CharField(max_length=50, verbose_name="Apellido Materno", blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    password = models.CharField(max_length=128, verbose_name="Contraseña")
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default_profile.png')

    # Relación con los cursos comprados
    cursos_comprados = models.ManyToManyField(
        'cursos.Curso', blank=True, related_name='usuarios', verbose_name="Cursos Comprados"
    )
    
    # Rol (estudiante o administrador)
    ROLE_CHOICES = [
        ('student', 'Estudiante'),
        ('admin', 'Administrador'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student', verbose_name="Rol")

    # Fecha de registro
    date_joined = models.DateTimeField(default=now, verbose_name="Fecha de Registro")

    # Flags administrativos
    is_active = models.BooleanField(default=True, verbose_name="Está Activo")
    is_staff = models.BooleanField(default=False, verbose_name="Es Staff")

    # Gestor personalizado
    objects = CustomUserManager()

    # Configuración de login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name_paternal', 'role']

    def __str__(self):
        return f"{self.first_name} {self.last_name_paternal} - {self.email}"
