import java.io.File

fun main()
{
    val infile = File("infile.txt")

    infile.forEachLine()
    {
        var l = it.split(",")
        println(l)

        for (i in l)
        {
            println(i)
        }
    }

}