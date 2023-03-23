fun main()
{
    // var names = mutableListOf("Alice", "Bob", "Jane", "Jim", "Julie", "Jeff")
    // var mixedup = mutableListOf(1, 2, "Three", "Four")
    // var listoflists = mutableListOf(mutableListOf(1, 2, 3), mutableListOf(4, 5, 6), mutableListOf(7, 8, 9))

    // add an item to a list
    // names.add("John")

    // remove an item at a given position
    // names.removeAt(3)

    // print a list, print the size of the list
    // println(names)
    // println(names.size)

    // lists can contain mixed types of data
    // println(mixedup)

    // iterate through a list
    /*
    for (name in names)
    {
        println(name)
    }
    */

    // can have a list of lists
    // println(listoflists)
    // println(listoflists[1][2])

    var alice = mutableMapOf("name" to "Alice Jones", "address" to "1 High Street", "id" to 12345)
    var bob = mutableMapOf("name" to "Bob Smith", "address" to "2 Main Road", "id" to 34567)

    println(alice)
    println(alice["address"])
    println(bob["name"])

    var people = mutableListOf(alice, bob)

    println("-------------------------------")
    println(people)
    println("-------------------------------")
    println(people[1]["address"])

    println("-------------------------------")
    var jane = mutableMapOf("name" to "Jane Johnson", "address" to "3 Broad Avenue", "id" to 56789)
    people.add(jane)
    println(people)
}