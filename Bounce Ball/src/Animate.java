public class Animate implements Runnable {

    GameWindowPanel gp;
    Animate(GameWindowPanel g){
        gp = g;
    }
    public void run(){
        while(true){
            gp.update();
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
    }
}
