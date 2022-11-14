MAKEFILE_PATH = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
TARGET_PROJECT_PATH = ${MAKEFILE_PATH}/target_project
TARGET_PROJECT_SOURCE_PATH = ${TARGET_PROJECT_PATH}/src
TARGET_PROJECT_TEST_PATH = ${TARGET_PROJECT_PATH}/test
BUILD_SPACE_PATH = ${TARGET_PROJECT_PATH}/build
BUILD_LOG_PATH = ${TARGET_PROJECT_PATH}/logs
EXECUTE_LOG_PATH = ${TARGET_PROJECT_PATH}/results
TIMESTAMP = $(shell date +%Y%m%d%H%M%S)

run:
	@python3 -Bm src

ptest:
	@rm -rf ${BUILD_SPACE_PATH}
	@mkdir -p ${BUILD_SPACE_PATH}
# ifeqにインデントを入れると動かないらしい
ifneq ($(wildcard ${TARGET_PROJECT_SOURCE_PATH}/*), )
	@cp -rp ${TARGET_PROJECT_SOURCE_PATH}/* ${BUILD_SPACE_PATH}
endif
ifneq ($(wildcard ${TARGET_PROJECT_TEST_PATH}/*), )
	@cp -rp ${TARGET_PROJECT_TEST_PATH}/* ${BUILD_SPACE_PATH}
endif
	cd ${BUILD_SPACE_PATH} && cmake ${TARGET_PROJECT_PATH}
	@mkdir -p ${BUILD_LOG_PATH}
	cd ${BUILD_SPACE_PATH} && cmake --build . 2> ${BUILD_LOG_PATH}/${TIMESTAMP}_error.txt
	@mkdir -p ${EXECUTE_LOG_PATH}
	cd ${BUILD_SPACE_PATH} && ./main > ${EXECUTE_LOG_PATH}/${TIMESTAMP}.txt