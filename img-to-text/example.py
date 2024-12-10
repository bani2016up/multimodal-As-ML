import torch
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import os
import requests

def download_model(model_name):
    base_url = f"https://huggingface.co/{model_name}/resolve/main/"
    files_to_download = ["pytorch_model.bin", "config.json", "tokenizer_config.json", "vocab.json", "merges.txt"]

    for file in files_to_download:
        url = base_url + file
        response = requests.get(url)
        if response.status_code == 200:
            os.makedirs(model_name, exist_ok=True)
            with open(os.path.join(model_name, file), "wb") as f:
                f.write(response.content)
        else:
            print(f"Failed to download {file}")

try:
    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
except OSError:
    print("Failed to load the model. Attempting to download...")
    download_model("nlpconnect/vit-gpt2-image-captioning")
    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

def predict_step(image_paths):
    images = []
    for image_path in image_paths:
        i_image = Image.open(image_path)
        if i_image.mode != "RGB":
            i_image = i_image.convert(mode="RGB")
        images.append(i_image)

    pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds

# Test the function
result = predict_step(['image.png'])
print(result)
