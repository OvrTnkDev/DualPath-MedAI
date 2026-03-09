# 1. Annulla l'ultimo commit che contiene i file pesanti (i file restano intatti sul PC)
git reset --soft HEAD~1

# 2. Rimuovi l'intera cartella data/ dal tracciamento di Git
git rm -r --cached data/

# 3. Crea il file .gitignore e istruiscilo a ignorare la cartella data
echo "data/" > .gitignore

# 4. Rifai il commit pulito e pusha (ora manderà solo il codice e il .gitignore)
git add .
git commit -m "chore: setup ambiente locale e aggiunta .gitignore"
git push origin main