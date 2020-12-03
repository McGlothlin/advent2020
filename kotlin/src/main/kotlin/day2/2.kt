package day2

import common.InputReader
import kotlin.text.Regex

class PasswordChecker {
    private val passwordList = InputReader("day2")
        .getInputListString()
        .map { Regex("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)").find(it) }
        .map { it!!.destructured }

    fun checkCharCount(): Int {
        val valid: MutableList<String> = mutableListOf()
        var charCount: Int
        for ((start, end, character, password) in this.passwordList) {
            charCount = password.filter { it == character.single() }.count()
            if (Integer.parseInt(start) <= charCount && charCount <= Integer.parseInt(end)) {
                valid.add(password)
            }
        }
        return valid.size
    }


    fun checkCharPlacement(): Int {
        val valid: MutableList<String> = mutableListOf()
        for ((position1, position2, character, password) in this.passwordList) {
            if ((password[getPosition(position1)] == character.single())
                            .xor(password[getPosition(position2)] == character.single())) {
                valid.add(password)
            }

        }
        return valid.size
    }


    private fun getPosition(position: String): Int {
        return Integer.parseInt(position) - 1
    }

}


fun main() {
    val checker = PasswordChecker()
    val answer1 = checker.checkCharCount()
    val answer2 = checker.checkCharPlacement()

    println("Answer 1: $answer1")
    println("Answer 2: $answer2")
}