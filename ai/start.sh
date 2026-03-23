#!/bin/bash
source ~/miniconda3/etc/profile.d/conda.sh
conda env update --file environment.yml --prune
conda activate md
python main.py