sdk_container = sdk_adc

help:
	@echo "    build                      build docker images"
	@echo "    up                         spin up docker images"
	@echo "    stop                       stop docker images"
	@echo "    down                       remove docker images"
	@echo "    start                      Enter to SDK"


build:
	docker-compose down
	docker-compose build --no-cache

up:
	docker-compose up -d
	@echo "All ready, let run make begin"

stop:
	docker-compose stop

down:
	docker-compose down
	@echo "SDK It's down!"

start:
	docker exec -it $(sdk_container) /bin/ash

