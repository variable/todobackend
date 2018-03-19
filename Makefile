include Makefile.settings
init:
	${INFO} "Starting database container ..."
	@ docker-compose up -d db
	@ sleep 5
	${INFO} "Creating todobackend database ..."
	@ docker exec todobackend_db mysql -uroot -e "create database todobackend"
	${INFO} "Initial migration ..."
	@ docker-compose run migrate
