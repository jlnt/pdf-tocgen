all: b2-alg-coverandinside-toc.pdf a2-alg-coverandinside-toc.pdf

clean:
	rm -f *_meta.txt *_bookmark.txt *-toc.pdf

b2-alg-coverandinside_meta.txt:   b2-alg-coverandinside.pdf
	pdftk b2-alg-coverandinside.pdf dump_data output b2-alg-coverandinside_meta.txt

b2-alg-coverandinside_bookmark.txt: b2-alg-coverandinside.txt
	./generate_toc.py -f b2-alg-coverandinside.txt -o 28 > b2-alg-coverandinside_bookmark.txt

b2-alg-coverandinside-toc.pdf: b2-alg-coverandinside_meta.txt b2-alg-coverandinside_bookmark.txt
	cat b2-alg-coverandinside_meta.txt b2-alg-coverandinside_bookmark.txt |\
	pdftk b2-alg-coverandinside.pdf update_info - output b2-alg-coverandinside-toc.pdf

a2-alg-coverandinside_meta.txt:   a2-alg-coverandinside.pdf
	pdftk a2-alg-coverandinside.pdf dump_data output a2-alg-coverandinside_meta.txt

a2-alg-coverandinside_bookmark.txt: a2-alg-coverandinside.txt
	./generate_toc.py -f a2-alg-coverandinside.txt -o 30 > a2-alg-coverandinside_bookmark.txt

a2-alg-coverandinside-toc.pdf: a2-alg-coverandinside_meta.txt a2-alg-coverandinside_bookmark.txt
	cat a2-alg-coverandinside_meta.txt a2-alg-coverandinside_bookmark.txt |\
	pdftk a2-alg-coverandinside.pdf update_info - output a2-alg-coverandinside-toc.pdf
