
BINARY = stoplight.py

CODE_DIR = stoplight


all:
	@./$(CODE_DIR)/$(BINARY)

debug:
	./.pdb.sh

clean:
	rm -rf $(CODE_DIR)/__pycache__
