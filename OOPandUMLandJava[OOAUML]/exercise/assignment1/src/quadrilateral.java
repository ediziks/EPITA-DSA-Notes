public class quadrilateral
{
    private double height;
    private double width;

    public quadrilateral (double h, double w)
    {
        this.height = h;
        this.width = w;
    }

    public double area()
    {
        return height * width;
    }

    public double perimeter(){
        return 2 * (height + width);
    }
}
