"""Génère index.html (FR) et en/index.html (EN) à partir du contenu ci-dessous.

Modifier le texte ici, puis lancer depuis la racine du dépôt :
    python _src/build.py
Le dossier _src n'est pas publié par GitHub Pages (préfixe « _ »).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://ede800.github.io/"
LINKEDIN = "https://www.linkedin.com/in/edouard-zhu-aa561223a/"
GITHUB = "https://github.com/ede800"
EMAIL = "edouardzhu@gmail.com"

ICONS = {
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>',
    "github": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 .3a12 12 0 0 0-3.8 23.38c.6.12.82-.26.82-.57v-2.04c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73 1.2.09 1.84 1.24 1.84 1.24 1.07 1.83 2.8 1.3 3.49 1 .11-.78.42-1.31.76-1.61-2.66-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.14-.3-.54-1.52.1-3.18 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.28-1.55 3.29-1.23 3.29-1.23.65 1.65.24 2.87.12 3.18.77.84 1.23 1.91 1.23 3.22 0 4.61-2.8 5.62-5.48 5.92.43.37.82 1.1.82 2.22v3.29c0 .31.21.69.83.57A12 12 0 0 0 12 .3"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 7 8.5 6 8.5-6"/></g></svg>',
    "download": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M12 4v11m0 0 4.5-4.5M12 15l-4.5-4.5M5 19h14"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-5-5 5 5-5 5"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></svg>',
}

FR = {
    "lang": "fr", "locale": "fr_FR", "path": "", "root": "",
    "title": "Edouard Zhu | Ingénieur Cybersécurité GRC & Digital Assets",
    "desc": "Élève-ingénieur cybersécurité (ESIEA), alternant GRC chez LVMH : risque tiers (TPRM), NIST CSF 2.0, ISO 27001, DORA, et investigation blockchain on-chain. Disponible en septembre 2027 (CDI).",
    "og_desc": "Gouvernance, Risques & Conformité chez LVMH · Investigation on-chain & DeFi. Disponible en septembre 2027 (CDI).",
    "skip": "Aller au contenu",
    "newtab": " (nouvel onglet)",
    "nav_label": "Navigation principale",
    "nav": [("apropos", "À propos"), ("experiences", "Expériences"), ("etudes", "Études de cas"), ("competences", "Compétences"), ("contact", "Contact")],
    "menu": "Menu",
    "other_lang": ("en/", "EN", "en", "English version"),
    "status": "Disponible sept. 2027 (CDI)",
    "cv": "Télécharger mon CV", "cv_pdf": "Télécharger mon CV (PDF)", "cv_file": "assets/CV_Edouard_Zhu.pdf",
    "badge": "Élève-Ingénieur Cybersécurité (ESIEA) <span aria-hidden=\"true\">•</span> Alternant GRC @ LVMH",
    "h1": "Ingénieur Cybersécurité — Gouvernance, Risques (GRC) &amp; Actifs Numériques",
    "lead": "J'accompagne les organisations dans la maîtrise de leurs risques technologiques et tiers (TPRM, DORA, ISO 27001), tout en combinant une solide base technique en investigation blockchain (On-Chain, DeFi) et automatisation.",
    "cta_cases": "Consulter mes études de cas",
    "social_label": "Profils et contact",
    "facts_label": "En bref",
    "facts": [("Poste visé", "Ingénieur GRC / Cyber-risques"), ("Disponibilité", "Septembre 2027 — CDI"), ("Localisation", "Paris · mobilité internationale"), ("Langues", "Français · Anglais · Chinois")],
    "about_kicker": "À propos", "about_h": "Deux expertises, un même objectif : maîtriser le risque.",
    "about": [
        "Élève-ingénieur en cybersécurité à l'ESIEA, je suis en alternance au sein de l'équipe Cybersécurité Groupe de LVMH (Design &amp; Compliance). J'y évalue les risques tiers, pilote des campagnes de conformité NIST CSF 2.0 et contribue à la standardisation des exigences de sécurité du Groupe.",
        "Mon parcours de développeur (Python/Django) et mon expérience d'investigation on-chain chez FAKGROUP me permettent de dialoguer aussi bien avec les équipes techniques qu'avec le management, les Achats, le Juridique ou le DPO.",
        "Passionné d'économie, je m'intéresse de près au fonctionnement de la monnaie — fiduciaire comme cryptomonnaies — et à la blockchain, que je suis à travers une veille réglementaire active (MiCA, DORA, GAFI).",
    ],
    "pillars": [
        ("GRC &amp; Audit IT", "TPRM, vérification par la preuve, NIST CSF 2.0, ISO 27001, arbitrages de risque pour le management."),
        ("Blockchain &amp; investigations", "Traçage de flux on-chain, analyse de smart contracts et de protocoles DeFi, logique AML / LCB-FT."),
        ("Automatisation", "Scripts Python sur-mesure pour l'extraction et le parsing de données, développement sécurisé et CI/CD."),
    ],
    "cases_kicker": "Études de cas &amp; méthodologie", "cases_h": "Comment je travaille, sur trois sujets concrets.",
    "steps": ("Problématique", "Méthodologie", "Résultat"),
    "cases": [
        {
            "tag": "GRC · LVMH", "title": "Maîtrise du risque tiers (TPRM) &amp; Security by Design en grand groupe",
            "steps": [
                "Évaluation de solutions SaaS et de prestataires critiques à l'échelle internationale (75 Maisons).",
                "Qualification de la sensibilité des actifs (modèle CIAT : Confidentialité, Intégrité, Disponibilité, Traçabilité) ; passage de l'auto-évaluation déclarative à la vérification par la preuve (rapports SOC 2, certificats ISO 27001, pentests).",
                "Notes d'arbitrage pour le management et intégration de mesures compensatoires techniques (SSO/MFA Okta, filtrage IP, chiffrement AES-256) et contractuelles (Plans d'Assurance Sécurité — PAS/SAP).",
            ],
            "tags": ["TPRM", "CIAT", "SOC 2", "ISO 27001", "PAS"],
        },
        {
            "tag": "Blockchain · FAKGROUP", "title": "Investigation forensique on-chain &amp; analyse de flux blockchain",
            "steps": [
                "Réponse à des incidents de sécurité liés à la blockchain et surveillance de flux transactionnels.",
                "Traçage de transactions sur explorateurs de blocs (Etherscan, Solscan), analyse des interactions avec des smart contracts, protocoles DeFi et DEX, détection de schémas d'obfuscation ou d'anomalies.",
                "Automatisation de l'extraction et du parsing des données transactionnelles via des scripts Python sur-mesure pour qualifier les comportements suspects (logique MAR / AML / LCB-FT).",
            ],
            "tags": ["Etherscan", "Solscan", "DeFi", "Python", "AML"],
        },
        {
            "tag": "Conformité · LVMH", "title": "Standardisation Groupe (Blueprints) &amp; conformité NIST CSF 2.0",
            "steps": [
                "Harmonisation des standards de sécurité et évaluation de la maturité cyber de multiples filiales.",
                "Pilotage des campagnes d'auto-évaluation sur les 6 piliers du NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) et structuration du catalogue de produits sécurisés recommandés (Blueprints).",
                "Cartographie précise des écarts de conformité et accompagnement pragmatique des équipes métiers (Build &amp; Run).",
            ],
            "tags": ["NIST CSF 2.0", "Blueprints", "Gap analysis", "Build &amp; Run"],
        },
    ],
    "exp_kicker": "Expériences", "exp_h": "Parcours professionnel",
    "jobs": [
        ("LVMH (Holding)", "https://www.lvmh.com", "Alternant Gouvernance, Risques &amp; Conformité (GRC) Cybersécurité", "Paris", "Sept. 2024 – Présent", [
            "Évaluation de la maturité sécurité des prestataires critiques (TPRM), analyse de preuves et arbitrages hebdomadaires.",
            "Pilotage des campagnes de conformité NIST CSF 2.0 auprès des Maisons du Groupe.",
            "Projet stratégique Blueprints : standardisation des exigences de sécurité IT/Cloud en lien avec les équipes Achats, Juridique et DPO.",
        ]),
        ("FAKGROUP", "https://fakgroup.fr", "Alternant Développeur &amp; Sécurité", "Paris", "Sept. 2023 – Août 2024", [
            "Investigation forensique blockchain, traçage de flux on-chain et analyse d'incidents.",
            "Développement full-stack sécurisé (Python/Django), remédiation OWASP Top 10 et intégration de contrôles dans les pipelines CI/CD.",
        ]),
        ("PIXIM Communication", "https://www.pixim.fr", "Stagiaire Développeur Web &amp; Automatisation", "France", "Juil. 2022 – Août 2022", [
            "Automatisation de flux transactionnels en Python/Django et optimisation de bases de données relationnelles (CRM/ERP).",
        ]),
    ],
    "edu_kicker": "Formation &amp; distinctions", "edu_h": "Formation",
    "schools": [
        ("ESIEA", "https://www.esiea.fr", "Diplôme d'Ingénieur, spécialisation Cybersécurité", "Titre CTI, grade de Master · Paris", "2024 – 2027"),
        ("EPITA", "https://www.epita.fr", "Bachelor Cybersécurité", "Paris", "2021 – 2024"),
    ],
    "award_kicker": "Distinction CTF",
    "award_h": "Top 5 % mondial sur Root-Me",
    "award": "Plus de 3 900 points. Pratique régulière de challenges d'investigation, de sécurité web et de résolution de problèmes techniques complexes.",
    "award_link": "Voir Root-Me",
    "skills_kicker": "Compétences", "skills_h": "Domaines d'expertise",
    "skills": [
        ("Gouvernance, Risques &amp; Réglementation", ["TPRM", "ISO 27001 / 27005 / 27036", "NIST CSF 2.0", "EBIOS RM", "DORA", "MiCA", "RGPD", "NIS 2", "Modèle CIAT", "Plans d'Assurance Sécurité (PAS/SAP)"]),
        ("Blockchain &amp; Digital Assets", ["Architecture Ethereum / Bitcoin / L2", "Smart Contracts", "Protocoles DeFi", "Stablecoins", "Tokens (ERC-20, ERC-721)", "Analyse on-chain (Etherscan)", "Logique Chainalysis / Scorechain"]),
        ("Sécurité technique &amp; Développement", ["Python (data parsing &amp; automatisation)", "SQL", "Django", "Bash", "OWASP Top 10", "CI/CD", "Burp Suite", "Wireshark", "Nmap", "Git"]),
        ("Langues", ["Français — natif", "Anglais — professionnel B2, usage quotidien", "Chinois — intermédiaire"]),
    ],
    "contact_kicker": "Contact", "contact_h": "Me contacter",
    "contact_lead": "Une opportunité en CDI à partir de septembre 2027, une mission GRC ou une question sur la blockchain ? Écrivez-moi, je réponds rapidement.",
    "copy": "Copier", "copy_sr": "l'adresse email", "copied": "Adresse email copiée.", "copy_fail": "La copie a échoué : sélectionnez l'adresse manuellement.",
    "a11y": "Accessibilité", "source": "Code source", "top": "Haut de page",
}

EN = {
    "lang": "en", "locale": "en_GB", "path": "en/", "root": "../",
    "title": "Edouard Zhu | Cybersecurity Engineer — GRC & Digital Assets",
    "desc": "Cybersecurity engineering student (ESIEA) and GRC apprentice at LVMH: third-party risk (TPRM), NIST CSF 2.0, ISO 27001, DORA and on-chain blockchain investigation. Available September 2027 (permanent role).",
    "og_desc": "Governance, Risk & Compliance at LVMH · On-chain & DeFi investigation. Available September 2027.",
    "skip": "Skip to content",
    "newtab": " (opens in a new tab)",
    "nav_label": "Main navigation",
    "nav": [("apropos", "About"), ("experiences", "Experience"), ("etudes", "Case studies"), ("competences", "Skills"), ("contact", "Contact")],
    "menu": "Menu",
    "other_lang": ("../", "FR", "fr", "Version française"),
    "status": "Available Sept. 2027 (permanent)",
    "cv": "Download my CV", "cv_pdf": "Download my CV (PDF)", "cv_file": "assets/CV_Edouard_Zhu_EN.pdf",
    "badge": "Cybersecurity Engineering Student (ESIEA) <span aria-hidden=\"true\">•</span> GRC Apprentice @ LVMH",
    "h1": "Cybersecurity Engineer — Governance, Risk (GRC) &amp; Digital Assets",
    "lead": "I help organisations control their technology and third-party risks (TPRM, DORA, ISO 27001), combining this with a solid technical background in blockchain investigation (on-chain, DeFi) and automation.",
    "cta_cases": "View my case studies",
    "social_label": "Profiles and contact",
    "facts_label": "At a glance",
    "facts": [("Target role", "GRC / Cyber-risk Engineer"), ("Availability", "September 2027 — permanent"), ("Location", "Paris · open to relocation"), ("Languages", "French · English · Chinese")],
    "about_kicker": "About", "about_h": "Two areas of expertise, one goal: controlling risk.",
    "about": [
        "I am a cybersecurity engineering student at ESIEA and an apprentice in LVMH's Group Cybersecurity team (Design &amp; Compliance), where I assess third-party risk, run NIST CSF 2.0 compliance campaigns and help standardise the Group's security requirements.",
        "My background as a developer (Python/Django) and my on-chain investigation experience at FAKGROUP let me work comfortably with technical teams as well as management, Procurement, Legal and the DPO.",
        "I am passionate about economics, especially how money works — fiat and cryptocurrencies alike — and about blockchain, which I follow closely through active regulatory watch (MiCA, DORA, FATF).",
    ],
    "pillars": [
        ("GRC &amp; IT Audit", "TPRM, evidence-based assessment, NIST CSF 2.0, ISO 27001, risk decisions for management."),
        ("Blockchain &amp; investigations", "On-chain flow tracing, smart contract and DeFi protocol analysis, AML / CFT logic."),
        ("Automation", "Custom Python scripts for data extraction and parsing, secure development and CI/CD."),
    ],
    "cases_kicker": "Case studies &amp; methodology", "cases_h": "How I work, through three concrete engagements.",
    "steps": ("Challenge", "Approach", "Outcome"),
    "cases": [
        {
            "tag": "GRC · LVMH", "title": "Third-party risk management (TPRM) &amp; Security by Design in a global group",
            "steps": [
                "Assessing SaaS solutions and critical suppliers on an international scale (75 Maisons).",
                "Classifying asset sensitivity (CIAT model: Confidentiality, Integrity, Availability, Traceability); moving from self-declared questionnaires to evidence-based verification (SOC 2 reports, ISO 27001 certificates, penetration tests).",
                "Decision memos for management and compensating controls, both technical (Okta SSO/MFA, IP filtering, AES-256 encryption) and contractual (Security Assurance Plans — SAP).",
            ],
            "tags": ["TPRM", "CIAT", "SOC 2", "ISO 27001", "SAP"],
        },
        {
            "tag": "Blockchain · FAKGROUP", "title": "On-chain forensic investigation &amp; blockchain flow analysis",
            "steps": [
                "Responding to blockchain-related security incidents and monitoring transaction flows.",
                "Tracing transactions on block explorers (Etherscan, Solscan), analysing interactions with smart contracts, DeFi protocols and DEXs, detecting obfuscation patterns and anomalies.",
                "Automated extraction and parsing of transaction data with custom Python scripts to qualify suspicious behaviour (MAR / AML / CFT logic).",
            ],
            "tags": ["Etherscan", "Solscan", "DeFi", "Python", "AML"],
        },
        {
            "tag": "Compliance · LVMH", "title": "Group standardisation (Blueprints) &amp; NIST CSF 2.0 compliance",
            "steps": [
                "Harmonising security standards and assessing the cyber maturity of multiple subsidiaries.",
                "Running self-assessment campaigns across the 6 NIST CSF 2.0 functions (Govern, Identify, Protect, Detect, Respond, Recover) and structuring the catalogue of recommended secure products (Blueprints).",
                "Precise mapping of compliance gaps and pragmatic support for business teams (Build &amp; Run).",
            ],
            "tags": ["NIST CSF 2.0", "Blueprints", "Gap analysis", "Build &amp; Run"],
        },
    ],
    "exp_kicker": "Experience", "exp_h": "Professional experience",
    "jobs": [
        ("LVMH (Holding)", "https://www.lvmh.com", "Cybersecurity Governance, Risk &amp; Compliance (GRC) Apprentice", "Paris", "Sept. 2024 – Present", [
            "Assessing the security maturity of critical suppliers (TPRM), reviewing evidence and weekly risk decisions.",
            "Running NIST CSF 2.0 compliance campaigns across the Group's Maisons.",
            "Strategic Blueprints project: standardising IT/Cloud security requirements with Procurement, Legal and the DPO.",
        ]),
        ("FAKGROUP", "https://fakgroup.fr", "Developer &amp; Security Apprentice", "Paris", "Sept. 2023 – Aug. 2024", [
            "Blockchain forensic investigation, on-chain flow tracing and incident analysis.",
            "Secure full-stack development (Python/Django), OWASP Top 10 remediation and security controls in CI/CD pipelines.",
        ]),
        ("PIXIM Communication", "https://www.pixim.fr", "Web Developer &amp; Automation Intern", "France", "Jul. 2022 – Aug. 2022", [
            "Automated transactional workflows in Python/Django and optimised relational databases (CRM/ERP).",
        ]),
    ],
    "edu_kicker": "Education &amp; awards", "edu_h": "Education",
    "schools": [
        ("ESIEA", "https://www.esiea.fr", "Engineering Degree, Cybersecurity major", "CTI-accredited, Master's level · Paris", "2024 – 2027"),
        ("EPITA", "https://www.epita.fr", "Bachelor's in Cybersecurity", "Paris", "2021 – 2024"),
    ],
    "award_kicker": "CTF distinction",
    "award_h": "Top 5% worldwide on Root-Me",
    "award": "3,900+ points. Regular practice of investigation, web security and complex technical problem-solving challenges.",
    "award_link": "Visit Root-Me",
    "skills_kicker": "Skills", "skills_h": "Areas of expertise",
    "skills": [
        ("Governance, Risk &amp; Regulation", ["TPRM", "ISO 27001 / 27005 / 27036", "NIST CSF 2.0", "EBIOS RM", "DORA", "MiCA", "GDPR", "NIS 2", "CIAT model", "Security Assurance Plans (SAP)"]),
        ("Blockchain &amp; Digital Assets", ["Ethereum / Bitcoin / L2 architecture", "Smart contracts", "DeFi protocols", "Stablecoins", "Tokens (ERC-20, ERC-721)", "On-chain analysis (Etherscan)", "Chainalysis / Scorechain logic"]),
        ("Technical security &amp; Development", ["Python (data parsing &amp; automation)", "SQL", "Django", "Bash", "OWASP Top 10", "CI/CD", "Burp Suite", "Wireshark", "Nmap", "Git"]),
        ("Languages", ["French — native", "English — professional B2, daily use", "Chinese — intermediate"]),
    ],
    "contact_kicker": "Contact", "contact_h": "Get in touch",
    "contact_lead": "A permanent role from September 2027, a GRC engagement or a question about blockchain? Drop me a line — I reply quickly.",
    "copy": "Copy", "copy_sr": "email address", "copied": "Email address copied.", "copy_fail": "Copy failed: please select the address manually.",
    "a11y": "Accessibility (FR)", "source": "Source code", "top": "Back to top",
}


def ext(href, label, t, cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{href}" target="_blank" rel="noopener"{extra}>{label}<span class="sr-only">{t["newtab"]}</span></a>'


def page(t):
    r = t["root"]
    alt_href, alt_txt, alt_lang, alt_label = t["other_lang"]
    nav = "\n".join(f'        <li><a href="#{i}">{l}</a></li>' for i, l in t["nav"])
    socials = (
        ext(LINKEDIN, ICONS["linkedin"] + '<span class="sr-only">LinkedIn</span>', t, "icon-btn", ' aria-label="LinkedIn"')
        + f'\n          <a class="icon-btn" href="mailto:{EMAIL}" aria-label="Email : {EMAIL}">{ICONS["mail"]}</a>\n          '
        + ext(GITHUB, ICONS["github"] + '<span class="sr-only">GitHub</span>', t, "icon-btn", ' aria-label="GitHub"')
    )
    facts = "\n".join(f"          <div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in t["facts"])
    about = "\n".join(f"        <p>{p}</p>" for p in t["about"])
    pillars = "\n".join(f'        <li><h3>{h}</h3><p>{p}</p></li>' for h, p in t["pillars"])

    cases = []
    for n, c in enumerate(t["cases"], 1):
        steps = "\n".join(
            f'            <li><span class="step-label">{lbl}</span><p>{txt}</p></li>' for lbl, txt in zip(t["steps"], c["steps"])
        )
        tags = "".join(f"<li>{x}</li>" for x in c["tags"])
        cases.append(f"""      <article class="case" aria-labelledby="case{n}">
        <p class="case-meta"><span class="case-num">0{n}</span>{c["tag"]}</p>
        <h3 id="case{n}">{c["title"]}</h3>
        <ol class="case-steps">
{steps}
        </ol>
        <ul class="tags" aria-label="Mots-clés">{tags}</ul>
      </article>""")
    cases = "\n".join(cases)

    jobs = []
    for org, url, role, place, dates, items in t["jobs"]:
        lis = "\n".join(f"            <li>{i}</li>" for i in items)
        jobs.append(f"""      <li class="tl-item">
        <div class="tl-date">{dates}</div>
        <div class="tl-body">
          <h3>{role}</h3>
          <p class="tl-org">{ext(url, org, t)} <span aria-hidden="true">·</span> {place}</p>
          <ul>
{lis}
          </ul>
        </div>
      </li>""")
    jobs = "\n".join(jobs)

    schools = "\n".join(
        f"""        <li class="edu-item"><div class="tl-date">{d}</div><div><h3>{deg}</h3><p class="tl-org">{ext(u, s, t)} <span aria-hidden="true">·</span> {sub}</p></div></li>"""
        for s, u, deg, sub, d in t["schools"]
    )
    skills = "\n".join(
        f"""      <div class="skill-group"><h3>{g}</h3><ul class="tags">{"".join(f"<li>{x}</li>" for x in items)}</ul></div>"""
        for g, items in t["skills"]
    )
    copy_btn = f'<button type="button" class="btn btn-ghost btn-sm copy" data-copy="{EMAIL}" data-ok="{t["copied"]}" data-fail="{t["copy_fail"]}">{t["copy"]} <span class="sr-only">{t["copy_sr"]}</span></button>'

    return f"""<!doctype html>
<html lang="{t["lang"]}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta name="author" content="Edouard Zhu">
<meta name="theme-color" content="#0F172A">
<link rel="canonical" href="{SITE}{t["path"]}">
<link rel="alternate" hreflang="fr" href="{SITE}">
<link rel="alternate" hreflang="en" href="{SITE}en/">
<link rel="alternate" hreflang="x-default" href="{SITE}">
<meta property="og:type" content="profile">
<meta property="og:url" content="{SITE}{t["path"]}">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["og_desc"]}">
<meta property="og:image" content="{SITE}assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Edouard Zhu — {t["h1"]}">
<meta property="og:locale" content="{t["locale"]}">
<meta property="profile:first_name" content="Edouard">
<meta property="profile:last_name" content="Zhu">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css">
<script>document.documentElement.className = "js";</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Edouard Zhu",
  "jobTitle": "{t["h1"].replace("&amp;", "&")}",
  "url": "{SITE}{t["path"]}",
  "image": "{SITE}assets/og-image.png",
  "email": "mailto:{EMAIL}",
  "address": {{ "@type": "PostalAddress", "addressLocality": "Paris", "addressCountry": "FR" }},
  "worksFor": {{ "@type": "Organization", "name": "LVMH", "url": "https://www.lvmh.com" }},
  "alumniOf": [
    {{ "@type": "CollegeOrUniversity", "name": "ESIEA", "url": "https://www.esiea.fr" }},
    {{ "@type": "CollegeOrUniversity", "name": "EPITA", "url": "https://www.epita.fr" }}
  ],
  "knowsAbout": ["GRC", "TPRM", "ISO 27001", "NIST CSF 2.0", "DORA", "MiCA", "EBIOS RM", "Blockchain", "DeFi", "On-chain analysis", "Python"],
  "knowsLanguage": ["fr", "en", "zh"],
  "sameAs": ["{LINKEDIN}", "{GITHUB}"]
}}
</script>
</head>
<body>
<a class="skip" href="#main">{t["skip"]}</a>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="#top" aria-label="Edouard Zhu — {t["top"]}"><span class="logo-mark" aria-hidden="true">EZ</span><span>Edouard Zhu</span></a>
    <button type="button" class="menu-btn" aria-expanded="false" aria-controls="site-nav">{ICONS["menu"]}<span>{t["menu"]}</span></button>
    <div class="nav-panel" id="site-nav">
      <nav aria-label="{t["nav_label"]}">
        <ul class="nav-links">
{nav}
        </ul>
      </nav>
      <div class="header-actions">
        <a class="lang" href="{alt_href}" hreflang="{alt_lang}" lang="{alt_lang}" aria-label="{alt_label}">{alt_txt}</a>
        <span class="status"><span class="status-dot" aria-hidden="true"></span>{t["status"]}</span>
        <a class="btn btn-primary btn-sm" href="{r}{t["cv_file"]}" download>{ICONS["download"]}{t["cv"]}</a>
      </div>
    </div>
  </div>
</header>

<main id="main" tabindex="-1">
  <span id="top"></span>

  <section class="hero" aria-labelledby="hero-title">
    <div class="wrap hero-grid">
      <div>
        <p class="print-only print-name">Edouard Zhu</p>
        <p class="print-only print-contact">{EMAIL} · linkedin.com/in/edouard-zhu-aa561223a · github.com/ede800 · ede800.github.io</p>
        <p class="badge"><span class="badge-dot" aria-hidden="true"></span>{t["badge"]}</p>
        <h1 id="hero-title">{t["h1"]}</h1>
        <p class="hero-lead">{t["lead"]}</p>
        <div class="hero-cta">
          <a class="btn btn-light" href="#etudes">{t["cta_cases"]}{ICONS["arrow"]}</a>
          <a class="btn btn-outline-light" href="{r}{t["cv_file"]}" download>{ICONS["download"]}{t["cv_pdf"]}</a>
        </div>
        <div class="socials" role="group" aria-label="{t["social_label"]}">
          {socials}
        </div>
      </div>
      <div class="facts" role="group" aria-label="{t["facts_label"]}">
        <p class="facts-name">Edouard Zhu</p>
        <dl>
{facts}
        </dl>
      </div>
    </div>
  </section>

  <section id="apropos" class="section" aria-labelledby="apropos-h">
    <div class="wrap about-grid">
      <div>
        <p class="kicker">{t["about_kicker"]}</p>
        <h2 id="apropos-h">{t["about_h"]}</h2>
      </div>
      <div class="prose">
{about}
      </div>
      <ul class="pillars">
{pillars}
      </ul>
    </div>
  </section>

  <section id="etudes" class="section section-alt" aria-labelledby="etudes-h">
    <div class="wrap">
      <p class="kicker">{t["cases_kicker"]}</p>
      <h2 id="etudes-h">{t["cases_h"]}</h2>
      <div class="cases">
{cases}
      </div>
    </div>
  </section>

  <section id="experiences" class="section" aria-labelledby="experiences-h">
    <div class="wrap">
      <p class="kicker">{t["exp_kicker"]}</p>
      <h2 id="experiences-h">{t["exp_h"]}</h2>
      <ol class="timeline">
{jobs}
      </ol>
    </div>
  </section>

  <section id="formation" class="section section-alt" aria-labelledby="formation-h">
    <div class="wrap edu-grid">
      <div>
        <p class="kicker">{t["edu_kicker"]}</p>
        <h2 id="formation-h">{t["edu_h"]}</h2>
        <ol class="edu">
{schools}
        </ol>
      </div>
      <div class="award">
        <p class="kicker kicker-gold">{t["award_kicker"]}</p>
        <h3>{t["award_h"]}</h3>
        <p>{t["award"]}</p>
        {ext("https://www.root-me.org", t["award_link"] + ' <span aria-hidden="true">→</span>', t, "text-link")}
      </div>
    </div>
  </section>

  <section id="competences" class="section" aria-labelledby="competences-h">
    <div class="wrap">
      <p class="kicker">{t["skills_kicker"]}</p>
      <h2 id="competences-h">{t["skills_h"]}</h2>
      <div class="skills">
{skills}
      </div>
    </div>
  </section>

  <section id="contact" class="section contact" aria-labelledby="contact-h">
    <div class="wrap contact-grid">
      <div>
        <p class="kicker">{t["contact_kicker"]}</p>
        <h2 id="contact-h">{t["contact_h"]}</h2>
        <p class="contact-lead">{t["contact_lead"]}</p>
      </div>
      <ul class="contact-list">
        <li>{ICONS["mail"]}<a href="mailto:{EMAIL}">{EMAIL}</a>{copy_btn}<span class="sr-only" role="status" data-copy-status></span></li>
        <li>{ICONS["linkedin"]}{ext(LINKEDIN, "linkedin.com/in/edouard-zhu", t)}</li>
        <li>{ICONS["github"]}{ext(GITHUB, "github.com/ede800", t)}</li>
      </ul>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <span>© 2026 Edouard Zhu</span>
    <ul>
      <li><a href="{r}accessibilite.html">{t["a11y"]}</a></li>
      <li>{ext(GITHUB + "/ede800.github.io", t["source"], t)}</li>
      <li><a href="#top">{t["top"]} <span aria-hidden="true">↑</span></a></li>
    </ul>
  </div>
</footer>

<script src="{r}assets/main.js" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    (ROOT / "index.html").write_text(page(FR), encoding="utf-8", newline="\n")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(page(EN), encoding="utf-8", newline="\n")
    print("index.html et en/index.html générés")
