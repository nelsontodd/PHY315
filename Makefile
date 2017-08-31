#
# == Paths ==
#
VENV_DIR            := .venv

#
# == Commands ==
#
PIP  := $(VENV_DIR)/bin/pip

#
# == Top-Level Targets ==
#

dependencies: python-dependencies

#
# == Dependencies ==
#

$(VENV_DIR):
	virtualenv -p python2  $(VENV_DIR)

python-dependencies: $(VENV_DIR)
	$(PIP) install -r requirements.txt
