fun main()
{
    var s:String
    
    for (i in 1..105)
    {
        s = ""
        if (i % 3 == 0)
        {
            s += "Fizz"
        }
        if (i % 5 == 0)
        {
            s += "Buzz"
        }
        if (i % 7 == 0)
        {
            s += "Meow"
        }
        if (s == "")
        {
            s += "$i"
        }
        println(s)
    }
}