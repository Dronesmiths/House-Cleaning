import os
import re

mapping = {
    r'patios?': 'home cleanings',
    r'Patios?': 'Home Cleanings',
    r'retaining walls?': 'kitchen deep-cleanings',
    r'Retaining [Ww]alls?': 'Kitchen Deep-Cleanings',
    r'irrigation( systems)?': 'deep scrubbing',
    r'Irrigation( [Ss]ystems)?': 'Deep Scrubbing',
    r'landscape( design)?': 'house cleaning',
    r'Landscape( [Dd]esign)?': 'House Cleaning',
    r'hardscaping?': 'residential cleaning',
    r'Hardscaping?': 'Residential Cleaning',
    r'handym[ae]n': 'cleaning specialist',
    r'Handym[ae]n': 'Cleaning Specialist',
    r'deep cleaning': 'deep cleaning',
    r'Deep Cleaning': 'Deep Cleaning',
}

def brute_purge(directory):
    for root, dirs, files in os.walk(directory):
        if ".git" in root or "scripts" in root: continue
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = content
                for pattern, subst in mapping.items():
                    new_content = re.sub(pattern, subst, new_content)
                
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Brute Purged: {path}")

if __name__ == "__main__":
    brute_purge(".")
