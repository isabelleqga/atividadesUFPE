public class Point {

    // (2) Data hiding
    private int x, y;

    // (1) Construtor Point(x,y)
    public Point(int x, int y) {
	// (3) Integridade do valor de x e y
	if (x >= 0 && x <= 400 && y >= 0 && y <= 400) {
		this.x = x;
		this.y = y;
	} else {
		System.out.println("Os valores de x e y devem estar entre 0 e 400.");
	}
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        // (3) Integridade do valor de X
        if (x >= 0 && x <= 400) {
            this.x = x;
        } else {
            System.out.println("O valor de x deve estar entre 0 e 400.");
        }
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        // (3) Integridade do valor de Y
        if (y >= 0 && y <= 400) {
            this.y = y;
        } else {
            System.out.println("O valor de y deve estar entre 0 e 400.");
        }
    }

    public void moveBy(int dx, int dy) {
        int newX = getX() + dx;
        int newY = getY() + dy;

        // (3) Verifica se os novos valores estão dentro 
        // dos limites antes de atualizar as coordenadas
        if (newX >= 0 && newX <= 400 && newY >= 0 && newY <= 400) {
            setX(newX);
            setY(newY);
        } else {
            System.out.println("A operação moveBy resultaria em coordenadas fora dos limites.");
        }
    }
}