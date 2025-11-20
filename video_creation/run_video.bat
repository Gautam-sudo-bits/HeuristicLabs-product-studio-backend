@echo off
set PYTHONUNBUFFERED=1
set MKL_NUM_THREADS=1
set NUMEXPR_NUM_THREADS=1
set OMP_NUM_THREADS=1
set KMP_DUPLICATE_LIB_OK=TRUE

python -u main.py create config_dewalt.json
pause