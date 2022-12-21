#include "gtest/gtest.h"
#include "DatePicker.h"

namespace foolish_coder{
    TEST(GetLastDayMonthTest, GetLastDayMonthTestCase1){
        DatePicker date_picker;
        EXPECT_EQ(date_picker.getLastDayMonth(0), 0);
    }
}