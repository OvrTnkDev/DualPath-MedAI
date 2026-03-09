#unzippo i file che sono in data/datazip e li porto in data
import zipfile
import os

def unzip_file(zip_file_path, extract_to_folder):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)
        
if __name__ == "__main__":
    
    #------------------zip1------------------
    zip_file_path = 'data/datazip/archive.zip'  # Percorso del file zip
    extract_to_folder = 'data/clinical'  # Cartella di destinazione per i file estratti
    
    unzip_file(zip_file_path, extract_to_folder)
    print(f"File estratti da {zip_file_path} a {extract_to_folder}")
    
    #------------------zip2------------------
    
    zip_file_path = 'data/datazip/lish-moa.zip'
    extract_to_folder = 'data/moa'
    
    unzip_file(zip_file_path, extract_to_folder)
    print(f"File estratti da {zip_file_path} a {extract_to_folder}")