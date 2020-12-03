package common

import java.io.File

class InputReader {
    private val basePath = System.getProperty("user.dir") + "/src/main/kotlin"
    private val inputList: List<String>

    constructor(currentDir: String, fileName: String = "input.txt") {
        this.inputList = File(this.basePath + "/" + currentDir + "/" + fileName).readLines()
    }

    fun getInputListString(): List<String> {
        return this.inputList
    }

    fun getInputListInt(): List<Int> {
        return this.inputList.map{ Integer.parseInt(it) }
    }

//    fun getPattern(pattern: Regex): List<Sequence<MatchResult>> {
//        return this.inputList.map{ pattern.findAll(it) }
//    }
}
