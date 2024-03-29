Import java util Scanner;
public class StringComparator {
    public static void main(String[] args) {
        Scanner scanner = new
Scanner(System.in);

    System.out.println("Введите первую строку: ")
    String firstString = scanner.nextLine();
    
    System.out.println("Введите вторую строку: ")
    String secondString = scanner.nextLine();
    
    if (firstString.equals(secondString)) {
        System.out.println("True");
    } else {
        System.out.println("False")
    }
    
    scaner.close();
    }
}