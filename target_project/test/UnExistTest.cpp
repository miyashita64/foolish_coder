/**
 * @file   UnExistTest.cpp
 * @brief  存在しないクラスのテスト
 * @author miyashita64
 */

#include "gtest/gtest.h"

namespace foolish_coder{
    TEST(unexist_class_test, test_create_class)
    {
        int expected = 0;
        ASSERT_EQ(expected, FoolishCoder::start());
    }
}