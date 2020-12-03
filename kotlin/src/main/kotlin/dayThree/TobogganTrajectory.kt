package dayThree

import common.InputReader

class TobogganTrajectory {
    private val treeMap = InputReader("dayThree").getInputListString()

    fun treesHit(stepsRight: Int, stepsDown: Int): Int {
        var hits: Int = 0
        var rowNumber: Int = 0
        var colNumber: Int = 0

        for (line in this.treeMap) {
            if (rowNumber % stepsDown != 0) {
                rowNumber += 1
                continue
            }

            colNumber = (rowNumber * stepsRight) % line.length

            if (line[colNumber] == '#')
                hits += 1

            rowNumber += 1
        }

        return hits
    }

}


fun main() {
    val treeChecker = TobogganTrajectory()
    val answer1 = treeChecker.treesHit(3, 1)
    val answer2 = treeChecker.treesHit(1, 1) * treeChecker.treesHit(3, 1) *
            treeChecker.treesHit(5, 1) *  treeChecker.treesHit(7, 1) *
            treeChecker.treesHit(1, 2)

    println("Answer 1: $answer1")
    println("Answer 2: $answer2")
}