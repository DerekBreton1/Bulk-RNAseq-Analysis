import sys
import subprocess
import os
import gzip
import shutil

# Get command-line arguments
accession_dir = sys.argv[1]
outdir = sys.argv[2]

# Construct the fastq-dump command
dump_command = f"fasterq-dump -O {outdir} {accession_dir}"
print(f"Created fasterq-dump command for: {accession_dir}")

# Run the fastq-dump command
subprocess.run(dump_command, shell=True)

# Define paths to output files
accession = os.path.basename(accession_dir).replace(".sra", "")
fastq_files = [f"{outdir}/{accession}.fastq",
               f"{outdir}/{accession}_1.fastq",
               f"{outdir}/{accession}_2.fastq"]

# Compress the FASTQ files
for file in fastq_files:
    if os.path.exists(file):
        with open(file, 'rb') as f_in:
            with gzip.open(file + '.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        os.remove(file) # remove uncompressed fastq file
os.remove(accession_dir) # remove SRA file to save space