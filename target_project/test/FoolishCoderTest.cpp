/**
 * @file   FoolishCoderTest.cpp
 * @brief  FoolishCoderのテスト
 * @author miyashita64
 */

#include "gtest/gtest.h"
#include "UnExistFile.h"
#include "UnExistClass.h"

namespace foolish_coder
{
    // 存在しないファイルがincludeされた場合のテスト
    TEST(UnExistFileTest, CreateUnExistFileTest){}

    // 存在しないクラスがインスタンス化された場合のテスト
    TEST(UnExistClassTest, CreateUnExistClassTest)
    {
        UnExistClass obj;
    }

    // 存在しないメソッドが呼び出された場合のテスト
    TEST(UnExistMethodTest, CreateUnExistMethodTest){
        UnExistClass obj;
        obj.unExistMethod();
    }

    // 存在しない0を返すメソッドが呼び出された場合のテスト
    TEST(ReturnValueMethodTest, CreateReturnValueMethodTest){
        UnExistClass obj;
        int acutual = obj.getValue();
        int expected = 0;
        EXPECT_EQ(acutual, expected);
    }
}