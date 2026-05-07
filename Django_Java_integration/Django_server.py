import subprocess, time

# Apply migrations first
subprocess.run(
    ["python", "manage.py", "migrate", "--run-syncdb"],
    cwd=DJANGO_APP
)

# Start server in background
server = subprocess.Popen(
    ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"],
    cwd=DJANGO_APP,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

time.sleep(4)
print("Django server started (PID:", server.pid, ")")
print("Running at http://localhost:8000")
