import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Game Windows");

        GameWindowPanel panel = new GameWindowPanel();

        frame.getContentPane().add(panel);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setVisible(true);
        frame.setSize(490, 600);

        frame.setResizable(false);
    }
}
