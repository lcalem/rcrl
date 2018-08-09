PROJECT_NAME := rcrl
SHARED := $(if $(SHARED_VOLUME), -v $(SHARED_VOLUME):$(SHARED_VOLUME),)


docker:
	docker build -t ${PROJECT_NAME}_dev -f docker/Dockerfile .

test:
	py.test tests/

run:
	docker rm ${PROJECT_NAME}_dev_${USER}
	docker run -it --name ${PROJECT_NAME}_dev_${USER} ${SHARED} -v ${PROJECT_HOME}:/workspace/ -v /var/run/docker.sock:/var/run/docker.sock:ro --entrypoint bash ${PROJECT_NAME}_dev

.PHONY: docker test run