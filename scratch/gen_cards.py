import os

def create_summary_card_0(out_dir):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="340" height="200" viewBox="0 0 340 200">
  <style>
    .bg { fill: #1a1b26; rx: 10px; stroke: #24283b; stroke-width: 1px; }
    .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 600; fill: #7aa2f7; }
    .label { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 13px; fill: #a9b1d6; }
    .val { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 13px; font-weight: 700; fill: #7dcfff; }
    .icon { fill: #bb9af7; }
  </style>
  <rect width="340" height="200" class="bg" />
  <text x="20" y="32" class="title">Profile Details</text>
  <line x1="20" y1="44" x2="320" y2="44" stroke="#24283b" stroke-width="1"/>
  
  <text x="20" y="75" class="label">⭐ Total Stars Earned</text>
  <text x="310" y="75" class="val" text-anchor="end">Active</text>
  
  <text x="20" y="105" class="label">📦 Total Repositories</text>
  <text x="310" y="105" class="val" text-anchor="end">Public &amp; Active</text>
  
  <text x="20" y="135" class="label">⚡ Total Commits</text>
  <text x="310" y="135" class="val" text-anchor="end">Consistent</text>
  
  <text x="20" y="165" class="label">🔥 Contribution Streak</text>
  <text x="310" y="165" class="val" text-anchor="end">Building daily</text>
</svg>'''
    with open(os.path.join(out_dir, '0-profile-details.svg'), 'w') as f:
        f.write(svg)

def create_summary_card_1(out_dir):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="340" height="200" viewBox="0 0 340 200">
  <style>
    .bg { fill: #1a1b26; rx: 10px; stroke: #24283b; stroke-width: 1px; }
    .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 600; fill: #7aa2f7; }
    .lang-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; fill: #c0caf5; }
    .pct { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #7dcfff; }
  </style>
  <rect width="340" height="200" class="bg" />
  <text x="20" y="32" class="title">Top Languages</text>
  <line x1="20" y1="44" x2="320" y2="44" stroke="#24283b" stroke-width="1"/>
  
  <circle cx="26" cy="72" r="5" fill="#3572A5" />
  <text x="38" y="76" class="lang-text">Python</text>
  <text x="310" y="76" class="pct" text-anchor="end">Core Backend &amp; AI</text>
  
  <circle cx="26" cy="102" r="5" fill="#f1e05a" />
  <text x="38" y="106" class="lang-text">JavaScript / Node.js</text>
  <text x="310" y="106" class="pct" text-anchor="end">APIs &amp; Bots</text>
  
  <circle cx="26" cy="132" r="5" fill="#A97BFF" />
  <text x="38" y="136" class="lang-text">Kotlin / Android</text>
  <text x="310" y="136" class="pct" text-anchor="end">Mobile Apps</text>
  
  <circle cx="26" cy="162" r="5" fill="#555555" />
  <text x="38" y="166" class="lang-text">C / C++</text>
  <text x="310" y="166" class="pct" text-anchor="end">Systems &amp; DSA</text>
</svg>'''
    with open(os.path.join(out_dir, '1-repos-per-language.svg'), 'w') as f:
        f.write(svg)

os.makedirs('/Users/nusrat/Documents/sowel/projects/antigravity/user/readme/woott07/profile-summary-card-output/tokyonight', exist_ok=True)
create_summary_card_0('/Users/nusrat/Documents/sowel/projects/antigravity/user/readme/woott07/profile-summary-card-output/tokyonight')
create_summary_card_1('/Users/nusrat/Documents/sowel/projects/antigravity/user/readme/woott07/profile-summary-card-output/tokyonight')
print("Cards created successfully!")
