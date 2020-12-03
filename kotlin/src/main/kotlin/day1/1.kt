package day1

import common.InputReader

class ExpenseReport {
    private val reader = InputReader("day1")
    private val expenseList = reader.getInputListInt()


    fun getProduct(): Int? {
        for (multiplicand in expenseList) {
            for (multiplier in expenseList) {
                if (multiplicand + multiplier == 2020) {
                    return multiplicand * multiplier
                }
            }
        }
        return null
    }


    fun getProductPart2(): Int? {
        for (first in expenseList) {
            for (second in expenseList) {
                for (third in expenseList) {
                    if (first + second + third == 2020) {
                        return first * second * third
                    }
                }
            }
        }
        return null
    }

}


fun main() {
    val report = ExpenseReport()
    val answer1 = report.getProduct()
    val answer2 = report.getProductPart2()

    println("Answer 1: $answer1")
    println("Answer 2: $answer2")
}