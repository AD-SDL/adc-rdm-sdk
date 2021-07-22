help:
	@echo "    install                   install all necesary things "
	@echo "    Create                	 make virtual enviroment "
	@echo "    start                     let you in the cli "


install:
	brew install python3
	brew install virtualenv

create:
	virtualenv sdk/adc

