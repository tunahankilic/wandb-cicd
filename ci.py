import wandb

print(f"The version of wandb is: {wandb.__version__}")
assert wandb.__version__ == '0.19.8', f'Expected version 0.19.8, but got {wandb.__version__}'
