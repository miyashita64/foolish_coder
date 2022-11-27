# 自身(Makefile)があるディレクトリの絶対パス
MAKEFILE_PATH = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
# FoolishCoderが生成したファイルを格納するパス
FOOLISH_WORK_LINK = ${MAKEFILE_PATH}/results
# FoolishCoderの対象プロジェクトのパス
TARGET_PROJECT_PATH = ${MAKEFILE_PATH}/target_project
# 対象プロジェクトのソースコードのディレクトリパス
TARGET_PROJECT_SOURCE_PATH = ${TARGET_PROJECT_PATH}/src
# 対象プロジェクトのテストコードのディレクトリパス
TARGET_PROJECT_TEST_PATH = ${TARGET_PROJECT_PATH}/test
# FoolishCoderがテストを実行する際にファイルを展開するパス
BUILD_SPACE_PATH = ${TARGET_PROJECT_PATH}/build
# FoolishCoderがビルド・テストのログを格納するパス
BUILD_LOG_PATH = ${TARGET_PROJECT_PATH}/logs
# FoolishCoderが編集後のプロジェクトを実行ログを格納するパス
EXECUTE_LOG_PATH = ${TARGET_PROJECT_PATH}/results
# 実行時刻
TIMESTAMP = $(shell date +%Y%m%d%H%M%S)

run:
	@make ptest || :
	@python3 -Bm src

ptest:
	@rm -rf ${BUILD_SPACE_PATH}
	@mkdir -p ${BUILD_SPACE_PATH}
# ifeqやifneqにインデントを入れると動かないらしい
ifneq ($(wildcard ${TARGET_PROJECT_SOURCE_PATH}/*), )
	@cp -rp ${TARGET_PROJECT_SOURCE_PATH}/* ${BUILD_SPACE_PATH}
endif
ifneq ($(wildcard ${TARGET_PROJECT_TEST_PATH}/*), )
	@cp -rp ${TARGET_PROJECT_TEST_PATH}/* ${BUILD_SPACE_PATH}
endif
ifneq ($(wildcard ${FOOLISH_WORK_LINK}/*), )
	@cp -rp ${FOOLISH_WORK_LINK}/* ${BUILD_SPACE_PATH}
endif
	cd ${BUILD_SPACE_PATH} && cmake ${TARGET_PROJECT_PATH}
	@mkdir -p ${BUILD_LOG_PATH}
	cd ${BUILD_SPACE_PATH} && cmake --build . 2> ${BUILD_LOG_PATH}/${TIMESTAMP}_error.txt
	@mkdir -p ${EXECUTE_LOG_PATH}
	cd ${BUILD_SPACE_PATH} && ./main > ${EXECUTE_LOG_PATH}/${TIMESTAMP}.txt