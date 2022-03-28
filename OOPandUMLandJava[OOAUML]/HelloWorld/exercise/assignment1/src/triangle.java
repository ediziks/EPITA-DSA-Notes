public class triangle
{
    private double side_a;
    private double side_b;
    private double height;
    private double base;

    public triangle (double h, double base, double a, double b)
    {

        this.height = h;
        this.base = base;
        this.side_a = a;
        this.side_b = b;

    }

    public double area()
    {
        return base * height * 0.5;
    }

    public double perimeter()
    {
        return side_a + side_b + base;
    }
}
