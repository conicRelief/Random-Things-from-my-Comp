package com.company;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.List;
import java.util.Scanner;

public class Main {
    // This class was used to test out the various NMM AI's. This process was very messy. But oyu basically get an artifact of it here.

    public static void main(String[] args) {


        NMMBoardSerializer boardSerializer = new NMMBoardSerializer();

        String fileToReadFrom = args[0];
        String fileToWriteTo = args[1];
        Integer depth = Integer.parseInt(args[2]);

        print(fileToReadFrom);
        Scanner sc = null;
        try {
            sc = new Scanner(new File(fileToReadFrom));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        String unprocessedString = sc.next();
        System.out.println("Board Position: " + unprocessedString + ".");

        Triable[] board = boardSerializer.serializedInputStream(unprocessedString);
//        printB(board);

        String miniMaxOpening = decodeBoard(MiniMaxModule.evaluateOpeningForWhite(board, depth));
        //        String miniMaxGame = decodeBoard(MiniMaxModule.evaluateMidGameForWhite(board, depth));
        //        String aBOpening = decodeBoard(MiniMaxModule.evaluateOpeningForWhite(board, depth));
        //        String aBGame = decodeBoard(MiniMaxModule.evaluateOpeningForWhite(board, depth));
        //        String miniMaxOpeningBlack = decodeBoard(MiniMaxModule.evaluateOpeningForBlack(board, depth));
        //        String miniMaxGameBlack = decodeBoard(MiniMaxModule.evaluateMidGameForBlack(board, depth));

            try {
            PrintWriter writer = new PrintWriter(fileToWriteTo);
            writer.write(miniMaxOpening);
            writer.close();

            } catch (FileNotFoundException e) {
            e.printStackTrace();
        }



    }

    public static void printB(Triable[] t)
    {
        System.out.println("Printing:::");
        printBoard(t);
        System.out.println(stringIt(t[20]) + " ------------ " +stringIt(t[21]) + " ------------ " + stringIt(t[22])) ;
        System.out.println(       "| \\            |            / |"        );
        System.out.println(       "|   \\          |          /   |"        );
        System.out.println("|    "   + stringIt(t[17]) + " ------- " +stringIt(t[18]) + " --------" +stringIt(t[19])  +"    | " ) ;
        System.out.println(       "|    |\\        |       / |    |"        );
        System.out.println(       "|    |  \\      |     /   |    |"        );
        System.out.println("|    |    " +stringIt(t[14])+ "--- " +stringIt(t[15]) + " ---"+stringIt(t[16])+"    |    | " ) ;
        System.out.println("|    |    |         |    |    |" ) ;
        System.out.println( stringIt(t[8]) +"----"+stringIt(t[9])+"----" +stringIt(t[10])+ "         "+stringIt(t[11])+"----"+stringIt(t[12])+"----" +  stringIt(t[13])) ;
        System.out.println("|    |    |         |    |    |" ) ;
        System.out.println("|    |    " +stringIt(t[6])+ "---------"+stringIt(t[7])+"    |    | " ) ;
        System.out.println(       "|    |  /            \\   |    |"        );
        System.out.println(       "|    |/                \\ |    |"        );
        System.out.println("|    "   + stringIt(t[3]) + " ------- " +stringIt(t[4]) + " --------" +stringIt(t[5])  +"    | " ) ;
        System.out.println(       "|   /          |          \\   |"        );
        System.out.println(       "| /            |            \\ |"        );
        System.out.println(stringIt(t[0]) + " ------------ " +stringIt(t[1]) + " ------------ " + stringIt(t[2])) ;

    }

    public static Triable[] insertWhite(Triable[] t, int i)
    {
        t[i].makeWhite();
        return t;
    }
    public static Triable[] insertBlack(Triable[] t, int i)
    {
        t[i].makeBlack();
        return t;
    }
    public static String stringIt(Triable t)
    {
        if(t.isNone())
        {
            return "o";
        }
        else if (t.isBlack())
        {
            return "B";
        }
        else if (t.isWhite())
        {
            return  "W";
        }
        else
            return "";
    }

    public static String decodeBoard(Triable[] t)
    {
        String s = "";
        for(Triable x : t)
        {
            if(x.isBlack())
            {
                s+="B";
            }
            else if (x.isWhite())
            {
                s+="W";
            }
            else if (x.isNone())
            {
                s+="x";            }
        }

        return s;
    }

    public static void printBoard(Triable[] t)
    {
       System.out.print("Board Position:");
        for(Triable x : t)
        {
            if(x.isBlack())
            {
                System.out.print("B");
            }
            else if (x.isWhite())
            {
                System.out.print("W");
            }
            else if (x.isNone())
            {
                System.out.print("x");
            }
        }
        System.out.println("");

    }

    public static void print(Object s)
    {
        System.out.println("Print Method Printing: " + s.toString());

    }
    public static void diff(Triable[] t1, Triable[] t2)
    {
    int sum = 0;
    for(int i = 0; i < t1.length ; i++)
    {
        if(t1[i].isWhite() != t2[i].isWhite() && t1[i].isBlack() != t2[i].isBlack() && t1[i].isNone() != t2[i].isNone())
        {       sum = sum+1;}

    }
        System.out.println("Dif boards is " +  sum);
    }


}
