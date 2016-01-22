package com.company;

/**
 * Created by otto on 10/24/15.
 */
public class NMMBoardSerializer<T> {
    char black_representation = 'b';
    char white_representation = 'w';
    char empty_representation  = 'e';
    int boardSize = 23;

    public NMMBoardSerializer() {}
    public NMMBoardSerializer(int boardSize)
    {
        this.boardSize = boardSize;
    }
    public NMMBoardSerializer(char b, char w, char e)
    {
        this.black_representation = b;
        this.white_representation = w;
        this.empty_representation = e;
    }
    public NMMBoardSerializer(int boardSize, char b, char w, char e)
    {
        this(b,w,e);
        this.boardSize = boardSize;
    }

    public MorrisTernary[] serializedInputStream(String s)
    {
        return serializedInputStream(s, 'b', 'w', 'x');
    }

    public MorrisTernary[] serializedInputStream(String s, char black, char white, char empty)
    {
//        System.out.println(s.toLowerCase());
        char[] stringAsChar = s.toLowerCase().toCharArray();        s = null;
        MorrisTernary[] boardState = new MorrisTernary[stringAsChar.length];
        if(stringAsChar.length == boardSize)
        {
                for(int i = 0; i < boardState.length; i++)
                {
                    boardState[i] = new MorrisTernary();
                    if (stringAsChar[i] == empty) {
                        boardState[i].makeEmpty();

                    } else if (stringAsChar[i] == black) {
                        boardState[i].makeBlack();

                    } else if (stringAsChar[i] == white) {
                        boardState[i].makeWhite();


                    } else {
                        throw new IllegalArgumentException("Something about the way you serialized your NMM board doesn't make sense.");
                    }
                }

        }
        else
        {
            throw new IllegalArgumentException("Something about the way you serialized your NMM board doesn't make sense.");
        }
        return boardState;
    }

}



