
BINARY = stoplight.py

CODE_DIR = stoplight


all:
	@python3 $(CODE_DIR)/$(BINARY)

clean:
	rm -rf $(CODE_DIR)/__pycache__
