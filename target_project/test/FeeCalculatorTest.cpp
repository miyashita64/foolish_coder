/**
 * @file   Sample1Test.cpp
 * @brief  Sample1のテスト
 * @author miyashita64
 */

#include "gtest/gtest.h"
#include "FeeCalculator.h"

namespace foolish_coder
{
    /*
    ＜想定＞
    料金計算機クラスFeeCalculatorに、
    入力された年齢によって利用料金を出力する
    メンバ関数calcFee()を追加する。

    料金設定は以下の通りである。
     0歳- 12歳:   0円
    13歳- 18歳: 500円
    19歳- 59歳: 800円
    60歳-120歳: 500円
    それ以外の数値: -1

    1. テストケースを1つだけ追加する
    2. $ make test でテストに失敗することを確認する
    3. results/ 下にファイルを追加、もしくは、修正する
    4. $ make test でテストを通過することを確認する
    5. 気になるところがある場合
        5.1. リファクタリングする
        5.2. $ make test でテストを通過することを確認する
        5.3. 再度気になる点がある場合は5.1に戻る
    6. $ make approve を実行する
    7. 想定のプログラムが完成したと思うまで、1-6を繰り返す

    // テストケースのサンプル
    TEST(CalcFeeTest, CalcFeeBy1OldTest){  // (テスト名, テストケース名(※一意))
        FeeCalculator feeCalculator;            // インスタンス化
        int acutual = feeCalculator.calcFee(1); // 算出値
        int expected = 0;   // 期待出力
        EXPECT_EQ(acutual, expected);   // 算出値と期待出力が等しいか判定する
    }
    */

   TEST(CalcFeeTest, CalcFeeBy0OldTest){  // (テスト名, テストケース名(※一意))
        FeeCalculator feeCalculator;            // インスタンス化
        int acutual = feeCalculator.calcFee(0); // 算出値
        int expected = 0;   // 期待出力
        EXPECT_EQ(acutual, expected);   // 算出値と期待出力が等しいか判定する
    }

   TEST(CalcFeeTest, CalcFeeBy13OldTest){  // (テスト名, テストケース名(※一意))
        FeeCalculator feeCalculator;            // インスタンス化
        int acutual = feeCalculator.calcFee(13); // 算出値
        int expected = 500;   // 期待出力
        EXPECT_EQ(acutual, expected);   // 算出値と期待出力が等しいか判定する
    }

   TEST(CalcFeeTest, CalcFeeBy19OldTest){  // (テスト名, テストケース名(※一意))
        FeeCalculator feeCalculator;            // インスタンス化
        int acutual = feeCalculator.calcFee(19); // 算出値
        int expected = 800;   // 期待出力
        EXPECT_EQ(acutual, expected);   // 算出値と期待出力が等しいか判定する
    }

   TEST(CalcFeeTest, CalcFeeBy60OldTest){  // (テスト名, テストケース名(※一意))
        FeeCalculator feeCalculator;            // インスタンス化
        int acutual = feeCalculator.calcFee(60); // 算出値
        int expected = 500;   // 期待出力
        EXPECT_EQ(acutual, expected);   // 算出値と期待出力が等しいか判定する
    }
}