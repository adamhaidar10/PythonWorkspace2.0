import java.io.File

fun main()
{
    val infile = File("airports.txt")
    val outfile = File("output.txt")

    outfile.writeText("")
    infile.forEachLine()
    {
        println(it)
        outfile.appendText("$it\n")
    }
}