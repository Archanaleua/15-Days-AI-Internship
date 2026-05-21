import requests
from PIL import Image
from io import BytesIO
import urllib.parse

def generate_image(prompt, filename):
    print(f"Generating image: {prompt}")
    
    # Encode prompt for URL
    encoded_prompt = urllib.parse.quote(prompt)
    
    # Pollinations AI - Free, no API key needed!
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&nologo=true"
    
    response = requests.get(url, timeout=60)
    
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(filename)
        print(f"✅ Image saved: {filename}")
    else:
        print(f"❌ Error: {response.status_code}")

# Generate 3 different images
generate_image("a beautiful sunset over mountains", "sunset.png")
generate_image("a futuristic city with AI robots", "future_city.png")
generate_image("a cute cat wearing glasses", "cat.png")

print("\n🎉 All images generated successfully!")