#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour extraire le texte structuré d'un fichier PDF
"""

import sys
from pathlib import Path

def extraire_pdf_basique(chemin_pdf):
    """Tente d'extraire le texte avec différentes bibliothèques"""
    print(f"📖 Extraction de {chemin_pdf}...")
    
    # Méthode 1 : PyPDF2
    try:
        import PyPDF2
        print("✅ PyPDF2 disponible, extraction en cours...")
        
        texte_blocks = []
        with open(chemin_pdf, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            num_pages = len(pdf_reader.pages)
            
            print(f"📄 Pages trouvées : {num_pages}")
            
            for i, page in enumerate(pdf_reader.pages):
                texte = page.extract_text()
                if texte.strip():
                    texte_blocks.append(texte)
                    
                    if (i + 1) % 10 == 0:
                        print(f"   Page {i + 1}/{num_pages} traitée...")
        
        return '\n\n'.join(texte_blocks)
        
    except ImportError:
        print("⚠️ PyPDF2 non disponible, tentative avec pdfplumber...")
    except Exception as e:
        print(f"⚠️ Erreur PyPDF2 : {e}, tentative avec pdfplumber...")
    
    # Méthode 2 : pdfplumber
    try:
        import pdfplumber
        print("✅ pdfplumber disponible, extraction en cours...")
        
        texte_blocks = []
        with pdfplumber.open(chemin_pdf) as pdf:
            num_pages = len(pdf.pages)
            print(f"📄 Pages trouvées : {num_pages}")
            
            for i, page in enumerate(pdf.pages):
                texte = page.extract_text()
                if texte:
                    texte_blocks.append(texte)
                    
                    if (i + 1) % 10 == 0:
                        print(f"   Page {i + 1}/{num_pages} traitée...")
        
        return '\n\n'.join(texte_blocks)
        
    except ImportError:
        print("⚠️ pdfplumber non disponible, tentative avec pymupdf (fitz)...")
    except Exception as e:
        print(f"⚠️ Erreur pdfplumber : {e}, tentative avec pymupdf...")
    
    # Méthode 3 : pymupdf (fitz)
    try:
        import fitz
        print("✅ pymupdf disponible, extraction en cours...")
        
        doc = fitz.open(chemin_pdf)
        num_pages = len(doc)
        print(f"📄 Pages trouvées : {num_pages}")
        
        texte_blocks = []
        for i in range(num_pages):
            page = doc[i]
            texte = page.get_text()
            if texte.strip():
                texte_blocks.append(texte)
                
                if (i + 1) % 10 == 0:
                    print(f"   Page {i + 1}/{num_pages} traitée...")
        
        doc.close()
        return '\n\n'.join(texte_blocks)
        
    except ImportError:
        print("❌ Aucune bibliothèque PDF disponible")
        print("\n💡 Installation possible :")
        print("   pip install PyPDF2")
        print("   pip install pdfplumber")
        print("   pip install pymupdf")
        return None
    except Exception as e:
        print(f"❌ Erreur pymupdf : {e}")
        return None

if __name__ == "__main__":
    chemin_pdf = Path("Apocalypse.pdf")
    
    if chemin_pdf.exists():
        texte_extrait = extraire_pdf_basique(chemin_pdf)
        
        if texte_extrait:
            # Nettoyer et structurer
            # Ajouter des sauts de ligne après les phrases
            texte_nettoye = texte_extrait.replace('.\n', '.\n\n')
            
            # Sauvegarder
            output_file = Path("Apocalypse_extraite_pdf.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("# Apocalypse - Extrait depuis PDF\n\n")
                f.write("*Extraction automatique depuis Apocalypse.pdf*\n\n")
                f.write("---\n\n")
                f.write(texte_nettoye)
            
            print(f"\n✅ Texte extrait sauvegardé dans {output_file}")
            print(f"📊 Longueur : {len(texte_extrait)} caractères")
            print(f"📊 Première ligne : {texte_extrait[:150]}...")
        else:
            print("❌ Échec de l'extraction")
    else:
        print(f"❌ Fichier {chemin_pdf} non trouvé")

