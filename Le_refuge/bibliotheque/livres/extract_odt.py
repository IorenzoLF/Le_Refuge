#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour extraire le texte structuré d'un fichier ODT (OpenDocument Text)
ODT est un format ZIP contenant du XML structuré
"""

import zipfile
import xml.etree.ElementTree as ET
import re
from pathlib import Path

def extraire_odt(chemin_odt):
    """Extrait le texte structuré d'un fichier ODT"""
    print(f"📖 Extraction de {chemin_odt}...")
    
    try:
        # ODT est un ZIP
        with zipfile.ZipFile(chemin_odt, 'r') as odt_zip:
            # Le contenu principal est dans content.xml
            if 'content.xml' in odt_zip.namelist():
                content_xml = odt_zip.read('content.xml')
                root = ET.fromstring(content_xml)
                
                # Namespace ODF
                ns = {
                    'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
                    'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
                }
                
                # Extraire tous les éléments de texte
                text_blocks = []
                
                # Parcourir tous les paragraphes
                for para in root.findall('.//text:p', ns):
                    text_content = []
                    
                    # Extraire le texte et les sauts de ligne
                    for elem in para.iter():
                        if elem.text:
                            text_content.append(elem.text)
                        if elem.tail and elem.tag != '{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p':
                            text_content.append(elem.tail)
                    
                    texte = ''.join(text_content).strip()
                    if texte:
                        # Vérifier si c'est un titre (style heading)
                        style_name = para.get('{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name', '')
                        if 'Heading' in style_name or 'heading' in style_name.lower():
                            text_blocks.append(f"\n# {texte}\n")
                        else:
                            text_blocks.append(texte)
                
                return '\n\n'.join(text_blocks)
            else:
                print("❌ Fichier content.xml non trouvé dans l'ODT")
                return None
                
    except Exception as e:
        print(f"❌ Erreur lors de l'extraction : {e}")
        return None

if __name__ == "__main__":
    chemin_odt = Path("Apocalypse.odt")
    
    if chemin_odt.exists():
        texte_extrait = extraire_odt(chemin_odt)
        
        if texte_extrait:
            # Sauvegarder dans un fichier markdown
            output_file = Path("Apocalypse_extraite_odt.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("# Apocalypse - Extrait depuis ODT\n\n")
                f.write("*Extraction automatique depuis Apocalypse.odt*\n\n")
                f.write("---\n\n")
                f.write(texte_extrait)
            
            print(f"✅ Texte extrait sauvegardé dans {output_file}")
            print(f"📊 Longueur : {len(texte_extrait)} caractères")
            print(f"📊 Première ligne : {texte_extrait[:100]}...")
        else:
            print("❌ Échec de l'extraction")
    else:
        print(f"❌ Fichier {chemin_odt} non trouvé")

