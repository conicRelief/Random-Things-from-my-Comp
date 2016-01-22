import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;

/**
 * Created by otto on 11/24/15.
 */
public class EasyPrint {
    private static boolean KEY_SEPERATION = false;
    private static HashMap<String,Boolean> allEndries = new HashMap<String, Boolean>();

//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
//                                  publicly accessible functions
//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    public static void enableOutputAnnotations()
    {
        KEY_SEPERATION = true;
    }
    public static void disableOutputAnnotations()
    {
        KEY_SEPERATION = false;
    }

    public static void print(Object message, String key)
    {
        checkAndAnnotateKeyDifferences(key);
        printLogic(tryCast(message),key,true);
    }
    public static void print(Object message)
    {
        checkAndAnnotateKeyDifferences("default");
        printLogic(tryCast(message),"default",true);
    }
    public static void println(Object message, String key)
    {
        checkAndAnnotateKeyDifferences(key);
        printLogic(tryCast(message), key, false);
    }
    public static void println(Object message)
    {
        checkAndAnnotateKeyDifferences("default");
        printLogic(tryCast(message),"default",false);
    }


//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
//                                  the hidden logic behind the print statements.
//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
public static void mute(String key)
{
    Boolean a = allEndries.get(key);
    if (a != null)
    {
        allEndries.put(key,false);
    }
    else
    {
        allEndries.put(key,false);
    }
}
    public static void muteAll()
    {
        List<String> allKeys = (List<String>) allEndries.keySet();
        for(String key : allKeys)
        {
            allEndries.put(key,false);
        }
    }

    private static String lastKey = "default";

    private static void checkAndAnnotateKeyDifferences(String key)
    {
        if(KEY_SEPERATION)
        {
         if(!key.equals(lastKey))
         {
             System.out.println("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:      |" + key + "|");
             lastKey = key;
         }

        }
    }

    private static String tryCast(Object o)
    {
        StringBuilder sb = new StringBuilder();
        sb.append("");
        sb.append(o);
        String strI = sb.toString();
        return strI;
    }


    private static void printLogic(String message, String key, boolean inline)
    {
        Boolean a = allEndries.get(key);
        if (a != null)
        {
            if(a)
            {
                if(inline)
                {
                    System.out.print(message);
                }
                else
                {
                    System.out.println(message);
                }
            }
        }
        else
        {
            allEndries.put(key,true);
            if(inline)
            {
                System.out.print(message);
            }
            else
            {
                System.out.println(message);
            }
        }
    }





}
