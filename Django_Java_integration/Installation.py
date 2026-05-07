!pip install djangorestframework django jpype1 -q
!apt-get install -y default-jdk -q   # installs Java for JPype

import subprocess
result = subprocess.run(['java', '-version'], capture_output=True, text=True)
print("Java:", result.stderr.strip())
print("Django install done")
