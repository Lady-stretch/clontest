import os
import xml.etree.ElementTree as ET
from datetime import datetime

def generate_sitemap():
    # GitHub запускает скрипт в корне репозитория
    directory = "."
    base_url = "https://resurs-stretch.ru/"
    
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    total_count = 0
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Сканируем репозиторий на наличие HTML-файлов
    for file in os.listdir(directory):
        if file.endswith(".html"):
            # Пропускаем технические файлы верификации и админку
            if "yandex_" in file or "google" in file or file == "admin_dashboard.html":
                continue
                
            url_element = ET.SubElement(urlset, "url")
            loc = ET.SubElement(url_element, "loc")
            loc.text = f"{base_url}{file}"
            
            lastmod = ET.SubElement(url_element, "lastmod")
            lastmod.text = current_date
            
            changefreq = ET.SubElement(url_element, "changefreq")
            changefreq.text = "weekly"
            
            priority = ET.SubElement(url_element, "priority")
            priority.text = "1.0" if file == "index.html" else "0.7"
            
            total_count += 1

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="    ", level=0)
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
    
    print(f"Робот GitHub Actions успешно синхронизировал страниц: {total_count}")

if __name__ == "__main__":
    generate_sitemap()
