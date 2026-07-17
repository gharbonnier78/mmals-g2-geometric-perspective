.PHONY: pdf test clean archive
pdf:
	mkdir -p dist
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
	cp paper/main.pdf dist/MMALS_G2_Geometric_Perspective_v0.2_Internal.pdf

test:
	python -m pytest -q

clean:
	cd paper && latexmk -C || true
	rm -f dist/*.pdf

archive: pdf test
	@echo "Internal snapshot ready for a private Git tag: v0.2-internal"
