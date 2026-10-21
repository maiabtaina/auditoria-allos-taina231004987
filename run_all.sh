#!/bin/sh
cd codigo && python3 01_gerar_base.py && python3 02_testes_auditoria.py && python3 03_gerar_planilhas.py && python3 04_gerar_dossie_pdf.py
