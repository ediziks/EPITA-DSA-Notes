public class circle
{
    private static final double PI = 3.14159;
    private double radius;

    public circle (double r)
    {
        this.radius = r;
    }

    public double area()
    {

        return PI * radius * radius;
    }

    public double perimeter()
    {

        return 2 * PI * radius;
    }
}



// ###### implemented in class
