CC = python3
EDIT = vim
ARCHPY = main.py
ARCHKV = main.kv
BUILDER = buildozer
ENT = android
ARCHSPEC = buildozer.spec

run: $(ARCHPY) $(ARCHKV)
	$(CC) $(ARCHPY)

py: $(ARCHPY)
	$(EDIT) $(ARCHPY)

kv: $(ARCHKV)
	$(EDIT) $(ARCHKV)

init: $(ARCHPY) $(ARCHKV)
	$(BUILDER) init

build: $(ARCHPY) $(ARCHKV) $(ARCHSPEC)
	$(BUILDER) $(ENT) debug

delete: $(ARCHSPEC)
	rm -r bin
	rm -f $(ARCHSPEC)
