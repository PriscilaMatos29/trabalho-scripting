#!/bin/bash

echo "A organizar ficheiros..."

mkdir -p imagens documentos outros

for file in *; do
    if [[ -f "$file" ]]; then
        case "$file" in
            *.jpg|*.png)
                mv "$file" imagens/
                ;;
            *.txt|*.pdf)
                mv "$file" documentos/
                ;;
            *)
                mv "$file" outros/
                ;;
        esac
    fi
done

echo "Organização concluída!"