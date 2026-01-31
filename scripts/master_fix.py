import os
import re

def master_fix(content, filename):
    # 1. Add Locations to Header Nav
    if '<a href="/locations/">Locations</a>' not in content:
        # Standardize: Find the </ul> in the nav
        content = content.replace('<li><a href="/blog/">Blog</a></li>', '<li><a href="/blog/">Blog</a></li>\n                                    <li><a href="/locations/">Locations</a></li>')

    # 2. Fix Palmdale Neighborhood Leaks (if in Palmdale page)
    if "locations/palmdale/index.html" in filename:
        content = content.replace('West Lancaster', 'West Palmdale')
        content = content.replace('East Lancaster', 'East Palmdale')
        content = content.replace('neighborhoods in East Lancaster', 'neighborhoods in East Palmdale')
        content = content.replace('service in Lancaster', 'service in Palmdale')
        content = content.replace('serving all of Lancaster', 'serving all of Palmdale')
        content = content.replace('residents choose Antelope Valley Home Cleaners', 'residents choose professional cleaning')

    # 3. Forensic Terminology Purge (Global)
    purges = {
        '[Business Name]': 'Antelope Valley Home Cleaners',
        '[City]': 'Palmdale',
        '[Niche]': 'Residential Cleaning',
        '[Service]': 'Home Cleaning',
        '[Location]': 'Antelope Valley',
        'custom kitchens': 'deep kitchen cleaning',
        'repair, cleanup, and outdoor improvements': 'cleaning, sanitizing, and interior care',
        'repairs, cleanup, and outdoor improvements': 'cleaning, sanitizing, and interior care',
        'small repairs to major improvements': 'routine cleans to deep-cleaning overhauls',
        'minor repairs to major': 'minor spills to major',
        'kitchens, retaining walls, scrubbing': 'kitchens, bathrooms, scrubbing',
        'fixed our deck and excellent cleaning': 'finished our move-out clean perfectly',
        'Fixed our deck': 'Cleaned our home',
        'landscape design': 'house cleaning',
        'irrigation systems': 'deep scrubbing',
        'junk removal': 'deep cleaning',
        'hauling': 'deep cleaning',
        'Hauling': 'Deep Cleaning',
        'handyman': 'cleaning specialist',
        'Handyman': 'Cleaning Specialist',
        'project - repairs': 'project - cleaning',
        'repairs, cleanup': 'sanitizing, cleanup',
        'home and property improvements': 'residential and property cleaning',
        'home and property needs': 'residential cleaning needs',
        'Professional home services': 'Professional home cleaning',
        'house-cleaning repairs': 'house-cleaning tasks',
        'all your home and property needs': 'all your home cleaning needs',
        'd1sxjpzrvgytjj.cloudfront.net': 'd20ht2uttlso5r.cloudfront.net',
        '/Users/mediusa/NOVA/Repos/Reed and Sons': '/Users/mediusa/NOVA/Repos/House Cleaners',
        'Reed and Sons': 'Antelope Valley Home Cleaners',
        'hauled away all our interior waste and construction debris': 'cleaned our entire home and handled all the deep-cleaning',
        'interior waste and construction debris': 'intensive cleaning and sanitizing',
        'waste-cleanup-pro.webp': 'deep-clean-master.webp',
        'debris removal': 'deep sanitizing',
        'What We Haul Away': 'Deep Cleaning Specialists',
        'hauling away': 'intensive cleaning',
        'construction waste': 'environmental dust',
        'trash': 'dust',
        'Trash': 'Sanitizing',
        'hauled': 'deep-cleaned',
        'Hauled': 'Deep-Cleaned',
        'debris': 'buildup',
        'My truck broke down': 'We needed a move-out clean',
        'towed it for free': 'scheduled us same-day',
        'paid me cash': 'gave us a great price',
        'towing': 'cleaning',
        'Towing': 'Cleaning',
        'junk car': 'dirty home',
        'cash same day': 'service same day'
    }

    for key, value in purges.items():
        content = content.replace(key, value)
    
    # Case insensitive regex for some missed ones
    content = re.sub(r'professional (home|property) services', r'professional home cleaning', content, flags=re.IGNORECASE)
    content = re.sub(r'home (and|&) property improvements', r'home cleaning services', content, flags=re.IGNORECASE)

    return content

def run_fix():
    for root, dirs, files in os.walk("."):
        if ".git" in root: continue
        for file in files:
            if file == "master_fix.py": continue
            if file.endswith((".html", ".md", ".py")):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = master_fix(content, path)
                
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Master Fixed: {path}")

if __name__ == "__main__":
    run_fix()
