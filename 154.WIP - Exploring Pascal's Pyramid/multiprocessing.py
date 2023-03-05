import subprocess

n = 200_000
split = [0, 50_000, 75_000, 100_000, 115_000, 130_000,
         145_000, 155_000, 165_000, 175_000, 185_000, 190_000, 195_000, 200_001]

for i in range(len(split)-1):
    subprocess.run(f'start cmd /k python 154m.py {i} {split[i]} {split[i+1]}', shell=True)