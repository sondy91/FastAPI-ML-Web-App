from pathlib import Path

import torch
from diffusers import StableDiffusionPipeline
from PIL.Image import Image

token_path = Path("token.txt")
token = token_path.read_text().strip()

#get your token at https://huggingface.co/settings/token
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", 
    revision="fp16", 
    torch_dtype=torch.float16, 
    use_auth_token=token,
)

pipe.to("cuda")

prompt = "a photograph of an astronaut riding a horse"

# image = pipe(prompt)["sample"][0]

# you can save the image with
# image.save(f"astronaut_rides_horse.png")