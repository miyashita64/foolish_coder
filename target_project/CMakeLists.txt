# 参考 https://zenn.dev/pictogram/scraps/aa1bfe72c9e6d6
cmake_minimum_required(VERSION 3.10)

# プロジェクト名と使用言語を設定
project(FoolishCoder CXX)

# GTestパッケージを利用可能にする
find_package(GTest REQUIRED)

# 対象とするファイルのパスを設定する
set(BUILD_SPACE_PATH build)
file(GLOB TARGET_HEADER_FILES ${BUILD_SPACE_PATH}/*.h)
file(GLOB TARGET_SOURCE_AND_TEST_FILES ${BUILD_SPACE_PATH}/*.cpp)

add_executable(
	main
	${TARGET_HEADER_FILES}
	${TARGET_SOURCE_AND_TEST_FILES}
)

target_link_libraries(
	main
    # リンクするライブラリにGtestを追加 (これでMainを書かなくてもテストが動くようです。)
	GTest::Main
)