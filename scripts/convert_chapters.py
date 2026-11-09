import os
import re

def md_to_html(md_text):
    # strip yaml frontmatter
    md_text = re.sub(r'^---\n.*?\n---\n', '', md_text, flags=re.DOTALL)
    
    lines = md_text.split('\n')
    output = []
    in_list = False
    in_quote = False
    
    for line in lines:
        stripped = line.strip()
        
        # hr
        if stripped in ('---', '***', '___'):
            if in_list:
                output.append('</ul>')
                in_list = False
            if in_quote:
                output.append('</blockquote>')
                in_quote = False
            output.append('<hr>')
            continue
            
        # headers
        m_h = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if m_h:
            if in_list:
                output.append('</ul>')
                in_list = False
            if in_quote:
                output.append('</blockquote>')
                in_quote = False
            level = len(m_h.group(1))
            text = m_h.group(2)
            text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
            text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
            output.append(f'<h{level}>{text}</h{level}>')
            continue
            
        # blockquote
        if stripped.startswith('>'):
            if in_list:
                output.append('</ul>')
                in_list = False
            quote_text = stripped[1:].strip()
            quote_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', quote_text)
            quote_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', quote_text)
            if not in_quote:
                output.append('<blockquote>')
                in_quote = True
            output.append(f'<p>{quote_text}</p>')
            continue
        elif in_quote:
            output.append('</blockquote>')
            in_quote = False
            
        # list items
        if stripped.startswith(('* ', '- ', '• ')):
            if not in_list:
                output.append('<ul>')
                in_list = True
            item_text = stripped[2:].strip()
            item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
            item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
            output.append(f'<li>{item_text}</li>')
            continue
        elif in_list and not stripped:
            output.append('</ul>')
            in_list = False
            continue
            
        # normal paragraph
        if stripped:
            p_text = stripped
            p_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p_text)
            p_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', p_text)
            p_text = re.sub(r'`([^`]+)`', r'<code>\1</code>', p_text)
            output.append(f'<p>{p_text}</p>')
            
    if in_list:
        output.append('</ul>')
    if in_quote:
        output.append('</blockquote>')
    return '\n'.join(output)

template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <title>{title} - Study Guide</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-deep: #070c15;
      --bg-surface: #0e1624;
      --bg-surface-elevated: #152033;
      --gold: #d4af59;
      --gold-light: #e6cb85;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border-light: rgba(212, 175, 89, 0.25);
      --border-card: rgba(255, 255, 255, 0.08);
      --radius-sm: 8px;
      --radius-md: 14px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background-color: var(--bg-deep);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', sans-serif;
      line-height: 1.75;
      padding: 0 0 80px 0;
    }}
    header {{
      background: rgba(7, 12, 21, 0.88);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-light);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 16px 36px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .brand-logo {{ display: flex; align-items: center; gap: 14px; text-decoration: none; }}
    .brand-crest {{
      width: 36px; height: 36px; border: 1.5px solid var(--gold);
      display: flex; align-items: center; justify-content: center;
      font-family: 'Cinzel', serif; font-weight: 700; color: var(--gold);
      border-radius: 6px; background: var(--bg-surface);
    }}
    .brand-title {{ font-family: 'Cinzel', serif; font-size: 1.15rem; font-weight: 700; color: var(--gold); }}
    .btn {{
      padding: 8px 16px; border-radius: var(--radius-sm); font-size: 0.82rem;
      font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;
    }}
    .btn-gold {{ background: linear-gradient(135deg, var(--gold) 0%, #b8933b 100%); color: var(--bg-deep); border: none; }}
    .btn-outline {{ background: transparent; color: var(--gold-light); border: 1px solid var(--border-light); }}
    .container {{ max-width: 900px; margin: 0 auto; padding: 40px 24px 0; }}
    h1, h2, h3, h4 {{ font-family: 'Cinzel', serif; color: var(--gold-light); margin: 30px 0 14px; }}
    h1 {{ font-size: 2.1rem; color: #fff; border-bottom: 1px solid var(--border-light); padding-bottom: 12px; }}
    h2 {{ font-size: 1.5rem; color: var(--gold); }}
    h3 {{ font-size: 1.2rem; }}
    p {{ color: #cbd5e1; margin-bottom: 16px; font-size: 1rem; line-height: 1.8; }}
    ul, ol {{ margin: 0 0 18px 24px; color: #cbd5e1; }}
    li {{ margin-bottom: 8px; }}
    strong {{ color: #fff; }}
    blockquote {{
      background: var(--bg-surface); border-left: 4px solid var(--gold);
      padding: 16px 20px; margin: 20px 0; border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      color: #e2e8f0; font-style: italic;
    }}
    hr {{ border: none; border-top: 1px solid var(--border-card); margin: 30px 0; }}
    footer {{
      border-top: 1px solid var(--border-card); padding-top: 30px; margin-top: 50px;
      text-align: center; font-size: 0.85rem; color: var(--text-muted);
    }}
    footer a {{ color: var(--gold); text-decoration: none; }}
    @media (max-width: 768px) {{
      header {{ padding: 12px 18px; flex-direction: column; gap: 10px; }}
      .container {{ padding: 24px 16px 0; }}
      h1 {{ font-size: 1.7rem; }}
    }}
  </style>
</head>
<body>
  <header>
    <a href="../index.html" class="brand-logo">
      <div class="brand-crest">H</div>
      <div><div class="brand-title">HUR STUDIO</div></div>
    </a>
    <div style="display:flex;gap:10px;">
      <a href="../index.html" class="btn btn-gold">← Mindmap Sanctuary</a>
      <a href="../portfolio.html" class="btn btn-outline">Master Portfolio</a>
    </div>
  </header>
  <div class="container">
    {body_html}
    <footer>
      <p style="margin-bottom:8px;">HUURS STUDIO • COME BACK TO THE QUR'AN</p>
      <div style="display:flex;justify-content:center;gap:16px;">
        <a href="../index.html">Mindmap Sanctuary</a>
        <a href="../portfolio.html">Portfolio Suite</a>
      </div>
    </footer>
  </div>
</body>
</html>'''

for target_dir in ['chapters', 'free_taster_package/chapters']:
    if not os.path.exists(target_dir):
        continue
    for f in sorted(os.listdir(target_dir)):
        if f.endswith('.md'):
            path = os.path.join(target_dir, f)
            with open(path, 'r', encoding='utf-8') as fp:
                content = fp.read()
            body_html = md_to_html(content)
            m_t = re.search(r'CHAPTER \d+: ([^\n<]+)', body_html)
            title = m_t.group(1).strip() if m_t else f
            
            page = template.format(title=title, body_html=body_html)
            out_name = f.replace('.md', '.html')
            with open(os.path.join(target_dir, out_name), 'w', encoding='utf-8') as out_fp:
                out_fp.write(page)
            print(f'Converted {path} -> {out_name}')
