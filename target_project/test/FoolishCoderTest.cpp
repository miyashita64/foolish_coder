/**
 * @file   FoolishCoderTest.cpp
 * @brief  FoolishCoderのテスト
 * @author miyashita64
 */

#include "gtest/gtest.h"
#include "FoolishCoder.h"

namespace foolish_coder
{
    // 存在しない静的メソッドが実行された場合のテスト
    TEST(FoolishCoderTest, CreateHeaderFileTest)
    {
        int expected = 0;
        FoolishCoder coder;
        coder.start();
    }
}