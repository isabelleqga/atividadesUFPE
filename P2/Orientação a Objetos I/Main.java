
public class Main {

	public static void main(String[] args) {
		Point p1 = new Point(1, 1);
		Point p2 = new Point(2, 2);

		p1.setX(10);
		p1.setY(10);

		p2.setX(20);
		p2.setY(20);

		System.out.println();
		System.out.println("P1");
		System.out.println(p1.getX());
		System.out.println(p1.getY());
		System.out.println("P2");
		System.out.println(p2.getX());
		System.out.println(p2.getY());

		p1.moveBy(1,40);
		p2.moveBy(2,80);

		System.out.println();
		System.out.println("P1");
		System.out.println(p1.getX());
		System.out.println(p1.getY());
		System.out.println("P2");
		System.out.println(p2.getX());
		System.out.println(p2.getY());

	}

}