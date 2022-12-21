#include "gtest/gtest.h"
#include "FeeCalculator.h"

namespace foolish_coder{
    TEST(CalcFeeTest, CalcFeeTestCase1){
        FeeCalculator fee_calculator;
        EXPECT_EQ(fee_calculator.calcFee(0), 0);
    }
}