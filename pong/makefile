CC = python
EDIT = vim
ARCHPY = main.py
ARCHKV = pong.kv
BUILDER = buildozer
ENT = android
ARCHSPEC = *.spec

run: $(ARCHPY) $(ARCHKV)
	$(CC) $(ARCHPY)
py: $(ARCHPY)
	$(EDIT) $(ARCHPY)
kv: $(ARCHKV)
	$(EDIT) $(ARCHKV)
build: $(ARCHPY) $(ARCHKV) $(ARCHSPEC)
	$(BUILDER) $(ENT) debug
