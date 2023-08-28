
public class Main {

	public static void main(String[] args) {

		System.out.println("-----Teste da classe Point-----");

		Point p1 = new Point(1, 1);
		p1.setX(10);
		p1.setY(10);

		Point p2 = new Point(2, 2);
		p2.setX(20);
		p2.setY(20);

		System.out.println("Valores iniciais:");
		System.out.println("P1: x = " + p1.getX() + " y = " + p1.getY());
		System.out.println("P2: x = " + p2.getX() + " y = " + p2.getY());
		System.out.println();

		System.out.println("Movendo pontos:");
		p1.moveBy(1,40);
		System.out.println("P1: x = " + p1.getX() + " y = " + p1.getY());
		// Indo além do permitido
		p2.moveBy(2,400);
		System.out.println("P2: x = " + p2.getX() + " y = " + p2.getY());
		System.out.println();


		System.out.println("-----Teste da classe PointII-----");

		System.out.println("Valores iniciais:");
		PointII point1 = new PointII();
		point1.setX(10);
		point1.setY(20);
		System.out.println("Point1: " + point1);

		PointII point2 = new PointII();
		point2.setX(10);
		point2.setY(20);
		System.out.println("Point2: " + point2);

		PointII point3 = new PointII();
		point3.setX(20);
		point3.setY(30);
		System.out.println("Point3: " + point3);

		PointII point4 = new PointII();
		point4.setX(20);
		point4.setY(301);
		System.out.println("Point4: " + point4);
		System.out.println();

		System.out.println("Comparações:");
		if (point1.equals(point1)) {
			System.out.println("point1 e point1 são iguais.");
		} else {
			System.out.println("point1 e point1 não são iguais.");
		}
		if (point1.equals(point2)) {
			System.out.println("point1 e point2 são iguais.");
		} else {
			System.out.println("point1 e point2 não são iguais.");
		}
		if (point1.equals(point3)) {
			System.out.println("point1 e point3 são iguais.");
		} else {
			System.out.println("point1 e point3 não são iguais.");
		}
		System.out.println();

		System.out.println("ScreenPoint:");
		ScreenPoint screenPoint1 = new ScreenPoint(100, 200);
		System.out.println("ScreenPoint1: " + screenPoint1);
		ScreenPoint screenPoint2 = new ScreenPoint(400, 500);
		System.out.println("ScreenPoint2: " + screenPoint2);

	}

}