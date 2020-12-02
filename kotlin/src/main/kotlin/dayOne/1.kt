package dayOne
import java.io.File

class ExpenseReport {
    private val fileName = System.getProperty("user.dir") + "/src/main/kotlin/dayOne/input.txt"
    private val expenseList: List<Int> = File(fileName).readLines().map { Integer.parseInt(it) }


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