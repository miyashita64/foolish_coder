/**
 * @file target.cpp
 * @author miyashita64
 * @brief 構文解析対象プログラム
 * @version 0.1
 * @date 2022-11-26
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <stdio.h>

int main(void){
    int current_num = 1;
    int prev_num = 0;
    int next_num = 1;

    for (int i = 0; i < 100; i++){
        printf("%d,", current_num);
        next_num = current_num + prev_num;
        prev_num = current_num;
        current_num = next_num;
    }
    printf("\n");
    return 0;
}