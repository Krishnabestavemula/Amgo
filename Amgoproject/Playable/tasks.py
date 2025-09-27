
import os
import subprocess
from django.conf import settings
from .models import Job




def render_job_function(job_id):
    job = Job.objects.get(id=job_id)
    job.status = 'processing'
    job.save()

    try:

        asset = job.project.assets.first()
        input_path = os.path.join(settings.MEDIA_ROOT, asset.file.name)
        output_dir = os.path.join(settings.BASE_DIR, 'outputs')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f'rendered_{job.id}.mp4')

        cmd = [
            "ffmpeg",
            "-i", input_path,
            "-vcodec", "libx264",
            "-b:v", "800k",
            "-vf", "scale=iw*0.5:ih*0.5",
            "-acodec", "aac",
            "-b:a", "128k",
            output_path
        ]

        subprocess.run(cmd, check=True)
        job.status = 'done'
        job.save()



    except Exception as e:
        job.status = 'failed'
        job.save()
        raise