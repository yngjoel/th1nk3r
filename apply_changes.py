import os
import glob
import re

directory = r"c:\Users\yngjo\OneDrive\Desktop\Personal Projects\Th1nk3r By Joel Yang"
html_files = glob.glob(os.path.join(directory, "*.html"))

avatar_pattern = re.compile(r'https://lh3\.googleusercontent\.com/aida-public/[A-Za-z0-9_-]+')

favicon_tag = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>&#x1F4A1;</text></svg>" type="image/svg+xml" />\n  <link rel="preconnect" href="https://fonts.googleapis.com" />'

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Update copyright year
        content = content.replace('© 2025', '© 2026')
        
        # 2. Update profile picture URL
        content = avatar_pattern.sub('profile.png', content)
        
        # 3. Add favicon 
        if 'image/svg+xml' not in content:
            content = content.replace('<link rel="preconnect" href="https://fonts.googleapis.com" />', favicon_tag)
            
        with open(file, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
            
        print(f"Applied changes to: {os.path.basename(file)}")
            
    except Exception as e:
        print(f"Error processing {os.path.basename(file)}: {e}")

print("All changes applied securely without encoding corruption.")
