# Amgo
Assignment
Use python 3.12.3
Installation steps:
# Installation Steps

1. **Run PostgreSQL and Redis with Docker**  
   Open a terminal and run:  
   ```bash
   docker compose up -d
   
2. Creating and activating your Python virtual environment
   
        python3 -m venv venv
        source venv/bin/activate
   
3.Install project dependencies

      pip install --upgrade pip
      pip install -r requirements.txt
      
4.Run database migrations

      python manage.py migrate
      
5.Start the Django development server

      python manage.py runserver
      
Swagger Url:

   http://127.0.0.1:8002/api/swagger/


To stop Docker containers:

    docker compose down
    
To deactivate the virtual environment:

    deactivate


FFmpeg Installation

FFmpeg is required for video processing in this project. Follow the instructions below to install FFmpeg on your system:

          Ubuntu / Debian
          sudo apt update
          sudo apt install ffmpeg

To run Queue use this command

          python manage.py rqworker --with-scheduler default

To create a user open shell

      python manage.py shell

      User.objects.create(email=test_mail)
      p=User.objects.get(id=id)
      p.is_superuser=True
      p.is_staff=True
      p.set_password=password
      p.save()
      
