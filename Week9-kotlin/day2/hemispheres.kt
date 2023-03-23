import java.io.File

fun main()
{
    val infile = File("cities.txt")
    val outfileNE = File("NE.txt")
    val outfileNW = File("NW.txt")
    val outfileSE= File("SE.txt")
    val outfileSW = File("SW.txt")

    var NW = mutableListOf("")
    var SW = mutableListOf("") //neg neg
    var NE = mutableListOf("") //pos pos
    var SE = mutableListOf("")

    outfileNE.writeText("")
    outfileNW.writeText("")
    outfileSE.writeText("")
    outfileSW.writeText("")
    infile.forEachLine()
    {
        var l = it.split(",")

            if((l[1].toFloat() > 0) && (l[2].toFloat() > 0))
            {
                NE.add(l[0])
            }

            if((l[1].toFloat() < 0) && (l[2].toFloat() < 0))
            {
                SW.add(l[0])
            }
            if((l[1].toFloat() > 0) && (l[2].toFloat() < 0))
            {
                NW.add(l[0])
            }
            if((l[1].toFloat() < 0) && (l[2].toFloat() > 0))
            {
                SE.add(l[0])
            }
            
    }
    outfileNE.appendText("$NE")
    outfileNW.appendText("$NW")
    outfileSE.appendText("$SE")
    outfileSW.appendText("$SW")
    
}
