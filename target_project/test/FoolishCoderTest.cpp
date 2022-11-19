/**
 * @file   UnExistTest.cpp
 * @brief  存在しないクラスのテスト
 * @author miyashita64
 */

#include "gtest/gtest.h"
#include "FoolishCoder.h"

namespace foolish_coder
{
    TEST(FoolishCoderTest, CreateHeaderFileTest)
    {
        int expected = 0;
        ASSERT_EQ(expected, FoolishCoder::start());
    }
}