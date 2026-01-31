import os

replacements = {
    "yard cleanup": "full house cleaning",
    "Yard cleanup": "Full house cleaning",
    "yard": "interior",
    "Yard": "Interior",
    "Transform Your Property": "Transform Your Home",
    "Professional handyman": "Professional house cleaning",
    "Professional Handyman": "Professional House Cleaning"
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
                    print(f"Final Polish: {path}")

if __name__ == "__main__":
    bulk_replace(".")
