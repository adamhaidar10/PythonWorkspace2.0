fun main()
{
    var s:String = "jackdaws love my 100 big sphinxes of quartz"

    // get the length of a string
    println(s.length)

    // get the character at a certain position
    // println(s[6])

    // iterate through thr characters of a string version 1
    // for (i in 0..s.length - 1)
    // {
    //     println(s[i])
    // }


    // iterate throguh the characters of a string version 2
    // for (c in s)
    // {
    //     // checking if the characters are letters or digits
    //     println("$c : ${c.isLetter()} : ${c.isDigit()}")
    // }

    // get an extract of a string
    println(s.subSequence(25..32))

}

