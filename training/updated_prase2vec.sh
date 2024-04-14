#!/bin/bash
#SBATCH --partition=cm3atou
#SBATCH --output=python_%J_stdout.txt
#SBATCH --error=python_%J_stderr.txt


#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=32G
#SBATCH --time=10:10:00

module load Python/3.8.6-GCCcore-10.2.0


source /home/xinwang/my_python_envs/python38/bin/activate

python "/training/updated_phrase2vec.py"  -hs -sg --corpus "training/models/test" --model_name "test"