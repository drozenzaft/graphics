all: run

run: image.py
	python image.py

clean:
	rm picmaker.ppm
