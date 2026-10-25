import re, os

files = ['index.html', 'metodologia.html', 'styles.css', 'app.js']
all_content = ''
for f in files:
    if os.path.exists(f):
        all_content += open(f, 'r', encoding='utf-8').read()

emoji_pattern = re.compile(r'[\u2600-\u27BF]|[\uD83C-\uD83E][\uDC00-\uDFFF]')
emojis = emoji_pattern.findall(all_content)
print('1. Emoji audit count:', len(emojis))

css = open('styles.css', 'r', encoding='utf-8').read()
touch_targets = [line for line in css.splitlines() if 'min-height: 44px' in line or 'min-height: 48px' in line]
print('2. Touch targets explicitly set (>=44px):', len(touch_targets))

focus_visible = [line for line in css.splitlines() if ':focus-visible' in line]
print('3. :focus-visible selectors:', len(focus_visible))

html = open('index.html', 'r', encoding='utf-8').read()
has_favicon_index = 'rel="icon"' in html and 'icon_editorial_duel_balance.jpg' in html
print('4. Favicon & Balance in index.html:', has_favicon_index)

met = open('metodologia.html', 'r', encoding='utf-8').read()
has_favicon_met = 'rel="icon"' in met and 'icon_brand_forensic_loupe.jpg' in met
print('5. Favicon & Loupe in metodologia.html:', has_favicon_met)

has_motion = 'prefers-reduced-motion' in css
print('6. prefers-reduced-motion in CSS:', has_motion)

clamps = [line for line in css.splitlines() if 'clamp(' in line]
print('7. Fluid typography clamp() count:', len(clamps))
