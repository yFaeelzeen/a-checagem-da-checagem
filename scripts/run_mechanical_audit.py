import re, os

ui_dir = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\interface'
html_path = os.path.join(ui_dir, 'index.html')
css_path = os.path.join(ui_dir, 'styles.css')
js_path = os.path.join(ui_dir, 'app.js')

html = open(html_path, 'r', encoding='utf-8').read()
css = open(css_path, 'r', encoding='utf-8').read()
js = open(js_path, 'r', encoding='utf-8').read()

all_content = html + css + js

emoji_pattern = re.compile(r'[\u2600-\u27BF]|[\uD83C-\uD83E][\uDC00-\uDFFF]')
emojis = emoji_pattern.findall(all_content)
print('1. Emoji audit count:', len(emojis))

touch_targets = [line for line in css.splitlines() if 'min-height: 44px' in line]
print('2. Touch targets explicitly set:', len(touch_targets))

focus_visible = [line for line in css.splitlines() if ':focus-visible' in line]
print('3. :focus-visible selectors:', len(focus_visible))

has_favicon = 'rel="icon"' in html
print('4. Favicon in head:', has_favicon)

has_motion = 'prefers-reduced-motion' in css
print('5. prefers-reduced-motion in CSS:', has_motion)

clamps = [line for line in css.splitlines() if 'clamp(' in line]
print('6. Fluid typography clamp() count:', len(clamps))
