# 自身(Makefile)があるディレクトリの絶対パス
MAKEFILE_PATH = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
# FoolishCoderが生成したファイルを格納するパス
FOOLISH_WORK_PATH = ${MAKEFILE_PATH}results
# FoolishCoderの対象プロジェクトのパス
TARGET_PROJECT_PATH = ${MAKEFILE_PATH}target_project
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

# リファクタリング用ブランチ名
REFACTORING_BRANCH = refactor
# 自動生成用ブランチ
GENERATE_BRANCH = generate

# 実行時刻
TIMESTAMP = $(shell date +%Y%m%d%H%M%S)

make = make --no-print-directory

run:
# || : で成功したことにして次の処理に移る
	@git switch ${GENERATE_BRANCH}
	@${make} close_log || :
	@python3 -Bm src

merge:
	@git switch ${GENERATE_BRANCH}
	@git add *
	@git commit -m "generate ${TIMESTAMP}"
# リファクタリングブランチを優先する
	@git switch -c ${GENERATE_BRANCH}_ahead_${REFACTORING_BRANCH}
	@git merge ${REFACTORING_BRANCH} || :
	@git checkout --theirs * || :
	@git add *
	@git commit -m "merge ahead ${REFACTORING_BRANCH} ${TIMESTAMP}"
# 自動生成ブランチを優先する
	@git switch ${GENERATE_BRANCH}
	@git switch -c ${GENERATE_BRANCH}_ahead_${GENERATE_BRANCH}
	@git metge ${REFACTORING_BRANCH} || :
	@git checkout --ours * || :
	@git add *
	@git commit -m "merge ahead ${GENERATE_BRANCH} ${TIMESTAMP}"
	@git switch ${GENERATE_BRANCH}

refactor:
	@git branch -D ${REFACTORING_BRANCH}
	@git switch -c ${REFACTORING_BRANCH}

approve:
	@cp ${FOOLISH_WORK_PATH}/* ${TARGET_PROJECT_SOURCE_PATH}
	@git add *
	@git commit -m "refactor ${TIMESTAMP}"
	@git switch ${GENERATE_BRANCH}

test:
	@echo "Running Test ..."
	@${make} build_space
	cd ${BUILD_SPACE_PATH} && cmake ${TARGET_PROJECT_PATH}
	cd ${BUILD_SPACE_PATH} && cmake --build .
	cd ${BUILD_SPACE_PATH} && ./main

close_log:
	@echo "Running Test ..."
	@${make} build_space
	@cd ${BUILD_SPACE_PATH} && cmake ${TARGET_PROJECT_PATH} &> /dev/null
	@mkdir -p ${BUILD_LOG_PATH}
	@cd ${BUILD_SPACE_PATH} && cmake --build . &> ${BUILD_LOG_PATH}/${TIMESTAMP}_error.txt
	@cp ${BUILD_LOG_PATH}/${TIMESTAMP}_error.txt ${BUILD_LOG_PATH}/latest_error.txt
	@mkdir -p ${EXECUTE_LOG_PATH}
	@cd ${BUILD_SPACE_PATH} && ./main &> ${EXECUTE_LOG_PATH}/${TIMESTAMP}.txt

open_log:
	@echo "Running Test ..."
	@${make} build_space
	cd ${BUILD_SPACE_PATH} && cmake ${TARGET_PROJECT_PATH}
	@mkdir -p ${BUILD_LOG_PATH}
	cd ${BUILD_SPACE_PATH} && cmake --build . 2>&1 | tee ${BUILD_LOG_PATH}/${TIMESTAMP}_error.txt
	@cp ${BUILD_LOG_PATH}/${TIMESTAMP}_error.txt ${BUILD_LOG_PATH}/latest_error.txt
	@mkdir -p ${EXECUTE_LOG_PATH}
	cd ${BUILD_SPACE_PATH} && ./main 2>&1 | tee ${EXECUTE_LOG_PATH}/${TIMESTAMP}.txt

clear:
	rm -rf ${BUILD_SPACE_PATH}
	rm -rf ${BUILD_LOG_PATH}
	rm -rf ${EXECUTE_LOG_PATH}
	rm -rf ${FOOLISH_WORK_PATH}/*
	touch ${FOOLISH_WORK_PATH}/.gitkeep

build_space:
	@rm -rf ${BUILD_SPACE_PATH}
	@mkdir -p ${BUILD_SPACE_PATH}
# ifeqやifneqにインデントを入れると動かないらしい
ifneq ($(wildcard ${TARGET_PROJECT_SOURCE_PATH}/*), )
	@cp -rp ${TARGET_PROJECT_SOURCE_PATH}/* ${BUILD_SPACE_PATH}
endif
ifneq ($(wildcard ${TARGET_PROJECT_TEST_PATH}/*), )
	@cp -rp ${TARGET_PROJECT_TEST_PATH}/* ${BUILD_SPACE_PATH}
endif
ifneq ($(wildcard ${FOOLISH_WORK_PATH}/*), )
	@cp -rp ${FOOLISH_WORK_PATH}/* ${BUILD_SPACE_PATH}
endif