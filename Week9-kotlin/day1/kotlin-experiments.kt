fun main()
{
    // val is an immutable variable
    // var is a mutable variable
    // var n: Int
    // val x: Int

    // operators
    // + = * / % Math.pow(x, y)
    // < > <= >= == !=
    // && || 


    // readLine() reads something from user
    // val s: String = readLine()

    // for loop
    // for (i in 1..10)
    // {
    //     println(i)
    // }

    // while loop
    // loop might not run at all if condition starts as false
    // n = 10
    // while (n > 3)
    // {
    //     println(n)
    //     n -= 1
    // }
    

    // do loop
    // always runs at least once because the condition is only checked at the end
    // n = 3
    // do
    // {
    //     println(n)
    //     n -= 1
    // }
    // while (n > 3)
    
    // n = 70
        
    // var s:String = if (n > 100) ">100" else "else"
    // var s:String
    // when (n)
    // {
    //     in 50..10 -> s = ">50"
    //     in 0..50 -> s = "<50"
    //     else -> s = "else"
    // }

    //  var s:String = when (n)
    // {
    //     in 50..10 -> ">50"
    //     in 0..75 -> "<50"
    //     else -> "else" // when statements must be exhaustive - cover all possible values
    // }

    var s1:String
    var s2:String
    s1 = "Hello"
    s2 = "Earth"

    println(s1.compareTo(s2))
    println("$s1 $s2")

    println(s1 + s2)
    println("The end")
    
}