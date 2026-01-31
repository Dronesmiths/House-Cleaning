import os

locations = {
    "palmdale": "Palmdale",
    "lancaster": "Lancaster",
    "quartz-hill": "Quartz Hill",
    "rosamond": "Rosamond",
    "leona-valley": "Leona Valley",
    "lake-los-angeles": "Lake Los Angeles",
    "littlerock": "Littlerock"
}

def fix_location_pages():
    for folder, city_name in locations.items():
        path = f"locations/{folder}/index.html"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace any service description mentions of Lancaster with city_name
            import re
            content = re.sub(r'services in Lancaster, CA', f'services in {city_name}, CA', content)
            
            # Check for any other Lancaster leaks in the main content area
            # (but not in the layout/footer where Lancaster might be listed as a service area)
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Deep Fixed Location: {city_name}")

if __name__ == "__main__":
    fix_location_pages()
