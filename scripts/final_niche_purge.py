import os

replacements = {
    "patio project": "move-out cleaning",
    "patio installation": "deep cleaning",
    "patio": "home cleaning",
    "retaining wall": "kitchen deep-clean",
    "Retaining wall": "Kitchen deep-clean",
    "Retaining Wall": "Kitchen Deep-Clean",
    "irrigation": "scrubbing",
    "Irrigation": "Scrubbing",
    "landscaping": "cleaning",
    "Landscaping": "Cleaning",
    "landscape": "cleaning",
    "Landscape": "Cleaning",
    "handyman": "house cleaning",
    "Handyman": "House Cleaning",
    "hauling": "deep cleaning",
    "Hauling": "Deep Cleaning",
    "outdoor structures": "home interiors",
    "outdoor space": "living space",
    "outdoor lighting": "light fixtures",
    "Fire-Resistant Vegetation": "Pet-Safe Cleaning",
    "Sod &": "Deep Scrub &",
    "Sod installation": "Carpet cleaning",
    "weathered backyard": "cluttered home",
    "fence restoration": "home transformation",
    "fence repair": "detail cleaning",
    "yard waste": "clutter",
    "Yard Waste": "Clutter",
    "Yard waste": "Clutter",
}

def bulk_replace(directory):
    for root, dirs, files in os.walk(directory):
        if ".git" in root or "scripts" in root: continue
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                original_content = content
                for key, value in replacements.items():
                    content = content.replace(key, value)
                if content != original_content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Purged Niche: {path}")

if __name__ == "__main__":
    bulk_replace(".")
