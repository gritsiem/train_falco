#!/bin/bash
#SBATCH --partition=amilan
#SBATCH --job-name=data-job
#SBATCH --output=example-job.%j.out
#SBATCH --time=01:00:00
#SBATCH --qos=normal
#SBATCH --nodes=1

