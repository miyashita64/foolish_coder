/**
 * @file   Sample1Test.cpp
 * @brief  Sample1のテスト
 * @author miyashita64
 */

#include "gtest/gtest.h"
#include "FeeCalculator.h"

namespace foolish_coder
{
    /* テストケースのサンプル
    TEST(IsMinusTest, IsMinusTrueTest){
        Judge judge;                            // インスタンス化
        bool acutual = judge.isMinus(-1);       // 算出値
        bool expected = True;                   // 期待出力
        EXPECT_EQ(acutual, expected);           // アサーション(算出値と期待出力が等しいか判定する)
    }
    */

    TEST(GetFeeTest, GetYoungestChildFeeTest){
        FeeCalculator fee_calculator;
        int acutual = fee_calculator.getFee(0);
        int expected = 0;
        EXPECT_EQ(acutual, expected);
    }

    // TEST(GetFeeTest, GetEldestChildFeeTest){
    //     FeeCalculator fee_calculator;
    //     int acutual = fee_calculator.getFee(12);
    //     int expected = 0;
    //     EXPECT_EQ(acutual, expected);
    // }

    // TEST(GetFeeTest, GetYoungestYouthFeeTest){
    //     FeeCalculator fee_calculator;
    //     int acutual = fee_calculator.getFee(13);
    //     int expected = 300;
    //     EXPECT_EQ(acutual, expected);
    // }

    // TEST(GetFeeTest, GetEldestYouthFeeTest){
    //     FeeCalculator fee_calculator;
    //     int acutual = fee_calculator.getFee(19);
    //     int expected = 300;
    //     EXPECT_EQ(acutual, expected);
    // }

    // TEST(GetFeeTest, GetYoungestAdultFeeTest){
    //     FeeCalculator fee_calculator;
    //     int acutual = fee_calculator.getFee(20);
    //     int expected = 500;
    //     EXPECT_EQ(acutual, expected);
    // }

    // TEST(GetFeeTest, GetEldestAdultFeeTest){
    //     FeeCalculator fee_calculator;
    //     int acutual = fee_calculator.getFee(59);
    //     int expected = 500;
    //     EXPECT_EQ(acutual, expected);
    // }

    // TEST(GetFeeTest, GetYoungestOldFeeTest){
    //     FeeCalculator fee_calculator;
    //     int acutual = fee_calculator.getFee(60);
    //     int expected = 300;
    //     EXPECT_EQ(acutual, expected);
    // }

    // TEST(GetFeeTest, GetEldestOldFeeTest){
    //     FeeCalculator fee_calculator;
    //     int acutual = fee_calculator.getFee(120);
    //     int expected = 300;
    //     EXPECT_EQ(acutual, expected);
    // }

    // TEST(GetFeeTest, GetTooYoungFeeTest){
    //     FeeCalculator fee_calculator;
    //     int acutual = fee_calculator.getFee(-1);
    //     int expected = -1;
    //     EXPECT_EQ(acutual, expected);
    // }

    // TEST(GetFeeTest, GetTooOldFeeTest){
    //     FeeCalculator fee_calculator;
    //     int acutual = fee_calculator.getFee(121);
    //     int expected = -1;
    //     EXPECT_EQ(acutual, expected);
    // }
}