import java.io.FileReader;
import java.io.IOException;

class MapController{
    private char[][] mapData;
    
    public MapController() throws IOException {
        this.mapData = new char[323][31];
        FileReader io = new FileReader("input.txt");
        for (int y = 0; y < this.mapData.length; y++){            
            for (int x = 0; x < this.mapData[y].length; x++) {
                char c = (char) io.read();
                if (String.valueOf(c).contains("\n")) {
                    c = (char) io.read();
                }
                this.mapData[y][x] = c;
            }   
        }
    }
    
    
    
    /**
     * Gives back the map data on a specific location
     */
    public char map(int x, int y) {
        int width = this.mapData[y].length;
        while (x >= width) {
            x -= width;
        }
        char r = this.mapData[y][x];
        return r;
    }
    
    /**
     * Returns the height of the map, this is the maximum you can go
     */
    public int height() {
        return this.mapData.length;
    }
    
}