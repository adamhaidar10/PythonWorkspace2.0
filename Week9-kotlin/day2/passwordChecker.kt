import java.io.File
fun main()
{
    filteringFile("passwords.txt", "validPasswords.txt")
}
fun filteringFile(infileName:String, outfileName:String): Unit{
    val infile = File(infileName)
    val outfile = File(outfileName)

    outfile.writeText("")

    infile.forEachLine()
    {
        var hasAnUpper = false ; var hasALower = false ; var hasADigit = false


        for(character in it){
            when{
                character.isUpperCase() == true -> hasAnUpper = true
                character.isLowerCase() == true -> hasALower = true
                character.isDigit() == true -> hasADigit = true
                else -> continue
            }
        }

        if(hasAnUpper == true && hasALower == true && hasADigit == true && it.length >= 8) outfile.appendText("$it : is a valid password\n")
    }
}