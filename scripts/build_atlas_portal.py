import json

with open('scripts/plates_data.json', 'r') as f:
    plates = json.load(f)

plates_json = json.dumps(plates)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  
  <!-- PWA & Mobile Meta -->
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#05080f">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Quran Atlas 03">
  <link rel="apple-touch-icon" href="icons/icon-192.png">
  <link rel="icon" type="image/png" href="icons/favicon.png">

  <title>The Visual Quran Atlas (Student Edition 03) | Huurs Studio</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --bg-deep: #05080f;
      --bg-surface: #0a1120;
      --bg-surface-elevated: #101c33;
      --bg-card: #0e172a;
      --bg-card-hover: #15223d;
      
      --gold: #d4af59;
      --gold-light: #f7e7b4;
      --gold-glow: rgba(212, 175, 89, 0.25);
      --gold-border: rgba(212, 175, 89, 0.35);
      
      --emerald: #10b981;
      --emerald-bg: rgba(16, 185, 129, 0.12);
      --sapphire: #3b82f6;
      --purple: #a855f7;
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --font-body: 'Plus Jakarta Sans', -apple-system, sans-serif;
      --font-title: 'Cinzel', Georgia, serif;
    }}
    
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    
    body {{
      background-color: var(--bg-deep);
      color: var(--text-main);
      font-family: var(--font-body);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}
    
    /* Top Bar */
    .top-strip {{
      background: rgba(5, 8, 15, 0.92);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(212, 175, 89, 0.2);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    
    .brand-tag {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    
    .brand-logo-text {{
      font-family: var(--font-title);
      font-size: 1.15rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: var(--gold);
      text-decoration: none;
    }}
    
    .edition-pill {{
      background: rgba(212, 175, 89, 0.15);
      color: var(--gold-light);
      border: 1px solid var(--gold-border);
      padding: 3px 10px;
      border-radius: 20px;
      font-size: 0.72rem;
      font-weight: 600;
      letter-spacing: 0.05em;
    }}
    
    .creed {{
      font-family: var(--font-title);
      font-size: 0.8rem;
      letter-spacing: 0.2em;
      color: var(--gold-light);
      display: none;
    }}
    
    @media (min-width: 900px) {{
      .creed {{ display: block; }}
    }}
    
    .top-actions {{
      display: flex;
      gap: 10px;
      align-items: center;
    }}
    
    .top-btn {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: var(--text-main);
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 0.82rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      transition: all 0.2s ease;
      font-weight: 500;
    }}
    
    .top-btn:hover {{
      background: rgba(212, 175, 89, 0.15);
      border-color: var(--gold);
      color: var(--gold-light);
    }}
    
    .top-btn.gold {{
      background: linear-gradient(135deg, rgba(212, 175, 89, 0.25), rgba(212, 175, 89, 0.1));
      border-color: var(--gold);
      color: var(--gold-light);
    }}
    
    .top-btn.portfolio-btn {{
      border-color: rgba(59, 130, 246, 0.4);
      color: #93c5fd;
    }}
    
    .top-btn.portfolio-btn:hover {{
      border-color: #3b82f6;
      background: rgba(59, 130, 246, 0.15);
    }}

    /* Hero Section */
    .hero {{
      padding: 60px 24px 40px;
      text-align: center;
      background: radial-gradient(circle at 50% 20%, rgba(21, 34, 61, 0.6) 0%, rgba(5, 8, 15, 0.95) 75%);
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }}
    
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(212, 175, 89, 0.12);
      border: 1px solid var(--gold-border);
      color: var(--gold-light);
      padding: 6px 16px;
      border-radius: 30px;
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 22px;
    }}
    
    .hero h1 {{
      font-family: var(--font-title);
      font-size: clamp(2.2rem, 5vw, 3.6rem);
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: 0.03em;
      line-height: 1.15;
      margin-bottom: 12px;
    }}
    
    .hero h1 span {{
      color: var(--gold);
      display: block;
      font-size: 0.65em;
      letter-spacing: 0.12em;
      margin-top: 4px;
    }}
    
    .hero-sub {{
      font-family: var(--font-title);
      font-size: clamp(1.05rem, 2.5vw, 1.4rem);
      color: var(--gold-light);
      letter-spacing: 0.06em;
      margin-bottom: 18px;
    }}
    
    .hero p {{
      max-width: 820px;
      margin: 0 auto 30px;
      color: var(--text-muted);
      font-size: 1.05rem;
      line-height: 1.7;
    }}
    
    .hero-actions {{
      display: flex;
      gap: 14px;
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 40px;
    }}
    
    .btn {{
      padding: 13px 26px;
      border-radius: 10px;
      font-size: 0.95rem;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      transition: all 0.25s ease;
    }}
    
    .btn-gold {{
      background: linear-gradient(135deg, var(--gold), #b38938);
      color: #05080f;
      box-shadow: 0 4px 20px var(--gold-glow);
    }}
    
    .btn-gold:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 26px rgba(212, 175, 89, 0.4);
      color: #000;
    }}
    
    .btn-outline {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(212, 175, 89, 0.4);
      color: var(--gold-light);
    }}
    
    .btn-outline:hover {{
      background: rgba(212, 175, 89, 0.12);
      border-color: var(--gold);
      transform: translateY(-2px);
    }}
    
    .btn-portfolio {{
      background: rgba(59, 130, 246, 0.1);
      border: 1px solid rgba(59, 130, 246, 0.4);
      color: #bfdbfe;
    }}
    
    .btn-portfolio:hover {{
      background: rgba(59, 130, 246, 0.2);
      border-color: #60a5fa;
      transform: translateY(-2px);
    }}
    
    /* Stats Bar */
    .hero-stats {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      max-width: 960px;
      margin: 0 auto;
      gap: 14px;
    }}
    
    .stat-card {{
      background: rgba(14, 23, 42, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 16px 12px;
      text-align: center;
      transition: border-color 0.2s;
    }}
    
    .stat-card:hover {{
      border-color: var(--gold-border);
    }}
    
    .stat-val {{
      display: block;
      font-family: var(--font-title);
      font-size: 1.55rem;
      font-weight: 700;
      color: var(--gold);
      margin-bottom: 4px;
    }}
    
    .stat-lbl {{
      font-size: 0.78rem;
      color: var(--text-muted);
      letter-spacing: 0.04em;
    }}

    /* Container */
    .container {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 50px 24px;
      width: 100%;
    }}

    /* Editorial Methodology Section */
    .methodology-box {{
      background: linear-gradient(180deg, rgba(16, 28, 51, 0.8) 0%, rgba(10, 17, 32, 0.95) 100%);
      border: 1px solid var(--gold-border);
      border-radius: 16px;
      padding: 32px 28px;
      margin-bottom: 60px;
      box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.6);
    }}
    
    .methodology-header {{
      text-align: center;
      margin-bottom: 26px;
    }}
    
    .methodology-tag {{
      font-family: var(--font-title);
      color: var(--gold);
      font-size: 0.8rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      margin-bottom: 8px;
    }}
    
    .methodology-title {{
      font-family: var(--font-title);
      font-size: 1.6rem;
      color: var(--text-main);
      font-weight: 700;
    }}
    
    .methodology-quote {{
      font-style: italic;
      color: #cbd5e1;
      max-width: 780px;
      margin: 12px auto 26px;
      text-align: center;
      line-height: 1.65;
      font-size: 0.98rem;
    }}
    
    .labels-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
    }}
    
    .label-card {{
      background: rgba(5, 8, 15, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 16px;
      display: flex;
      gap: 12px;
      align-items: flex-start;
    }}
    
    .label-badge {{
      font-family: var(--font-title);
      font-weight: 700;
      font-size: 0.72rem;
      padding: 4px 10px;
      border-radius: 6px;
      white-space: nowrap;
      letter-spacing: 0.08em;
    }}
    
    .label-quran {{ background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid #10b981; }}
    .label-hadith {{ background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid #3b82f6; }}
    .label-tafsir {{ background: rgba(212, 175, 89, 0.2); color: #fde047; border: 1px solid #d4af59; }}
    .label-reflection {{ background: rgba(168, 85, 247, 0.2); color: #d8b4fe; border: 1px solid #a855f7; }}
    
    .label-info h4 {{
      font-size: 0.88rem;
      font-weight: 600;
      margin-bottom: 4px;
      color: var(--text-main);
    }}
    
    .label-info p {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    /* Section Titles */
    .section-head {{
      text-align: center;
      margin-bottom: 40px;
    }}
    
    .section-head-tag {{
      font-family: var(--font-title);
      color: var(--gold);
      font-size: 0.82rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      margin-bottom: 8px;
    }}
    
    .section-head-title {{
      font-family: var(--font-title);
      font-size: clamp(1.8rem, 3.5vw, 2.4rem);
      font-weight: 700;
      color: var(--text-main);
    }}
    
    .section-head-desc {{
      color: var(--text-muted);
      max-width: 680px;
      margin: 10px auto 0;
      font-size: 0.95rem;
    }}

    /* 3 Core Studies Grid */
    .studies-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 32px;
      margin-bottom: 70px;
    }}
    
    @media (min-width: 980px) {{
      .studies-grid {{
        grid-template-columns: repeat(3, 1fr);
      }}
    }}
    
    .study-card {{
      background: var(--bg-card);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 12px 28px -10px rgba(0, 0, 0, 0.5);
    }}
    
    .study-card:hover {{
      transform: translateY(-5px);
      border-color: var(--gold-border);
      box-shadow: 0 18px 40px -10px rgba(212, 175, 89, 0.18);
    }}
    
    .study-thumb-wrap {{
      position: relative;
      width: 100%;
      height: 230px;
      background: #020408;
      overflow: hidden;
      cursor: pointer;
    }}
    
    .study-thumb-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
      transition: transform 0.4s ease;
    }}
    
    .study-card:hover .study-thumb-wrap img {{
      transform: scale(1.04);
    }}
    
    .study-thumb-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 40%, rgba(5, 8, 15, 0.85) 100%);
      display: flex;
      align-items: flex-end;
      padding: 16px;
    }}
    
    .study-badge {{
      background: rgba(5, 8, 15, 0.85);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.05em;
    }}
    
    .study-badge.bonus {{
      border-color: #a855f7;
      color: #e9d5ff;
    }}
    
    .study-body {{
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }}
    
    .study-number {{
      font-family: var(--font-title);
      font-size: 0.75rem;
      letter-spacing: 0.15em;
      color: var(--gold);
      text-transform: uppercase;
      margin-bottom: 6px;
    }}
    
    .study-title {{
      font-family: var(--font-title);
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 6px;
    }}
    
    .study-meta {{
      font-size: 0.82rem;
      color: #38bdf8;
      margin-bottom: 12px;
      font-weight: 500;
    }}
    
    .study-desc {{
      color: var(--text-muted);
      font-size: 0.88rem;
      line-height: 1.6;
      margin-bottom: 20px;
      flex-grow: 1;
    }}
    
    .study-specs {{
      background: rgba(5, 8, 15, 0.4);
      border-radius: 8px;
      padding: 12px;
      margin-bottom: 20px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      font-size: 0.78rem;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }}
    
    .study-spec-item strong {{
      display: block;
      color: var(--text-main);
      font-size: 0.82rem;
    }}
    
    .study-spec-item span {{
      color: var(--text-dim);
    }}
    
    .study-btn-group {{
      display: flex;
      gap: 10px;
    }}
    
    .study-btn-group .btn {{
      flex: 1;
      padding: 10px 14px;
      font-size: 0.82rem;
      justify-content: center;
    }}

    /* Gallery Filter Tabs */
    .gallery-filter-bar {{
      display: flex;
      gap: 10px;
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 30px;
    }}
    
    .filter-tab {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-muted);
      padding: 8px 18px;
      border-radius: 30px;
      font-size: 0.85rem;
      cursor: pointer;
      transition: all 0.2s;
      font-weight: 500;
    }}
    
    .filter-tab:hover {{
      background: rgba(212, 175, 89, 0.1);
      color: var(--text-main);
      border-color: rgba(212, 175, 89, 0.3);
    }}
    
    .filter-tab.active {{
      background: var(--gold);
      color: #05080f;
      border-color: var(--gold);
      font-weight: 700;
      box-shadow: 0 4px 14px var(--gold-glow);
    }}

    /* 26-Plate Gallery Grid */
    .gallery-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 20px;
      margin-bottom: 60px;
    }}
    
    .plate-card {{
      background: var(--bg-card);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      overflow: hidden;
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
    }}
    
    .plate-card:hover {{
      transform: translateY(-4px);
      border-color: var(--gold-border);
      box-shadow: 0 12px 28px -8px rgba(212, 175, 89, 0.2);
    }}
    
    .plate-thumb {{
      position: relative;
      width: 100%;
      height: 330px;
      background: #020408;
      overflow: hidden;
    }}
    
    .plate-thumb img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
      transition: transform 0.3s ease;
    }}
    
    .plate-card:hover .plate-thumb img {{
      transform: scale(1.03);
    }}
    
    .plate-page-badge {{
      position: absolute;
      top: 10px;
      left: 10px;
      background: rgba(5, 8, 15, 0.85);
      border: 1px solid rgba(212, 175, 89, 0.6);
      color: var(--gold-light);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
    }}
    
    .plate-cat-badge {{
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(14, 23, 42, 0.85);
      color: #94a3b8;
      font-size: 0.68rem;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 6px;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .plate-info {{
      padding: 14px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }}
    
    .plate-title {{
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 4px;
      line-height: 1.35;
    }}
    
    .plate-desc {{
      font-size: 0.76rem;
      color: var(--text-dim);
      line-height: 1.4;
      flex-grow: 1;
    }}

    /* Lightbox Modal */
    .lightbox-modal {{
      position: fixed;
      inset: 0;
      background: rgba(3, 5, 10, 0.95);
      backdrop-filter: blur(12px);
      z-index: 1000;
      display: none;
      flex-direction: column;
      justify-content: space-between;
      padding: 16px 20px;
    }}
    
    .lightbox-modal.active {{
      display: flex;
    }}
    
    .lightbox-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .lightbox-title-box {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    
    .lightbox-page-num {{
      background: var(--gold);
      color: #05080f;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.8rem;
    }}
    
    .lightbox-plate-title {{
      font-family: var(--font-title);
      font-size: 1.05rem;
      color: var(--text-main);
      font-weight: 600;
    }}
    
    .lightbox-close {{
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: var(--text-main);
      width: 36px;
      height: 36px;
      border-radius: 50%;
      font-size: 1.2rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.2s;
    }}
    
    .lightbox-close:hover {{
      background: rgba(239, 68, 68, 0.4);
      color: #fff;
    }}
    
    .lightbox-center {{
      position: relative;
      flex-grow: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 12px 0;
      overflow: hidden;
    }}
    
    .lightbox-img {{
      max-height: calc(100vh - 160px);
      max-width: 90vw;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.9);
      border: 1px solid rgba(212, 175, 89, 0.2);
    }}
    
    .lightbox-nav-btn {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(14, 23, 42, 0.75);
      border: 1px solid rgba(212, 175, 89, 0.3);
      color: var(--gold-light);
      width: 48px;
      height: 48px;
      border-radius: 50%;
      font-size: 1.3rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
      z-index: 10;
    }}
    
    .lightbox-nav-btn:hover {{
      background: var(--gold);
      color: #05080f;
    }}
    
    .lightbox-nav-btn.prev {{ left: 20px; }}
    .lightbox-nav-btn.next {{ right: 20px; }}
    
    .lightbox-bottom {{
      padding: 10px 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }}
    
    .lightbox-desc {{
      color: var(--text-muted);
      font-size: 0.85rem;
      max-width: 700px;
    }}

    /* Download Banner Callout */
    .dl-banner {{
      background: radial-gradient(circle at 50% 50%, rgba(21, 34, 61, 0.9) 0%, rgba(8, 14, 27, 0.98) 100%);
      border: 1px solid var(--gold-border);
      border-radius: 20px;
      padding: 40px 32px;
      text-align: center;
      margin-bottom: 70px;
      box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.8);
    }}
    
    .dl-banner h2 {{
      font-family: var(--font-title);
      font-size: clamp(1.8rem, 3.5vw, 2.3rem);
      color: var(--gold-light);
      margin-bottom: 12px;
    }}
    
    .dl-banner p {{
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 28px;
      font-size: 1rem;
      line-height: 1.6;
    }}
    
    .dl-btns {{
      display: flex;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
    }}

    /* Footer */
    footer {{
      margin-top: auto;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 36px 24px;
      text-align: center;
      background: #03050a;
    }}
    
    .footer-brand {{
      font-family: var(--font-title);
      font-size: 1.1rem;
      color: var(--gold);
      letter-spacing: 0.12em;
      margin-bottom: 6px;
    }}
    
    .footer-sub {{
      color: var(--text-muted);
      font-size: 0.82rem;
      margin-bottom: 16px;
    }}
    
    .footer-links {{
      display: flex;
      justify-content: center;
      gap: 20px;
      flex-wrap: wrap;
      margin-bottom: 16px;
    }}
    
    .footer-links a {{
      color: var(--gold-light);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 500;
    }}
    
    .footer-links a:hover {{
      text-decoration: underline;
    }}
    
    .footer-waqf {{
      color: var(--text-dim);
      font-size: 0.74rem;
      max-width: 600px;
      margin: 0 auto;
      line-height: 1.5;
    }}

    /* Mobile adjustments */
    @media (max-width: 768px) {{
      .hero {{ padding: 40px 16px 30px; }}
      .container {{ padding: 30px 16px; }}
      .methodology-box {{ padding: 24px 16px; }}
      .lightbox-nav-btn.prev {{ left: 6px; }}
      .lightbox-nav-btn.next {{ right: 6px; }}
      .lightbox-img {{ max-width: 98vw; }}
    }}
  </style>
</head>
<body>

  <!-- Top Strip -->
  <div class="top-strip">
    <div class="brand-tag">
      <a href="index.html" class="brand-logo-text">HUR STUDIO</a>
      <span class="edition-pill">Student Edition 03</span>
    </div>
    <div class="creed">READ. REFLECT. RETURN.</div>
    <div class="top-actions">
      <a href="#studies" class="top-btn">
        <span>📖 3 Studies</span>
      </a>
      <a href="#gallery" class="top-btn">
        <span>🖼️ 26-Plate Gallery</span>
      </a>
      <a href="1st_step_review03.pdf" class="top-btn gold" download="1st_step_review03.pdf">
        <span>📥 Download PDF</span>
      </a>
      <a href="portfolio.html" class="top-btn portfolio-btn" title="View Institutional Investment Suite">
        <span>🏢 Portfolio</span>
      </a>
    </div>
  </div>

  <!-- Hero Header -->
  <header class="hero">
    <div class="hero-badge">✦ Flagship Visual Publication • Student Edition 03</div>
    <h1>1st STEP: THE VISUAL QURAN ATLAS<br><span>AN ILLUSTRATED QURAN STUDY COMPANION</span></h1>
    <div class="hero-sub">Surah Al-Fatihah • Surah Al-Baqarah • Bonus Study: Ayat al-Kursi</div>
    <p>
      An open, contemplative visual study companion designed to invite readers into the structural beauty and theological depth of the Quran. Bringing together original Arabic verse banners, concise classical Sunni exegesis, and visual relationship maps across 26 publication plates.
    </p>
    
    <div class="hero-actions">
      <a href="1st_step_review03.pdf" class="btn btn-gold" download="1st_step_review03.pdf">
        <span>📥 Download 1st Step Atlas PDF (Edition 03 • 26 Pages • 1.0 MB)</span>
      </a>
      <a href="#gallery" class="btn btn-outline">
        <span>👁️ Browse 26-Plate Visual Gallery</span>
      </a>
      <a href="portfolio.html" class="btn btn-portfolio">
        <span>🏢 Institutional Portfolio & Deliverables ➔</span>
      </a>
    </div>

    <div class="hero-stats">
      <div class="stat-card">
        <span class="stat-val">3</span>
        <span class="stat-lbl">Core Studies</span>
      </div>
      <div class="stat-card">
        <span class="stat-val">26</span>
        <span class="stat-lbl">Master Plates (14 Thematic + 3 Maps)</span>
      </div>
      <div class="stat-card">
        <span class="stat-val">4</span>
        <span class="stat-lbl">Scholarly Labels ([QURAN], [HADITH], etc.)</span>
      </div>
      <div class="stat-card">
        <span class="stat-val">100%</span>
        <span class="stat-lbl">Waqf / Free Study Access</span>
      </div>
    </div>
  </header>

  <main class="container">
    
    <!-- Methodology Section -->
    <section class="methodology-box">
      <div class="methodology-header">
        <div class="methodology-tag">Editorial Approach & Reading Discipline</div>
        <h2 class="methodology-title">The Student Perspective & The 4 Labels</h2>
        <p class="methodology-quote">
          "This atlas is not intended to tell readers what they must see in the Quran. It is an invitation to explore the Quran through the eyes of a student, discover possible connections, and develop their own understanding through study and reflection."
        </p>
      </div>
      
      <div class="labels-grid">
        <div class="label-card">
          <span class="label-badge label-quran">[QURAN]</span>
          <div class="label-info">
            <h4>Textual Revelation</h4>
            <p>Directly from the Quranic text: Arabic wording, ayah numbers, and established translations.</p>
          </div>
        </div>
        <div class="label-card">
          <span class="label-badge label-hadith">[HADITH]</span>
          <div class="label-info">
            <h4>Prophetic Tradition</h4>
            <p>Based on canonical narrations from the primary Sahih collections with complete collection citations.</p>
          </div>
        </div>
        <div class="label-card">
          <span class="label-badge label-tafsir">[TAFSIR]</span>
          <div class="label-info">
            <h4>Classical Exegesis</h4>
            <p>Derived from verified Sunni scholarship (Ibn Kathir, Al-Tabari, Al-Qurtubi, Al-Razi, As-Sa'di).</p>
          </div>
        </div>
        <div class="label-card">
          <span class="label-badge label-reflection">[REFLECTION]</span>
          <div class="label-info">
            <h4>Student Synthesis</h4>
            <p>The student-author's own thematic observations, relationship structures, and synthesis offered for contemplation.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 3 Core Surahs / Studies Showcase -->
    <section id="studies">
      <div class="section-head">
        <div class="section-head-tag">Volume I Core Curriculum</div>
        <h2 class="section-head-title">Explore the 3 Core Studies</h2>
        <p class="section-head-desc">
          Structured visual guides and macrostructural relationship maps for the opening of the revelation, its longest legislative pillar, and its supreme verse.
        </p>
      </div>

      <div class="studies-grid">
        
        <!-- Study 1: Surah Al-Fatihah -->
        <div class="study-card">
          <div class="study-thumb-wrap" onclick="openLightbox(4)">
            <img src="previews_review03/review03_page-04.png" alt="Surah Al-Fatihah Preview">
            <div class="study-thumb-overlay">
              <span class="study-badge">Surah 01 • 7 Ayahs</span>
            </div>
          </div>
          <div class="study-body">
            <div class="study-number">Part I • The Mother of the Book</div>
            <h3 class="study-title">Surah 01: Al-Fatihah</h3>
            <div class="study-meta">The Opening • 4 Plates + Mindmap + Source Registry</div>
            <p class="study-desc">
              The celestial prologue establishing divine praise (Hamd), universal lordship, paired mercy, the day of accountability, and the master covenant of guidance.
            </p>
            <div class="study-specs">
              <div class="study-spec-item">
                <strong>Plates 01–04</strong>
                <span>4 Thematic Exegesis Plates</span>
              </div>
              <div class="study-spec-item">
                <strong>Mindmap 01</strong>
                <span>Al-Fatihah & Bridge to Baqarah</span>
              </div>
            </div>
            <div class="study-btn-group">
              <button class="btn btn-gold" onclick="openLightbox(4)">
                <span>👁️ View Plates (4–9)</span>
              </button>
              <button class="btn btn-outline" onclick="filterGallery('fatihah')">
                <span>Filter Gallery</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Study 2: Surah Al-Baqarah -->
        <div class="study-card">
          <div class="study-thumb-wrap" onclick="openLightbox(10)">
            <img src="previews_review03/review03_page-10.png" alt="Surah Al-Baqarah Preview">
            <div class="study-thumb-overlay">
              <span class="study-badge">Surah 02 • 286 Ayahs</span>
            </div>
          </div>
          <div class="study-body">
            <div class="study-number">Part II • The Foundational Legislation</div>
            <h3 class="study-title">Surah 02: Al-Baqarah</h3>
            <div class="study-meta">The Heifer • 8 Plates + Mindmap + 2 Registries</div>
            <p class="study-desc">
              The grand architecture of faith: Adam's caliphate, Banu Isra'il covenants, Abrahamic legacy, the sacred Qiblah pivot, Medina community constitution, and ethical economics.
            </p>
            <div class="study-specs">
              <div class="study-spec-item">
                <strong>Plates 01–08</strong>
                <span>8 Thematic Plates (16 Pillars)</span>
              </div>
              <div class="study-spec-item">
                <strong>Mindmap 02</strong>
                <span>Full Architectural Macro-Map</span>
              </div>
            </div>
            <div class="study-btn-group">
              <button class="btn btn-gold" onclick="openLightbox(10)">
                <span>👁️ View Plates (10–20)</span>
              </button>
              <button class="btn btn-outline" onclick="filterGallery('baqarah')">
                <span>Filter Gallery</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Study 3: Bonus Ayat al-Kursi -->
        <div class="study-card">
          <div class="study-thumb-wrap" onclick="openLightbox(21)">
            <img src="previews_review03/review03_page-21.png" alt="Ayat al-Kursi Preview">
            <div class="study-thumb-overlay">
              <span class="study-badge bonus">Bonus Deep Dive • Ayah 2:255</span>
            </div>
          </div>
          <div class="study-body">
            <div class="study-number">Part III • The Supreme Throne Verse</div>
            <h3 class="study-title">Bonus: Ayat al-Kursi</h3>
            <div class="study-meta">The Greatest Ayah • 2 Plates + Concentric Map</div>
            <p class="study-desc">
              A dedicated master study analyzing the 10 divine sentences of Ayah 2:255, its concentric ring symmetry, canonical virtues from the Kutub al-Sittah, and spiritual shielding.
            </p>
            <div class="study-specs">
              <div class="study-spec-item">
                <strong>Plates 01–02</strong>
                <span>Ontology & Canonical Virtues</span>
              </div>
              <div class="study-spec-item">
                <strong>Mindmap 03</strong>
                <span>10-Clause Concentric Ring Map</span>
              </div>
            </div>
            <div class="study-btn-group">
              <button class="btn btn-gold" onclick="openLightbox(21)">
                <span>👁️ View Plates (21–23)</span>
              </button>
              <button class="btn btn-outline" onclick="filterGallery('kursi')">
                <span>Filter Gallery</span>
              </button>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- Complete 26-Plate Visual Gallery -->
    <section id="gallery">
      <div class="section-head">
        <div class="section-head-tag">Interactive Visual Plates & Relationship Maps</div>
        <h2 class="section-head-title">The Complete 26-Plate Visual Gallery</h2>
        <p class="section-head-desc">
          Click any plate to view the high-resolution vector plate in full-screen reader mode with complete commentary notes and cross-references.
        </p>
      </div>

      <!-- Filter Bar -->
      <div class="gallery-filter-bar">
        <button class="filter-tab active" onclick="filterGallery('all')">All 26 Plates</button>
        <button class="filter-tab" onclick="filterGallery('fatihah')">Surah 01: Al-Fatihah (6)</button>
        <button class="filter-tab" onclick="filterGallery('baqarah')">Surah 02: Al-Baqarah (11)</button>
        <button class="filter-tab" onclick="filterGallery('kursi')">Bonus: Ayat al-Kursi (3)</button>
        <button class="filter-tab" onclick="filterGallery('reference')">Reference & Glossary (3)</button>
        <button class="filter-tab" onclick="filterGallery('prelim')">Preliminaries (3)</button>
      </div>

      <!-- Gallery Grid -->
      <div class="gallery-grid" id="galleryGrid">
        <!-- Rendered dynamically -->
      </div>
    </section>

    <!-- Download Banner -->
    <section class="dl-banner">
      <h2>Download Your Complete Study Companion</h2>
      <p>
        Get the complete 26-page high-definition PDF edition of <strong>1st Step: The Visual Quran Atlas (Student Edition 03)</strong>. Optimized for tablet reading on iPad, Kindle Scribe, reMarkable, and high-resolution print.
      </p>
      <div class="dl-btns">
        <a href="1st_step_review03.pdf" class="btn btn-gold" download="1st_step_review03.pdf">
          <span>📥 Download Vector Master PDF (1.0 MB)</span>
        </a>
        <a href="portfolio.html" class="btn btn-portfolio">
          <span>🏢 Explore Huurs Studio Master Portfolio</span>
        </a>
      </div>
    </section>

  </main>

  <!-- Lightbox Modal -->
  <div class="lightbox-modal" id="lightboxModal">
    <div class="lightbox-top">
      <div class="lightbox-title-box">
        <span class="lightbox-page-num" id="modalPageNum">Page 01</span>
        <span class="lightbox-plate-title" id="modalPlateTitle">Plate Title</span>
      </div>
      <button class="lightbox-close" onclick="closeLightbox()" title="Close Lightbox (Esc)">✕</button>
    </div>
    
    <div class="lightbox-center">
      <button class="lightbox-nav-btn prev" onclick="prevPlate()" title="Previous Plate (Left Arrow)">❮</button>
      <img src="" alt="Enlarged Plate" class="lightbox-img" id="modalImg">
      <button class="lightbox-nav-btn next" onclick="nextPlate()" title="Next Plate (Right Arrow)">❯</button>
    </div>
    
    <div class="lightbox-bottom">
      <div class="lightbox-desc" id="modalPlateDesc">Plate description and exegesis details.</div>
      <div>
        <a href="#" target="_blank" class="btn btn-outline" id="modalViewOriginalBtn" style="padding: 6px 14px; font-size: 0.8rem;">
          <span>🔍 View Full Resolution</span>
        </a>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <div class="footer-brand">HUURS STUDIO  •  THE VISUAL QURAN ATLAS</div>
    <div class="footer-sub">Autonomous Sacred Media & Cartography  •  Student Edition 03</div>
    <div class="footer-links">
      <a href="index.html">Atlas Gateway</a> •
      <a href="portfolio.html">Institutional Portfolio</a> •
      <a href="documentation.html">Master Documentation</a> •
      <a href="1st_step_review03.pdf" download="1st_step_review03.pdf">Download PDF</a> •
      <a href="https://hur-studio.github.io/quran-camp/" target="_blank">Quran Study Portal</a>
    </div>
    <p class="footer-waqf">
      Dedicated as an open educational waqf for sincere seekers of sacred knowledge. Preserving classical Sunni exegesis through clean, contemplative visual architecture. Zero human depictions, zero music, zero sensationalism.
    </p>
  </footer>

  <script>
    const plates = {plates_json};
    let currentPlateIndex = 0;
    let currentFilter = 'all';

    function renderGallery() {{
      const grid = document.getElementById('galleryGrid');
      grid.innerHTML = '';
      
      const filtered = currentFilter === 'all' 
        ? plates 
        : plates.filter(p => p.cat === currentFilter);
        
      filtered.forEach(p => {{
        const card = document.createElement('div');
        card.className = 'plate-card';
        card.onclick = () => openLightbox(p.page);
        
        card.innerHTML = `
          <div class="plate-thumb">
            <img src="${{p.img}}" alt="${{p.title}}" loading="lazy">
            <span class="plate-page-badge">P. ${{p.page < 10 ? '0' + p.page : p.page}}</span>
            <span class="plate-cat-badge">${{p.badge}}</span>
          </div>
          <div class="plate-info">
            <h4 class="plate-title">${{p.title}}</h4>
            <p class="plate-desc">${{p.desc}}</p>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    function filterGallery(cat) {{
      currentFilter = cat;
      document.querySelectorAll('.filter-tab').forEach(tab => {{
        tab.classList.toggle('active', tab.getAttribute('onclick').includes(`'${{cat}}'`));
      }});
      renderGallery();
      
      // If clicking from study card, smooth scroll to gallery
      const galleryEl = document.getElementById('gallery');
      if (galleryEl && window.scrollY < galleryEl.offsetTop - 200) {{
        galleryEl.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }}

    function openLightbox(pageNum) {{
      const idx = plates.findIndex(p => p.page === pageNum);
      if (idx !== -1) {{
        currentPlateIndex = idx;
        updateModal();
        const modal = document.getElementById('lightboxModal');
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }}
    }}

    function closeLightbox() {{
      const modal = document.getElementById('lightboxModal');
      modal.classList.remove('active');
      document.body.style.overflow = 'auto';
    }}

    function updateModal() {{
      const p = plates[currentPlateIndex];
      document.getElementById('modalPageNum').textContent = `Page ${{p.page < 10 ? '0' + p.page : p.page}} / 26 • ${{p.badge}}`;
      document.getElementById('modalPlateTitle').textContent = p.title;
      document.getElementById('modalPlateDesc').textContent = p.desc;
      const modalImg = document.getElementById('modalImg');
      modalImg.src = p.img;
      modalImg.alt = p.title;
      document.getElementById('modalViewOriginalBtn').href = p.img;
    }}

    function nextPlate() {{
      currentPlateIndex = (currentPlateIndex + 1) % plates.length;
      updateModal();
    }}

    function prevPlate() {{
      currentPlateIndex = (currentPlateIndex - 1 + plates.length) % plates.length;
      updateModal();
    }}

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {{
      const modal = document.getElementById('lightboxModal');
      if (!modal.classList.contains('active')) return;
      
      if (e.key === 'Escape') closeLightbox();
      else if (e.key === 'ArrowRight') nextPlate();
      else if (e.key === 'ArrowLeft') prevPlate();
    }});

    // Initialize gallery on load
    document.addEventListener('DOMContentLoaded', () => {{
      renderGallery();
    }});
  </script>

</body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(html_content)

with open('START_HERE.html', 'w') as f:
    f.write(html_content)

print('Successfully written index.html and START_HERE.html!')
