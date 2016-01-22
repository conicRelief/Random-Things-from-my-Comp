import com.company.AlphaBetaModule;
import com.company.MiniMaxModule;
import com.company.NMMBoardSerializer;
import com.company.Triable;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Created by otto on 10/29/15.
 */
public class ABOPening {
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
        String unprocessedString = sc.next();

        Triable[] board = boardSerializer.serializedInputStream(unprocessedString);
        String aBOpening = decodeBoard(AlphaBetaModule.evaluateOpeningForWhite(board, depth));

        System.out.println("Board Position: " +  aBOpening + ".");

        try {
            PrintWriter writer = new PrintWriter(fileToWriteTo);
            writer.write(aBOpening);
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
