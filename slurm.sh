#!/bin/bash

#SBATCH --account=$USERNAME
#SBATCH --job-name=Snake
#SBATCH --partition= $SelectedPartition
#SBATCH --time=0-00:15:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --workdir= $Path-of-output-files
#SBATCH --output=Boutput.txt
#SBATCH --error=Berror.txt

if command -v mpirun > /dev/null 2>&1; then
        module purge
        //Load related and necessary modules
fi

cd $path-of-necessary-files

mpirun -np 4 python -m mpi4py jobs.py

exit
