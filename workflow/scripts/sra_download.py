import sys
import subprocess

# Get command-line arguments
accession = sys.argv[1]
outdir = sys.argv[2]

# Construct the prefetch command
prefetch_command = f"prefetch {accession} -O {outdir}"
print(f"Created prefetch command for {accession}")

# Run the prefetch command
subprocess.run(prefetch_command, shell=True)