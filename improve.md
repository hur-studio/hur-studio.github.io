Here is a structured, execution-ready improve04.md specification written specifically for an AI coding agent (Cursor, Claude Code, Windsurf, or GitHub Copilot Workspace) to implement the interactive Ayat al-Kursi 10-Clause Concentric Ring Explorer inside your hur-studio.github.io repository cleanly and safely.



Markdown
# `improve04.md` — Interactive Ayat al-Kursi 10-Clause Concentric Ring Explorer

## 1. Objective & Context
Upgrade `hur-studio.github.io` (`Student Edition 03` -> `Edition 04` interactive layer) by integrating a self-contained, mobile-friendly, offline-ready **Ayat al-Kursi (Surah Al-Baqarah 2:255) 10-Clause Concentric Ring Explorer**.

### Design & Theological Guardrails (Strict)
- **Aesthetic:** Contemplative dark-emerald/gold sacred manuscript styling matching HUR Studio (`#0d1210` canvas, `#131a17` cards, `#c9a86a` warm gold accents, `#4e8c73` muted emerald symmetry highlights).
- **Epistemological Discipline:** Every clause card MUST strictly preserve HUR Studio's 4-label taxonomy (`[QURAN]`, `[HADITH]`, `[TAFSIR]`, `[REFLECTION]`) so divine revelation is never conflated with student synthesis.
- **Adab Constraints:** Zero human depictions, zero background music/audio auto-play, zero external heavy JS frameworks, and zero ad/tracking scripts.
- **PWA Readiness:** Must function 100% offline once cached by the existing Service Worker and add < 15 KB to the total page weight.

---

## 2. Target Files & Integration Strategy
1. **Inspect existing structure first:** Check `index.html`, `manifest.json`, and any existing stylesheet (e.g., `style.css` or inline `<style>` in `index.html`) before modifying.
2. **Placement in `index.html`:** Insert the `<section id="kursi-explorer">` directly after the **"Explore the 3 Core Studies"** section (specifically beneath the *Bonus: Ayat al-Kursi* study card) and before **"The Complete 26-Plate Visual Gallery"**.
3. **Encapsulation:** Namespace all CSS classes with `.hk-` (HUR Kursi) and scope all JS inside an IIFE (`(() => { ... })()`) so there are zero CSS or global variable collisions with the existing 26-plate gallery modal.

---

## 3. Functional Requirements

### A. Interactive SVG Concentric Ring Map (Left Column / Top on Mobile)
- Render an accessible `<svg viewBox="0 0 420 420">` containing **10 concentric circles** (radii stepping evenly from outer `r=192` down to inner `r=37.2`).
- Place numbered interactive node badges (`01` through `10`) along staggered angles (`-90deg + index * 36deg`) so touch targets never overlap on 360px mobile viewports.
- **Symmetry Mirroring Logic:**
  - Selecting any clause `N` highlights its ring and node in active gold (`.is-active`).
  - Simultaneously highlight its concentric symmetry counterpart `pairId` in dashed muted emerald (`.is-pair`):
    - Ring 1 (`Clause 01`)  Ring 1 Outer Seal (`Clause 10`)
    - Ring 2 (`Clause 02`)  (`Clause 09`)
    - Ring 3 (`Clause 03`)  (`Clause 08`)
    - Ring 4 (`Clause 04`)  (`Clause 07`)
    - Ring 5 Inner Core (`Clause 05`)  (`Clause 06`)

### B. Mobile-First Horizontal Pill Bar
- Render a horizontally scrollable pill strip (`Clause 01` – `Clause 10`) above the grid for thumb-friendly mobile navigation.
- Selecting a ring, node, pill, or Next/Previous button must synchronize all UI states and smoothly center the active pill via `scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" })`.

### C. Epistemological Study Card (Right Column / Bottom on Mobile)
- Include a 1-tap **"Symmetry Mirror: Clause XX ⇄"** button in the card header that jumps directly to `pairId`.
- Render structured blocks with exact badges:
  - `[QURAN]` — Full vocalized Uthmani Arabic (`lang="ar"`, `dir="rtl"`, `Amiri` serif font) + italicized English translation.
  - `[HADITH]` *(displayed on Clause 10 / Canonical Virtue)* — Sahih Muslim (810) & Sahih al-Bukhari (2311) citations.
  - `[TAFSIR]` — Concise Sunni exegesis attributed explicitly to *Ibn Kathir*, *Al-Tabari*, *Al-Qurtubi*, or *Al-Sa'di*.
  - `[REFLECTION]` — Student structural observation explaining the concentric symmetry relationship.
- Include keyboard navigation (`ArrowLeft` / `ArrowRight`) when the section is focused or hovered.

---

## 4. Implementation Code (Reference Module)

### HTML Section (`index.html`)
```html
<section id="kursi-explorer" class="hk-explorer" aria-label="Ayat al-Kursi Concentric Ring Explorer">
  <div class="hk-header">
    <div class="hk-eyebrow">Interactive Study Plate • Surah Al-Baqarah 2:255</div>
    <h2 class="hk-title">Ayat al-Kursi: 10-Clause Concentric Ring Map</h2>
    <p class="hk-subtitle">
      Select any ring or clause to trace how the outer frame of Divine Majesty mirrors inward toward the central axis of divine omniscience and human humility.
    </p>
  </div>

  <div class="hk-pills" id="hkClausePills" role="tablist" aria-label="Select Ayat al-Kursi Clause"></div>

  <div class="hk-grid">
    <div class="hk-stage">
      <svg class="hk-svg" viewBox="0 0 420 420" id="hkConcentricSvg" role="img" aria-label="Concentric rings representing the 10 clauses of Ayat al-Kursi"></svg>
      <div class="hk-legend">
        <span class="hk-legend-item"><i class="hk-dot-active"></i> Selected Clause</span>
        <span class="hk-legend-item"><i class="hk-dot-pair"></i> Concentric Symmetry Mirror</span>
      </div>
    </div>

    <article class="hk-panel" aria-live="polite">
      <div class="hk-panel-meta">
        <span class="hk-clause-badge" id="hkClauseBadge">Clause 01 of 10</span>
        <button type="button" class="hk-pair-btn" id="hkPairBtn">Symmetry Mirror ⇄</button>
      </div>

      <div class="hk-block">
        <span class="hk-tag hk-tag-quran">[QURAN]</span>
        <div class="hk-arabic" id="hkArabic" lang="ar" dir="rtl"></div>
        <div class="hk-translation" id="hkTranslation"></div>
      </div>

      <div class="hk-block" id="hkHadithBlock" hidden>
        <span class="hk-tag hk-tag-hadith">[HADITH]</span>
        <p class="hk-copy" id="hkHadithText"></p>
        <span class="hk-cite" id="hkHadithSource"></span>
      </div>

      <div class="hk-block">
        <span class="hk-tag hk-tag-tafsir">[TAFSIR]</span>
        <p class="hk-copy" id="hkTafsirText"></p>
        <span class="hk-cite" id="hkTafsirSource"></span>
      </div>

      <div class="hk-block">
        <span class="hk-tag hk-tag-reflection">[REFLECTION]</span>
        <p class="hk-copy" id="hkReflectionText"></p>
      </div>

      <div class="hk-nav">
        <button type="button" class="hk-nav-btn" id="hkPrevBtn">← Previous</button>
        <span class="hk-ring-label" id="hkRingLabel">Ring 1 • Outer Frame</span>
        <button type="button" class="hk-nav-btn" id="hkNextBtn">Next →</button>
      </div>
    </article>
  </div>
</section>


CSS Styles (hk- Namespaced)



CSS
.hk-explorer {
  --hk-bg: #131a17;
  --hk-elevated: #19221e;
  --hk-border: rgba(201, 168, 106, 0.24);
  --hk-gold: #c9a86a;
  --hk-gold-bright: #e6c88a;
  --hk-emerald: #4e8c73;
  --hk-text: #f2efe9;
  --hk-text-dim: #a8b0ac;
  --hk-muted: #75807b;

  max-width: 1120px;
  margin: 3rem auto;
  background: var(--hk-bg);
  border: 1px solid var(--hk-border);
  border-radius: 16px;
  padding: 2.25rem 1.5rem;
  color: var(--hk-text);
}

.hk-header { text-align: center; max-width: 680px; margin: 0 auto 1.75rem; }
.hk-eyebrow { font-size: 0.72rem; letter-spacing: 0.16em; text-transform: uppercase; color: var(--hk-gold); font-weight: 600; margin-bottom: 0.45rem; }
.hk-title { font-family: 'Cormorant Garamond', Georgia, serif; font-size: clamp(1.7rem, 3.2vw, 2.35rem); font-weight: 600; line-height: 1.2; margin-bottom: 0.6rem; }
.hk-subtitle { font-size: 0.92rem; color: var(--hk-text-dim); line-height: 1.6; }

.hk-pills { display: flex; gap: 0.45rem; overflow-x: auto; padding-bottom: 0.5rem; margin-bottom: 1.25rem; scrollbar-width: none; }
.hk-pills::-webkit-scrollbar { display: none; }
.hk-pill { flex: 0 0 auto; background: var(--hk-elevated); border: 1px solid var(--hk-border); color: var(--hk-text-dim); padding: 0.4rem 0.8rem; border-radius: 999px; font-size: 0.78rem; cursor: pointer; transition: 0.2s ease; }
.hk-pill:hover { border-color: var(--hk-gold); color: var(--hk-text); }
.hk-pill.is-active { background: var(--hk-gold); color: #0d1210; border-color: var(--hk-gold); font-weight: 600; }

.hk-grid { display: grid; grid-template-columns: 1fr 1.15fr; gap: 2rem; align-items: center; }
@media (max-width: 860px) {
  .hk-grid { grid-template-columns: 1fr; gap: 1.5rem; }
  .hk-explorer { padding: 1.5rem 1rem; margin: 2rem 0.75rem; }
}

.hk-stage { display: flex; flex-direction: column; align-items: center; }
.hk-svg { width: 100%; max-width: 410px; height: auto; overflow: visible; touch-action: manipulation; }
.hk-ring { fill: rgba(201, 168, 106, 0.02); stroke: rgba(201, 168, 106, 0.25); stroke-width: 2; cursor: pointer; transition: 0.3s ease; }
.hk-ring:hover { stroke: rgba(230, 200, 138, 0.65); fill: rgba(201, 168, 106, 0.06); }
.hk-ring.is-pair { stroke: var(--hk-emerald); stroke-width: 2.5; stroke-dasharray: 5 3; fill: rgba(78, 140, 115, 0.08); }
.hk-ring.is-active { stroke: var(--hk-gold-bright); stroke-width: 3.5; stroke-dasharray: none; fill: rgba(201, 168, 106, 0.14); filter: drop-shadow(0 0 10px rgba(201, 168, 106, 0.35)); }

.hk-node { cursor: pointer; }
.hk-node circle { fill: var(--hk-bg); stroke: rgba(201, 168, 106, 0.5); stroke-width: 1.5; transition: 0.25s ease; }
.hk-node text { fill: var(--hk-text-dim); font-size: 10px; font-weight: 600; text-anchor: middle; dominant-baseline: central; pointer-events: none; }
.hk-node.is-pair circle { stroke: var(--hk-emerald); fill: #162620; }
.hk-node.is-active circle { fill: var(--hk-gold); stroke: var(--hk-gold-bright); }
.hk-node.is-active text { fill: #0d1210; font-weight: 700; }

.hk-legend { display: flex; gap: 1.25rem; margin-top: 0.9rem; font-size: 0.78rem; color: var(--hk-text-dim); flex-wrap: wrap; justify-content: center; }
.hk-legend-item { display: flex; align-items: center; gap: 0.4rem; }
.hk-dot-active { display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: var(--hk-gold-bright); }
.hk-dot-pair { display: inline-block; width: 10px; height: 10px; border-radius: 50%; border: 1.5px dashed var(--hk-emerald); background: rgba(78, 140, 115, 0.25); }

.hk-panel { background: var(--hk-elevated); border: 1px solid var(--hk-border); border-radius: 12px; padding: 1.5rem; }
.hk-panel-meta { display: flex; justify-content: space-between; align-items: center; gap: 0.75rem; margin-bottom: 1rem; flex-wrap: wrap; }
.hk-clause-badge { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--hk-gold); }
.hk-pair-btn { font-size: 0.74rem; color: #8cc9b0; background: rgba(78, 140, 115, 0.15); border: 1px solid rgba(78, 140, 115, 0.35); padding: 0.25rem 0.65rem; border-radius: 999px; cursor: pointer; }
.hk-pair-btn:hover { background: rgba(78, 140, 115, 0.28); }

.hk-block { margin-bottom: 1.1rem; padding-bottom: 1.1rem; border-bottom: 1px solid rgba(255, 255, 255, 0.06); }
.hk-block:last-of-type { margin-bottom: 0; padding-bottom: 0; border-bottom: none; }
.hk-tag { display: inline-block; font-family: monospace; font-size: 0.72rem; font-weight: 700; padding: 0.15rem 0.45rem; border-radius: 4px; margin-bottom: 0.45rem; }
.hk-tag-quran { background: rgba(201, 168, 106, 0.18); color: var(--hk-gold-bright); }
.hk-tag-hadith { background: rgba(180, 130, 90, 0.2); color: #e8b88a; }
.hk-tag-tafsir { background: rgba(78, 140, 115, 0.18); color: #8cc9b0; }
.hk-tag-reflection { background: rgba(168, 176, 172, 0.15); color: #d4dad7; }

.hk-arabic { font-family: 'Amiri', serif; font-size: clamp(1.6rem, 3vw, 2.05rem); line-height: 1.85; color: var(--hk-text); text-align: right; margin: 0.25rem 0 0.45rem; }
.hk-translation { font-family: 'Cormorant Garamond', Georgia, serif; font-size: 1.15rem; font-style: italic; color: var(--hk-gold-bright); }
.hk-copy { font-size: 0.9rem; color: var(--hk-text-dim); line-height: 1.6; margin: 0; }
.hk-cite { display: block; font-size: 0.76rem; color: var(--hk-muted); margin-top: 0.35rem; }

.hk-nav { display: flex; justify-content: space-between; align-items: center; margin-top: 1.35rem; padding-top: 1rem; border-top: 1px solid var(--hk-border); }
.hk-nav-btn { background: transparent; border: 1px solid var(--hk-border); color: var(--hk-text); padding: 0.45rem 0.95rem; border-radius: 8px; font-size: 0.82rem; cursor: pointer; }
.hk-nav-btn:hover { border-color: var(--hk-gold); background: rgba(201, 168, 106, 0.08); }
.hk-ring-label { font-size: 0.78rem; color: var(--hk-muted); }


JavaScript Data & Controller (IIFE)



JavaScript
(() => {
  const CLAUSES = [
    {
      id: 1, pairId: 10, ringLabel: "Ring 1 • Outer Frame (Majesty)",
      arabic: "اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ",
      translation: "“Allah — there is no deity except Him, the Ever-Living, the All-Sustaining.”",
      tafsir: "Opens with absolute Tawhid and two comprehensive Names: Al-Hayy (perfection of divine life) and Al-Qayyum (self-subsisting and sustaining every atom of creation). Classical scholars noted the Greatest Name of Allah (Ism Allah al-A'zam) resides within these attributes.",
      tafsirSource: "Tafsir Ibn Kathir & Al-Sa'di (2:255)",
      reflection: "Matches Clause 10 on the outermost ring: the verse begins with Allah's self-sustaining perfection (Al-Hayy Al-Qayyum) and seals with His effortless preservation of creation."
    },
    {
      id: 2, pairId: 9, ringLabel: "Ring 2 • Tireless Vigilance",
      arabic: "لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ",
      translation: "“Neither drowsiness overtakes Him nor sleep.”",
      tafsir: "Negates every trace of fatigue, slumber, or lapse in awareness. Unlike created beings whose vigilance fades, Allah's watchfulness over His creation is unbroken for even a fraction of a moment.",
      tafsirSource: "Tafsir al-Tabari & Al-Qurtubi (2:255)",
      reflection: "Mirrors Clause 9: because neither drowsiness nor sleep ever touches Him, preserving the heavens and earth causes Him zero fatigue."
    },
    {
      id: 3, pairId: 8, ringLabel: "Ring 3 • Cosmic Sovereignty",
      arabic: "لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ",
      translation: "“To Him belongs whatever is in the heavens and whatever is on the earth.”",
      tafsir: "Establishes exclusive ownership (Mulk). Every galaxy, angel, ruler, and human being is an owned servant under His dominion—leaving no room for independent rivals.",
      tafsirSource: "Tafsir Ibn Kathir (2:255)",
      reflection: "Mirrors Clause 8 (His Kursi encompassing the heavens and earth): absolute ownership in Clause 3 is visually echoed by all-encompassing expanse in Clause 8."
    },
    {
      id: 4, pairId: 7, ringLabel: "Ring 4 • Boundary of Authority",
      arabic: "مَن ذَا الَّذِي يَشْفَعُ عِندَهُ إِلَّا بِإِذْنِهِ",
      translation: "“Who is it that can intercede with Him except by His permission?”",
      tafsir: "Refutes the illusion that angels, prophets, or idols possess independent lobbying power before God. Intercession occurs solely after Allah grants explicit leave.",
      tafsirSource: "Tafsir al-Qurtubi & Al-Sa'di (2:255)",
      reflection: "Mirrors Clause 7: no one can access His decree through intercession without His permission (Clause 4), just as no one can grasp His knowledge except what He wills (Clause 7)."
    },
    {
      id: 5, pairId: 6, ringLabel: "Ring 5 • Inner Core (Omniscience)",
      arabic: "يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ",
      translation: "“He knows what is before them and what will be after them,”",
      tafsir: "At the structural center of the verse lies Allah's complete knowledge of human past, present, and future—nothing in a servant's history or tomorrow is hidden from His sight.",
      tafsirSource: "Tafsir al-Tabari & Ibn Kathir (2:255)",
      reflection: "Forms the innermost axis with Clause 6: divine omniscience encompasses all human timelines (Clause 5), while human comprehension remains strictly bounded by divine will (Clause 6)."
    },
    {
      id: 6, pairId: 5, ringLabel: "Ring 5 • Inner Core (Human Limit)",
      arabic: "وَلَا يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلَّا بِمَا شَاءَ",
      translation: "“and they encompass not a thing of His knowledge except for what He wills.”",
      tafsir: "Instills intellectual humility before revelation. Human reason and empirical inquiry only perceive what Allah chooses to unveil through revelation and creation.",
      tafsirSource: "Tafsir al-Sa'di (2:255)",
      reflection: "Paired at the center with Clause 5: when a believer feels anxious about an unknown future, resting inside Allah's boundless knowledge brings immediate calm."
    },
    {
      id: 7, pairId: 4, ringLabel: "Ring 4 • Boundary of Authority",
      arabic: "وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ",
      translation: "“His Kursi extends over the heavens and the earth,”",
      tafsir: "Ibn 'Abbas (may Allah be pleased with him) explained that the Kursi is the footstool before the Throne ('Arsh), and its vastness dwarfs the seven heavens and earth like a ring thrown into an open desert.",
      tafsirSource: "Narrated via Ibn Abi Shaybah; cited in Tafsir Ibn Kathir",
      reflection: "Echoes the majestic scale of Clauses 3 & 4—recalibrating human perspective so worldly anxieties shrink beside the vastness of Allah's dominion."
    },
    {
      id: 8, pairId: 3, ringLabel: "Ring 3 • Cosmic Sovereignty",
      arabic: "وَلَا يَئُودُهُ حِفْظُهُمَا",
      translation: "“and their preservation tires Him not.”",
      tafsir: "Upholding the orbits of stars, the provision of every creature, and the protection of His servants places zero burden or strain upon Allah.",
      tafsirSource: "Tafsir al-Tabari & Ibn Kathir (2:255)",
      reflection: "Mirrors Clause 3: because all that is in the heavens and earth belongs entirely to Him, sustaining it all is effortless."
    },
    {
      id: 9, pairId: 2, ringLabel: "Ring 2 • Tireless Vigilance",
      arabic: "وَهُوَ الْعَلِيُّ الْعَظِيمُ",
      translation: "“And He is the Most High, the Most Great.”",
      tafsir: "Al-'Aliyy affirms His absolute elevation in essence, status, and power above all creation; Al-'Azim affirms supreme magnificence before which every earthly power bows.",
      tafsirSource: "Tafsir al-Sa'di (2:255)",
      reflection: "Completes the outer symmetry with Clauses 1 & 2—sealing the verse with two majestic Names just as it opened with Al-Hayy Al-Qayyum."
    },
    {
      id: 10, pairId: 1, ringLabel: "Ring 1 • Outer Seal (Covenant)",
      arabic: "﴿ آيَةُ الْكُرْسِيِّ — سُورَةُ الْبَقَرَةِ ٢٥٥ ﴾",
      translation: "“The Greatest Ayah in the Book of Allah — Complete 10-Clause Shield”",
      hadith: "The Prophet ﷺ asked Ubayy ibn Ka'b which verse in the Book of Allah is greatest, and affirmed when Ubayy recited Ayat al-Kursi. Reciting it after every obligatory prayer and before sleep brings continuous divine protection.",
      hadithSource: "Sahih Muslim (810) & Sahih al-Bukhari (2311)",
      tafsir: "Classical exegetes summarize that Ayat al-Kursi unites the foundations of Divine Names, Attributes, Creation, Command, and Decree in a single self-contained architectural jewel.",
      tafsirSource: "Tafsir Ibn Kathir & Al-Qurtubi (2:255)",
      reflection: "Stepping back to view all 10 rings together shows how the entire verse orbits divine knowledge and protection."
    }
  ];

  const svg = document.getElementById("hkConcentricSvg");
  const pills = document.getElementById("hkClausePills");
  if (!svg || !pills) return;

  let activeId = 1;

  const el = (id) => document.getElementById(id);

  function init() {
    const cx = 210, cy = 210, maxR = 192, stepR = 17.2;

    CLAUSES.forEach((item, idx) => {
      const r = maxR - idx * stepR;
      const ring = document.createElementNS("[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)", "circle");
      ring.setAttribute("cx", cx);
      ring.setAttribute("cy", cy);
      ring.setAttribute("r", r);
      ring.setAttribute("class", "hk-ring");
      ring.dataset.id = item.id;
      ring.addEventListener("click", () => render(item.id));
      svg.appendChild(ring);

      const rad = ((-90 + idx * 36) * Math.PI) / 180;
      const nx = cx + r * Math.cos(rad);
      const ny = cy + r * Math.sin(rad);

      const g = document.createElementNS("[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)", "g");
      g.setAttribute("class", "hk-node");
      g.dataset.id = item.id;
      g.addEventListener("click", () => render(item.id));

      const dot = document.createElementNS("[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)", "circle");
      dot.setAttribute("cx", nx);
      dot.setAttribute("cy", ny);
      dot.setAttribute("r", 10.5);

      const label = document.createElementNS("[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)", "text");
      label.setAttribute("x", nx);
      label.setAttribute("y", ny);
      label.textContent = item.id;

      g.appendChild(dot);
      g.appendChild(label);
      svg.appendChild(g);

      const pill = document.createElement("button");
      pill.type = "button";
      pill.className = "hk-pill";
      pill.dataset.id = item.id;
      pill.textContent = `Clause ${String(item.id).padStart(2, "0")}`;
      pill.addEventListener("click", () => render(item.id));
      pills.appendChild(pill);
    });

    el("hkPrevBtn").addEventListener("click", () => render(activeId === 1 ? 10 : activeId - 1));
    el("hkNextBtn").addEventListener("click", () => render(activeId === 10 ? 1 : activeId + 1));

    render(1);
  }

  function render(id) {
    activeId = id;
    const current = CLAUSES.find((c) => c.id === id);
    if (!current) return;

    svg.querySelectorAll(".hk-ring, .hk-node").forEach((node) => {
      const nId = Number(node.dataset.id);
      node.classList.toggle("is-active", nId === current.id);
      node.classList.toggle("is-pair", nId === current.pairId);
    });

    pills.querySelectorAll(".hk-pill").forEach((btn) => {
      const bId = Number(btn.dataset.id);
      const isMatch = bId === current.id;
      btn.classList.toggle("is-active", isMatch);
      if (isMatch) btn.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
    });

    el("hkClauseBadge").textContent = `Clause ${String(current.id).padStart(2, "0")} of 10`;
    const pairBtn = el("hkPairBtn");
    pairBtn.textContent = `Symmetry Mirror: Clause ${String(current.pairId).padStart(2, "0")} ⇄`;
    pairBtn.onclick = () => render(current.pairId);

    el("hkArabic").textContent = current.arabic;
    el("hkTranslation").textContent = current.translation;

    const hadithBlock = el("hkHadithBlock");
    if (current.hadith) {
      hadithBlock.hidden = false;
      el("hkHadithText").textContent = current.hadith;
      el("hkHadithSource").textContent = `Source: ${current.hadithSource}`;
    } else {
      hadithBlock.hidden = true;
    }

    el("hkTafsirText").textContent = current.tafsir;
    el("hkTafsirSource").textContent = `Source: ${current.tafsirSource}`;
    el("hkReflectionText").textContent = current.reflection;
    el("hkRingLabel").textContent = current.ringLabel;
  }

  init();
})();


5. Verification Checklist for Agent
Before marking improve04.md complete, verify:
Viewport Test (375px mobile & 1280px desktop): Confirm no horizontal page overflow occurs (overflow-x stays confined to .hk-pills), and all 10 SVG node numbers remain legible and tappable.
Font Inheritance: Confirm 'Amiri' and 'Cormorant Garamond' are loaded in <head> (or inherit cleanly from HUR Studio's existing Google Fonts link).
Zero Console Errors & Offline Check: Disconnect network in DevTools and verify all 10 clauses, symmetry mirrors, and Next/Previous buttons operate with zero network requests.
Versioning Update: Increment the footer/badge label cleanly if appropriate (e.g., Student Edition 03 • Interactive Plate 04) without breaking existing 1st_step_review03.pdf download links.



<ElicitationsGroup message="Would you like to generate the next implementation specs for your agent?">
  <Elicitation label="Write improve05.md for emotional-state entry doors and mobile swipeable plate cards" query="Write an improve05.md agent specification to add emotional-state entry doors and mobile swipeable plate cards to hur-studio.github.io."/>
  <Elicitation label="Write improve06.md for an offline Service Worker and 7-day study progress tracker" query="Write an improve06.md agent specification to upgrade hur-studio.github.io with full offline Service Worker caching and a localStorage 7-day study tracker."/>
  <Elicitation label="Audit and separate the institutional portfolio from the student landing page" query="Write an agent spec to cleanly separate portfolio.html from index.html on hur-studio.github.io so the main landing page stays focused on Quran learners."/>
</ElicitationsGroup>


