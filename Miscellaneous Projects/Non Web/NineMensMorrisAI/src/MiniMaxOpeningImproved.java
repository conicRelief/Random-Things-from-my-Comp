import com.company.*;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Created by otto on 10/29/15.
 */
public class MiniMaxOpeningImproved {

    public static void main(String args[])
    {

        NMMBoardSerializer boardSerializer = new NMMBoardSerializer();

        String fileToReadFrom = args[0];
        String fileToWriteTo = args[1];
        Integer depth = Integer.parseInt(args[2]);

        Scanner sc = null;
        try {
            sc = new Scanner(new File(fileToReadFrom));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }


        //Difference in peices and ownership of the board sound like
        Heuristic improvementOnStaticEstimation = new Heuristic() {
            @Override
            public double generateHeuristic(Triable[] t) {



                double whiteNumber = StateSieves.countWhite(t);
                double blackNumber = StateSieves.countBlack(t);
                return whiteNumber/(whiteNumber + blackNumber);
            }};
        BoardWorker.addedHeuristics.add(improvementOnStaticEstimation);


        String unprocessedString = sc.next();

        Triable[] board = boardSerializer.serializedInputStream(unprocessedString);
        String miniMaxGame = decodeBoard(MiniMaxModule.evaluateOpeningForWhite(board, depth));

        System.out.println("Board Position: " +  miniMaxGame + ".");

        try {
            PrintWriter writer = new PrintWriter(fileToWriteTo);
            writer.write(miniMaxGame);
            writer.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }



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
}
