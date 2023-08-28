import java.util.Objects;
public class PointII {
    public int x = 0, y = 0;
    public int getX() { return x; }
    public int getY() { return y; }

    public void setX(int x) {
        if (validateCoordinate(x)){
            this.x = x;
        }
    }
    public void setY(int y) {
        if (validateCoordinate(y)){
            this.y = y;
        }
    }

    public void moveBy(int dx, int dy) {
        setX(getX() + dx);
        setY(getY() + dy);
    }

    // (1) Sobrescrever o método equals
    @Override
    public boolean equals(Object o) {
        // Se é nulo ou não tem a mesma classe
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        PointII point = (PointII) o;
        // Se as coordenadas são iguais
        if (x == point.x && y == point.y) {
            return true;
        } else {
            return false;
        }
    }
    // Precisa sobrescrever hashCode pra equals funcionar
    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    // (2) Sobrescrever o método toString
    @Override
    public String toString() {
        return "Point { " + "x = " + x + ", y = " + y + " }";
    }

    // Usado em PointII e em ScreenPoint através do set
    private boolean validateCoordinate(int number) {
        if (!(number >= 0 && number <= 300)) {
            System.out.println("Ponto " + number + " inválido. Os valores de x e y devem estar entre 0 e 300.");
            return false;
        } else {
            return true;
        }
    }
}

// (3) Subclasse chamada ScreenPoint
class ScreenPoint extends PointII {
    public ScreenPoint(int x, int y) {
        super();
        setX(x);
        setY(y);
    }

}