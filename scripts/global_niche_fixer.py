import os

replacements = {
    "irrigation": "scrubbing",
    "Irrigation": "Scrubbing",
    "landscaping": "cleaning",
    "Landscaping": "Cleaning",
    "residentials": "residential cleanings",
    "Residentials": "Residential Cleanings",
    "move-out-cleaning design": "move-out cleaning",
    "deep cleaning": "deep cleaning",
    "buildup deep-cleaning": "sanitizing",
    "outdoor lighting": "surface polishing",
    "Outdoor lighting": "Surface polishing",
    "Custom kitchens": "Full kitchen cleaning",
    "Custom Bathrooms": "Full bathroom sanitizing",
    "transform your outdoor space": "transform your home atmosphere",
    "outdoor space": "living space",
    "stunning results": "sparkling results",
    "design to installation": "booking to sparkling finish",
    "create outdoor spaces": "create clean homes",
    "concrete, paver, and stone": "tile, grout, and hardwood",
    "erosion control": "odor control",
    "showcase your property": "sanitize your property",
    "sprinkler and drip": "eco-friendly cleaning",
    "lawn transformation": "home transformation",
    "sprinkler": "cleaning agent",
    "Design Consult": "Free Quote",
    "Expert Build": "Deep Clean",
    "expert repairs": "expert cleaning",
    "beautiful residentials": "beautiful homes",
    "property cleanups": "property cleanings"
}

def bulk_replace(directory):
    for root, dirs, files in os.walk(directory):
        if ".git" in root or "scripts" in root: continue
        for file in files:
            if file.endswith((".html", ".md")):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                original_content = content
                for key, value in replacements.items():
                    content = content.replace(key, value)
                if content != original_content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Global Sweep: {path}")

if __name__ == "__main__":
    bulk_replace(".")
