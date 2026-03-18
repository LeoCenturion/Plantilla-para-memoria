# Makefile for LaTeX compilation

# Define the main LaTeX file (without the .tex extension)
MAIN_FILE = memorianueva

# Default target: running "make" will execute this
all: $(MAIN_FILE).pdf

# Rule to generate the PDF
# This runs pdflatex, then bibtex, and then pdflatex twice more
# to ensure all references and cross-references are correct.
$(MAIN_FILE).pdf: $(MAIN_FILE).tex references.bib Chapters/*.tex portada.tex
	pdflatex $(MAIN_FILE).tex
	bibtex $(MAIN_FILE).aux
	pdflatex $(MAIN_FILE).tex
	pdflatex $(MAIN_FILE).tex

# Clean target: running "make clean" will remove generated files
clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.pdf

# Phony targets don't represent actual files
.PHONY: all clean
