import os

def fix_content(content):
    # Service 1: Residential Cleaning (Routine)
    s1_title = "<h3>Residential Cleaning</h3>"
    s1_desc = """<p>Routine Home Cleaning<br>
                        Dusting & Vacuuming<br>
                        Floor Mopping & Care<br>
                        Kitchen & Bath Wipe Down<br>
                        Linen & Bed Changes</p>"""
    
    # Service 2: Move-Out Cleaning
    s2_title = "<h3>Move-Out Cleaning</h3>"
    s2_desc = """<p>Rental Turnover Service<br>
                        Security Deposit Recovery<br>
                        Full Appliance Cleaning<br>
                        Cabinet & Drawer Detail<br>
                        Move-Ready Standards</p>"""
    
    # Service 3: Deep Cleaning
    s3_title = "<h3>Deep Cleaning</h3>"
    s3_desc = """<p>Top-to-Bottom Sanitizing<br>
                        Inside Oven & Fridge<br>
                        Baseboard & Trim Detail<br>
                        Window & Sills Scrub<br>
                        Full Wall Washing</p>"""

    # We need to find the blocks and replace them safely. 
    # Since the structure is consistent, we can use some markers.
    
    # This is a bit complex for a simple replace if we want to be exact.
    # I'll just look for the H3 and replace the following P tag.
    
    import re
    
    content = re.sub(r"<h3>Move-Out Cleaning</h3>\s*<p>.*?</p>", s2_title + "\n                    " + s2_desc, content, flags=re.DOTALL)
    content = re.sub(r"<h3>Residential Cleaning</h3>\s*<p>.*?</p>", s1_title + "\n                    " + s1_desc, content, flags=re.DOTALL)
    content = re.sub(r"<h3>Deep Cleaning</h3>\s*<p>.*?</p>", s3_title + "\n                    " + s3_desc, content, flags=re.DOTALL)

    # Fix images
    content = content.replace("url('/images/move-out-cleaning-hero.webp')", "url('/images/handyman-team-refined.webp')")
    content = content.replace("url('/images/handyman-hero.webp')", "url('/images/leona-valley-oasis.webp')")
    content = content.replace("url('/images/hauling-junk.webp')", "url('/images/waste-cleanup-pro.webp')")
    
    return content

def bulk_replace(directory):
    for root, dirs, files in os.walk(directory):
        if ".git" in root or "scripts" in root: continue
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = fix_content(content)
                
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Verified & Fixed: {path}")

if __name__ == "__main__":
    bulk_replace(".")
