import java.io.*;
import java.io.IOException;

public class Day3 {
    
    public static void main(String[] args) {
        
        // Output
        System.out.println("Ufff");
        System.out.println("Part 1: " + partOne());
        System.out.println("Part 2: " + partTwo());
    }
    
    /**
     * Yeah this does something, and it does it well and its seems kinda similar
     * to part one but different and we get a result back
     */
    public static int partTwo() {
        int result = 1;
        try {
            MapController mc = new MapController();
            result = result * stepper(mc, 1, 1);
            result = result * stepper(mc, 3, 1);
            result = result * stepper(mc, 5, 1);
            result = result * stepper(mc, 7, 1);
            result = result * stepper(mc, 1, 2);
        } catch (IOException exc) {
            System.out.println("Sorry, cant handle that in part 2 :/");
            exc.printStackTrace();
        }
        return result;
    }
    
    /**
     * We do, this does, something and so we get the result back
     */
    public static int partOne() {
        int result = 0;
        try {
            MapController mc = new MapController();
            result = stepper(mc, 3, 1);
        } catch (IOException exc) {
            System.out.println("Sorry, cant handle that :/");
            exc.printStackTrace();
        }
        return result;
    }
    
    /**
     * Makes step step and gives back an int how man trees he steps
     */
    public static int stepper(MapController mc, int stepX, int stepY) {
        int returnValue = 0;
        int x = 0;
        for (int y = 0; y < mc.height(); y += stepY) {
            if (mc.map(x, y) == "#".toCharArray()[0]) {
                returnValue++;
            }
            x+=stepX;
        }
        return returnValue;
    }
}