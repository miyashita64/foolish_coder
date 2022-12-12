#include "gtest/gtest.h"
#include "FeeCalculator.h"
namespace foolish_coder {
    TEST(GetFeeTest, GetYoungestChildFeeTest){
        FeeCalculator fee_calculator;
        EXPECT_EQ(fee_calculator.getFee(0), 300);}
    TEST(GetFeeTest, GetEldestChildFeeTest){
        FeeCalculator fee_calculator;
        int actual = fee_calculator.getFee(19);
        int expected = 300;
        EXPECT_EQ(actual, expected);}
    TEST(GetFeeTest, GetYoungestAdultFeeTest){
        FeeCalculator fee_calculator;
        EXPECT_EQ(fee_calculator.getFee(20), 500);}
    TEST(GetFeeTest, GetEldestAdultFeeTest){
        FeeCalculator fee_calculator;
        EXPECT_EQ(fee_calculator.getFee(59), 500);}
    TEST(GetFeeTest, GetYoungestOldFeeTest){
        FeeCalculator fee_calculator;
        EXPECT_EQ(fee_calculator.getFee(60), 300);}
    TEST(GetFeeTest, GetEldestOldFeeTest){
        FeeCalculator fee_calculator;
        EXPECT_EQ(fee_calculator.getFee(120), 300);}
    TEST(GetFeeTest, GetTooYoungFeeTest){
        FeeCalculator fee_calculator;
        EXPECT_EQ(fee_calculator.getFee(-1), -1);}
    TEST(GetFeeTest, GetTooOldFeeTest){
        FeeCalculator fee_calculator;
        EXPECT_EQ(fee_calculator.getFee(121), -1);}
}