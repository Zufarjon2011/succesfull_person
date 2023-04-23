import random
from time import sleep
from tqdm import tqdm

print("Взлом telegram в процессе ...")
for i in tqdm(range(100), colour="yellow"):
	sleep(random.uniform(0.01, 0.1))

print("TELEGRAM успешно взломана!!!")	