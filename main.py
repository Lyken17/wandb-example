import wandb
import random


def main(
    seed=42, 
    lora_weights="lora_weights.pt",
    dataset="task",
    model="NousResearch/Llama-7b-hf",
):
    accuracy = random.random()
    # evaluation
    wandb.init(
        # set the wandb project where this run will be logged
        project="sparselora-eval",
        name=f"{model.replace('/', '-')}-{lora_weights}", # => unique name
        # track hyperparameters and run metadata
        config={
            "seed": seed,
            "batch_size": 12,
            "lora_rank": 8,
        },
        resume="auto", # => resume
    )
    wandb.log({
        f'{dataset}-acc': accuracy, 
    })
    
    
import fire
if __name__ == "__main__":
    fire.Fire(main)