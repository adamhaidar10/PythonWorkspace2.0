enum class FuelType
{
    PETROL,
    ELECTRIC,
    DIESEL,
    HYBRID,
    STEAM,
    FUSION,
    FOOT
}



enum class FareClass
{
    CHILD,
    ADULT,
    SENIOR
}



data class Passenger(val name : String, val destination : String, val fareclass : FareClass)



abstract class VehicleClass (var make: String, var model: String, var colour: String, var year: Int, var fueltype: FuelType)
{
    private var speed: Int
   
    init
    {
        println("Vehicle is created")
        this.speed = 0
    }

    fun getSpeed() : String
    {
        return "The current speed is ${this.speed}"
    }

    open fun start()
    {
        println("Vehicle is started")
    }

    fun stop()
    {
        println("Vehicle is stopped")
        this.speed = 0
    }

    fun accelerate()
    {
        println("Accelerating")
        this.speed += 5
    }

    fun brake()
    {
        println("Braking")
        this.speed -= 5
    }
}



class CarClass (make: String, model: String, colour: String, year: Int, fueltype: FuelType): VehicleClass(make, model, colour, year, fueltype)
{
}



class TruckClass (make: String, model: String, colour: String, year: Int, fueltype: FuelType): VehicleClass(make, model, colour, year, fueltype)
{
}



class BusClass (make: String, model: String, colour: String, year: Int, fueltype: FuelType): VehicleClass(make, model, colour, year, fueltype)
{
    private var passengers : Int
    private var passengerList : MutableList<Passenger>

    init
    {
        this.passengers = 0
        this.passengerList = mutableListOf<Passenger>()
    }

    fun pickUpPassenger(passengerName : Passenger)
    {
        this.passengers += 1
        this.passengerList.add(passengerName)
    }

    fun dropOffPassenger()
    {
        this.passengers -= 1
    }

    fun getPassengers() : Int
    {
        return this.passengers
    }

    fun getPassengerList() : List<Passenger>
    {
        return this.passengerList
    }

    override fun start()
    {
        println("Bus is started")
    }
}



fun main()
{
    //var c1 = CarClass("Ford", "Fiesta", "Red", 2008, "Petrol")
    //var c2 = CarClass("Volkswagen", "Golf", "Black", 2009, "Petrol")

    //var t1 = TruckClass("Mercedes", "Truck1", "Green", 2011, "Petrol")

    var b1 = BusClass("BusCo", "Bus1", "Red", 2020, FuelType.ELECTRIC)

    b1.start()
    b1.pickUpPassenger(Passenger("Alice", "Woking", FareClass.ADULT))
    b1.pickUpPassenger(Passenger("Bob", "Romsey", FareClass.SENIOR))
    b1.pickUpPassenger(Passenger("Jane", "Winchester", FareClass.ADULT))
    b1.pickUpPassenger(Passenger("Jeff", "Southampton", FareClass.ADULT))
    b1.pickUpPassenger(Passenger("Jim", "Southampton", FareClass.CHILD))

    var p1 = Passenger("Joe", "Bournemouth", FareClass.ADULT)
    b1.pickUpPassenger(p1)

    println(b1.getPassengers())
    println(b1.getPassengerList())

    b1.dropOffPassenger()
    b1.dropOffPassenger()
    b1.dropOffPassenger()

    println(b1.getPassengers())


    // println(b1.fueltype)

    /*
    println(c1)
    println(c2)

    println(c1.make)
    println(c2.colour)

    println(t1.year)
    println(b1.fueltype)

    c1.start()
    c1.accelerate()
    c1.accelerate()
    c1.accelerate()
    println(c1.getSpeed())    
    c1.stop()
    println(c1.getSpeed())        
    */
}