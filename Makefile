TARGET_PROJECT_PATH = target_project
TARGET_PROJECT_SOURCE_PATH = ${TARGET_PROJECT_PATH}/src
TARGET_PROJECT_TEST_PATH = ${TARGET_PROJECT_PATH}/test
BUILD_SPACE_PATH = ${TARGET_PROJECT_PATH}/build

run:
	@mkdir -p build
	cd build && cmake .. && cmake --build . && ./main
	@rm -rf build

target_test:
	@rm -rf ${BUILD_SPACE_PATH}
	@mkdir -p ${BUILD_SPACE_PATH}
	@cp -rp ${TARGET_PROJECT_SOURCE_PATH}/* ${BUILD_SPACE_PATH}
	@cp -rp ${TARGET_PROJECT_TEST_PATH}/* ${BUILD_SPACE_PATH}
	cd ${BUILD_SPACE_PATH} && cmake .. && cmake --build . && ./main
	@rm -rf ${BUILD_SPACE_PATH}