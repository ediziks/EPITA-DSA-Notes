public class geometry
{
    public static void main(String[] args) {
        circle circ = new circle(25);
        quadrilateral quad = new quadrilateral(7, 11);
        triangle tri = new triangle(5, 7, 6, 9);

        System.out.println("Circle perimeter : " + circ.perimeter() + ". Circle area : " + circ.area());
        System.out.println("Quadrilateral perimeter : " + quad.perimeter() + ". Quadrilateral area : " + quad.area());
        System.out.println("Triangle perimeter : " + tri.perimeter() + ". Triangle area : " + tri.area());

    }
}
