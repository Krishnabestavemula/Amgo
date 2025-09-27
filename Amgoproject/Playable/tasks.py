
import os
import subprocess
from django.conf import settings
from .models import Job, Asset




def render_job_function(job_id):
    job = Job.objects.get(id=job_id)
    job.status = 'processing'
    job.save()

    try:
        # Simulate rendering via ffmpeg
        # e.g., overlay text, compress, etc.
        # Suppose project has one asset; pick its file path
        asset = job.project.assets.first()
        input_path = os.path.join(settings.MEDIA_ROOT, asset.file.name)
        output_dir = os.path.join(settings.BASE_DIR, 'outputs')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f'rendered_{job.id}.mp4')

        # Example FFmpeg command (this is just for simulation)
        cmd = [
            "ffmpeg",
            "-i", input_path,
            "-vf", "drawtext=text='Rendered':fontcolor=white:fontsize=24:x=10:y=10",
            output_path
        ]
        subprocess.run(cmd, check=True)

        # Save output path in the job (you may add a field in Job model for output file)
        job.status = 'done'
        job.save()

    except Exception as e:
        job.status = 'failed'
        job.save()
        raise