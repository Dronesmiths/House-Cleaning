import os

replacements = {
    "Deep Cleaning Services Services": "Deep Cleaning Services",
    "[CITY_6]": "Lake Los Angeles",
    "[SERVICE_AREAS]": "Palmdale, Lancaster, Quartz Hill",
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
                    print(f"Final Fixup: {path}")

if __name__ == "__main__":
    bulk_replace(".")
