package fr.epita.geometry.launcher;

import fr.epita.geometry.datamodel.triangle;

public class Launcher {
    public static void main (String[] args) {
        Triangle t1 = new Triangle(sideA:20, sideb:30, height:25, base:10);

        Circle c1 = new Circle(radius 20);

        Square s1 = new Square(side 10);

        doble area = 0.0;
        for (Shape shape : shapes){
            System.out.println(shape.calculatePerimeter());
            System.out.println(shape.calculateArea());
            area += shape.calculateArea();
        }
        System.out.println("Global Area: ", area);

//        for loop replaced these
//        System.out.println(t1.calculatePerimeter());
//        System.out.println(c1.calculatePerimeter());
//        System.out.println(s1.calculatePerimeter());
//
//        System.out.println(t1.calculateArea());
//        System.out.println(c1.calculateArea());
//        System.out.println(s1.calculateArea());
    }
}