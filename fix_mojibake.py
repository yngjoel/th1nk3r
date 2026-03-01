import os
import glob

directory = r"c:\Users\yngjo\OneDrive\Desktop\Personal Projects\Th1nk3r By Joel Yang"
html_files = glob.glob(os.path.join(directory, "*.html"))

def fix_mojibake(text):
    # If the text has sequences like 'â€”' (UTF-8 bytes read as CP1252)
    # we can reverse it by encoding it to CP1252 then decoding as UTF-8.
    try:
        # We only want to transcode the corrupted parts. Doing it globally on the
        # whole string might fail if there's actual CP1252 invalid bytes or if 
        # it was already fixed. We'll do a safe string replacement for known common 
        # corrupted sequences.
        replacements = {
            'â€”': '—',
            'â€™': '’',
            'â€œ': '“',
            'â€': '”',
            'â€‘': '‑',
            'â€¦': '…',
            'Â': '',   # non-breaking spaces often become Â
            'Ã©': 'é',
            'Ã¨': 'è',
            'Ã': 'à',
            # Add specific fix for the non-breaking space artifact
            'Â ': ' ',
        }
        
        for k, v in replacements.items():
            text = text.replace(k, v)
            
        # Also clean up any lingering invisible Â characters before non-breaking spaces
        text = text.replace('Â\xa0', '\xa0')
        text = text.replace('Â&nbsp;', '&nbsp;')
        text = text.replace('Â', '')
            
        return text
    except Exception as e:
        print(f"Error fixing mojibake: {e}")
        return text

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'â' in content or 'Â' in content or 'Ã' in content:
            new_content = fix_mojibake(content)
            
            with open(file, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_content)
            print(f"Fixed encoding artifacts in: {os.path.basename(file)}")
            
    except Exception as e:
        print(f"Error processing {os.path.basename(file)}: {e}")

print("Encoding fix complete.")
