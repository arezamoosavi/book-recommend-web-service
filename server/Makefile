run-locust-locally:
	locust -f crm/loadtests/locustfile.py -P 8090

remove-containers:
	docker container prune -f

localdocker-build:
	docker-compose build
	docker-compose rm -f

localdocker-start:
	docker-compose up --remove-orphans

localdocker-cleanup:
	docker-compose down -v

proddocker-build:
	docker-compose -f prod.yml build
	docker-compose rm -f

proddocker-start:
	docker-compose -f prod.yml up --remove-orphans

proddocker-cleanup:
	docker-compose down -v