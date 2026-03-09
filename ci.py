import wandb
import os


print(f"The version of wandb is: {wandb.__version__}")
assert wandb.__version__ == '0.25.0', f'Expected version 0.25.0, but got {wandb.__version__}'
