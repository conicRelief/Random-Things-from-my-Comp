package com.company;

/**
 * Created by otto on 9/18/15.
 */
public class Board {
    final int width;
    final int height;
    final char[][] configuration;

    public Board(int width, int height)
    {
        this.width = width;
        this.height = height;
        this.configuration = new char[width][height];
        for(int y = 0; y < height; y++)
        {
            for(int x = 0; x<width; x ++)
            {
                configuration[x][y] = '0';
            }
        }
    }

    public void printBoard()
    {
        print("Printing Board");

        for(int y = 0; y < height; y++)
        {
            for(int x = 0; x<width; x ++)
            {
                System.out.print(configuration[x][y]);
            }
            System.out.print("\n");
        }

    }
    public boolean insert(int column, char value)
    {
        for(int y = 0; y<height; y++)
        {
            if (configuration[column][y] == '0')
            {
                configuration[column][y] = value;
                return true;
            }
        }
        return false;
    }
    private void print(String s)
    {
        System.out.println(s);
    }
    public void find_n_in_a_row(int n, int numberOfOpenEnds)
    {
        // Excluding 0
        // Scan x
        // Scan y
        // Scan diag
        // Scans a subset of our master array for n in a row
        // Scan top layer of our board. returns list of different sequences of length n in a row.
        // Scans bottom lay
    }

}
